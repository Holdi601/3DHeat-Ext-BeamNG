---
title: Before you start
nav_order: 1.5
---

# Before you start

New to the command line? This page takes you from nothing to a first run.
It takes about fifteen minutes, once.

## 1. Install Python

This tool needs **Python 3.10 or later**.

- **Windows:** download Python from [python.org/downloads](https://www.python.org/downloads/)
  and run the installer. On its first screen, tick **Add python.exe to PATH**,
  then click **Install Now**.
- **macOS and Linux:** Python 3 is often there already. Where these pages say
  `python`, type `python3`.

## 2. Get this tool

Open [github.com/Holdi601/3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG), click the
green **Code** button, then **Download ZIP**, and unzip it into a folder of your
choice. If you use git: `git clone https://github.com/Holdi601/3DHeat-Ext-BeamNG`.

## 3. Open a terminal in that folder

A terminal is a window where you type commands.

- **Windows:** open the folder in Explorer, click into the address bar, type
  `powershell` and press Enter. A blue or black window opens, already in that
  folder.
- **macOS:** open **Terminal**, type `cd ` (with a space), drag the folder into
  the window and press Enter.

`cd` means "change folder": `cd C:\Tools\3DHeat-Ext-BeamNG` goes to that folder.

## 4. Install the tool

Type this and press Enter:

```bash
python -m pip install -e .
```

This also installs [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/),
the library the readers build on, and numpy, Pillow, msgpack and zstandard.
You should see, at the end: `Successfully installed ... heat3d-ext-beamng-...`.

Already have a GameFiles checkout? The tool also finds it without pip: in the
folder the `HEAT3D_GAMEFILES` environment variable names, inside a 3DHeat
checkout (`exporters/gamefiles`), or in a `3DHeat-GameFiles` folder next to
this one.

## 5. Check that the game is found

```bash
heat3d-beamng-maps levels
```

You should see something like:

```text
BeamNG.drive at C:\Program Files (x86)\Steam\steamapps\common\BeamNG.drive
  example_level
  ...
12 levels, with mods
```

## 6. Record a lap, then export its course

Record a lap with the 3DHeat GameCapture recorder and its BeamNG mod
([Telemetry: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html)),
then:

```bash
heat3d-beamng-maps course laps\my_lap.json
```

Next: [Course export](course-beamng.md).

## How to read the commands on these pages

| You see | It means |
|---|---|
| `<level folder>` | a placeholder: type your own value instead, without the `< >` |
| `[--install FOLDER]` | optional: leave it out, or type it as shown |
| `# a note` | a comment for you: do not type it |
| `"C:\My Files\x"` | put a path that has spaces in quotes |

## When something goes wrong

| The message | What to do |
|---|---|
| `'python' is not recognized` | Python is not installed, or the PATH box was not ticked: install it again and tick it (or type `py` instead of `python`). |
| `'heat3d-beamng-maps' is not recognized` | Run step 4 again in the tool's folder, or type `python -m heat3d_ext_beamng` instead of `heat3d-beamng-maps`: it does the same. |
| `needs 3DHeat GameFiles: ...` | Step 4 did not install GameFiles: run `python -m pip install git+https://github.com/Holdi601/3DHeat-GameFiles.git`, or set `HEAT3D_GAMEFILES` to a GameFiles folder. |
| `no BeamNG.drive install found in the Steam libraries` | Give the game's folder, the one holding `gameengine.zip`: `--install "D:\Games\BeamNG.drive"`. |
| `... is a forza-... lap, not a BeamNG.drive one` | That lap is from another game; the message names the tool for it. |
| `the lap does not lie on any installed level's terrain` | Name the level: `--level <level folder>`, as `levels` lists it. |
| anything else | Read the last line of the message, then open an issue on GitHub with it. |

Every command also ends with an **exit status**: 0 means it worked, 2 that
the game, GameFiles or a BeamNG file was not found, 1 that reading or writing
failed. To see it, type `echo $LASTEXITCODE` in PowerShell or `echo $?` on
macOS and Linux.
