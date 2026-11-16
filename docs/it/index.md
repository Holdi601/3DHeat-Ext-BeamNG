---
title: Home
nav_order: 1
lang: "it"
source: index.md
source_hash: "fdb34c981312"
nav_exclude: true
search_exclude: true
permalink: /it/
---
# 3DHeat BeamNG {#dheat-beamng}

**Che cos'è?** Questo strumento legge un livello di BeamNG.drive dalla **tua installazione**
e ritaglia il tratto che hai percorso: il terreno con la sua texture cotta, le strade,
i cordoli, le barriere, i cartelli, gli edifici e l'acqua lungo il tuo giro, come un unico
percorso 3D per il visualizzatore [3DHeat](https://github.com/Holdi601/3DHeat)
([documentazione](https://holdi601.github.io/3DHeat/)).

**Perché usarlo?** Per analizzare i tuoi giri di BeamNG sulla strada vera - punti di frenata, traiettorie e
curve in 3D - invece che su una linea nel vuoto.

**Esempio:** `heat3d-beamng-maps course my_lap.json` -> `my_lap.glb`, nello stesso sistema di riferimento del giro:
entra nella scheda Analisi di gara del visualizzatore sotto il giro, senza dover posizionarlo né ridimensionarlo.

## Avvio rapido {#quick-start}

Non hai mai usato la riga di comando? Leggi prima [Prima di iniziare](before-you-start.md).
Ti servono Python 3.10 o successivo, BeamNG.drive, un giro registrato con quel gioco e
[3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/) (installato
con questo strumento). Esegui questi comandi nella cartella in cui hai clonato o decompresso lo strumento:

```bash
python -m pip install -e .                      # installs the heat3d-beamng-maps command
heat3d-beamng-maps levels                       # where BeamNG.drive is, and its levels
heat3d-beamng-maps course my_lap.json           # the course around that lap
```

Il giro viene dal recorder 3DHeat GameCapture e dalla sua mod per BeamNG
([Telemetria: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html)).
`course` trova il livello a partire dal giro e termina con
`wrote my_lap.glb (... bytes)`. Carica il `.glb` nel pannello **Sfondo / livello**
del visualizzatore con **Modello 3D…**.

Il percorso è costruito a partire dai file del gioco: resta **sul tuo computer**, per
guardarlo, non per condividerlo o pubblicarlo ([Termini](terms.md)).

## Pagine {#pages}

| Pagina | Cosa contiene |
|---|---|
| [Prima di iniziare](before-you-start.md) | Python, GameFiles, un terminale, una prima esecuzione |
| [Esportazione del percorso: course](course-beamng.md) | come un giro diventa un percorso: l'installazione, il livello, il suolo, le strade, i modelli, l'acqua |
| [Trovare il gioco: levels](levels.md) | dove viene trovato BeamNG.drive, cosa stampa `levels` |
| [Che file è questo: identify](identify.md) | una forma `.cdae`, un terreno `.ter` o uno zip di livello |
| [File di BeamNG](reader-beamng.md) | i formati dei file in dettaglio |
| [Termini e licenza](terms.md) | i contenuti di BeamNG, i formati, perché questo è un pacchetto separato |
| [Riferimento dei comandi](../cli-reference.md) | ogni opzione, generata dal codice |
| [Manutenzione di queste pagine](maintaining.md) | la checklist di rilascio |

## Collegamenti {#related}

- Il visualizzatore 3DHeat: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentazione su [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Registrare i giri di BeamNG: il recorder GameCapture e la sua mod per BeamNG,
  [Telemetria: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html).
- La libreria su cui si basa questo strumento, e il suo comando `course`, che passa a questo strumento
  i giri di BeamNG: [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/).

## Gli strumenti 3DHeat {#the-3dheat-tools}

| Strumento | Cosa fa | Codice | Documentazione |
|---|---|---|---|
| Visualizzatore 3DHeat | mostra i dati: mappe di calore, analisi di gara, revisione delle partite | [3DHeat](https://github.com/Holdi601/3DHeat) | [docs](https://holdi601.github.io/3DHeat/) |
| GameFiles | livelli e percorsi dai file propri di un gioco | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [docs](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | telemetria dei giri, e livelli ricostruiti dai video di gioco | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [docs](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | un plugin per Unreal Editor: un livello come un unico `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [docs](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | demo e mappe di Counter-Strike 2 | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [docs](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | registra ciò che i giochi pubblicano mentre giochi | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [docs](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | replay di War Thunder | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [docs](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | replay di World of Tanks | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [docs](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | replay di World of Warships | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [docs](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | demo dei server di Squad | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [docs](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | mappe di DCS World come livelli 3D | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [docs](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | mappe di IL-2 Sturmovik come livelli 3D | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [docs](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | la mappa di Dota 2 come livello 3D | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [docs](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | replay di Dota 2 come tabelle | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [docs](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | replay di League of Legends e VALORANT | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [docs](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | percorsi e auto di Forza Horizon | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [docs](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | livelli di Battlefield 6 come livelli 3D | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [docs](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | percorsi di BeamNG.drive intorno ai tuoi giri | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [docs](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | tappe di Assetto Corsa Rally intorno ai tuoi giri | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [docs](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | mondi di Arma Reforger come livelli 3D | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [docs](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | replay di partite di Rainbow Six Siege | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [docs](https://holdi601.github.io/3DHeat-Ext-R6/) |
