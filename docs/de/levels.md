---
title: "Das Spiel finden: levels"
nav_order: 3
lang: "de"
source: levels.md
source_hash: "7b7b8d5cee93"
nav_exclude: true
search_exclude: true
---
# Das Spiel finden: `levels` {#finding-the-game-levels}

```bash
heat3d-beamng-maps levels [--install FOLDER]
```

gibt aus, wo BeamNG.drive installiert ist, und jedes Level, das es einbinden kann, einschließlich
der Level deiner Mods, mit dem Ordnernamen, den `course --level` entgegennimmt. Führe es zuerst aus:
Wenn es Levels auflistet und mit 0 endet, hat [`course`](course-beamng.md) das Spiel, das es braucht.

```text
BeamNG.drive at C:\Program Files (x86)\Steam\steamapps\common\BeamNG.drive
  example_level
  ...
12 levels, with mods
```

## Wo nach dem Spiel gesucht wird {#where-the-game-is-looked-for}

Zuerst `--install`: der Ordner mit `gameengine.zip` und `content`. Ohne diese Option
`steamapps\common\BeamNG.drive` in jeder Steam-Bibliothek: Steams eigener Ordner (aus der Registry,
sonst die üblichen Orte) und jede Bibliothek, die ihre `steamapps\libraryfolders.vdf` auflistet.
Der erste Ordner, der beides enthält, wird genommen. `course` sucht an denselben Orten.

Deine eigenen Inhalte (Mods, entpackte Mods und ein Ordner `levels` des Benutzers) werden aus
`%LOCALAPPDATA%\BeamNG\BeamNG.drive` und `%LOCALAPPDATA%\BeamNG.drive` gelesen, wie
[Streckenexport](course-beamng.md#the-file-system) erklärt.

## Meldungen und Exit-Status {#messages-and-exit-status}

| Meldung | Exit | Bedeutung |
|---|---|---|
| `heat3d-beamng-maps: no BeamNG.drive install found in the Steam libraries. ...` | 2 | installiere das Spiel über Steam, oder gib `--install` an |
| `heat3d-beamng-maps: no BeamNG.drive in <folder> ...` | 2 | `--install` zeigt auf einen Ort ohne `gameengine.zip` und `content` |
| `0 levels, with mods` | 2 | das Spiel wurde gefunden, aber kein Level hat eine Szene |
| `heat3d-beamng-maps: <reason>` | 1 | ein Archiv konnte nicht gelesen werden |
