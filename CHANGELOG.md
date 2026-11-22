# Changelog

## 0.3.0

- Its own icon: the 3DHeat cube with a text badge for its game (letters in 3DHeat's colours), as the
  program, window, taskbar and docs icon.
- A new window: the 3DHeat look in dark and light (follows the system, switchable), the logo and
  icon, sharp at any display scaling. Four steps: find the game (each requirement with its fix),
  choose (maps ticked when there is something to do, filters, search; jobs with their fields
  inline), work (progress, time left, cancel), done (open in 3DHeat, open the output folder, and
  for a failure what went wrong and what to do, copy details, report a problem).
- No console window on Windows: the program is a window program. From a terminal it still prints
  as before; `heat3d-beamng-cli.cmd` beside it waits for it in a terminal and passes its exit code.
- The update offer in the same look: Update now / Later / Skip this version, and "Update
  automatically" from the dialog.
- CI draws every page and dialog of the window (on Linux under a virtual display) and checks the
  Windows build is a window program.

## 0.2.0

- A standalone program for Windows and Linux (native and Steam/Proton, Steam Deck included; no Python needed),
  built by CI with a `SHA256SUMS` file. Without arguments it opens a window: what is found and what is missing
  (install, 3DHeat GameFiles, disk space), the levels folder, the course around a lap you pick, the level list,
  and updates. `--check --json` and `status --json` for scripts; a course is cut around a lap, so `extract` has
  nothing to extract from the install alone and says so.
- Updates ask first (update now / later / skip this version) unless automatic updates were chosen
  (`--auto-update`, the window's checkbox, or `HEAT3D_AUTO_UPDATE=1`).
- The install is also found in Steam libraries on Linux (native and flatpak), and the user folder of the native
  Linux game and of a Proton prefix.

## 0.1.0

- First version, moved out of 3DHeat GameFiles with its history (GameFiles'
  `course` now runs this tool for a BeamNG lap, and its `identify` asks it
  about BeamNG's files): the ground, roads, placed models and water around a
  BeamNG.drive lap as a 3DHeat course, the level found from the lap. `course`
  takes exactly GameFiles' `course` options; another game's lap exits 2 and
  names the tool for it. New: `levels` says where the game is and lists its
  levels; `identify` names a `.cdae` shape, a `.ter` terrain or a level zip.
  Builds on 3DHeat GameFiles as a library, installed by pip or found beside a
  checkout.
- Installs with one pip line from the release zip, no Git needed (GameFiles comes from its own release zip); a pip install knows its version and updates itself with pip when a newer release is out.
- README: a quick start for new users.

## Docs

Where each feature is documented
([holdi601.github.io/3DHeat-Ext-BeamNG](https://holdi601.github.io/3DHeat-Ext-BeamNG/)):

| Feature | Page |
|---|---|
| Installing, GameFiles, a first run | [Before you start](docs/before-you-start.md) |
| Exporting a course (`course` and its options): the install, the level, ground, roads, models, water | [Course export](docs/course-beamng.md) |
| Finding the install and its levels (`levels`, `--install`) | [Finding the game: levels](docs/levels.md) |
| Naming a BeamNG file (`identify`) | [What is this file: identify](docs/identify.md) |
| The file formats: level archives, `.ter`, `.cdae`, `.dae` | [BeamNG files](docs/reader-beamng.md) |
| BeamNG's content, the formats | [Terms and licence](docs/terms.md) |
| Every option and part name, generated | [Command reference](docs/cli-reference.md) |
| Release checklist for the docs | [Maintaining these docs](docs/maintaining.md) |
