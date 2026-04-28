---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-28-salubrista-corpus-skills"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-28"
    source: "Cierre de sesion: consolidacion fisica del corpus salubrista, desacople de conocimiento vs perfiles/razonamiento, y materializacion de skills Hospitalista, HODOM y FIRS."
version: "1.0.0"
status: publicado
tags: [handoff, salubrista, hospitalista, hospitalizacion-domiciliaria, hodom, firs, corpus, salud]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:salud:artefacto:salubrista"
    - "urn:salud:artefacto:hospitalista"
    - "urn:salud:artefacto:hospitalizacion-domiciliaria"
    - "urn:salud:artefacto:firs-razonamiento-sanitario"
    - "urn:salud:kb:salubrista"
    - "urn:salud:kb:salubrista-fuentes-base-curadas"
    - "urn:salud:kb:salubrista-fuente-salud-publica-global"
    - "urn:salud:kb:salubrista-fuente-management-engineering"
    - "urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss"
---

# Handoff - Salubrista, Corpus Fisico y Skills

## Estado Actual

Trabajo cerrado sobre `/home/felix/kora` en rama `master`.

Resultado central: `salubrista` queda como agente productivo unico para salud
publica aplicada, hospitalista de red y hospitalista a domicilio. El
conocimiento vive fisicamente en `artifacts/knowledge/salud/salubrista`; las
capacidades procedurales/personales se expresan como artefactos agente o
skills, no como KB.

Validacion ejecutada durante el cierre:

- `python3 toolchain/kora index`: OK.
- `python3 toolchain/kora check --strict`: 20/20 OK.
- `python3 toolchain/kora kb-graph --json --orphans`: 0 broken edges, 0 ciclos
  en `depends`; 11 huerfanos reales ya clasificados por la herramienta.
- `python3 -m unittest tests.test_salubrista_hodom`: 7 OK.
- `python3 -m unittest discover -s tests`: 349 OK, 1 skipped.

## Decisiones

1. Corpus fisico: las fuentes base no quedan solo referenciadas desde INBOX;
   fueron movidas/integradas bajo `artifacts/knowledge/salud/salubrista`.
2. No duplicacion: `publihealth` se conserva como alias fisico deprecado del
   atomizado Oxford, no como fuente independiente.
3. Shards `--pNN.md`: son fragmentos fisicos del mismo documento canonico,
   generados para cumplir lint de chunks; no crean nuevas fuentes semanticas.
4. Desacople: FIRS deja de ser KB de razonamiento y pasa a skill
   `urn:salud:artefacto:firs-razonamiento-sanitario`.
5. Hospitalista: el modo hospitalista intrahospitalario se materializa como
   skill propia `urn:salud:artefacto:hospitalista`.
6. HODOM: hospitalizacion domiciliaria queda como skill operativa
   `urn:salud:artefacto:hospitalizacion-domiciliaria`, coordinada con
   Hospitalista y FIRS.
7. `salubrista-hah`: queda deprecado/subsumido por `salubrista`; no debe
   evolucionar como agente paralelo.

## Artefactos Relevantes

Agentes:

- `artifacts/agents/salud/salubrista/AGENT.md`
- `artifacts/agents/salud/salubrista-hah/AGENT.md`

Skills:

- `artifacts/skills/salud/hospitalista/SKILL.md`
- `artifacts/skills/salud/hospitalizacion-domiciliaria/SKILL.md`
- `artifacts/skills/salud/firs-razonamiento-sanitario/SKILL.md`

Corpus:

- `artifacts/knowledge/salud/salubrista/index.md`
- `artifacts/knowledge/salud/salubrista/atlas-integrado.md`
- `artifacts/knowledge/salud/salubrista/body-of-knowledge-salubrista.md`
- `artifacts/knowledge/salud/salubrista/fuentes-base-curadas.md`
- `artifacts/knowledge/salud/salubrista/fuentes/`
- `artifacts/knowledge/salud/salubrista/hodom/`

Toolchain y tests:

- `toolchain/kora_lib/config.py`
- `tests/test_salubrista_hodom.py`

## Pendientes

1. Decidir si las modificaciones en `artifacts/agents/_FRAGUA/INBOX/salubrista`
   deben promoverse, archivarse o eliminarse en una limpieza separada.
2. Revisar las 11 orfandades reales reportadas por `kb-graph`; no bloquean el
   cierre, pero conviene clasificar si son intencionales.
3. Si se quiere una transmutacion OpenClaw especifica de `salubrista`, usar el
   agente productivo y las tres skills actuales como fuente; no usar los
   perfiles KB deprecados ni `salubrista-hah`.
4. Mantener fuera de este cierre las modificaciones ajenas ya existentes en
   `docs/`, `ontology/` y `runtime/`.

## Supuestos

- El despliegue OpenClaw tendra un clon actualizado de KORA, por lo que los
  agentes pueden asumir acceso local al KB mediante filesystem/URN.
- La verificacion web solo aplica cuando una respuesta dependa de vigencia
  normativa, fecha, arancel, autoridad o dato actual.
- HODOM es atencion cerrada en domicilio, no atencion domiciliaria ambulatoria.
- La conduccion estrategica y responsabilidad decisional siguen en el humano.

## Riesgos

- Riesgo de duplicacion si alguien trata shards `--pNN.md` o `publihealth` como
  fuentes nuevas.
- Riesgo de regresion si se reintroducen perfiles/persona como KB autorizada.
- Riesgo operativo si `hospitalista` se usa como sustituto de juicio clinico o
  direccion medica.
- Riesgo de commit accidental: el working tree contenia cambios no relacionados
  en `docs/`, `ontology/` y `runtime`; deben seguir aislados.
