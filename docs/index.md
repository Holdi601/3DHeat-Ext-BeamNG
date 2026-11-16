---
title: Home
nav_order: 1
---

# 3DHeat BeamNG

**What is it?** This tool reads a BeamNG.drive level from **your own install**
and cuts out the stretch you drove: the ground with its baked texture, the
roads, kerbs, barriers, signs, buildings and water along your lap, as one 3D
course for the [3DHeat](https://github.com/Holdi601/3DHeat) viewer
([documentation](https://holdi601.github.io/3DHeat/)).

**Why would I use it?** To analyse your BeamNG laps on the real road - braking
points, lines and corners in 3D - instead of on a line in empty space.

**Example:** `heat3d-beamng-maps course my_lap.json` -> `my_lap.glb`, in the
same frame as the lap: it drops into the viewer's Race tab under the lap with
no placing or scaling.

## Quick start

New to the command line? Read [Before you start](before-you-start.md) first.
You need Python 3.10 or later, BeamNG.drive, a lap recorded in it, and
[3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/) (installed
with this tool). Run these in the folder you cloned or unzipped:

```bash
python -m pip install -e .                      # installs the heat3d-beamng-maps command
heat3d-beamng-maps levels                       # where BeamNG.drive is, and its levels
heat3d-beamng-maps course my_lap.json           # the course around that lap
```

The lap comes from the 3DHeat GameCapture recorder and its BeamNG mod
([Telemetry: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html)).
`course` finds the level from the lap and ends with
`wrote my_lap.glb (... bytes)`. Load the `.glb` in the viewer's
**Background / level** panel with **3D model…**.

The course is built from the game's files: it stays **on your machine**, to
view, not to share or publish ([Terms](terms.md)).

Each game reader is its own small project with its own licence file, releases
and issue tracker, so it can be installed, updated, maintained - or withdrawn
on a rights holder's request - on its own, without affecting the viewer or the
other tools.

## Pages

| Page | What it covers |
|---|---|
| [Before you start](before-you-start.md) | Python, GameFiles, a terminal, a first run |
| [Course export: course](course-beamng.md) | how a lap becomes a course: the install, the level, ground, roads, models, water |
| [Finding the game: levels](levels.md) | where BeamNG.drive is found, what `levels` prints |
| [What is this file: identify](identify.md) | a `.cdae` shape, a `.ter` terrain or a level zip |
| [BeamNG files](reader-beamng.md) | the file formats in detail |
| [Terms and licence](terms.md) | BeamNG's content, the formats, a project of its own |
| [Command reference](cli-reference.md) | every option, generated from the code |
| [Maintaining these docs](maintaining.md) | the release checklist |

## Related

- The 3DHeat viewer: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentation at [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Recording BeamNG laps: the GameCapture recorder and its BeamNG mod,
  [Telemetry: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html).
- The library this tool builds on, and its `course` command, which hands
  BeamNG laps to this tool: [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/).

## The 3DHeat tools

| Tool | What it does | Code | Docs |
|---|---|---|---|
| 3DHeat viewer | shows the data: heatmaps, race analysis, match review | [3DHeat](https://github.com/Holdi601/3DHeat) | [docs](https://holdi601.github.io/3DHeat/) |
| GameFiles | levels and courses from a game's own files | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [docs](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | lap telemetry, and levels rebuilt from gameplay video | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [docs](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | an Unreal Editor plugin: a level as one `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [docs](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | Counter-Strike 2 demos and maps | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [docs](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | records what games publish while you play | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [docs](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | War Thunder replays | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [docs](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | World of Tanks replays | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [docs](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | World of Warships replays | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [docs](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | Squad server demos | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [docs](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | DCS World maps as 3D levels | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [docs](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | IL-2 Sturmovik maps as 3D levels | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [docs](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | the Dota 2 map as a 3D level | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [docs](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | Dota 2 replays as tables | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [docs](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | League of Legends and VALORANT replays | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [docs](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | Forza Horizon courses and cars | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [docs](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | Battlefield 6 levels as 3D levels | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [docs](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | BeamNG.drive courses around your laps | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [docs](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | Assetto Corsa Rally stages around your laps | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [docs](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | Arma Reforger worlds as 3D levels | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [docs](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | Rainbow Six Siege match replays | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [docs](https://holdi601.github.io/3DHeat-Ext-R6/) |
