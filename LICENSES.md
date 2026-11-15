# Third-party licences

This tool is MIT licensed ([`LICENSE`](LICENSE)). What it uses, and under which
licence; each package's own source is what counts, not this file.

| Software | Licence | How it is used |
|---|---|---|
| 3DHeat GameFiles | MIT | a dependency, installed by pip: the glTF writer, lap files, corridor, surfaces, detail budget and Steam libraries |
| numpy | BSD-3-Clause | a dependency, installed by pip: mesh and terrain decoding |
| Pillow | MIT-CMU (HPND) | a dependency, installed by pip: decoding the level's textures, writing the baked ground |
| msgpack | Apache-2.0 | a dependency, installed by pip: BeamNG's compiled shapes (`.cdae`) |
| zstandard | BSD-3-Clause | a dependency, installed by pip: the few `.cdae` shapes that are zstd-compressed |
| pytest | MIT | development only: the tests |

All permissive. This tool carries no restriction of its own.

## The game's files

BeamNG.drive belongs to BeamNG GmbH. This repository holds no file of the game
and no course made from one; the tool reads the copy the user installed, on
the user's machine, and the course it writes stays there. BeamNG publishes its
`.cdae` shape cache's layout, and the reader follows that; no other project's
code was used. See
[Terms and licence](https://holdi601.github.io/3DHeat-Ext-BeamNG/terms.html).
