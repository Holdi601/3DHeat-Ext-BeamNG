# 3DHeat BeamNG: BeamNG.drive courses around your laps

**What is it?** This tool reads a BeamNG.drive level from your own install and
cuts out the stretch you drove: the ground with its baked texture, the roads,
kerbs, barriers, signs, buildings and water along your lap, as one 3D course
for the [3DHeat](https://github.com/Holdi601/3DHeat) viewer.

**Why would I use it?** To analyse your BeamNG laps on the real road - braking
points, lines and corners in 3D - instead of on a line in empty space.

**Example:** `heat3d-beamng-maps course my_lap.json` -> `my_lap.glb`, in the
lap's own frame: it drops into the viewer's Race tab under the lap.

**Documentation:** [holdi601.github.io/3DHeat-Ext-BeamNG](https://holdi601.github.io/3DHeat-Ext-BeamNG/), a page per
command with step-by-step use and example output. Part of
[3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)).

Each game reader is its own small project with its own licence file, releases
and issue tracker, so it can be installed, updated, maintained - or withdrawn
on a rights holder's request - on its own, without affecting the viewer or the
other tools.

The courses it writes stay on your machine.

## The standalone program

No Python needed: download the file for your system (Windows, Linux incl. Steam Deck) from the
[latest release](https://github.com/Holdi601/3DHeat-Ext-BeamNG/releases/latest), check it against
`SHA256SUMS`, unpack it and start `heat3d-beamng`. Its window finds your install, says what is missing,
exports the course around a lap you pick into the 3DHeat levels folder, lists the levels, and asks before
it updates itself. `heat3d-beamng --help` lists its commands (every command below runs through it too:
`heat3d-beamng heat3d-beamng-maps course my_lap.json`); `--check --json` and `status --json` are for
scripts. The 3DHeat app's Extractors panel can install and update it for you. See
[Before you start](https://holdi601.github.io/3DHeat-Ext-BeamNG/before-you-start.html).

The window walks through four steps (find the game, choose, work, done) in the 3DHeat look, dark or light. On Windows the program opens only its window, with no console window; in a terminal it prints as usual, and `heat3d-beamng-cli.cmd` in the same folder makes the terminal wait for it and pass on its exit code.

## Quick start for new users

You need: Windows, [Python](https://www.python.org/downloads/) 3.10 or later
("Add python.exe to PATH" ticked in its installer), BeamNG.drive installed
through Steam, and a lap recorded with
[3DHeat GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) and its
BeamNG mod (`python -m heat3d_capture telemetry --game beamng --install` once,
then `python -m heat3d_capture telemetry --game beamng -o laps`, see
[Telemetry: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html)).
No Git is needed.

1. Install the tool (one line, in PowerShell or a command prompt); it brings
   [3DHeat GameFiles](https://github.com/Holdi601/3DHeat-GameFiles), the
   library it reads with:

   ```bash
   python -m pip install https://github.com/Holdi601/3DHeat-Ext-BeamNG/archive/refs/tags/v0.1.0.zip
   ```

2. Check that the game is found, then export the course around your lap (the
   level is worked out from the lap; a game outside the Steam libraries needs
   `--install "<game folder>"`, the one holding `gameengine.zip`):

   ```bash
   heat3d-beamng-maps levels
   heat3d-beamng-maps course laps\<lap>.json -o my_lap.glb
   ```

3. The output is `my_lap.glb` in the folder you ran it in (without `-o`, it is
   named after the lap). `course` ends with `wrote my_lap.glb (... bytes)`; a
   level takes seconds to minutes.
4. Open it in the [3DHeat viewer](https://github.com/Holdi601/3DHeat#quick-start):
   download the viewer (**Code -> Download ZIP**, unpack) and double-click
   `start.bat`; it offers to install [Node.js](https://nodejs.org/) when it is
   missing and opens Chrome or Edge at `http://127.0.0.1:5273`. There,
   **Background / level -> 3D model...** and pick the `.glb`, then the
   **Race analysis** tab, **Load lap files...** and pick the lap.

When a new release is out, the tool says so when it starts and offers to
update itself (`python -m heat3d_ext_beamng.update` does the same).

## Install from a checkout

New to the command line? Read [Before you start](https://holdi601.github.io/3DHeat-Ext-BeamNG/before-you-start.html) first.

1. Install Python 3.10 or later, and BeamNG.drive.
2. `git clone https://github.com/Holdi601/3DHeat-Ext-BeamNG` (or download the
   ZIP) and open a terminal in that folder.
3. Install the command - this also installs
   [3DHeat GameFiles](https://github.com/Holdi601/3DHeat-GameFiles), the library
   the readers build on - and check that the game is found:

```bash
python -m pip install -e .        # installs the heat3d-beamng-maps command
heat3d-beamng-maps levels         # where BeamNG.drive is, and its levels
```

Without pip, a GameFiles checkout is found in `HEAT3D_GAMEFILES`, in
`../../gamefiles` (inside a 3DHeat checkout) or in `../3DHeat-GameFiles`.

Laps come from the 3DHeat GameCapture recorder and its BeamNG mod
([Telemetry: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html),
code in [GameCapture's `mods/beamng`](https://github.com/Holdi601/3DHeat-GameCapture/tree/main/mods/beamng)).

## Commands

| Command | Does | Page |
|---|---|---|
| `course <lap> [-o file.glb]` | the ground, roads, models and water around a BeamNG lap, the level found from the lap | [course](https://holdi601.github.io/3DHeat-Ext-BeamNG/course-beamng.html) |
| `levels [--install FOLDER]` | where BeamNG.drive is, and every level it has (mods included) | [levels](https://holdi601.github.io/3DHeat-Ext-BeamNG/levels.html) |
| `identify <path>` | whether a file is a BeamNG `.cdae` shape, `.ter` terrain or level zip, and what it holds | [identify](https://holdi601.github.io/3DHeat-Ext-BeamNG/identify.html) |

```bash
heat3d-beamng-maps course laps\my_lap.json                        # the level found from the lap
heat3d-beamng-maps course my_lap.json --level <level folder>      # or named
heat3d-beamng-maps course my_lap.json --install "D:\Games\BeamNG.drive" --no-textures
```

| `course` option | Does |
|---|---|
| `-o`, `--out FILE` | the `.glb` to write (default: the lap's name, in `$HEAT3D_LEVELS/beamng/courses` when that is set, else here) |
| `--level NAME` | the level's folder name, when it should not be found from the lap |
| `--install FOLDER` | the game's folder (holding `gameengine.zip`), when it is in no Steam library |
| `--margin METRES` | ground kept either side of the driving (default 80) |
| `--texture-size {2048,1024,512}` | baked ground texture per 512 m square (default 2048, 25 cm a pixel) |
| `--no-textures` | flat colours only |
| `--no-placed` | terrain and modelled road only |
| `--trees` | also trees and bushes |
| `--detail-budget N` | a ceiling on placed triangles |
| `--game {forza,beamng,acrally}` | which game the lap is from (default: what the lap says, else BeamNG); another game's lap exits 2 and names its tool |
| `--track`, `--season` | Forza only: accepted, so 3DHeat GameFiles can pass its arguments on unchanged, and ignored |

Exit status: 0 done; 1 reading or writing failed; 2 nothing found - no
BeamNG.drive install, no such level, a lap on no installed level, not a BeamNG lap or
file, GameFiles missing (the message
says which, and what to do). Every option, as the program prints it:
[Command reference](https://holdi601.github.io/3DHeat-Ext-BeamNG/cli-reference.html).

3DHeat GameFiles' `course` runs this tool for a BeamNG lap, and its `identify`
asks this tool about files its own readers do not know.

## What comes out, and loading it

One glTF binary in the viewer's frame (metres, Y up): ground per 512 m square
with a baked texture (`ground:terrain`, `ground:road`, ...), placed models per
category and material (`structure:barriers <material>`, `ground:kerbs <material>`, ...)
and `water:water`. Load it in the viewer's **Background / level** panel with
**3D model…** under the lap.
[The course, step by step](https://holdi601.github.io/3DHeat-Ext-BeamNG/course-beamng.html).

## Terms

3DHeat BeamNG is not affiliated with or endorsed by BeamNG GmbH. BeamNG.drive
and related names and trademarks belong to their owners. Nothing of the game is
in this repository or downloaded by it - no game assets, no game code, no
DLLs; the level comes out of your own install, and the course it writes stays
on your machine
([Terms and licence](https://holdi601.github.io/3DHeat-Ext-BeamNG/terms.html)).

Rights holders: open an issue at
[github.com/Holdi601/3DHeat-Ext-BeamNG/issues](https://github.com/Holdi601/3DHeat-Ext-BeamNG/issues)
- we respond quickly and remove anything on request.

## Tests

```bash
python -m pip install -e .[test]
python -m pytest
```

On made-up data only: an install built the way the game ships one. The tests
on the real game run only where BeamNG.drive is installed, and write nothing
into the repository.

## Licence

MIT ([`LICENSE`](LICENSE)). Third-party software it uses: [`LICENSES.md`](LICENSES.md).
