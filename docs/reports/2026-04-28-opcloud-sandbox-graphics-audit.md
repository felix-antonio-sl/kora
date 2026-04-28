# Auditoria grafica de OPCloud sandbox

Fecha de captura: 2026-04-28
URL auditada: https://opcloud-sandbox.web.app/

## Alcance

- Se descargo un mirror estatico acotado del deploy publico: HTML entrypoint, bundles CSS/JS same-origin y recursos graficos/font referenciados de forma estatica por esos bundles.
- El mirror local esta en `docs/reports/opcloud-sandbox-graphics-audit/mirror_static/`.
- El mirror binario queda ignorado por Git; el repositorio versiona el script, el manifest, el catalogo y este reporte.
- No hay source maps publicados en el deploy descargado; la auditoria de scripts se hizo sobre bundles compilados/minificados.

## Artefactos generados

- `docs/reports/opcloud-sandbox-graphics-audit/download_opcloud_graphics.py`
- `docs/reports/opcloud-sandbox-graphics-audit/download-manifest.json`
- `docs/reports/opcloud-sandbox-graphics-audit/download-inventory.md`
- `docs/reports/opcloud-sandbox-graphics-audit/asset-catalog.csv`

## Inventario descargado

| Clase | Conteo | Observacion |
|---|---:|---|
| `graphic_asset` | 136 | SVG, PNG, JPG, GIF, ICO usados por toolbar, links OPM, stencil y ayuda visual |
| `font_asset` | 11 | Roboto Condensed, Alegreya Sans, Averia Libre, Material Icons y toolbar icon font |
| `asset_reference_fallback` | 2 | Rutas con extension grafica que devuelven HTML fallback del SPA, no imagen real |
| `script_bundle` | 5 | `main`, `scripts`, `polyfills`, `runtime` y `assets/workers/typings-worker.js` |
| `style_bundle` | 1 | `styles.4e77ba1f976bae6e.css` |
| `data_or_config` | 1 | `assets/config/edx.config.json` |
| `html_entry` | 1 | `index.html` |

Peso local del mirror corregido: 68 MB. Peso de scripts descargados: 29,475,564 bytes. Peso de recursos graficos reales: 39,527,185 bytes. Dos referencias `.png` (`assets/OPM_Links/StructuralAgg.png` y `logo.png`) devolvieron HTML fallback de 54,181 bytes cada una.

## Arquitectura grafica inferida

- La base de diagramacion es JointJS/Rappid: el CSS declara `Rappid v2.0.0 - HTML5 Diagramming Framework` y `main.d9176050fd6f9943.js` contiene referencias directas a `joint.dia`, `joint.ui`, `joint.shapes`, `PaperScroller`, `Stencil`, `Navigator`, `Halo`, `Toolbar` y `Graph`.
- La UI es Angular/Angular Material: el entrypoint monta `opcloud-root`, carga bundles Angular hashados y usa variables MDC/Material en el CSS.
- El canvas operativo se organiza alrededor de `paperScroller`, `paper`, `stencil`, `navigator`, `halo`, `toolbar`, zoom/layout/export y rutas SVG.
- La capa OPM visible se materializa con assets canonicos: `objectDrag.svg`, `processDrag.svg`, `assets/SVG/links/structural/*.svg`, `assets/SVG/links/procedural/*.svg`, `assets/OPM_Links/StructuralAgg.png` y `assets/SVG/list-logical/*`.
- La capa textual OPL esta estilizada en CSS: `.opl .object` usa verde `#00b050` y `.opl .process` usa azul `#0070c0`; ambos truncados a `max-width:20ch`.

## Distribucion de recursos graficos

| Familia | Conteo | Rol |
|---|---:|---|
| `assets/SVG` | 46 | Objetos, procesos, estados, halo, folder/file icons, notas, URL, simulacion, acciones OPM |
| `assets/SVG/links/procedural` | 27 | Agent, consumption, effect, instrument, invocation, relation, condition/event/negation variants |
| `assets/SVG/links/structural` | 4 | Aggregation, classification, exhibition, generalization |
| `assets/gifs` | 40 | Ayuda visual/feature demos: navigator, OPL pane, zoom, unfolding, requirements, units, computation |
| `assets/icons` | 7 | Iconos generales de modo/lista/pin/token/key/select |
| `assets/icons/OPM_Links` | 5 | Sprites PNG para familias de links OPM |
| `assets/icons/essenceAffil` | 4 | Iconos JPG para essence/affiliation de object/process |

## Paleta y sistema visual

- Primario de marca/header: `#1a3763`.
- Acentos Material heredados: `#3f51b5`, `#2979ff`, `#f44336`.
- Neutros y estructura: `#fff`, `#f6f6f6`, `#ecf0f8`, `#d0d8e8`, `#586d8c`, `#8b9094`.
- Seleccion/navigator/puertos: `#31d0c6`, `#00a8ffa6`, glow a `#ff8300`.
- Objetos OPM: SVG rectangular blanco con borde `#70E483`.
- Procesos OPM: SVG eliptico blanco con borde `#3BC3FF`.

## Hallazgos

1. La superficie grafica esta concentrada en un bundle monolitico.
   `main.d9176050fd6f9943.js` pesa 21,963,040 bytes y concentra Joint/Rappid, toolbar, navigator, halo, graph, export, zoom, drag/drop y semantica OPM. Sin source maps, cualquier mantenimiento fino queda obligado a trabajar contra un bundle opaco.

2. La licencia Rappid aparece embebida en el CSS.
   `styles.4e77ba1f976bae6e.css` declara `Rappid v2.0.0` bajo Rappid Academic License. Eso es relevante si se piensa redistribuir mirror, assets o derivados; por eso el mirror binario queda fuera del commit.

3. Hay fuerte dependencia de rutas graficas hard-coded.
   El bundle referencia decenas de rutas `assets/SVG/...`, `assets/gifs/...`, `assets/icons/...` y tres patrones dinamicos no enumerables: `assets/SVG/${handle.svg}.svg`, `assets/SVG/toolbar/{{textAutoFormatHandle.svg}}.svg` y `assets/SVG/toolbar/{{userInputHandle.svg}}.svg`.

4. La carga visual incluye GIFs pesados.
   Los 40 GIFs suman una parte relevante del peso grafico. Los mayores son `opl_pane.gif` (4.7 MB), `handle_navigator.gif` (2.9 MB), `toggle_notes.gif` (2.1 MB) y `create_view.gif` (2.1 MB). Sirven para onboarding/ayuda, pero penalizan mirror y cache.

5. El layout es desktop-first y rigido.
   El CSS mantiene medidas fijas como `left:240px`, `right:240px`, `width:240px`, toolbar heights fijas y media queries amplias. En la inspeccion visual el header/toolbar se montaban parcialmente sobre el canvas en viewport estrecho.

6. El modelo visual de OPM esta bien separado por vocabulario grafico.
   Objetos, procesos, links estructurales/procedurales, estados, requirements y acciones tienen assets dedicados. Esta separacion permite reconstruir una UI compatible sin clonar toda la app, usando solo el vocabulario grafico y las reglas visuales observadas.

## Scripts relacionados con lo grafico

| Script | Peso | Responsabilidad grafica inferida |
|---|---:|---|
| `main.d9176050fd6f9943.js` | 21,963,040 | Nucleo de modelado grafico: Joint/Rappid, OPD graph, paper scroller, navigator, stencil, halo, toolbar, export, zoom, drag/drop, imagen/SVG/canvas |
| `scripts.8153de010e3d945e.js` | 6,110,542 | Vendor/support bundle con canvas, objetos, procesos, links, navigator y utilidades globales |
| `polyfills.5336622b9feb4652.js` | 1,383,170 | Compatibilidad runtime; menciones graficas incidentales |
| `runtime.880ef43bea70a15e.js` | 14,696 | Loader de chunks Angular |
| `assets/workers/typings-worker.js` | 4,116 | Worker auxiliar descargado por referencia estatica |

Conteos de señales en `main`: `Rappid` 1721, `paperScroller` 149, `Halo` 158, `Toolbar` 180, `Navigator` 119, `Graph` 558, `canvas` 217, `toSVG` 10, `toPNG` 6, `html2canvas` 13, `canvg` 21, `JSZip` 8.

## Criterio de cierre

- El mirror corregido descarga 157 archivos sin errores de transporte.
- El manifest conserva URL, path local, byte size, SHA-256, content type, ETag y clase por archivo.
- El catalogo CSV conserva 149 filas de assets graficos/font/fallback con extension, peso, SHA-256, tipo/dimensiones cuando son detectables, content type y URL de origen.
- Las rutas dinamicas quedan registradas como no enumerables en vez de contaminar el mirror con paths sinteticos.
