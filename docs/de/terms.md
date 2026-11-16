---
title: Bedingungen und Lizenz
nav_order: 9
lang: "de"
source: terms.md
source_hash: "f80913a345e5"
nav_exclude: true
search_exclude: true
---
# Bedingungen und Lizenz {#terms-and-licence}

## BeamNGs Inhalte {#beamngs-content}

BeamNG.drive und seine Level gehören der BeamNG GmbH. 3DHeat BeamNG ist nicht mit der BeamNG GmbH
verbunden und wird von ihr nicht unterstützt. BeamNG.drive und die zugehörigen Namen und Marken
gehören ihren Inhabern.

Dieses Werkzeug liefert nichts vom Spiel mit und lädt nichts herunter: keine Spielinhalte, keinen
Spielcode, keine DLLs. Es liest die Dateien der Kopie, die **du** installiert hast, auf deinem
Rechner, außerhalb des Spiels. Es verändert nichts im Spiel und spricht mit keinem Server. Eine Strecke, die es schreibt,
wird aus dem Level von BeamNG geschnitten und bleibt auf deinem Rechner, zum Analysieren deiner
eigenen Runden; bitte teile oder veröffentliche sie nicht.

Jeder Spiele-Leser ist ein eigenes kleines Projekt mit eigener Lizenzdatei, eigenen Releases und eigenem Issue-Tracker. So lässt er sich für sich allein installieren, aktualisieren und pflegen - oder auf Wunsch eines Rechteinhabers zurückziehen -, ohne dass der Viewer oder die anderen Werkzeuge davon berührt werden.

Rechteinhaber: Bitte ein Issue unter [github.com/Holdi601/3DHeat-Ext-BeamNG/issues](https://github.com/Holdi601/3DHeat-Ext-BeamNG/issues) eröffnen - wir antworten schnell und entfernen auf Anfrage alles.

Die Regeln von 3DHeat GameFiles gelten hier unverändert
([Regeln und Lizenzen](https://holdi601.github.io/3DHeat-GameFiles/rules-and-licences.html)):

- **Deine eigenen Dateien.** Das Werkzeug liest die Spieldateien, die auf deinem
  Rechner installiert sind. Es lädt nie Spielinhalte herunter.
- **Die Ausgabe ist nicht zur Weitergabe bestimmt.** Behalte exportierte `.glb`-Dateien und die Texturen
  darin für deine eigene Analyse. Veröffentliche, teile oder verkaufe keine exportierten Strecken, Level,
  Modelle oder Texturen. Die `.gitignore` des Repositorys hält Spieldateien, Exporte und Runden aus der
  Versionsverwaltung heraus.
- **Keine Schlüssel.** BeamNG liefert einfache Zip-Archive aus; nichts ist verschlüsselt, und hier wird
  nichts entschlüsselt.

## Die Formate {#the-formats}

BeamNG liefert einfache Zip-Archive aus, es gibt also keinen Container, den man rückentwickeln müsste.
BeamNG veröffentlicht sein `.cdae`-Layout, und der Leser folgt ihm. Das `.ter`-Gelände, die
Szenendateien und die Materialien wurden aus den ausgelieferten Leveln gelesen und an ihnen geprüft
([BeamNG-Dateien](reader-beamng.md)).

## Lizenz und Quellen {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-BeamNG/blob/main/LICENSE)).
Benötigt werden 3DHeat GameFiles (MIT), numpy (BSD-3-Clause), Pillow (MIT-CMU), msgpack
(Apache-2.0) und zstandard (BSD-3-Clause); für die Tests pytest (MIT). Siehe
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-BeamNG/blob/main/LICENSES.md).
Für dieses Projekt geschrieben; aus keinem anderen Projekt wurde Code übernommen.
