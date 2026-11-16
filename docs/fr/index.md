---
title: Accueil
nav_order: 1
lang: "fr"
source: index.md
source_hash: "fdb34c981312"
nav_exclude: true
search_exclude: true
permalink: /fr/
---
# 3DHeat BeamNG {#dheat-beamng}

**Qu'est-ce que c'est ?** Cet outil lit un niveau de BeamNG.drive depuis **votre propre
installation** et découpe le tronçon que vous avez roulé : le sol avec sa texture cuite, les
routes, bordures, glissières, panneaux, bâtiments et eau le long de votre tour, en un seul
parcours 3D pour le visualiseur [3DHeat](https://github.com/Holdi601/3DHeat)
([documentation](https://holdi601.github.io/3DHeat/)).

**Pourquoi l'utiliser ?** Pour analyser vos tours de BeamNG sur la vraie route - points de
freinage, trajectoires et virages en 3D - au lieu d'une ligne dans le vide.

**Exemple :** `heat3d-beamng-maps course my_lap.json` -> `my_lap.glb`, dans le même repère
que le tour : il s'insère dans l'onglet Analyse de course du visualiseur, sous le tour,
sans placement ni mise à l'échelle.

## Démarrage rapide {#quick-start}

Vous ne connaissez pas la ligne de commande ? Lisez d'abord [Avant de commencer](before-you-start.md).
Il vous faut Python 3.10 ou plus récent, BeamNG.drive, un tour enregistré dedans, et
[3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/) (installé avec cet outil).
Lancez ces commandes dans le dossier où vous avez cloné ou décompressé l'outil :

```bash
python -m pip install -e .                      # installs the heat3d-beamng-maps command
heat3d-beamng-maps levels                       # where BeamNG.drive is, and its levels
heat3d-beamng-maps course my_lap.json           # the course around that lap
```

Le tour vient de l'enregistreur 3DHeat GameCapture et de son mod BeamNG
([Telemetry: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html)).
`course` trouve le niveau à partir du tour et se termine par
`wrote my_lap.glb (... bytes)`. Chargez le `.glb` dans le panneau
**Arrière-plan / niveau** du visualiseur avec **Modèle 3D…**.

Le parcours est construit à partir des fichiers du jeu : il reste **sur votre machine**, pour
le regarder, et non pour le partager ou le publier ([Conditions](terms.md)).

## Pages {#pages}

| Page | Ce qu'elle couvre |
|---|---|
| [Avant de commencer](before-you-start.md) | Python, GameFiles, un terminal, une première exécution |
| [Export de parcours : course](course-beamng.md) | comment un tour devient un parcours : l'installation, le niveau, le sol, les routes, les modèles, l'eau |
| [Trouver le jeu : levels](levels.md) | où est trouvé BeamNG.drive, ce qu'affiche `levels` |
| [Quel est ce fichier : identify](identify.md) | une forme `.cdae`, un terrain `.ter` ou le zip d'un niveau |
| [Fichiers BeamNG](reader-beamng.md) | les formats de fichiers en détail |
| [Conditions et licence](terms.md) | le contenu de BeamNG, les formats, pourquoi c'est un paquet séparé |
| [Référence des commandes](../cli-reference.md) | chaque option, générée depuis le code |
| [Maintenance de ces documents](maintaining.md) | la liste de contrôle de chaque version |

## Liens {#related}

- Le visualiseur 3DHeat : [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentation sur [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Enregistrer des tours de BeamNG : l'enregistreur GameCapture et son mod BeamNG,
  [Telemetry: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html).
- La bibliothèque sur laquelle cet outil s'appuie, et sa commande `course`, qui transmet les
  tours de BeamNG à cet outil : [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/).

## Les outils 3DHeat {#the-3dheat-tools}

| Outil | Ce qu'il fait | Code | Documentation |
|---|---|---|---|
| Visualiseur 3DHeat | affiche les données : cartes de chaleur, analyse de course, revue de match | [3DHeat](https://github.com/Holdi601/3DHeat) | [docs](https://holdi601.github.io/3DHeat/) |
| GameFiles | niveaux et parcours depuis les fichiers propres d'un jeu | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [docs](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | télémétrie des tours, et niveaux reconstruits depuis une vidéo de jeu | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [docs](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | un plugin pour l'éditeur Unreal : un niveau en un seul `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [docs](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | démos et cartes de Counter-Strike 2 | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [docs](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | enregistre ce que les jeux publient pendant que vous jouez | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [docs](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | replays de War Thunder | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [docs](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | replays de World of Tanks | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [docs](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | replays de World of Warships | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [docs](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | démos de serveurs Squad | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [docs](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | cartes de DCS World en niveaux 3D | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [docs](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | cartes d'IL-2 Sturmovik en niveaux 3D | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [docs](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | la carte de Dota 2 en niveau 3D | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [docs](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | replays de Dota 2 sous forme de tableaux | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [docs](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | replays de League of Legends et VALORANT | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [docs](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | parcours et voitures de Forza Horizon | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [docs](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | niveaux de Battlefield 6 en niveaux 3D | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [docs](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | parcours BeamNG.drive autour de vos tours | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [docs](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | étapes d'Assetto Corsa Rally autour de vos tours | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [docs](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | mondes d'Arma Reforger en niveaux 3D | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [docs](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | replays de matchs Rainbow Six Siege | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [docs](https://holdi601.github.io/3DHeat-Ext-R6/) |
