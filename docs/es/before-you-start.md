---
title: Antes de empezar
nav_order: 1.5
lang: "es"
source: before-you-start.md
source_hash: "97e80f09283e"
nav_exclude: true
search_exclude: true
---
# Antes de empezar {#before-you-start}

¿Nunca has usado la línea de comandos? Esta página te lleva de cero a tu primera ejecución.
Tarda unos quince minutos, una sola vez.

## 1. Instalar Python {#install-python}

Esta herramienta necesita **Python 3.10 o posterior**.

- **Windows:** descarga Python desde [python.org/downloads](https://www.python.org/downloads/)
  y ejecuta el instalador. En su primera pantalla, marca **Add python.exe to PATH**
  y luego haz clic en **Install Now**.
- **macOS y Linux:** Python 3 suele estar ya instalado. Donde estas páginas dicen
  `python`, escribe `python3`.

## 2. Obtener esta herramienta {#get-this-tool}

Abre [github.com/Holdi601/3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG), haz clic en el
botón verde **Code** y luego en **Download ZIP**, y descomprímelo en una carpeta de tu
elección. Si usas git: `git clone https://github.com/Holdi601/3DHeat-Ext-BeamNG`.

## 3. Abrir una terminal en esa carpeta {#open-a-terminal-in-that-folder}

Una terminal es una ventana donde escribes comandos.

- **Windows:** abre la carpeta en el Explorador, haz clic en la barra de direcciones, escribe
  `powershell` y pulsa Intro. Se abre una ventana azul o negra, ya dentro de
  esa carpeta.
- **macOS:** abre **Terminal**, escribe `cd ` (con un espacio), arrastra la carpeta a
  la ventana y pulsa Intro.

`cd` significa "cambiar de carpeta": `cd C:\Tools\3DHeat-Ext-BeamNG` va a esa carpeta.

## 4. Instalar la herramienta {#install-the-tool}

Escribe esto y pulsa Intro:

```bash
python -m pip install -e .
```

Esto también instala [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/),
la biblioteca en la que se basan los lectores, además de numpy, Pillow, msgpack y zstandard.
Al final deberías ver: `Successfully installed ... heat3d-ext-beamng-...`.

¿Ya tienes una copia de GameFiles? La herramienta también la encuentra sin pip: en la
carpeta que indica la variable de entorno `HEAT3D_GAMEFILES`, dentro de una copia
de 3DHeat (`exporters/gamefiles`), o en una carpeta `3DHeat-GameFiles` junto
a esta.

## 5. Comprobar que se encuentra el juego {#check-that-the-game-is-found}

```bash
heat3d-beamng-maps levels
```

Deberías ver algo parecido a:

```text
BeamNG.drive at C:\Program Files (x86)\Steam\steamapps\common\BeamNG.drive
  example_level
  ...
12 levels, with mods
```

## 6. Grabar una vuelta y exportar su recorrido {#record-a-lap-then-export-its-course}

Graba una vuelta con el grabador 3DHeat GameCapture y su mod para BeamNG
([Telemetría: BeamNG.drive](https://holdi601.github.io/3DHeat-GameCapture/telemetry-beamng.html)),
y después:

```bash
heat3d-beamng-maps course laps\my_lap.json
```

Siguiente: [Exportar el recorrido](course-beamng.md).

## Cómo leer los comandos de estas páginas {#how-to-read-the-commands-on-these-pages}

| Lo que ves | Significa |
|---|---|
| `<level folder>` | un marcador: escribe tu propio valor en su lugar, sin los `< >` |
| `[--install FOLDER]` | opcional: omítelo, o escríbelo tal como aparece |
| `# a note` | un comentario para ti: no lo escribas |
| `"C:\My Files\x"` | pon entre comillas una ruta que tenga espacios |

## Cuando algo sale mal {#when-something-goes-wrong}

| El mensaje | Qué hacer |
|---|---|
| `'python' is not recognized` | Python no está instalado, o no se marcó la casilla PATH: instálalo de nuevo y márcala (o escribe `py` en lugar de `python`). |
| `'heat3d-beamng-maps' is not recognized` | Vuelve a ejecutar el paso 4 en la carpeta de la herramienta, o escribe `python -m heat3d_ext_beamng` en lugar de `heat3d-beamng-maps`: hace lo mismo. |
| `needs 3DHeat GameFiles: ...` | El paso 4 no instaló GameFiles: ejecuta `python -m pip install git+https://github.com/Holdi601/3DHeat-GameFiles.git`, o define `HEAT3D_GAMEFILES` con una carpeta de GameFiles. |
| `no BeamNG.drive install found in the Steam libraries` | Indica la carpeta del juego, la que contiene `gameengine.zip`: `--install "D:\Games\BeamNG.drive"`. |
| `... is a forza-... lap, not a BeamNG.drive one` | Esa vuelta es de otro juego; el mensaje indica la herramienta que le corresponde. |
| `the lap does not lie on any installed level's terrain` | Indica el nivel: `--level <level folder>`, tal como lo muestra `levels`. |
| cualquier otro caso | Lee la última línea del mensaje y abre un issue en GitHub con ella. |

Todos los comandos terminan también con un **código de salida**: 0 significa que funcionó, 2 que
no se encontró el juego, GameFiles o un archivo de BeamNG, y 1 que falló la lectura o la
escritura. Para verlo, escribe `echo $LASTEXITCODE` en PowerShell, o `echo $?` en
macOS y Linux.
