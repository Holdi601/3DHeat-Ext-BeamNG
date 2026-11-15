import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
# The tests never ask GitHub for a newer release.
os.environ["HEAT3D_NO_UPDATE"] = "1"

# 3DHeat GameFiles, the library the readers build on: installed, in
# HEAT3D_GAMEFILES, or beside this checkout (see heat3d_ext_beamng/_gamefiles.py).
from heat3d_ext_beamng._gamefiles import find_gamefiles  # noqa: E402

find_gamefiles()
