---
title: Condiciones y licencias
nav_order: 9
lang: "es"
source: terms.md
source_hash: "d94421d4d212"
nav_exclude: true
search_exclude: true
---
# Condiciones y licencias {#terms-and-licence}

## El contenido de BeamNG {#beamngs-content}

BeamNG.drive y sus niveles pertenecen a BeamNG GmbH, que no respalda este proyecto. Esta
herramienta no incluye nada del juego ni descarga nada: lee los archivos de la copia que **tú**
instalaste, en tu equipo, al margen del juego. No cambia nada en el juego ni se comunica
con ningún servidor. Un recorrido que escribe es una derivada del nivel de BeamNG: es tuyo para
analizar tus propias vueltas, no para compartirlo ni publicarlo. Usar la herramienta es
decisión tuya, bajo las condiciones que aceptaste para el juego.

Por eso es un paquete aparte: si BeamNG alguna vez pide que se retire, se retira sola, y el
visor, GameFiles y las demás herramientas se quedan.

Las normas de 3DHeat GameFiles se aplican aquí sin cambios
([Normas y licencias](https://holdi601.github.io/3DHeat-GameFiles/rules-and-licences.html)):

- **Tus archivos, tu responsabilidad.** La herramienta lee los archivos del juego
  instalados en tu equipo. Nunca descarga contenido del juego.
- **La salida no es para redistribuir.** Guarda los `.glb` exportados, y las texturas
  que contienen, solo para tu propio análisis. No publiques, compartas ni vendas
  recorridos, niveles, modelos ni texturas exportados. El `.gitignore` del repositorio
  mantiene los archivos del juego, las exportaciones y las vueltas fuera del control de versiones.
- **Sin claves.** BeamNG distribuye archivos zip sin cifrar; nada está cifrado y aquí
  no se descifra nada.

## Los formatos {#the-formats}

BeamNG distribuye archivos zip sin cifrar, así que no hay ningún contenedor que tener que
desmontar. BeamNG publica el diseño de sus `.cdae`, y el lector lo sigue. Los
terrenos `.ter`, los archivos de escena y los materiales se leyeron de los niveles incluidos
y se comprobaron contra ellos ([Archivos de BeamNG](reader-beamng.md)).

## Licencia y fuentes {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-BeamNG/blob/main/LICENSE)).
Necesita 3DHeat GameFiles (MIT), numpy (BSD-3-Clause), Pillow (MIT-CMU), msgpack
(Apache-2.0) y zstandard (BSD-3-Clause); las pruebas necesitan pytest (MIT). Mira
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-BeamNG/blob/main/LICENSES.md).
Escrito para este proyecto; no se tomó código de ningún otro proyecto.
