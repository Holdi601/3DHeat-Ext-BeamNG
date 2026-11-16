---
title: "Trovare il gioco: levels"
nav_order: 3
lang: "it"
source: levels.md
source_hash: "7b7b8d5cee93"
nav_exclude: true
search_exclude: true
---
# Trovare il gioco: `levels` {#finding-the-game-levels}

```bash
heat3d-beamng-maps levels [--install FOLDER]
```

stampa dove è installato BeamNG.drive e ogni livello che può montare, compresi
i livelli delle tue mod, con il nome della cartella che accetta `course --level`. Eseguilo per primo:
quando elenca i livelli e termina con 0, [`course`](course-beamng.md) ha il gioco di cui ha bisogno.

```text
BeamNG.drive at C:\Program Files (x86)\Steam\steamapps\common\BeamNG.drive
  example_level
  ...
12 levels, with mods
```

## Dove viene cercato il gioco {#where-the-game-is-looked-for}

Per prima cosa `--install`: la cartella che contiene `gameengine.zip` e `content`. Senza di esso,
`steamapps\common\BeamNG.drive` in ogni libreria di Steam: la cartella di Steam stessa
(dal registro, altrimenti nei soliti posti) e ogni libreria elencata nel suo
`steamapps\libraryfolders.vdf`. Viene usata la prima cartella che contiene entrambi.
Anche `course` cerca nello stesso posto.

I tuoi contenuti (mod, mod non compresse e una cartella `levels` dell'utente) vengono letti da
`%LOCALAPPDATA%\BeamNG\BeamNG.drive` e `%LOCALAPPDATA%\BeamNG.drive`, come spiega
[Esportazione del percorso](course-beamng.md#the-file-system).

## Messaggi e stato di uscita {#messages-and-exit-status}

| Messaggio | Uscita | Significa |
|---|---|---|
| `heat3d-beamng-maps: no BeamNG.drive install found in the Steam libraries. ...` | 2 | installa il gioco tramite Steam, oppure passa `--install` |
| `heat3d-beamng-maps: no BeamNG.drive in <folder> ...` | 2 | `--install` punta a un posto senza `gameengine.zip` e `content` |
| `0 levels, with mods` | 2 | il gioco è stato trovato, ma nessun livello ha una scena |
| `heat3d-beamng-maps: <reason>` | 1 | non è stato possibile leggere un archivio |
