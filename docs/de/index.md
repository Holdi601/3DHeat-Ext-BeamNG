---
title: Startseite
nav_order: 1
lang: "de"
source: index.md
source_hash: "fa2c58a5b149"
nav_exclude: true
search_exclude: true
permalink: /de/
---
# 3DHeat BeamNG {#dheat-beamng}

**Was ist das?** Dieses Werkzeug liest ein BeamNG.drive-Level aus **deiner eigenen Installation**
und schneidet das Stück heraus, das du gefahren bist: den Boden mit seiner eingebackenen Textur, die
Straßen, Bordsteine, Leitplanken, Schilder, Gebäude und das Wasser entlang deiner Runde, als eine
3D-Strecke für den [3DHeat](https://github.com/Holdi601/3DHeat)-Viewer
([Dokumentation](https://holdi601.github.io/3DHeat/)).

**Wozu braucht man das?** Um deine BeamNG-Runden auf der echten Straße zu analysieren – Bremspunkte,
Linien und Kurven in 3D – statt auf einer Linie im leeren Raum.

**Beispiel:** `heat3d-beamng-maps course my_lap.json` -> `my_lap.glb`, im selben Koordinatensystem wie
die Runde: Die Datei passt im Rennanalyse-Tab des Viewers unter die Runde, ohne Platzieren oder Skalieren.

## Schnellstart {#quick-start}

Neu bei der Kommandozeile? Lies zuerst [Bevor du anfängst](before-you-start.md).
Du brauchst Python 3.10 oder neuer, BeamNG.drive, eine darin aufgenommene Runde und
[3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/) (wird mit diesem Werkzeug installiert).
Führe diese Befehle in dem Ordner aus, den du geklont oder entpackt hast:

```bash
python -m pip install -e .                      # installs the heat3d-beamng-maps command
heat3d-beamng-maps levels                       # where BeamNG.drive is, and its levels
heat3d-beamng-maps course my_lap.json           # the course around that lap
```

Die Runde stammt vom 3DHeat-GameCapture-Recorder und seinem BeamNG-Mod
([Telemetrie: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html)).
`course` findet das Level anhand der Runde und endet mit
`wrote my_lap.glb (... bytes)`. Lade die `.glb`-Datei im Viewer im Panel **Hintergrund / Level**
mit **3D-Modell…**.

Die Strecke wird aus den Dateien des Spiels gebaut. Sie bleibt **auf deinem Rechner**, zum
Anschauen, nicht zum Teilen oder Veröffentlichen ([Bedingungen](terms.md)).

Jeder Spiele-Leser ist ein eigenes kleines Projekt mit eigener Lizenzdatei, eigenen Releases und eigenem Issue-Tracker. So lässt er sich für sich allein installieren, aktualisieren und pflegen - oder auf Wunsch eines Rechteinhabers zurückziehen -, ohne dass der Viewer oder die anderen Werkzeuge davon berührt werden.

## Seiten {#pages}

| Seite | Was sie behandelt |
|---|---|
| [Bevor du anfängst](before-you-start.md) | Python, GameFiles, ein Terminal, ein erster Lauf |
| [Streckenexport: course](course-beamng.md) | wie aus einer Runde eine Strecke wird: die Installation, das Level, Boden, Straßen, Modelle, Wasser |
| [Das Spiel finden: levels](levels.md) | wo BeamNG.drive gefunden wird, was `levels` ausgibt |
| [Was ist diese Datei: identify](identify.md) | eine `.cdae`-Form, ein `.ter`-Gelände oder ein Level-Zip |
| [BeamNG-Dateien](reader-beamng.md) | die Dateiformate im Detail |
| [Bedingungen und Lizenz](terms.md) | BeamNGs Inhalte, die Formate, ein Projekt für sich |
| [Befehlsreferenz](../cli-reference.md) | jede Option, aus dem Code erzeugt |
| [Diese Doku pflegen](maintaining.md) | die Checkliste für Releases |

## Verwandtes {#related}

- Der 3DHeat-Viewer: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  Dokumentation unter [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- BeamNG-Runden aufnehmen: der GameCapture-Recorder und sein BeamNG-Mod,
  [Telemetrie: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html).
- Die Bibliothek, auf der dieses Werkzeug aufbaut, und ihr `course`-Befehl, der BeamNG-Runden an dieses
  Werkzeug übergibt: [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/).

## Die 3DHeat-Werkzeuge {#the-3dheat-tools}

| Werkzeug | Was es tut | Code | Doku |
|---|---|---|---|
| 3DHeat-Viewer | zeigt die Daten: Heatmaps, Rennanalyse, Match-Auswertung | [3DHeat](https://github.com/Holdi601/3DHeat) | [Doku](https://holdi601.github.io/3DHeat/) |
| GameFiles | Level und Strecken aus den eigenen Dateien eines Spiels | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [Doku](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | Runden-Telemetrie und Level, die aus Spielvideos nachgebaut werden | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [Doku](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | ein Unreal-Editor-Plugin: ein Level als eine `.glb`-Datei | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [Doku](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | Counter-Strike-2-Demos und Karten | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [Doku](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | zeichnet auf, was Spiele veröffentlichen, während du spielst | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [Doku](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | War-Thunder-Replays | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [Doku](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | World-of-Tanks-Replays | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [Doku](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | World-of-Warships-Replays | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [Doku](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | Squad-Serverdemos | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [Doku](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | DCS-World-Karten als 3D-Level | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [Doku](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | IL-2-Sturmovik-Karten als 3D-Level | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [Doku](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | die Dota-2-Karte als 3D-Level | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [Doku](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | Dota-2-Replays als Tabellen | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [Doku](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | League-of-Legends- und VALORANT-Replays | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [Doku](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | Forza-Horizon-Strecken und -Autos | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [Doku](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | Battlefield-6-Level als 3D-Level | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [Doku](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | BeamNG.drive-Strecken rund um deine Runden | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [Doku](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | Assetto-Corsa-Rally-Etappen rund um deine Runden | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [Doku](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | Arma-Reforger-Welten als 3D-Level | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [Doku](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | Rainbow-Six-Siege-Match-Replays | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [Doku](https://holdi601.github.io/3DHeat-Ext-R6/) |
