---
title: "Quel est ce fichier : identify"
nav_order: 4
lang: "fr"
source: identify.md
source_hash: "a6ea1b58215b"
nav_exclude: true
search_exclude: true
---
# Quel est ce fichier : `identify` {#what-is-this-file-identify}

```bash
heat3d-beamng-maps identify <path>
```

indique si un fichier appartient à BeamNG.drive, et ce qu'il contient. Il se fie aux
octets, pas à l'extension :

| Fichier | Reconnu par |
|---|---|
| une forme compilée, `.cdae` | sa version (31) et une forme qui se lit correctement |
| un terrain, `.ter` | pas de signature : la taille, les hauteurs, la carte des couches et les noms des couches doivent tous concorder |
| le `.zip` d'un niveau | des entrées sous `levels/<name>/` |

```text
rail.cdae  (1,234 bytes)
  BeamNG.drive shape (.cdae), version 31
    meshes     2
    detail     1 drawn levels
    materials  rail_mat
```

Tout le reste affiche `not a BeamNG.drive file: <name>` sur la sortie d'erreur et se
termine avec le code 2 ; un fichier absent affiche `no such file` et se termine avec le code 2.
La commande `identify` de 3DHeat GameFiles interroge cet outil sur les fichiers que ses
propres lecteurs de moteur ne connaissent pas. Les formats sont décrits dans
[Fichiers BeamNG](reader-beamng.md).
