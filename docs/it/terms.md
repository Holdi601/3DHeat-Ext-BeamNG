---
title: "Termini e licenza"
nav_order: 9
lang: "it"
source: terms.md
source_hash: "d94421d4d212"
nav_exclude: true
search_exclude: true
---
# Termini e licenza {#terms-and-licence}

## I contenuti di BeamNG {#beamngs-content}

BeamNG.drive e i suoi livelli appartengono a BeamNG GmbH, che non approva questo progetto.
Questo strumento non include nulla del gioco e non scarica nulla: legge i file della copia **che
hai** installato, sul tuo computer, al di fuori del gioco. Non modifica nulla nel gioco e non comunica
con nessun server. Un percorso che lo strumento scrive è una derivazione del livello di BeamNG: è tuo per
analizzare i tuoi giri, non per condividerlo o pubblicarlo. Usare lo strumento è una tua decisione,
secondo i termini che hai accettato per il gioco.

Per questo è un pacchetto separato: se BeamNG dovesse chiederne la rimozione, va via da solo,
e il visualizzatore, GameFiles e gli altri strumenti restano.

Si applicano qui, invariate, le regole di 3DHeat GameFiles
([Regole e licenze](https://holdi601.github.io/3DHeat-GameFiles/rules-and-licences.html)):

- **I tuoi file, la tua responsabilità.** Lo strumento legge i file di gioco installati sul tuo
  computer. Non scarica mai contenuti di gioco.
- **L'output non è da ridistribuire.** Conserva i file `.glb` esportati, e le texture al loro interno,
  per la tua analisi. Non pubblicare, condividere né vendere percorsi, livelli, modelli o texture esportati. Il
  file `.gitignore` del repository tiene fuori dal controllo di versione i file di gioco, le esportazioni e i giri.
- **Nessuna chiave.** BeamNG distribuisce semplici archivi zip; nulla è cifrato, e qui nulla viene decifrato.

## I formati {#the-formats}

BeamNG distribuisce semplici archivi zip, quindi non c'è alcun contenitore da sottoporre a reverse
engineering. BeamNG pubblica la struttura dei suoi file `.cdae`, e il lettore la segue. Il terreno `.ter`,
i file di scena e i materiali sono stati letti dai livelli distribuiti e verificati su di essi
([File di BeamNG](reader-beamng.md)).

## Licenza e fonti {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-BeamNG/blob/main/LICENSE)).
Richiede 3DHeat GameFiles (MIT), numpy (BSD-3-Clause), Pillow (MIT-CMU), msgpack
(Apache-2.0) e zstandard (BSD-3-Clause); i test richiedono pytest (MIT). Vedi
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-BeamNG/blob/main/LICENSES.md).
Scritto per questo progetto; non è stato preso codice da nessun altro progetto.
