"""
The standalone app's description of this tool (app/spec.py): the BeamNG.drive
install it reads, the checks before a course can be exported, and the course
export as a task. A course is cut around a recorded lap, and the level is found
from the lap, so there are no maps to extract from the install alone: the
window lists what is found and runs `course` and `levels`.
`python -m heat3d_ext_beamng.standalone_spec` runs the app from a checkout;
the release executables run the same.
"""

from __future__ import annotations

from pathlib import Path

from . import __version__
from .app.spec import Check, GameSpec, Input, Spec, Task, game_folders

TOOL = "heat3d-beamng-maps"


def _find(given: str | None) -> Path | None:
    from .beamng import find_install

    if given:
        return find_install((given,), defaults=False)
    return find_install()


def _install_args() -> list[str]:
    """`--install <folder>` when the install is known (chosen in the window, or found)."""
    game = game_folders(SPEC).get("beamng")
    return ["--install", str(game)] if game else []


def _checks(found: dict, levels: Path) -> list[Check]:
    from ._gamefiles import NEEDED, find_gamefiles

    ok = find_gamefiles()
    return [Check("gamefiles", "3DHeat GameFiles (the readers this tool builds on)", ok, "found" if ok else NEEDED)]


SPEC = Spec(
    id="heat3d-beamng",
    name="3DHeat BeamNG",
    repo="Holdi601/3DHeat-Ext-BeamNG",
    version=__version__,
    tools={TOOL: "heat3d_ext_beamng.cli:main"},
    default_tool=TOOL,
    description="BeamNG.drive levels around your laps, as 3DHeat courses",
    module="heat3d_ext_beamng.standalone_spec",
    games=[GameSpec(
        key="beamng", label="BeamNG.drive", find=_find, subdir="beamng",
        platforms=("windows-x64", "linux-x64"),
    )],
    checks=_checks,
    tasks=[
        Task(
            "course", "Course around a lap",
            [Input("lap", "A recorded lap (a lap file, or a .csv with its positions)", "file")],
            lambda v, levels: [TOOL, "course", v["lap"], *_install_args()],
            help="the ground, roads, placed models and water along the lap, into <levels>/beamng/courses",
        ),
        Task(
            "levels", "List the levels",
            [],
            lambda v, levels: [TOOL, "levels", *_install_args()],
            help="where the game is, and every level it has, mods included",
        ),
    ],
    min_free_gb=2.0,
    notice="Not affiliated with or endorsed by BeamNG GmbH.",
)

if __name__ == "__main__":
    from .app.entry import main
    from .update import apply

    raise SystemExit(main(SPEC, apply_source=apply))
