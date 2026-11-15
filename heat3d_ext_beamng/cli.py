"""
heat3d-beamng-maps course <lap> [-o file.glb]   the ground around a BeamNG.drive lap, as a 3DHeat course
heat3d-beamng-maps levels [--install FOLDER]    where BeamNG.drive is, and the levels it has
heat3d-beamng-maps identify <path>              a BeamNG.drive shape (.cdae), terrain (.ter) or level zip

`course` takes exactly the options of 3DHeat GameFiles' `course`, so GameFiles
can hand a BeamNG lap over unchanged; the ones that only mean something for
another game (`--track`, `--season`) are accepted and ignored.

Exit status: 0 done, 1 failed, 2 nothing found (no BeamNG.drive install, not a
BeamNG lap or file, 3DHeat GameFiles missing).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from . import __version__
from ._gamefiles import NEEDED, find_gamefiles

PROG = "heat3d-beamng-maps"

#: The tool that exports a course for each other game a lap can be from.
_OTHER_TOOLS = {"acrally": "heat3d-acrally-maps", "assetto-corsa-rally": "heat3d-acrally-maps"}

#: What `levels` and `course` say when the game is not found.
_NO_INSTALL = (
    "no BeamNG.drive install found in the Steam libraries. Name its folder "
    "with --install (the one holding gameengine.zip)."
)


def _slug(name: str) -> str:
    """A course name as a file name: `Example Circuit` -> `example_circuit`."""
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_") or "course"


def _install(given: Path | None) -> Path | None:
    """The game's folder: the one given, if it is one, else the Steam libraries'."""
    from .beamng import find_install

    if given is not None:
        return find_install((given,), defaults=False)
    return find_install()


def _not_beamng(name: str, game: str) -> str:
    tool = "heat3d-forza-maps" if game.startswith("forza") else _OTHER_TOOLS.get(game)
    if tool:
        return f"{PROG}: {name} is a {game} lap, not a BeamNG.drive one: export its course with `{tool} course`."
    return (
        f"{PROG}: {name} is a {game} lap, not a BeamNG.drive one, and no 3DHeat tool exports its course; "
        "`heat3d-gamefiles course` says why."
    )


def _course(args) -> int:
    """A BeamNG lap in, the ground around it out: the level is found from the lap."""
    from heat3d_gamefiles import levelshome
    from heat3d_gamefiles.lapinput import UnreadableLap, read

    try:
        driven = read(args.lap)
    except UnreadableLap as exc:
        print(exc, file=sys.stderr)
        return 1
    # A lap that does not say which game it is from is taken as BeamNG's: that is
    # the game this tool reads.
    game = (args.game or driven.game or "beamng").lower()
    if game != "beamng":
        print(_not_beamng(driven.name, game), file=sys.stderr)
        return 2
    install = _install(args.install)
    if install is None:
        where = f"no BeamNG.drive in {args.install} (the folder holding gameengine.zip and content)" if args.install else _NO_INSTALL
        print(f"{PROG}: {where}", file=sys.stderr)
        return 2
    target = args.out or levelshome.default(_slug(driven.name) + ".glb", "beamng", "courses")
    target.parent.mkdir(parents=True, exist_ok=True)
    from .beamngcourse import export

    if len(driven) < 2:
        print(f"{driven.name} holds no driving", file=sys.stderr)
        return 1
    print(f"{driven.name}: {len(driven):,} samples, {driven.metres:,.0f} m driven (BeamNG.drive)")
    return export(driven, target, args, install=install)


def _levels(args) -> int:
    """Where the game is, and every level it can mount, mods included."""
    from .beamng import BeamNGError, Files, list_levels

    install = _install(args.install)
    if install is None:
        where = f"no BeamNG.drive in {args.install} (the folder holding gameengine.zip and content)" if args.install else _NO_INSTALL
        print(f"{PROG}: {where}", file=sys.stderr)
        return 2
    print(f"BeamNG.drive at {install}")
    try:
        names = list_levels(Files.of_install(install))
    except (BeamNGError, OSError, ValueError) as exc:
        print(f"{PROG}: {exc}", file=sys.stderr)
        return 1
    for name in names:
        print(f"  {name}")
    print(f"{len(names)} levels, with mods")
    return 0 if names else 2


# --------------------------------------------------------------------- identify


def _head(path: Path, size: int) -> bytes:
    with path.open("rb") as handle:
        return handle.read(size)


#: What a zip begins with: a local file header, or the end record of an empty one.
_ZIP_MAGIC = (b"PK\x03\x04", b"PK\x05\x06")


def _identify_level_zip(path: Path) -> list[str] | None:
    """A zip laid out as a BeamNG level (everything under `levels/<name>/`); else None."""
    import zipfile
    from collections import Counter

    if _head(path, 4) not in _ZIP_MAGIC:
        return None
    try:
        with zipfile.ZipFile(path) as bundle:
            names = [n for n in bundle.namelist() if not n.endswith("/")]
    except (zipfile.BadZipFile, OSError):
        return None
    # BeamNG ships one zip per level, everything in it under `levels/<name>/`.
    levels = sorted({n.split("/")[1] for n in names if n.lower().startswith("levels/") and n.count("/") >= 2})
    if not levels:
        return None
    lines = [f"  zip archive, {len(names):,} entries"]
    kinds = Counter(
        "." + n.rsplit(".", 1)[-1].lower() if "." in n.rsplit("/", 1)[-1] else "(no extension)"
        for n in names
    )
    if kinds:
        lines.append("    holds      " + ", ".join(f"{n} x {k}" for k, n in kinds.most_common(6)))
    lines.append(f"    levels     {', '.join(levels[:6])} (laid out as a BeamNG.drive level)")
    return lines


def _identify_beamng(path: Path) -> list[str] | None:
    """A BeamNG `.cdae` shape or `.ter` terrain, by their contents; else None."""
    import struct

    from .beamngshape import SHAPE_VERSION

    head = _head(path, 8)
    if len(head) == 8 and struct.unpack_from("<I", head)[0] & 0xFF == SHAPE_VERSION:
        from .beamngshape import read_shape

        try:
            shape = read_shape(path.read_bytes())
        except Exception:  # noqa: BLE001 - whatever does not parse is not a shape
            shape = None
        if shape is not None:
            return [
                f"  BeamNG.drive shape (.cdae), version {SHAPE_VERSION}",
                f"    meshes     {len(shape.meshes):,}",
                f"    detail     {len(shape.levels())} drawn levels",
                f"    materials  {', '.join(shape.materials[:6]) or 'none'}",
            ]
    if len(head) < 5:
        return None
    # A `.ter`: a version byte, the side, side x side heights and as many layer
    # bytes, then the layer names. No magic, so all of it has to add up.
    side = int.from_bytes(head[1:5], "little")
    if not 2 <= side <= 16384:
        return None
    at = 5 + side * side * 3
    with path.open("rb") as handle:
        handle.seek(at)
        tail = handle.read(4 + 256 * 256)
    if len(tail) < 4:
        return None
    count = int.from_bytes(tail[:4], "little")
    if not 0 < count <= 255:
        return None
    names, at = [], 4
    for _ in range(count):
        if at >= len(tail) or at + 1 + tail[at] > len(tail):
            return None
        name = tail[at + 1 : at + 1 + tail[at]]
        if not name or not all(32 <= c < 127 for c in name):
            return None
        names.append(name.decode("ascii"))
        at += 1 + tail[at]
    return [
        f"  BeamNG.drive terrain (.ter), version {head[0]}",
        f"    heights    {side:,} x {side:,}",
        f"    layers     {', '.join(names[:6])}" + (f" and {len(names) - 6} more" if len(names) > 6 else ""),
    ]


def _identify(args) -> int:
    path = args.path
    if not path.is_file():
        print(f"{PROG}: no such file: {path}", file=sys.stderr)
        return 2
    found = _identify_level_zip(path) or _identify_beamng(path)
    if found is None:
        print(f"not a BeamNG.drive file: {path.name}", file=sys.stderr)
        return 2
    print("\n".join([f"{path.name}  ({path.stat().st_size:,} bytes)"] + found))
    return 0


# --------------------------------------------------------------------- the command line


def _export_options(p) -> None:
    """The options GameFiles' `course` takes for what goes into the file, with its defaults."""
    from heat3d_gamefiles.detail import DEFAULT_BUDGET

    p.add_argument(
        "--texture-size",
        type=int,
        choices=(2048, 1024, 512),
        default=2048,
        help="ground texture per 512 m tile, in pixels (2048 = 25 cm a pixel)",
    )
    p.add_argument(
        "--no-textures",
        action="store_true",
        help="flat colours only: a far smaller file, and no ground detail",
    )
    p.add_argument(
        "--season",
        choices=("summer", "autumn", "winter", "spring"),
        default="summer",
        help="Forza only; accepted and ignored here",
    )
    p.add_argument(
        "--no-placed",
        action="store_true",
        help="terrain and modelled road only: leave out kerbs, barriers, signs, rocks and buildings",
    )
    p.add_argument(
        "--trees",
        action="store_true",
        help="also place trees and bushes (many triangles, and they hide the road)",
    )
    p.add_argument(
        "--detail-budget",
        type=int,
        default=None,
        help=(
            "a ceiling on triangles for everything placed; the costliest models drop "
            "to coarser levels of detail until it fits, and past that the furthest "
            "copies are left out (default: enough to keep every copy, and at least "
            f"{DEFAULT_BUDGET:,}; kerbs and driving surface always stay at full detail)"
        ),
    )


def main(argv: list[str] | None = None) -> int:
    if not find_gamefiles():
        print(f"{PROG}: {NEEDED}", file=sys.stderr)
        return 2
    try:
        import heat3d_update

        heat3d_update.startup("heat3d_ext_beamng")
    except Exception:  # an update check never stops an export
        pass
    ap = argparse.ArgumentParser(
        prog=PROG,
        description="BeamNG.drive levels from your own install as 3DHeat courses",
        epilog="What you point it at is BeamNG GmbH's, under the game's own licence; the courses stay on your machine.",
    )
    ap.add_argument("--version", action="version", version=__version__)
    sub = ap.add_subparsers(dest="verb", required=True)

    p = sub.add_parser("course", help="export the ground around a BeamNG.drive lap, working out the level")
    _export_options(p)
    p.add_argument(
        "lap",
        help=(
            "a lap: a file written by heat3d_capture (the BeamNG mod's recording), "
            "a lap folder, or a .csv with the BeamNG positions"
        ),
    )
    p.add_argument(
        "-o",
        "--out",
        type=Path,
        default=None,
        help=(
            "where to write the .glb (default: the lap's name, in "
            "$HEAT3D_LEVELS/beamng/courses when that is set, else here)"
        ),
    )
    p.add_argument("--track", type=Path, default=None, help="Forza only; accepted and ignored here")
    p.add_argument(
        "--margin",
        type=float,
        default=80.0,
        help="metres of ground to keep either side of the driving (default 80)",
    )
    p.add_argument(
        "--game",
        choices=("forza", "beamng", "acrally"),
        default=None,
        help="which game the lap is from (default: what the lap file says, else BeamNG); another game's lap exits 2",
    )
    p.add_argument("--level", default=None, help="the level's folder name, if it should not be found from the lap")
    p.add_argument(
        "--install",
        type=Path,
        default=None,
        help="the game's folder (the one holding gameengine.zip), if it is not in a Steam library",
    )
    p.set_defaults(run=_course)

    p = sub.add_parser("levels", help="where BeamNG.drive is, and every level it has (mods included)")
    p.add_argument("--install", type=Path, default=None, help="the game's folder, if it is not in a Steam library")
    p.set_defaults(run=_levels)

    p = sub.add_parser("identify", help="say whether a file is BeamNG.drive's, and what it holds")
    p.add_argument("path", type=Path, help="a .cdae shape, a .ter terrain or a level's .zip")
    p.set_defaults(run=_identify)

    args = ap.parse_args(argv)
    return args.run(args)


if __name__ == "__main__":
    sys.exit(main())
