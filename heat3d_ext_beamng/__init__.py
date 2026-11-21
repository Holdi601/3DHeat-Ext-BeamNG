"""BeamNG.drive levels from your own install as 3DHeat courses: the ground, roads, placed models and water around a recorded lap."""

from ._gamefiles import find_gamefiles as _find_gamefiles

__version__ = "0.2.0"

# The readers import 3DHeat GameFiles; from a plain checkout it has to be found first.
_find_gamefiles()
