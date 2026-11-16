---
title: "¿Qué es este archivo: identify"
nav_order: 4
lang: "es"
source: identify.md
source_hash: "a6ea1b58215b"
nav_exclude: true
search_exclude: true
---
# ¿Qué es este archivo: `identify` {#what-is-this-file-identify}

```bash
heat3d-beamng-maps identify <path>
```

indica si un archivo es de BeamNG.drive, y qué contiene. Se fija en los bytes, no en la
extensión:

| Archivo | Se reconoce por |
|---|---|
| una forma compilada, `.cdae` | su versión (31) y una forma que se puede leer |
| un terreno, `.ter` | no tiene cabecera: el lado, las alturas, el mapa de capas y los nombres de capas deben cuadrar |
| el `.zip` de un nivel | entradas bajo `levels/<name>/` |

```text
rail.cdae  (1,234 bytes)
  BeamNG.drive shape (.cdae), version 31
    meshes     2
    detail     1 drawn levels
    materials  rail_mat
```

Cualquier otro archivo muestra `not a BeamNG.drive file: <name>` en la salida de error y
sale con código 2; un archivo que no existe muestra `no such file` y sale con código 2.
El propio `identify` de 3DHeat GameFiles pregunta a esta herramienta por los archivos que
sus lectores de motor no conocen. Los formatos se describen en [Archivos de BeamNG](reader-beamng.md).
