---
title: "Encontrar el juego: levels"
nav_order: 3
lang: "es"
source: levels.md
source_hash: "7b7b8d5cee93"
nav_exclude: true
search_exclude: true
---
# Encontrar el juego: `levels` {#finding-the-game-levels}

```bash
heat3d-beamng-maps levels [--install FOLDER]
```

muestra dónde está instalado BeamNG.drive y cada nivel que puede montar, incluidos los
niveles de tus mods, con el nombre de carpeta que acepta `course --level`. Ejecútalo
primero: cuando lista niveles y sale con código 0, [`course`](course-beamng.md)
ya tiene el juego que necesita.

```text
BeamNG.drive at C:\Program Files (x86)\Steam\steamapps\common\BeamNG.drive
  example_level
  ...
12 levels, with mods
```

## Dónde se busca el juego {#where-the-game-is-looked-for}

Primero `--install`: la carpeta que contiene `gameengine.zip` y `content`. Sin esta opción,
busca `steamapps\common\BeamNG.drive` en cada biblioteca de Steam: la carpeta propia de Steam
(desde el registro, o los lugares habituales) y cada biblioteca que figura en su
`steamapps\libraryfolders.vdf`. Se usa la primera carpeta que tenga ambos.
`course` busca en los mismos lugares.

Tu contenido propio (mods, mods descomprimidos y una carpeta `levels` de usuario) se lee desde
`%LOCALAPPDATA%\BeamNG\BeamNG.drive` y `%LOCALAPPDATA%\BeamNG.drive`, como explica
[Exportar el recorrido](course-beamng.md#the-file-system).

## Mensajes y código de salida {#messages-and-exit-status}

| Mensaje | Salida | Significa |
|---|---|---|
| `heat3d-beamng-maps: no BeamNG.drive install found in the Steam libraries. ...` | 2 | instala el juego a través de Steam, o indica `--install` |
| `heat3d-beamng-maps: no BeamNG.drive in <folder> ...` | 2 | `--install` apunta a un lugar sin `gameengine.zip` ni `content` |
| `0 levels, with mods` | 2 | el juego se encontró, pero ningún nivel tiene escena |
| `heat3d-beamng-maps: <reason>` | 1 | no se pudo leer un archivo comprimido |
