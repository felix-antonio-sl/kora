---
_manifest:
  urn: urn:gn:kb:agente-patrimonial-config-legacy
  provenance:
    created_by: FS
    created_at: '2026-04-23'
    source: artifacts/knowledge/_SCRIPTORIUM/INBOX/agente-patrimonial.yml — configuracion
      YAML legacy v1 de agente GORE Asistente de Alta Jerarquia (admin regional, estrategia
      politica, comunicaciones, marco presupuestario 2026)
version: 1.0.0
status: publicado
tags:
- config-legacy
- gn
- agente-patrimonial
- admin-regional
- gore-nuble
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:gn:kb:agente-patrimonial-config-legacy
relations:
  cites:
  - urn:gn:kb:ssot-master
---

# Agente Patrimonial — Configuracion Legacy

## Naturaleza del artefacto

Registro conceptual del agente **Patrimonial / Asistente de Alta Jerarquia GORE Nuble** cuyo artefacto de autoria original vivia en un YAML monolitico legacy (agentfile v1 pre-unified) orientado al Gobernador, Admin Regional, Jefe de Gabinete y jefaturas de division.

Este nodo de conocimiento preserva el **perfil funcional** del agente para futura migracion al shape unified autoria-spec v1.2; NO sustituye a los agentes productivos ya migrados (`gn/ar-virtual`, `gn/gobernador-virtual`, `gn/dgi-virtual`).

## Rol declarado en el original

- **Objetivo**: Apoyar al Gobernador y directivos en decisiones, gestion, articulacion, imagen estrategica y soluciones alineadas con la vision regional y el marco operativo-presupuestario 2026.
- **Audiencia**: Gobernador Regional, Admin Regional, Jefe de Gabinete y jefaturas de division.
- **Content lang**: `es-CL`.

## Politica KB (EXCLUSIVE_USE)

Uso exclusivo de fuentes declaradas. Protocolo de incertidumbre: `DECLARE_ABSENCE`. Interaccion: declarar faltantes y sugerir busqueda externa; pedir enfoque/formato/audiencia/plazo ante ambiguedad; validar glosas, restricciones, fuentes y reportes antes de recomendar en presupuesto 2026. Siempre ofrecer borrador + siguiente paso.

## KB de origen

- `kb_gn_000_intro_gores_nuble`
- `kb_gn_031_ley_19175_sts`
- `kb_gn_200_marco_legal_gores_sts`
- `kb_gn_950_todo_nuble_futuro_sts`
- `kb_gn_035_estrategia_gestion_sts`
- `kb_gn_900_gore_ideal`
- `kb_gn_030_guia_comunicaciones_sts`
- `kb_gn_008_comunicaciones_oc`
- `kb_gn_011_selector_ipr_sts`
- `kb_gn_920_agregado_ipr_gestion_idis_programas_sts`
- `kb_gn_930_agregado_ipr_guias_especificas_no_idis_no_programas_sts`
- `kb_gn_018_gestion_prpto_sts`
- `kb_gn_020_gestion_rendiciones_sts`
- `kb_gn_009_ccpp_sts`
- `kb_gn_005_indicadores_nuble`
- `kb_gn_002_noticias`
- `kb_gn_003_idis`
- `kb_gn_012_progs_vigentes`
- `kb_gn_100_modelos_actos_juridicos_sts`
- `kb_gn_212_ley_presupuestos_2026_gore_nuble`

Estos identificadores pertenecen al regimen de referencias legacy previo al catalogo KORA. Al migrar a productivo, se traducen a URNs `urn:gn:kb:{slug}` correspondientes.

## Nota de migracion

Para convertirlo en agente agentico productivo aplica `autoria-spec v1.2`:

1. Emitir `artifacts/agents/{gn}/{slug}/AGENT.md` con frontmatter unified.
2. Declarar `artefacto.contexto.knowledge.allowed_kb` con URNs resueltos.
3. Derivar a sub-agentes especializados ya existentes (`gn/ar-virtual`, `gn/gobernador-virtual`, `gn/asesor-juridico`, `gn/gestor-ipr-360`, `gn/erp-gore`, `gn/dgi-virtual`) en lugar de reencarnar el monolito.
