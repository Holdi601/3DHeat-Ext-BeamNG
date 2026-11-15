# Changelog

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
