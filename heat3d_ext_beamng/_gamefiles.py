"""
Finding 3DHeat GameFiles, the library this tool's readers build on.

Installed with pip it is simply importable. From a plain checkout it is looked
for in `HEAT3D_GAMEFILES`, then beside this tool inside a 3DHeat checkout
(`exporters/gamefiles`), then in a `3DHeat-GameFiles` folder next to this one.
"""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

#: This tool's own folder: the repository's root.
ROOT = Path(__file__).resolve().parents[1]

#: What to say when it is nowhere: one line, and what to do.
NEEDED = (
    "needs 3DHeat GameFiles: pip install https://github.com/Holdi601/3DHeat-GameFiles/archive/refs/tags/v1.1.0.zip, "
    "or set HEAT3D_GAMEFILES to its folder"
)


def find_gamefiles() -> bool:
    """Make `heat3d_gamefiles` importable if it can be found; say whether it is."""
    spec = importlib.util.find_spec("heat3d_gamefiles")
    # An empty folder of that name is a namespace package, not the library.
    if spec is not None and spec.origin not in (None, "namespace"):
        return True
    for place in (os.environ.get("HEAT3D_GAMEFILES"), ROOT.parent.parent / "gamefiles", ROOT.parent / "3DHeat-GameFiles"):
        if place and (Path(place) / "heat3d_gamefiles" / "__init__.py").is_file():
            sys.path.insert(0, str(Path(place).resolve()))
            return True
    return False
