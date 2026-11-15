---
title: "Finding the game: levels"
nav_order: 3
---

# Finding the game: `levels`

```bash
heat3d-beamng-maps levels [--install FOLDER]
```

prints where BeamNG.drive is installed and every level it can mount, your
mods' levels included, by the folder name `course --level` takes. Run it
first: when it lists levels and exits with 0, [`course`](course-beamng.md)
has the game it needs.

```text
BeamNG.drive at C:\Program Files (x86)\Steam\steamapps\common\BeamNG.drive
  example_level
  ...
12 levels, with mods
```

## Where the game is looked for

`--install` first: the folder holding `gameengine.zip` and `content`. Without
it, `steamapps\common\BeamNG.drive` in every Steam library: Steam's own folder
(from the registry, else the usual places) and each library its
`steamapps\libraryfolders.vdf` lists. The first folder that holds both is used.
`course` looks in the same places.

Your own content (mods, unpacked mods and a user `levels` folder) is read from
`%LOCALAPPDATA%\BeamNG\BeamNG.drive` and `%LOCALAPPDATA%\BeamNG.drive`, as
[Course export](course-beamng.md#the-file-system) explains.

## Messages and exit status

| Message | Exit | Means |
|---|---|---|
| `heat3d-beamng-maps: no BeamNG.drive install found in the Steam libraries. ...` | 2 | install the game through Steam, or pass `--install` |
| `heat3d-beamng-maps: no BeamNG.drive in <folder> ...` | 2 | `--install` points somewhere without `gameengine.zip` and `content` |
| `0 levels, with mods` | 2 | the game was found but no level has a scene |
| `heat3d-beamng-maps: <reason>` | 1 | an archive could not be read |
