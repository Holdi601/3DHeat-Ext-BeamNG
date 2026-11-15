"""Write docs/cli-reference.md from the code itself, so the reference cannot drift.

The options come from the program's own `--help`; the course's parts from the
part names the code gives them.

    python tools/gen_docs_reference.py          # rewrite the page
    python tools/gen_docs_reference.py --check  # exit 1 when the page is stale
"""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "cli-reference.md"
COMMAND = "heat3d-beamng-maps"
VERBS = ["course", "levels", "identify"]


def run(args):
    env = dict(os.environ, HEAT3D_NO_UPDATE="1", COLUMNS="88", PYTHONIOENCODING="utf-8",
               PYTHONPATH=str(ROOT) + os.pathsep + os.environ.get("PYTHONPATH", ""))
    r = subprocess.run([sys.executable, "-m", "heat3d_ext_beamng"] + args, capture_output=True, text=True,
                       env=env, encoding="utf-8", cwd=ROOT)
    return (r.stdout or r.stderr).rstrip()


def outputs():
    sys.path.insert(0, str(ROOT))
    from heat3d_ext_beamng import beamngcourse

    placed = ", ".join(f"`{part} <material>` ({c})" for c, part in beamngcourse._CATEGORY_PART.items())
    surfaces = ", ".join(f"`{part}` ({k})" for k, part in beamngcourse.SURFACE_PART.items())
    defaults = ", ".join(f"`{c}`" for c in beamngcourse.DEFAULT_CATEGORIES)
    return ["### `.glb` parts", "",
            "The ground, per 512 m square: `<surface part> <x>_<y>`, the surface being one of "
            f"{surfaces} or `ground:terrain`; modelled driving surface adds its material's name.", "",
            f"Placed models, per category and material: {placed}.", "",
            f"Categories placed by default: {defaults}; `--trees` adds `trees`.", "",
            "Water: `water:water`.", ""]


def build():
    out = ["---", "title: Command reference", "nav_order: 90", "---", "", "# Command reference", "",
           "Generated from the code by `tools/gen_docs_reference.py`: do not edit by hand.",
           "The other pages explain each command step by step.", "",
           f"## `{COMMAND}`", "", "```text", run(["--help"]), "```", ""]
    for v in VERBS:
        out += [f"## `{v}`", "", "```text", run([v, "--help"]), "```", ""]
    out += ["## Output", ""]
    return "\n".join(out + outputs())


if __name__ == "__main__":
    text = build()
    if "--check" in sys.argv:
        sys.exit(0 if OUT.exists() and OUT.read_text(encoding="utf-8") == text else 1)
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT.relative_to(ROOT))
