---
title: "Mantener estos documentos"
nav_order: 91
lang: "es"
source: maintaining.md
source_hash: "1d37de5d268d"
nav_exclude: true
search_exclude: true
---
# Mantener estos documentos {#maintaining-these-docs}

Una lista de comprobaciones para cada versión, para que las páginas nunca se queden atrás del código.

1. **Regenerar la referencia.** `python tools/gen_docs_reference.py` reescribe
   [Referencia de comandos](../cli-reference.md) a partir del `--help` del propio programa y de
   sus columnas de salida. `python tools/gen_docs_reference.py --check` sale con código 1 cuando
   la página guardada en el repositorio está desactualizada.
2. **Listar lo que cambió.** `git log v<VERSION>..HEAD --oneline`, donde
   `<VERSION>` es la última versión publicada (el archivo `VERSION` en la publicación). Dale a cada
   función nueva, opción y columna de salida un lugar en una página, y una fila en la sección **Docs** de
   [`CHANGELOG.md`](https://github.com/Holdi601/3DHeat-Ext-BeamNG/blob/main/CHANGELOG.md).
3. **Revisión independiente.** Alguien que no escribió las páginas lee el
   README y cada página cambiada, también las imágenes, tres veces: como principiante que nunca ha usado
   una terminal, como un niño de 8 años y como experto que comprueba cada opción contra
   `--help`. Los ejemplos usan solo nombres y números inventados.
4. **Corregir** todo lo que encuentre la revisión.
5. **Traducciones.** Cada página traducida guarda el hash de la página inglesa de la que
   procede. Vuelve a traducir las páginas cuyo original en inglés cambió,
   y luego revisa cada idioma: texto claro, etiquetas de los diagramas correctas, y las mismas
   palabras que la interfaz traducida del visor 3DHeat.
6. **Ejecutar las pruebas** (`pytest`).
7. **Subir los cambios** (push) solo con el visto bueno del propietario.

## Traducciones: los comandos {#translations-the-commands}

El sitio está traducido a los 40 idiomas del visor 3DHeat (hasta ahora: la página de recorrido y la de formatos de archivo, en 18 de ellos): el inglés está en
`docs/`, cada otro idioma en `docs/<lang>/` con los mismos nombres de archivo. `tools/docs_i18n.py` lleva la contabilidad:

```bash
python tools/docs_i18n.py hashes             # after any English change: record each page's hash
python tools/docs_i18n.py svg-strings        # after any picture change: the labels to translate
python tools/docs_i18n.py status             # per language: current, outdated, missing pages
python tools/docs_i18n.py todo --lang de     # the German pages to (re)translate
python tools/docs_i18n.py svg-build --lang de    # German pictures from docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stamp the German pages with their English hash
python tools/docs_i18n.py check              # exit 1 when hashes or labels are stale
```

Traduce solo lo que lista `todo`: mantén el Markdown, los enlaces, el código, los nombres de archivo y de columna tal cual,
traduce los títulos y las descripciones de las imágenes, y usa las palabras propias del visor 3DHeat para sus botones
y paneles (su `src/i18n/locales/<lang>/`). Las páginas de referencia generadas y las imágenes de terminal se quedan
en inglés. En el sitio, una traducción desactualizada lo indica y enlaza la página en inglés; una que falta
recurre al inglés. El menú de idiomas del encabezado y la redirección por idioma del navegador en la página de inicio
vienen de `docs/_includes/`.
