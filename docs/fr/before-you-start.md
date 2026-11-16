---
title: "Avant de commencer"
nav_order: 1.5
lang: "fr"
source: before-you-start.md
source_hash: "97e80f09283e"
nav_exclude: true
search_exclude: true
---
# Avant de commencer {#before-you-start}

Vous ne connaissez pas la ligne de commande ? Cette page vous guide de zéro
jusqu'à une première exécution. Cela prend environ quinze minutes, une seule fois.

## 1. Installer Python {#install-python}

Cet outil a besoin de **Python 3.10 ou plus récent**.

- **Windows :** téléchargez Python sur [python.org/downloads](https://www.python.org/downloads/)
  et lancez l'installateur. Sur son premier écran, cochez **Add python.exe to PATH**,
  puis cliquez sur **Install Now**.
- **macOS et Linux :** Python 3 est souvent déjà là. Là où ces pages écrivent
  `python`, tapez `python3`.

## 2. Récupérer cet outil {#get-this-tool}

Ouvrez [github.com/Holdi601/3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG), cliquez sur le
bouton vert **Code**, puis sur **Download ZIP**, et décompressez-le dans un dossier de votre
choix. Si vous utilisez git : `git clone https://github.com/Holdi601/3DHeat-Ext-BeamNG`.

## 3. Ouvrir un terminal dans ce dossier {#open-a-terminal-in-that-folder}

Un terminal est une fenêtre dans laquelle vous tapez des commandes.

- **Windows :** ouvrez le dossier dans l'Explorateur, cliquez dans la barre d'adresse,
  tapez `powershell` et appuyez sur Entrée. Une fenêtre bleue ou noire s'ouvre,
  déjà dans ce dossier.
- **macOS :** ouvrez **Terminal**, tapez `cd ` (avec un espace), faites glisser le
  dossier dans la fenêtre et appuyez sur Entrée.

`cd` veut dire « changer de dossier » : `cd C:\Tools\3DHeat-Ext-BeamNG` va dans ce dossier.

## 4. Installer l'outil {#install-the-tool}

Tapez cette ligne et appuyez sur Entrée :

```bash
python -m pip install -e .
```

Cela installe aussi [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/),
la bibliothèque sur laquelle s'appuient les lecteurs, ainsi que numpy, Pillow, msgpack et
zstandard. À la fin, vous devez voir : `Successfully installed ... heat3d-ext-beamng-...`.

Vous avez déjà une copie de GameFiles ? L'outil la trouve aussi sans pip : dans le
dossier que désigne la variable d'environnement `HEAT3D_GAMEFILES`, dans une copie de
3DHeat (`exporters/gamefiles`), ou dans un dossier `3DHeat-GameFiles` à côté de celui-ci.

## 5. Vérifier que le jeu est trouvé {#check-that-the-game-is-found}

```bash
heat3d-beamng-maps levels
```

Vous devez voir quelque chose comme :

```text
BeamNG.drive at C:\Program Files (x86)\Steam\steamapps\common\BeamNG.drive
  example_level
  ...
12 levels, with mods
```

## 6. Enregistrer un tour, puis exporter son parcours {#record-a-lap-then-export-its-course}

Enregistrez un tour avec l'enregistreur 3DHeat GameCapture et son mod BeamNG
([Telemetry: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html)),
puis :

```bash
heat3d-beamng-maps course laps\my_lap.json
```

Suite : [Export du parcours](course-beamng.md).

## Comment lire les commandes de ces pages {#how-to-read-the-commands-on-these-pages}

| Vous voyez | Cela signifie |
|---|---|
| `<level folder>` | un emplacement : tapez votre propre valeur à la place, sans les `< >` |
| `[--install FOLDER]` | facultatif : omettez-le, ou tapez-le comme indiqué |
| `# a note` | un commentaire pour vous : ne le tapez pas |
| `"C:\My Files\x"` | mettez entre guillemets un chemin qui contient des espaces |

## Quand quelque chose ne va pas {#when-something-goes-wrong}

| Le message | Que faire |
|---|---|
| `'python' is not recognized` | Python n'est pas installé, ou la case PATH n'était pas cochée : réinstallez-le et cochez-la (ou tapez `py` au lieu de `python`). |
| `'heat3d-beamng-maps' is not recognized` | Refaites l'étape 4 dans le dossier de l'outil, ou tapez `python -m heat3d_ext_beamng` au lieu de `heat3d-beamng-maps` : cela fait la même chose. |
| `needs 3DHeat GameFiles: ...` | L'étape 4 n'a pas installé GameFiles : lancez `python -m pip install git+https://github.com/Holdi601/3DHeat-GameFiles.git`, ou réglez `HEAT3D_GAMEFILES` sur un dossier GameFiles. |
| `no BeamNG.drive install found in the Steam libraries` | Indiquez le dossier du jeu, celui qui contient `gameengine.zip` : `--install "D:\Games\BeamNG.drive"`. |
| `... is a forza-... lap, not a BeamNG.drive one` | Ce tour vient d'un autre jeu ; le message nomme l'outil qui lui correspond. |
| `the lap does not lie on any installed level's terrain` | Nommez le niveau : `--level <level folder>`, comme la liste de `levels` l'indique. |
| autre chose | Lisez la dernière ligne du message, puis ouvrez un ticket sur GitHub avec cette ligne. |

Chaque commande se termine aussi par un **code de sortie** : 0 veut dire que cela a
réussi, 2 que le jeu, GameFiles ou un fichier BeamNG n'a pas été trouvé, 1 que la
lecture ou l'écriture a échoué. Pour le voir, tapez `echo $LASTEXITCODE` dans
PowerShell, ou `echo $?` sous macOS et Linux.
