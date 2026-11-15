---
title: Command reference
nav_order: 90
---

# Command reference

Generated from the code by `tools/gen_docs_reference.py`: do not edit by hand.
The other pages explain each command step by step.

## `heat3d-beamng-maps`

```text
usage: heat3d-beamng-maps [-h] [--version] {course,levels,identify} ...

BeamNG.drive levels from your own install as 3DHeat courses

positional arguments:
  {course,levels,identify}
    course              export the ground around a BeamNG.drive lap, working out the
                        level
    levels              where BeamNG.drive is, and every level it has (mods included)
    identify            say whether a file is BeamNG.drive's, and what it holds

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit

What you point it at is BeamNG GmbH's, under the game's own licence; the courses stay
on your machine.
```

## `course`

```text
usage: heat3d-beamng-maps course [-h] [--texture-size {2048,1024,512}] [--no-textures]
                                 [--season {summer,autumn,winter,spring}]
                                 [--no-placed] [--trees]
                                 [--detail-budget DETAIL_BUDGET] [-o OUT]
                                 [--track TRACK] [--margin MARGIN]
                                 [--game {forza,beamng,acrally}] [--level LEVEL]
                                 [--install INSTALL]
                                 lap

positional arguments:
  lap                   a lap: a file written by heat3d_capture (the BeamNG mod's
                        recording), a lap folder, or a .csv with the BeamNG positions

options:
  -h, --help            show this help message and exit
  --texture-size {2048,1024,512}
                        ground texture per 512 m tile, in pixels (2048 = 25 cm a
                        pixel)
  --no-textures         flat colours only: a far smaller file, and no ground detail
  --season {summer,autumn,winter,spring}
                        Forza only; accepted and ignored here
  --no-placed           terrain and modelled road only: leave out kerbs, barriers,
                        signs, rocks and buildings
  --trees               also place trees and bushes (many triangles, and they hide the
                        road)
  --detail-budget DETAIL_BUDGET
                        a ceiling on triangles for everything placed; the costliest
                        models drop to coarser levels of detail until it fits, and
                        past that the furthest copies are left out (default: enough to
                        keep every copy, and at least 1,500,000; kerbs and driving
                        surface always stay at full detail)
  -o, --out OUT         where to write the .glb (default: the lap's name, in
                        $HEAT3D_LEVELS/beamng/courses when that is set, else here)
  --track TRACK         Forza only; accepted and ignored here
  --margin MARGIN       metres of ground to keep either side of the driving (default
                        80)
  --game {forza,beamng,acrally}
                        which game the lap is from (default: what the lap file says,
                        else BeamNG); another game's lap exits 2
  --level LEVEL         the level's folder name, if it should not be found from the
                        lap
  --install INSTALL     the game's folder (the one holding gameengine.zip), if it is
                        not in a Steam library
```

## `levels`

```text
usage: heat3d-beamng-maps levels [-h] [--install INSTALL]

options:
  -h, --help         show this help message and exit
  --install INSTALL  the game's folder, if it is not in a Steam library
```

## `identify`

```text
usage: heat3d-beamng-maps identify [-h] path

positional arguments:
  path        a .cdae shape, a .ter terrain or a level's .zip

options:
  -h, --help  show this help message and exit
```

## Output

### `.glb` parts

The ground, per 512 m square: `<surface part> <x>_<y>`, the surface being one of `ground:road` (road), `ground:gravel and dirt` (loose), `ground:verge` (verge), `ground:kerbs` (kerbs), `ground:markings` (markings), `ground:tyre marks` (tyremarks) or `ground:terrain`; modelled driving surface adds its material's name.

Placed models, per category and material: `ground:kerbs <material>` (kerbs), `ground:road <material>` (road), `ground:verge <material>` (verge), `structure:barriers <material>` (barriers), `structure:signs <material>` (signs), `structure:buildings <material>` (buildings), `structure:infrastructure <material>` (infrastructure), `structure:bridges <material>` (bridges), `structure:rocks <material>` (rocks), `structure:props <material>` (props), `structure:trees <material>` (trees).

Categories placed by default: `kerbs`, `road`, `verge`, `barriers`, `signs`, `buildings`, `infrastructure`, `bridges`, `rocks`, `props`; `--trees` adds `trees`.

Water: `water:water`.
