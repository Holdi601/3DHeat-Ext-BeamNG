---
title: "Prima di iniziare"
nav_order: 1.5
lang: "it"
source: before-you-start.md
source_hash: "97e80f09283e"
nav_exclude: true
search_exclude: true
---
# Prima di iniziare {#before-you-start}

Non hai mai usato la riga di comando? Questa pagina ti porta da zero alla prima esecuzione.
Ci vogliono circa quindici minuti, una volta sola.

## 1. Installa Python {#install-python}

Questo strumento richiede **Python 3.10 o successivo**.

- **Windows:** scarica Python da [python.org/downloads](https://www.python.org/downloads/)
  ed esegui l'installer. Nella sua prima schermata spunta **Add python.exe to PATH**,
  poi clicca **Install Now**.
- **macOS e Linux:** Python 3 spesso è già presente. Dove queste pagine dicono
  `python`, scrivi `python3`.

## 2. Ottieni questo strumento {#get-this-tool}

Apri [github.com/Holdi601/3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG), clicca il
pulsante verde **Code**, poi **Download ZIP**, e decomprimilo in una cartella a tua scelta. Se usi git:
`git clone https://github.com/Holdi601/3DHeat-Ext-BeamNG`.

## 3. Apri un terminale in quella cartella {#open-a-terminal-in-that-folder}

Un terminale è una finestra in cui scrivi i comandi.

- **Windows:** apri la cartella in Esplora file, clicca nella barra degli indirizzi, scrivi
  `powershell` e premi Invio. Si apre una finestra blu o nera, già dentro quella cartella.
- **macOS:** apri **Terminale**, scrivi `cd ` (con uno spazio), trascina la cartella
  nella finestra e premi Invio.

`cd` vuol dire "cambia cartella": `cd C:\Strumenti\3DHeat-Ext-BeamNG` va in quella cartella.

## 4. Installa lo strumento {#install-the-tool}

Scrivi questo e premi Invio:

```bash
python -m pip install -e .
```

Installa anche [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/),
la libreria su cui si basano i lettori, più numpy, Pillow, msgpack e zstandard.
Alla fine dovresti vedere: `Successfully installed ... heat3d-ext-beamng-...`.

Hai già una copia di GameFiles? Lo strumento la trova anche senza pip: nella cartella
indicata dalla variabile d'ambiente `HEAT3D_GAMEFILES`, dentro una copia di 3DHeat
(`exporters/gamefiles`), oppure in una cartella `3DHeat-GameFiles` accanto a questa.

## 5. Controlla che il gioco venga trovato {#check-that-the-game-is-found}

```bash
heat3d-beamng-maps levels
```

Dovresti vedere qualcosa di simile:

```text
BeamNG.drive at C:\Program Files (x86)\Steam\steamapps\common\BeamNG.drive
  example_level
  ...
12 levels, with mods
```

## 6. Registra un giro, poi esporta il suo percorso {#record-a-lap-then-export-its-course}

Registra un giro con il recorder 3DHeat GameCapture e la sua mod per BeamNG
([Telemetria: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html)),
poi:

```bash
heat3d-beamng-maps course laps\my_lap.json
```

Prossimo passo: [Esportazione del percorso](course-beamng.md).

## Come leggere i comandi di queste pagine {#how-to-read-the-commands-on-these-pages}

| Vedi | Significa |
|---|---|
| `<level folder>` | un segnaposto: scrivi il tuo valore al suo posto, senza i `< >` |
| `[--install FOLDER]` | facoltativo: puoi ometterlo, oppure scriverlo come mostrato |
| `# a note` | un commento per te: non scriverlo |
| `"C:\My Files\x"` | metti tra virgolette un percorso che contiene spazi |

## Quando qualcosa va storto {#when-something-goes-wrong}

| Il messaggio | Cosa fare |
|---|---|
| `'python' is not recognized` | Python non è installato, oppure non hai spuntato la casella PATH: installalo di nuovo e spuntala (oppure scrivi `py` al posto di `python`). |
| `'heat3d-beamng-maps' is not recognized` | Ripeti il passo 4 nella cartella dello strumento, oppure scrivi `python -m heat3d_ext_beamng` al posto di `heat3d-beamng-maps`: fa lo stesso. |
| `needs 3DHeat GameFiles: ...` | Il passo 4 non ha installato GameFiles: esegui `python -m pip install git+https://github.com/Holdi601/3DHeat-GameFiles.git`, oppure imposta `HEAT3D_GAMEFILES` su una cartella di GameFiles. |
| `no BeamNG.drive install found in the Steam libraries` | Indica la cartella del gioco, quella che contiene `gameengine.zip`: `--install "D:\Games\BeamNG.drive"`. |
| `... is a forza-... lap, not a BeamNG.drive one` | Quel giro viene da un altro gioco; il messaggio indica lo strumento giusto per quello. |
| `the lap does not lie on any installed level's terrain` | Indica il livello: `--level <level folder>`, come lo elenca `levels`. |
| qualsiasi altra cosa | Leggi l'ultima riga del messaggio, poi apri una segnalazione su GitHub con quella riga. |

Ogni comando termina anche con uno **stato di uscita**: 0 vuol dire che ha funzionato, 2 che
non è stato trovato il gioco, GameFiles o un file di BeamNG, 1 che la lettura o la scrittura
non è riuscita. Per vederlo, scrivi `echo $LASTEXITCODE` in PowerShell, oppure `echo $?` su
macOS e Linux.
