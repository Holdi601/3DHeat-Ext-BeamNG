---
title: Bevor du anfängst
nav_order: 1.5
lang: "de"
source: before-you-start.md
source_hash: "97e80f09283e"
nav_exclude: true
search_exclude: true
---
# Bevor du anfängst {#before-you-start}

Neu bei der Kommandozeile? Diese Seite führt dich von null bis zum ersten Lauf.
Es dauert einmalig etwa fünfzehn Minuten.

## 1. Python installieren {#install-python}

Dieses Werkzeug braucht **Python 3.10 oder neuer**.

- **Windows:** Lade Python von [python.org/downloads](https://www.python.org/downloads/)
  herunter und starte das Installationsprogramm. Setze auf dem ersten Bildschirm das Häkchen bei
  **Add python.exe to PATH** und klicke dann auf **Install Now**.
- **macOS und Linux:** Python 3 ist oft schon vorhanden. Wo diese Seiten
  `python` schreiben, tippe `python3`.

## 2. Dieses Werkzeug holen {#get-this-tool}

Öffne [github.com/Holdi601/3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG), klicke auf den
grünen Button **Code** und dann auf **Download ZIP**. Entpacke das Archiv in einen Ordner
deiner Wahl. Wenn du git benutzt: `git clone https://github.com/Holdi601/3DHeat-Ext-BeamNG`.

## 3. Ein Terminal in diesem Ordner öffnen {#open-a-terminal-in-that-folder}

Ein Terminal ist ein Fenster, in das du Befehle tippst.

- **Windows:** Öffne den Ordner im Explorer, klicke in die Adresszeile, tippe
  `powershell` und drücke Enter. Ein blaues oder schwarzes Fenster öffnet sich, schon im
  richtigen Ordner.
- **macOS:** Öffne **Terminal**, tippe `cd ` (mit Leerzeichen), ziehe den Ordner in das
  Fenster und drücke Enter.

`cd` heißt „Ordner wechseln“: `cd C:\Tools\3DHeat-Ext-BeamNG` geht in diesen Ordner.

## 4. Das Werkzeug installieren {#install-the-tool}

Tippe das und drücke Enter:

```bash
python -m pip install -e .
```

Dabei wird auch [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/) installiert,
die Bibliothek, auf der die Leser aufbauen, sowie numpy, Pillow, msgpack und zstandard.
Am Ende solltest du sehen: `Successfully installed ... heat3d-ext-beamng-...`.

Du hast schon eine GameFiles-Kopie? Das Werkzeug findet sie auch ohne pip: in dem Ordner,
den die Umgebungsvariable `HEAT3D_GAMEFILES` nennt, in einer 3DHeat-Kopie
(`exporters/gamefiles`) oder in einem Ordner `3DHeat-GameFiles` neben diesem.

## 5. Prüfen, ob das Spiel gefunden wird {#check-that-the-game-is-found}

```bash
heat3d-beamng-maps levels
```

Du solltest etwa so etwas sehen:

```text
BeamNG.drive at C:\Program Files (x86)\Steam\steamapps\common\BeamNG.drive
  example_level
  ...
12 levels, with mods
```

## 6. Eine Runde aufnehmen, dann ihren Kurs exportieren {#record-a-lap-then-export-its-course}

Nimm eine Runde mit dem 3DHeat-GameCapture-Recorder und seinem BeamNG-Mod auf
([Telemetrie: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html)).
Dann:

```bash
heat3d-beamng-maps course laps\my_lap.json
```

Weiter: [Streckenexport](course-beamng.md).

## So liest du die Befehle auf diesen Seiten {#how-to-read-the-commands-on-these-pages}

| Du siehst | Es bedeutet |
|---|---|
| `<level folder>` | ein Platzhalter: Tippe stattdessen deinen eigenen Wert, ohne die `< >` |
| `[--install FOLDER]` | optional: Lass es weg, oder tippe es wie gezeigt |
| `# a note` | ein Kommentar für dich: nicht eintippen |
| `"C:\My Files\x"` | ein Pfad mit Leerzeichen kommt in Anführungszeichen |

## Wenn etwas schiefgeht {#when-something-goes-wrong}

| Die Meldung | Was zu tun ist |
|---|---|
| `'python' is not recognized` | Python ist nicht installiert, oder das Kästchen PATH war nicht angehakt: Installiere es neu und hake es an (oder tippe `py` statt `python`). |
| `'heat3d-beamng-maps' is not recognized` | Führe Schritt 4 im Ordner des Werkzeugs noch einmal aus, oder tippe `python -m heat3d_ext_beamng` statt `heat3d-beamng-maps`: Das tut dasselbe. |
| `needs 3DHeat GameFiles: ...` | Schritt 4 hat GameFiles nicht installiert: Führe `python -m pip install git+https://github.com/Holdi601/3DHeat-GameFiles.git` aus, oder setze `HEAT3D_GAMEFILES` auf einen GameFiles-Ordner. |
| `no BeamNG.drive install found in the Steam libraries` | Gib den Ordner des Spiels an, also den, der `gameengine.zip` enthält: `--install "D:\Games\BeamNG.drive"`. |
| `... is a forza-... lap, not a BeamNG.drive one` | Diese Runde stammt aus einem anderen Spiel; die Meldung nennt das Werkzeug dafür. |
| `the lap does not lie on any installed level's terrain` | Nenne das Level: `--level <level folder>`, so wie `levels` es auflistet. |
| alles andere | Lies die letzte Zeile der Meldung und eröffne damit ein Issue auf GitHub. |

Jeder Befehl endet außerdem mit einem **Exit-Status**: 0 heißt, es hat geklappt; 2 heißt, das
Spiel, GameFiles oder eine BeamNG-Datei wurde nicht gefunden; 1 heißt, Lesen oder Schreiben
ist fehlgeschlagen. Um ihn zu sehen, tippe `echo $LASTEXITCODE` in PowerShell oder `echo $?`
unter macOS und Linux.
