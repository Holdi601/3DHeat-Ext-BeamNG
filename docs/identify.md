---
title: "What is this file: identify"
nav_order: 4
---

# What is this file: `identify`

```bash
heat3d-beamng-maps identify <path>
```

says whether a file is one of BeamNG.drive's, and what it holds. It goes by the
bytes, not the extension:

| File | Recognised by |
|---|---|
| a compiled shape, `.cdae` | its version (31) and a shape that reads |
| a terrain, `.ter` | no magic: the side, the heights, the layer map and the layer names all have to add up |
| a level's `.zip` | entries under `levels/<name>/` |

```text
rail.cdae  (1,234 bytes)
  BeamNG.drive shape (.cdae), version 31
    meshes     2
    detail     1 drawn levels
    materials  rail_mat
```

Anything else prints `not a BeamNG.drive file: <name>` on the error output and
exits with 2; a file that is not there says `no such file` and exits with 2.
3DHeat GameFiles' own `identify` asks this tool about files its engine readers
do not know. The formats are described on [BeamNG files](reader-beamng.md).
