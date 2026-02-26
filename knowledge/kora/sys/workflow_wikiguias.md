---
_manifest:
  urn: urn:kora:kb:workflow-wikiguias
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: KORA system config
version: 2.0.0
status: published
tags:
- kora
- sistema
- configuracion
- sys
- workflow
lang: es
---

# TDE-WORKFLOW-WIKIGUIAS-029

ID: TDE-WORKFLOW-WIKIGUIAS-029 | Dominio: tde_lineamientos
Misión (ID: TDE_WORKFLOW_WIKIGUIAS_GLOBAL_001): Transformar progresivamente corpus wikiguias en KB KODA/TDE con alta fidelidad semántica, eficiencia de tokens y densa red de referencias cruzadas.

## Métricas Objetivo (ID: TDE_WORKFLOW_WIKIGUIAS_METRICAS_001)

| Métrica | Definición | Objetivo |
|---------|-----------|----------|
| FS (Fidelity Score) | % de MEAT (hechos, requisitos, definiciones, estructuras normativas) de la fuente presente en el artefacto KODA | FS=100% |
| TER (Token Efficiency Ratio) | (tokens_KODA / tokens_fuente) × 100 | TER≥30% (idealmente 30–60% según tipo de documento) |
| RD (Reference Density) | Promedio Ref/XRef/Ctx por bloque Tier1 significativo | RD≥2.0 en artefactos estratégicos/normativos/plataformas; RD≥1.0 en piezas breves |

Rec: Calcular FS y TER a nivel de documento; monitorear RD por bloque para detectar zonas pobres en referencias.

## Fase 1: Análisis (ID: TDE_WORKFLOW_WIKIGUIAS_F1_001)

Propósito: Entender la pieza fuente, clasificar tipo y decidir mapeo (1:1, 1:n, n:1); identificar todo el MEAT.

**Paso 1 — Tipificación:**
- Identificar tipo de fuente: Norma técnica, Reglamento, Guía técnica, Estrategia, Estándar, Manual de plataforma, Política, etc.
- Identificar dominio TDE afectado: seguridad/ciberseguridad, protección de datos, plataformas compartidas, TD/STD, datos abiertos, etc.

**Paso 2 — Estructura y MEAT:**
- Leer fuente completa; construir esquema jerárquico (secciones, artículos, capítulos, anexos).
- Marcar explícitamente: definiciones, objetos, propósitos, requisitos, procedimientos, métricas, anexos normativos, tablas de parámetros.
- Separar MEAT vs FAT (retórica, portada, lenguaje motivacional, repeticiones, ejemplos ilustrativos).

**Paso 3 — Decisión de Mapeo:**
- 1:1: fuente acotada y cohesiva (ej. una norma técnica individual, guía acotada).
- 1:n: fuente paraguas que conviene descomponer en lineamientos específicos (ej. estrategia amplia).
- n:1: varias fuentes pequeñas/complementarias describen el mismo objeto → un solo lineamiento KODA.
- Rec: Documentar conjunto real de archivos fuente en `Metadata_Original` aunque relación no sea 1:1.

## Fase 2: Telegrafización (ID: TDE_WORKFLOW_WIKIGUIAS_F2_001)

Propósito: Convertir MEAT en estructuras KODA Tier1 compactas y reutilizables; eliminar FAT sin perder contenido.

**Paso 1 — Mapping Tier1:**
- Mapear secciones a bloques estándar: Ctx, Def, Obj, Purp, Req, Rec, Act, Res, Warn.
- Normas/guías: privilegiar contexto, objeto, definiciones, requisitos mínimos, procesos, métricas, disposiciones finales.
- Plataformas: privilegiar contexto/rol, definiciones, requisitos de uso, flujos de integración, operación, gobernanza.

**Paso 2 — Telegrafía Semántica:**
- Redactar en estilo telegráfico pero completo: frases cortas sin perder condiciones, excepciones ni umbrales.
- Eliminar redundancias retóricas (introducciones repetidas, justificaciones extensas); conservar justificaciones que aportan criterio.
- Tablas: convertir solo celdas con MEAT (parámetros, umbrales, condiciones); simplificar el resto.

**Paso 3 — Inyección XRef y Lexicon:**
- Detectar conceptos en Lexicon TDE; referenciar con XRef en lugar de redefinir.
- Agregar Ctx_Required/XRef_Required hacia normas, reglamentos y estrategias citados como base.
- Asegurar RD≥2.0 en artefactos complejos; referencias deben ser relevantes, no decorativas.

## Fase 3: Deduplicación (ID: TDE_WORKFLOW_WIKIGUIAS_F3_001)

Propósito: Evitar bloques KODA redundantes o inconsistentes entre distintas fuentes.

**Paso 1 — Chequeo contra KB:**
- Antes de crear nuevo bloque Def/Req/Proc, buscar en KB TDE si existe bloque equivalente.
- Si existe: referenciar (Ref/XRef); solo especializar cuando la nueva fuente agrega detalles objetivos.

**Paso 2 — Consolidación:**
- Cuando varias fuentes describen el mismo concepto (ej. DDU, PISEE, CasillaÚnica): consolidar definición en Lexicon o lineamiento central; usar referencias desde el resto.
- No copiar tablas idénticas; representar una sola vez el parámetro y usar referencias.

**Paso 3 — Mapping n:1:**
- Cond: varias fuentes pequeñas describen diferentes aspectos de la misma plataforma/proceso → artefacto único n:1 con Metadata que liste todas las fuentes.
- Rec: Documentar decisiones de consolidación fuera de KODA para futuras auditorías.

## Fase 4: Validación (ID: TDE_WORKFLOW_WIKIGUIAS_F4_001)

Propósito: Verificar que el artefacto KODA sea sintácticamente válido, cubra 100% del MEAT y cumpla TER y RD objetivo.

**Paso 1 — Validación Sintaxis:**
- Validar YAML sintácticamente correcto (indentación, tipos, listas).
- Verificar IDs internos únicos; Ref apuntan a IDs existentes.

**Paso 2 — Validación MEAT:**
- Recorrer fuente y artefacto bloque a bloque; verificar FS=100%.
- Si MEAT perdido: regresar a Fase 2 para telegrafiar e incorporar.

**Paso 3 — Validación Métricas:**
- Estimar TER (tokens fuente vs tokens artefacto); verificar TER≥30%.
- Calcular RD por bloque semántico; verificar mínimos.
- Si TER<30% o RD<objetivo: revisar si se telegrafió en exceso o faltan referencias clave.

**Paso 4 — Validación Cruzada:**
- Verificar coherencia con artefactos relacionados (Norma + Guía + Plataforma); ajustar XRef para representar dependencias reales.
- Registrar resultado (Aprobado/Observado/Rechazado) y acciones pendientes fuera de KODA.

## Patrones de Mapeo (ID: TDE_WORKFLOW_WIKIGUIAS_PATTERNS_001)

| Patrón | Condición | Recomendación |
|--------|-----------|---------------|
| Norma Técnica Individual | Norma completa y autocontenida (ej. Decretos 7, 8, 9, 10, 12) | 1:1; conservar artículos, objeto, definiciones, funciones/categorías, disposiciones finales; guías técnicas por separado (1:n) |
| Guía Operativa de Norma | Guías que desarrollan controles de una norma (ej. GU-CIBER-001) | 1:1 operacionalizando norma base; XRef_Required hacia norma técnica base |
| Plataforma Compartida | Manuales de ClaveÚnica, Notificador, SIMPLE, DocDigital, PISEE, Datos.gob | n:1 cuando existan varios manuales (inicio + integración + otros); foco en contexto/rol, habilitación, flujos, operación, gobernanza |
| Estrategias y Marcos | Estrategias paraguas (Datos, Gobierno Digital, STD, EVALTIC, Orientaciones TIC) | 1:n generando lineamientos temáticos; usar como Ctx_Required/XRef en piezas operativas |

## Articulación con Agentes (ID: TDE_WORKFLOW_WIKIGUIAS_AGENTES_001)

- Fase 1 (Análisis): mayor participación humana en fuentes ambiguas o políticamente sensibles.
- Fases 2–3 (Telegrafización/Deduplicación): automatización parcial con KODA_TRANSFORMER.
- Fase 4 (Validación): mixta — validación automática básica (sintaxis, referencias, métricas) + revisión humana muestral.
