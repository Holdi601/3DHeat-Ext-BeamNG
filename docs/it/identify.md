---
title: "Che file è questo: identify"
nav_order: 4
lang: "it"
source: identify.md
source_hash: "a6ea1b58215b"
nav_exclude: true
search_exclude: true
---
# Che file è questo: `identify` {#what-is-this-file-identify}

```bash
heat3d-beamng-maps identify <path>
```

dice se un file appartiene a BeamNG.drive, e che cosa contiene. Guarda i byte, non l'estensione:

| File | Riconosciuto da |
|---|---|
| una forma compilata, `.cdae` | la sua versione (31) e una forma che si legge |
| un terreno, `.ter` | nessuna firma: lato, altezze, mappa dei layer e nomi dei layer devono tornare tutti |
| lo `.zip` di un livello | voci sotto `levels/<name>/` |

```text
rail.cdae  (1,234 bytes)
  BeamNG.drive shape (.cdae), version 31
    meshes     2
    detail     1 drawn levels
    materials  rail_mat
```

Qualsiasi altro file stampa `not a BeamNG.drive file: <name>` sull'uscita degli errori e
termina con 2; un file che non esiste risponde `no such file` e termina con 2.
Lo strumento `identify` di 3DHeat GameFiles chiede a questo strumento i file che i suoi
lettori di motore non conoscono. I formati sono descritti in [File di BeamNG](reader-beamng.md).
