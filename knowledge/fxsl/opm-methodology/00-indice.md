---
_manifest:
  urn: "urn:fxsl:kb:opm-methodology"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-06"
    source: "opm_youtube.md + OPM version felix.md + ISO 19450"
version: "1.0.0"
status: published
tags: [opm, iso19450, modelado-conceptual, mbse, objetos, procesos, opl, opd, sistemas]
lang: es
---

# OPM — Object Process Methodology (ISO 19450)

Metodologia de modelado conceptual de sistemas basada en ontologia minima de objetos stateful y procesos que los transforman. Estandar ISO 19450. Bimodal: OPD (grafico) + OPL (textual).

---

## Mapa de la KB

| Archivo | Contenido |
|---------|-----------|
| 01-ontologia-opm.md | Objetos, procesos, estados, atributos, todos los tipos de enlaces (OPL grammar) |
| 02-diagrama-sistema.md | SD (5 componentes), procedimiento de modelado, SD1, refinamiento, OPD tree |
| 03-comportamiento-control.md | ECA, condiciones, operadores logicos (AND/XOR/OR), rutas, invocacion, duracion, probabilidades |
| 04-tipos-sistemas-mbse.md | Tipos de sistemas, MBSE, soluciones alternativas, PDR, integracion virtual |
| 05-glosario-iso19450.md | 83 terminos ISO 19450 |

---

## Conceptos Clave

**Tres primitivas:** Objeto + Proceso + Enlace.

**Tres aspectos de todo sistema:** Estructura (que) + Comportamiento (como) + Funcion (para que).

**Bimodalidad:** Todo lo expresado en OPD se expresa en OPL y viceversa. Equivalencia completa.

**Funcion del sistema:** Par (proceso-principal, objeto-principal). Proceso transforma objeto entregando beneficio al beneficiario.

---

## Herramientas

- **OPCloud** (opcloud.tech): software en la nube para construccion colaborativa de modelos OPM. Genera OPL automaticamente al construir OPD.
- **OPCAT**: software patentado previo, disponible gratuitamente.
