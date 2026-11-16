---
title: Terms and licence
nav_order: 9
---

# Terms and licence

## BeamNG's content

BeamNG.drive and its levels belong to BeamNG GmbH. 3DHeat BeamNG is not
affiliated with or endorsed by BeamNG GmbH. BeamNG.drive and related names and
trademarks belong to their owners.

This tool ships nothing of the game and downloads nothing: no game assets, no
game code, no DLLs. It reads the files of the copy **you** installed, on your
machine, outside the game. It changes nothing in the game and talks to no
server. A course it writes is cut from BeamNG's level and stays on your
machine, for analysing your own laps; please do not share or publish it.

Each game reader is its own small project with its own licence file, releases
and issue tracker, so it can be installed, updated, maintained - or withdrawn
on a rights holder's request - on its own, without affecting the viewer or the
other tools.

Rights holders: open an issue at
[github.com/Holdi601/3DHeat-Ext-BeamNG/issues](https://github.com/Holdi601/3DHeat-Ext-BeamNG/issues)
- we respond quickly and remove anything on request.

The rules of 3DHeat GameFiles apply here unchanged
([Rules and licences](https://holdi601.github.io/3DHeat-GameFiles/rules-and-licences.html)):

- **Your own files.** The tool reads the game files
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
