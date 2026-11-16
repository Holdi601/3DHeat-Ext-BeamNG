---
title: "Trouver le jeu : levels"
nav_order: 3
lang: "fr"
source: levels.md
source_hash: "7b7b8d5cee93"
nav_exclude: true
search_exclude: true
---
# Trouver le jeu : `levels` {#finding-the-game-levels}

```bash
heat3d-beamng-maps levels [--install FOLDER]
```

affiche où BeamNG.drive est installé et chaque niveau qu'il peut monter, y compris
les niveaux de vos mods, sous le nom de dossier que prend `course --level`. Lancez-la
en premier : quand elle liste des niveaux et se termine avec le code 0, [`course`](course-beamng.md)
dispose du jeu dont il a besoin.

```text
BeamNG.drive at C:\Program Files (x86)\Steam\steamapps\common\BeamNG.drive
  example_level
  ...
12 levels, with mods
```

## Où le jeu est cherché {#where-the-game-is-looked-for}

D'abord `--install` : le dossier qui contient `gameengine.zip` et `content`. Sans cette
option, `steamapps\common\BeamNG.drive` dans chaque bibliothèque Steam : le dossier de Steam
lui-même (d'après le registre, sinon les emplacements habituels) et chaque bibliothèque que
liste `steamapps\libraryfolders.vdf`. Le premier dossier qui contient les deux est utilisé.
`course` cherche aux mêmes endroits.

Votre propre contenu (mods, mods décompressés et dossier `levels` de l'utilisateur) est lu dans
`%LOCALAPPDATA%\BeamNG\BeamNG.drive` et `%LOCALAPPDATA%\BeamNG.drive`, comme l'explique
[Export du parcours](course-beamng.md#the-file-system).

## Messages et code de sortie {#messages-and-exit-status}

| Message | Code | Signification |
|---|---|---|
| `heat3d-beamng-maps: no BeamNG.drive install found in the Steam libraries. ...` | 2 | installez le jeu via Steam, ou passez `--install` |
| `heat3d-beamng-maps: no BeamNG.drive in <folder> ...` | 2 | `--install` pointe vers un endroit sans `gameengine.zip` ni `content` |
| `0 levels, with mods` | 2 | le jeu a été trouvé, mais aucun niveau n'a de scène |
| `heat3d-beamng-maps: <reason>` | 1 | une archive n'a pas pu être lue |
