---
title: "Was ist diese Datei: identify"
nav_order: 4
lang: "de"
source: identify.md
source_hash: "a6ea1b58215b"
nav_exclude: true
search_exclude: true
---
# Was ist diese Datei: `identify` {#what-is-this-file-identify}

```bash
heat3d-beamng-maps identify <path>
```

sagt, ob eine Datei eine von BeamNG.drive ist, und was sie enthält. Das Werkzeug urteilt
anhand der Bytes, nicht anhand der Endung:

| Datei | Erkannt an |
|---|---|
| eine kompilierte Form, `.cdae` | ihrer Version (31) und einer Form, die sich lesen lässt |
| ein Gelände, `.ter` | keine Kennung: Seitenlänge, Höhen, Ebenenkarte und Ebenennamen müssen alle zusammenpassen |
| das `.zip` eines Levels | Einträge unter `levels/<name>/` |

```text
rail.cdae  (1,234 bytes)
  BeamNG.drive shape (.cdae), version 31
    meshes     2
    detail     1 drawn levels
    materials  rail_mat
```

Alles andere gibt `not a BeamNG.drive file: <name>` auf der Fehlerausgabe aus und endet
mit Exit-Code 2; eine Datei, die nicht da ist, meldet `no such file` und endet ebenfalls mit 2.
Das `identify` von 3DHeat GameFiles fragt dieses Werkzeug nach Dateien, die seine eigenen
Engine-Leser nicht kennen. Die Formate sind auf [BeamNG-Dateien](reader-beamng.md) beschrieben.
