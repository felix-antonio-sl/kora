---
_manifest:
  urn: "urn:kora:kb:pendientes-corpus-grandes-inbox-2026-04-23"
  provenance:
    created_by: "FS"
    created_at: "2026-04-23"
    source: "Registro de corpus grandes en artifacts/knowledge/_SCRIPTORIUM/INBOX/ que requieren procesamiento con atomize u otro pipeline especializado; no procesables como koraficacion directa a un solo artefacto"
version: "1.0.0"
status: borrador
tags: [pendientes, corpus-grande, atomize, inbox, intake]
lang: es
extensions:
  kora:
    family: catalog
---

# Pendientes: Corpus Grandes en SCRIPTORIUM/INBOX

## Naturaleza del artefacto

Registro de materiales en `artifacts/knowledge/_SCRIPTORIUM/INBOX/` que por su tamano, formato o densidad semantica NO fueron procesables como koraficacion directa a un artefacto KORA/MD unico durante la ronda del 2026-04-23. Requieren procesamiento dedicado via `urn:kora:artefacto:atomize` u otro pipeline.

## Catalogo

### Libros completos en TXT (requieren atomize)

| Archivo | Tamano | Plan |
|---------|--------|------|
| `Procrastination - Fuschia M. Sirois.txt` | 470 KB | `atomize` a `atomic-procrastination-sirois` en `urn:pro:kb:`. |
| `opm-libro.txt` | 825 KB | Ya existe curacion en `opm-libro-curado/`. Evaluar si duplica. |

### Corpus scraping

| Archivo | Tamano | Plan |
|---------|--------|------|
| `dankoe_articles_full.json` | 1.2 MB | Procesar con script que extraiga articulos a MD y luego `atomize`. Destino: `urn:korvo:kb:atomic-dankoe-*`. |
| `seleccion-dan.json` | 595 KB | Idem; seleccion curada, priorizar. |

### Documentos institucionales

| Archivo | Formato | Plan |
|---------|---------|------|
| `legal/15869-19 y 16821-19 ... IA.docx` | DOCX | Convertir a MD + frontmatter familia `normative`, namespace `legal`. |
| `salud/Oxford Handbook of Emergency Medicine ... libgen.li.pdf` | PDF | Material de referencia consultiva; no koraficar (copyright). Usar referencia externa. |
| `salud/ARSENAL AFT EDITABLE_MAYO-24.pdf` | PDF | Depende del uso; convertir a MD si interno. |
| `salud/perfil-urgenciologo.md` | MD | Ya cubierto por `salud/artefacto/urgenciologo`. |
| `salud/razo-urg.md` | MD | Cubierto por agente urgenciologo. |
| `salud/toc_med-urg.md` | MD | Similar. |

### Directorios de curacion

| Directorio | Estado | Plan |
|------------|--------|------|
| `agengai/` | Sin inspeccionar | Inspeccionar y ruta a `agengai` namespace. |
| `curso-dov-dori/` | 5 archivos TXT | Transcripciones curso OPM; atomize a `urn:fxsl:kb:atomic-opm-curso-*`. |
| `opm/transcripciones-videos-opcloud.txt` | 1 archivo | Atomize a `urn:fxsl:kb:atomic-opcloud-tutorials`. |
| `opm-libro-curado/` | 24 capitulos MD | Index creado en REVIEW; promover cada capitulo o aplicar atomize. |
| `fxsl/opm-methodology/` | 14 archivos MD | Index creado en REVIEW; promover individualmente. |
| `fxsl/gist/*.ttl` | 5 archivos Turtle | Ontologia; no requiere koraficacion. Registrar como recursos del `ontologista-gist`. |
| `sii/documents.json, sii/questions.json` | JSON | Datasets; registrar en namespace `sii` tras curar. |
| `wikiguias_corpus_tde/README.md` | README | Ampliar a knowledge note. |
| `pro/` | Vacio o sin inspeccionar | Pendiente revision. |

### Archivos redundantes (descarte recomendado)

- `*/local-machine-inventory-2026-04-22.md` en varios subdirectorios — es un dump de estado de la maquina de Felix, duplicado en multiples directorios. No aporta al corpus canonico; eliminar o mover a `~/kora/notas-operativas/`.

## Proximos pasos sugeridos

1. Ejecutar `atomize` sobre los libros completos (Procrastination, curso OPM, transcripciones).
2. Construir scripts de conversion JSON -> MD para dankoe y sii.
3. Convertir DOCX legal.
4. Promover capitulos OPM de a uno o atomizar el libro entero si se prefiere granularidad.
5. Limpiar `local-machine-inventory-*` duplicados.
