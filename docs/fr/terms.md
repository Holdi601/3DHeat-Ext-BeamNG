---
title: "Conditions et licence"
nav_order: 9
lang: "fr"
source: terms.md
source_hash: "f80913a345e5"
nav_exclude: true
search_exclude: true
---
# Conditions et licence {#terms-and-licence}

## Le contenu de BeamNG {#beamngs-content}

BeamNG.drive et ses niveaux appartiennent à BeamNG GmbH. 3DHeat BeamNG n'est ni affilié à BeamNG
GmbH ni soutenu par elle. BeamNG.drive ainsi que les noms et marques associés appartiennent à leurs
propriétaires.

Cet outil ne livre rien du jeu et ne télécharge rien : ni ressources du jeu, ni code du jeu, ni
DLL. Il lit les fichiers de la copie **que vous** avez installée, sur votre machine, en dehors du
jeu. Il ne modifie rien dans le jeu et ne parle à aucun serveur. Un parcours qu'il écrit est découpé
dans le niveau de BeamNG et reste sur votre machine, pour analyser vos propres tours ; merci de ne
pas le partager ni le publier.

Chaque lecteur de jeu est un petit projet à part, avec son propre fichier de licence, ses propres versions et son propre suivi des tickets : il peut être installé, mis à jour, maintenu - ou retiré à la demande d'un ayant droit - seul, sans toucher au visualiseur ni aux autres outils.

Ayants droit : ouvrez un ticket sur [github.com/Holdi601/3DHeat-Ext-BeamNG/issues](https://github.com/Holdi601/3DHeat-Ext-BeamNG/issues) - nous répondons rapidement et retirons tout ce qui est demandé.

Les règles de 3DHeat GameFiles s'appliquent ici sans changement
([Règles et licences](https://holdi601.github.io/3DHeat-GameFiles/rules-and-licences.html)) :

- **Vos fichiers.** L'outil lit les fichiers du jeu installés sur votre
  machine. Il ne télécharge jamais de contenu du jeu.
- **Le résultat n'est pas destiné à être redistribué.** Gardez les `.glb` exportés, et les textures
  qu'ils contiennent, pour votre propre analyse. Ne publiez, ne partagez ni ne vendez les parcours,
  niveaux, modèles ou textures exportés. Le `.gitignore` du dépôt tient les fichiers du jeu, les
  exports et les tours hors du contrôle de version.
- **Aucune clé.** BeamNG livre de simples archives zip ; rien n'est chiffré, et rien ici ne déchiffre.

## Les formats {#the-formats}

BeamNG livre de simples archives zip : il n'y a donc aucun conteneur à rétro-concevoir. BeamNG publie
la structure de ses fichiers `.cdae`, et le lecteur la suit. Le terrain `.ter`, les fichiers de scène
et les matériaux ont été lus dans les niveaux livrés, puis vérifiés sur eux
([Fichiers BeamNG](reader-beamng.md)).

## Licence et sources {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-BeamNG/blob/main/LICENSE)). Nécessite
3DHeat GameFiles (MIT), numpy (BSD-3-Clause), Pillow (MIT-CMU), msgpack (Apache-2.0) et zstandard
(BSD-3-Clause) ; les tests nécessitent pytest (MIT). Voir
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-BeamNG/blob/main/LICENSES.md).
Écrit pour ce projet ; aucun code n'a été repris d'un autre projet.
