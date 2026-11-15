---
title: Terms and licence
nav_order: 9
---

# Terms and licence

## BeamNG's content

BeamNG.drive and its levels belong to BeamNG GmbH, who do not endorse this
project. This tool ships nothing of the game and downloads nothing: it reads
the files of the copy **you** installed, on your machine, outside the game. It
changes nothing in the game and talks to no server. A course it writes is a
derivative of BeamNG's level: it is yours to analyse your own laps on, not to
share or publish. Using the tool is your decision, under the terms you
accepted for the game.

That is why it is a separate package: if BeamNG ever asks for it to go, it
goes alone, and the viewer, GameFiles and the other tools stay.

The rules of 3DHeat GameFiles apply here unchanged
([Rules and licences](https://holdi601.github.io/3DHeat-GameFiles/rules-and-licences.html)):

- **Your own files, your responsibility.** The tool reads the game files
  installed on your machine. It never downloads game content.
- **Output is not for redistribution.** Keep exported `.glb` files, and the
  textures inside them, for your own analysis. Do not publish, share or sell
  exported courses, levels, models or textures. The repository's `.gitignore`
  keeps game files, exports and laps out of version control.
- **No keys.** BeamNG ships plain zip archives; nothing is encrypted, and
  nothing here decrypts.

## The formats

BeamNG ships plain zip archives, so there is no container to reverse engineer.
BeamNG publishes its `.cdae` layout, and the reader follows it. The `.ter`
terrain, the scene files and the materials were read from the shipped levels
and checked against them ([BeamNG files](reader-beamng.md)).

## Licence and sources

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-BeamNG/blob/main/LICENSE)).
Needs 3DHeat GameFiles (MIT), numpy (BSD-3-Clause), Pillow (MIT-CMU), msgpack
(Apache-2.0) and zstandard (BSD-3-Clause); the tests need pytest (MIT). See
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-BeamNG/blob/main/LICENSES.md).
Written for this project; no code was taken from any other project.
