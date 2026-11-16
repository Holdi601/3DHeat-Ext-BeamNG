---
title: Diese Doku pflegen
nav_order: 91
lang: "de"
source: maintaining.md
source_hash: "1d37de5d268d"
nav_exclude: true
search_exclude: true
---
# Diese Doku pflegen {#maintaining-these-docs}

Eine Checkliste für jedes Release, damit die Seiten nie hinter dem Code zurückbleiben.

1. **Die Referenz neu erzeugen.** `python tools/gen_docs_reference.py` schreibt
   [Befehlsreferenz](../cli-reference.md) aus der `--help` des Programms und seinen
   Ausgabespalten neu. `python tools/gen_docs_reference.py --check` endet mit 1, wenn die
   festgeschriebene Seite veraltet ist.
2. **Auflisten, was sich geändert hat.** `git log v<VERSION>..HEAD --oneline`, wobei
   `<VERSION>` die zuletzt veröffentlichte Version ist (die Datei `VERSION` zum Release). Jede neue
   Funktion, Option und Ausgabespalte bekommt einen Platz auf einer Seite und eine Zeile im Abschnitt
   **Docs** von [`CHANGELOG.md`](https://github.com/Holdi601/3DHeat-Ext-BeamNG/blob/main/CHANGELOG.md).
3. **Unabhängige Prüfung.** Jemand, der die Seiten nicht geschrieben hat, liest README und jede
   geänderte Seite, die Bilder eingeschlossen, dreimal: als Anfänger, der noch nie ein Terminal
   benutzt hat, als Achtjähriger und als Experte, der jede Option gegen `--help` prüft. Beispiele
   verwenden nur erfundene Namen und Zahlen.
4. **Beheben**, was die Prüfung findet.
5. **Übersetzungen.** Jede übersetzte Seite hält den Hash der englischen Seite fest, aus der sie
   entstanden ist. Übersetze die Seiten neu, deren englische Quelle sich geändert hat, und prüfe dann
   jede Sprache: klarer Text, richtige Beschriftungen in den Diagrammen, dieselben Wörter wie die
   übersetzte Oberfläche des Viewers.
6. **Die Tests laufen lassen** (`pytest`).
7. **Erst nach dem Einverständnis des Eigentümers pushen.**

## Übersetzungen: die Befehle {#translations-the-commands}

Die Seite wird in die 40 Sprachen des 3DHeat-Viewers übersetzt (bisher: die Strecken- und
Dateiformat-Seiten, in 18 davon): Englisch in `docs/`, jede andere Sprache in `docs/<lang>/` mit denselben
Dateinamen. `tools/docs_i18n.py` erledigt die Buchführung:

```bash
python tools/docs_i18n.py hashes             # nach jeder englischen Änderung: den Hash jeder Seite festhalten
python tools/docs_i18n.py svg-strings        # nach jeder Bildänderung: die zu übersetzenden Beschriftungen
python tools/docs_i18n.py status             # je Sprache: aktuelle, veraltete und fehlende Seiten
python tools/docs_i18n.py todo --lang de     # die deutschen Seiten, die (neu) übersetzt werden müssen
python tools/docs_i18n.py svg-build --lang de    # deutsche Bilder aus docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # die deutschen Seiten mit ihrem englischen Hash stempeln
python tools/docs_i18n.py check              # endet mit 1, wenn Hashes oder Beschriftungen veraltet sind
```

Übersetze nur, was `todo` auflistet: Markdown, Links, Code, Datei- und Spaltennamen bleiben, wie sie sind.
Übersetze Titel und Bildbeschreibungen, und verwende für Schaltflächen und Panels die eigenen Wörter des
3DHeat-Viewers (seine `src/i18n/locales/<lang>/`). Erzeugte Referenzseiten und Terminal-Bilder bleiben
Englisch. Auf der Website sagt eine veraltete Übersetzung das und verlinkt die englische Seite; fehlt
eine, greift Englisch. Das Sprachmenü im Header und die Weiterleitung der Startseite nach
Browser-Sprache kommen aus `docs/_includes/`.
