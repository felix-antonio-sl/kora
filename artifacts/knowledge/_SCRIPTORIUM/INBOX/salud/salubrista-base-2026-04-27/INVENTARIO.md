---
_manifest:
  urn: "urn:salud:kb:inventario-salubrista-base-2026-04-27"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-27"
    source: "Reconstruccion del inventario salubrista tras poda accidental de dossier untracked; fuentes recuperadas desde KORA vigente."
version: "0.3.0"
status: borrador
tags: [salubrista, salud-publica, gestion-redes, hodom, hah, inventario, inbox, reconstruido]
lang: es
extensions:
  kora:
    family: curation-inventory
    dossier_root: "artifacts/knowledge/_SCRIPTORIUM/INBOX/salud/salubrista-base-2026-04-27"
relations:
  cites:
    - "urn:salud:kb:gestion-redes-indice"
    - "urn:salud:kb:gestion-redes-general"
    - "urn:salud:kb:gestion-redes-unidades"
    - "urn:salud:kb:gestion-redes-urgencias"
    - "urn:salud:kb:gestion-redes-salud-mental"
    - "urn:salud:kb:gestion-redes-herramientas"
    - "urn:salud:kb:salubrista-fuente-salud-publica-global"
    - "urn:salud:kb:salubrista-fuente-management-engineering"
    - "urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss"
    - "urn:salud:kb:hodom-reglamento-ds1-2022"
    - "urn:salud:kb:hodom-decreto-exento-31-2024"
    - "urn:salud:kb:hodom-norma-tecnica-2024"
    - "urn:salud:kb:hodom-direccion-tecnica"
    - "urn:salud:kb:hodom-manual-alta-complejidad"
    - "urn:salud:kb:hodom-situacion-chile-2026"
---

# Inventario base Salubrista — 2026-04-27

## Estado de reconstruccion

Este dossier fue reconstruido despues de una poda accidental de archivos nuevos
no versionados. El inventario original y sus copias de trabajo no estaban
tracked, por lo que `git restore` no podia recuperarlos. Se rearmo desde las
fuentes que siguen presentes en KORA.

Recuperado:

| Grupo | Archivos | Estado |
|---|---:|---|
| `agentes-productivos/` | 2 | recuperado |
| `agentes-staging/` | 30 | recuperado |
| `kb-publicada/` | 45 | recuperado |
| `fuentes-crudas/salubrista/` | 4 | recuperado |
| `perfiles/` | 2 | recuperado |
| `docs-operativos/` | 6 | recuperado |
| `runtime-toolchain/` | 6 | recuperado |
| **Total fuentes recuperadas** | **95** | dossier reconstruido |

No recuperado en disco:

| Fuente previa | Estado |
|---|---|
| `artifacts/knowledge/_SCRIPTORIUM/INBOX/hodom/corpus-hah-completo.md` | perdida del working tree untracked |
| `artifacts/knowledge/_SCRIPTORIUM/INBOX/hodom/Hospital at Home and Home First Care Models.md` | perdida del working tree untracked |
| `artifacts/knowledge/_SCRIPTORIUM/INBOX/hodom/hodom-hsc-canonico.opl` | perdida del working tree untracked |
| `artifacts/knowledge/_SCRIPTORIUM/INBOX/hodom/hodom-hsc-procesos.md` | perdida del working tree untracked |
| `artifacts/knowledge/_SCRIPTORIUM/INBOX/omega/salubrista.md` | perdida del working tree untracked |
| `artifacts/knowledge/_SCRIPTORIUM/INBOX/omega/salubrista-hosp-hodom.md` | perdida del working tree untracked |

Las copias recuperadas se guardaron como `*.source.txt` para evitar duplicar
frontmatter y URNs KORA durante `python3 toolchain/kora index`.

## Escala

**Calidad documental**: Alta = estructurada, trazable y usable; Media =
legible pero requiere normalizacion; Baja = cruda o incompleta.

**Cumplimiento KORA**: Alto = manifesto/URN/status/relaciones validas; Medio =
staging o legacy util; Bajo = raw source sin shape KORA.

**Calidad de dominio**: Alta = directamente util para salud publica,
epidemiologia, gestion sanitaria o HODOM; Media = util pero parcial o
indirecta; Baja = operacional/historica.

## Diagnostico ejecutivo

La base salubrista recuperada sigue siendo suficiente para diseñar el agente
definitivo:

1. `salud/salubrista` productivo entrega el esqueleto de rol generalista:
   epidemiologia aplicada, vigilancia, diagnostico situacional, gestion de
   redes, evaluacion, politica sanitaria y diseno de servicios.
2. El antiguo `salud/salubrista-hah` entrega el linaje especializado HODOM/HaH
   que fue subsumido por `salud/salubrista` v3.0.0: continuidad
   hospital-domicilio, camas/capacidad, direccion tecnica HD y cumplimiento
   normativo.
3. `gestion-redes` + fuentes fisicas curadas son el nucleo de conocimiento
   salubrista; FIRS fue desacoplado como skill de razonamiento.
4. `HODOM` publicado cubre normativa y direccion tecnica bajo
   `artifacts/knowledge/salud/salubrista/hodom/`; las fuentes crudas
   HaH no recuperadas eran enriquecimiento, no unico soporte canonico.
5. Las fuentes crudas de salud publica global, management engineering y PAC/LTSS
   ya fueron promovidas fisicamente dentro de `salud/salubrista/fuentes/`.

Riesgo residual: la perdida de las 6 fuentes no versionadas reduce evidencia
auxiliar para HaH y perfil narrativo, pero no elimina los KB publicados que
consumen los agentes actuales.

## Inventario por paquete

### 1. Agentes productivos

**Archivos**

- `fuentes/agentes-productivos/salubrista/AGENT.source.txt`
- `fuentes/agentes-productivos/salubrista-hah/AGENT.source.txt`

**Que son**: versiones productivas actuales de los agentes salubristas.

**Contenido**:

- `salubrista`: copiloto tecnico para salud publica, epidemiologia aplicada,
  vigilancia, gestion de redes y evaluacion de servicios.
- `salubrista-hah`: especializacion en hospitalizacion integrada,
  hospitalizacion domiciliaria, continuidad, capacidad y normativa HD.

| Dimension | Evaluacion | Razon |
|---|---|---|
| Documental | Alta | Shape unificado, version, status, FSM, guardrails y KB permitida |
| Cumplimiento KORA | Alto | Manifestos validos y agentes productivos activos |
| Dominio | Media-Alta | Buen modelo de conducta; no es fuente primaria |

Uso recomendado: tomar `salubrista` como base. `salubrista-hah` ya no debe
operar como agente separado; su contenido se conserva como fuente y queda
materializado como modo interno + skill HODOM.

### 2. Workspaces staging legacy

**Archivos**: `fuentes/agentes-staging/salubrista/**` y
`fuentes/agentes-staging/salubrista-hah/**`.

**Contenido**: bootstrap legacy, `config.json` y skills como
`CM-EPI-ANALYST`, `CM-EPI-VIGILANCE`, `CM-NETWORK-ANALYST`,
`CM-HAH-SPECIALIST`, `CM-HOSPITAL-SYSTEM-ANALYST`, `CM-QUALITY-AUDITOR` y
`CM-REPORT-BUILDER`.

| Dimension | Evaluacion | Razon |
|---|---|---|
| Documental | Media | Informacion util pero redundante y legacy |
| Cumplimiento KORA | Medio | Tiene metadata, pero no es destino productivo vigente |
| Dominio | Media-Alta | Captura tareas reales de vigilancia, red y HODOM |

Uso recomendado: extraer capacidades, no copiar la topologia legacy.

### 3. KB publicada: gestion de redes

**Archivos**: `fuentes/kb-publicada/salubrista/gestion-redes/**`.

**Contenido**: gobernanza, modelo de atencion, procesos, calidad, indicadores,
digital, RRHH, finanzas, abastecimiento, unidades asistenciales, urgencias,
salud mental, KPIs, BPMN, FHIR/HL7, plantillas y simulacion.

| Dimension | Evaluacion | Razon |
|---|---|---|
| Documental | Alta con deuda de shard | Corpus estructurado, pero hay raiz y fragmentos `--pNN` |
| Cumplimiento KORA | Alto | Manifestos y relaciones publicadas |
| Dominio | Alta | Columna vertebral del salubrista general |

Uso recomendado: nucleo obligatorio del salubrista definitivo.

### 4. Razonamiento operativo: FIRS

**Archivo**:
`artifacts/skills/salud/firs-razonamiento-sanitario/SKILL.md`.

**Contenido**: razonamiento clinico, epidemiologico y de gestion sanitaria;
separacion micro/meso/macro; clinical epidemiology; systems thinking; VBHC,
HRO, calidad y seguridad.

| Dimension | Evaluacion | Razon |
|---|---|---|
| Documental | Alta | Documento unico y estructurado |
| Cumplimiento KORA | Alto | Skill activa con referencia fuente preservada |
| Dominio | Metodo, no corpus | Guardrail epistemico para evitar cruces de nivel indebidos |

Uso recomendado: activar como skill cuando la respuesta cruce niveles de
analisis o mezcle evidencia clinica, epidemiologica y operacional.

### 5. KB publicada: HODOM / HaH

**Archivos**: `artifacts/knowledge/salud/salubrista/hodom/**`.

**Contenido**: DS 1/2022, Decreto Exento 31/2024, Norma Tecnica HD 2024,
direccion tecnica HD, modelo de alta complejidad y situacion Chile 2026.

| Dimension | Evaluacion | Razon |
|---|---|---|
| Documental | Media-Alta | Canonizado y fragmentado |
| Cumplimiento KORA | Alto | URNs publicados y usados por `salubrista-hah` |
| Dominio | Alta para HODOM | Modulo especializado, no nucleo general |

Uso recomendado: activar por triggers de hospitalizacion domiciliaria,
continuidad hospital-domicilio, camas, transiciones o direccion tecnica HD.

### 6. Perfiles

**Archivos**:

- `fuentes/perfiles/salubrista-copiloto-estrategico.source.txt`
- `fuentes/perfiles/salubrista-hospitalizacion-integrada.source.txt`

| Dimension | Evaluacion | Razon |
|---|---|---|
| Documental | Media-Alta | Claros y reutilizables |
| Cumplimiento KORA | Deprecado como KB | Subsumidos por agente y skill |
| Dominio | No corpus | Identidad, scope y modo de activacion; no evidencia primaria |

Uso recomendado: no consumir como conocimiento. El contenido operativo vive en
`urn:salud:artefacto:salubrista` y
`urn:salud:artefacto:hospitalizacion-domiciliaria`.

### 7. Fuentes crudas salubrista

**Archivos canonicos publicados**:

- `artifacts/knowledge/salud/salubrista/fuentes/salud-publica-global.md`
- `artifacts/knowledge/salud/salubrista/fuentes/management-engineering-sanitario.md`
- `artifacts/knowledge/salud/salubrista/fuentes/continuidad-post-aguda-ltss.md`
- `artifacts/knowledge/salud/salubrista/fuentes/duplicados/publihealth-oxford-alias.source.txt`

| Dimension | Evaluacion | Razon |
|---|---|---|
| Documental | Media-Alta | Atomizadas, con manifesto y procedencia |
| Cumplimiento KORA | Alto salvo alias | Tres nodos publicados; `publihealth` no indexado por duplicacion |
| Dominio | Alta potencial | Valiosas si se curan selectivamente |

Uso recomendado: consumir como fuentes canonicas del corpus salubrista, con
`publihealth` solo como evidencia de alias redundante.

### 8. Docs operativos y runtime

**Archivos**: `fuentes/docs-operativos/**` y `fuentes/runtime-toolchain/**`.

| Dimension | Evaluacion | Razon |
|---|---|---|
| Documental | Media | Memoria de trabajo y specs auxiliares |
| Cumplimiento KORA | Mixto | Algunos docs con frontmatter, scripts legacy auxiliares |
| Dominio | Baja-Media | Operacional, no sanitario primario |

Uso recomendado: guiar arquitectura, transmutacion y decisiones de despliegue.

## Brechas

1. Reponer o reacopiar las 6 fuentes no recuperadas si existen fuera de este
   repo.
2. Decision tomada: `salubrista-hah` queda como modulo interno de `salubrista`
   y no como agente productivo separado.
3. Resolver politica de lectura de shards `gestion-redes`.
4. Mantener `publihealth` como alias no indexado; no convertirlo en segunda KB.
5. Preparar contrato OpenClaw usando KB montada desde clon KORA vivo.

## Decision curatorial inicial

1. Base: `salud/salubrista`.
2. Modulo especializado: HODOM/HaH dentro de `salud/salubrista` mediante la
   skill `urn:salud:artefacto:hospitalizacion-domiciliaria`.
3. Nucleo obligatorio: `gestion-redes` + fuentes fisicas del corpus.
4. Knowledge condicionado: HODOM/HaH por trigger.
5. Metodo condicionado: FIRS como skill, no como KB.
6. Runtime: OpenClaw debe montar KB desde `$KORA_REPO/artifacts/knowledge/salud/salubrista/...`.
