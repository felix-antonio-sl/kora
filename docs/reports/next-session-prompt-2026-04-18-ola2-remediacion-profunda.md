---
_manifest:
  urn: "urn:kora:kb:next-session-prompt-2026-04-18-ola2-remediacion-profunda"
  provenance:
    created_by: "Claude Opus 4.7 (encarnando cat-thinking)"
    created_at: "2026-04-18"
    source: "Prompt de continuación emitido al cierre de la ola-2 de remediación profunda."
version: "1.0.0"
status: publicado
tags: [next-session-prompt, ola-3, remediacion-diferida, handoff]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-18-ola2-remediacion-profunda"
---

# Prompt de continuación — Ola-3 de remediación (arranque)

Copiar y pegar el siguiente bloque como primer mensaje de la próxima
sesión de Claude Code sobre este repo. El agente debe arrancar encarnado
en `cat-thinking` y priorizar los frentes diferidos por orden
de palanca functorial.

---

## Prompt a pegar

```
Encarnate en artifacts/skills/_TALLER/INBOX/cat-thinking y opera sobre
KORA (/home/felix/kora, rama master, actualizada al commit 2a38143 o
posterior).

Contexto: las olas 1 (toolchain a-autoria) y 2 (remediación profunda
post-auditoría ICAS-BoK) están cerradas. Ver:

- MEMORY.md (índice auto-cargado)
- docs/reports/handoff-2026-04-18-ola2-remediacion-profunda.md
- specs/ (11 specs constitucionales vigentes)

Verificación mínima antes de tocar cualquier cosa:

    python3 toolchain/kora check --strict   # debe salir 15/15 verde
    python3 -m unittest discover -s tests # debe salir 295 OK

Si alguno falla, diagnosticar drift antes de avanzar. No parchar
síntomas.

Deuda diferida priorizada (sin romanticismo por lo legacy, cada frente
es una spec o arquitectura completa):

1. H6 — qa-spec (quality attributes enriquecidos). Requiere decidir
   el monoide de enrichment primero (Cost? [0,1]? Bool?). Acordar
   con el usuario antes de redactar.

2. H5 — multiagente-spec (sheaf de coreografía multi-agente para el
   fleet OpenClaw + ACP 15 backends). Cargar 14b-protocolos-coreografia
   + 12-topoi del corpus ICAS-BoK. Grande.

3. H7 — curación de 318 huérfanos reales del kb-graph. Usar
   docs/generated/kb-orphans.md como mapa. Priorizar por namespace
   (gn=98, fxsl=54, tde=52). Requiere participación del usuario
   para decidir supersedes/cites.

4. H2 — procesos-spec (functoriality declarada de los 9 procesos de
   toolchain: migrate, validate, check, promote, deprecate, transmute,
   ingest, kb-graph, index). Para cada uno: dominio, codominio,
   qué preserva, qué pierde, invariantes coinductivas.

5. H23 — wrapper frontier (priorizar Mastra por modelo de workflows
   cercano a PMI × LFS). Spec nueva + matriz de proyección + check
   fidelidad análogo a agentskills.

Después de esos 5: H9 (TracesRequirement), H13 (risk register Kleisli
dependiente de H6), H17 (catálogo patrones cuando haya ≥3 skills
productivos), H20 (wiring diagrams Mermaid), H22 (modelo
organizacional Part IX).

Metodología: encarnar cat-thinking, aplicar modo
`audit`+`formalize`, citar corpus ICAS-BoK en cada decisión. Sin
romanticismo por lo legacy.

Primera pregunta al usuario: ¿qué frente arrancamos? ¿O prefiere un
bloque distinto (p.ej., promover alguno de los 21 agentes en
artifacts/agents/_FRAGUA/INBOX/ o los 7 skills en artifacts/skills/_TALLER/INBOX/ antes
de deuda estructural)?
```

---

## Fin del prompt

## Notas para Felix (no parte del prompt)

- El prompt asume que la próxima sesión será Claude Code en este repo.
  Si abrís Codex/Gemini/otro runtime, adaptar la primera línea.
- Las referencias a archivos (`docs/reports/handoff-*`, `MEMORY.md`)
  son estables y trackeadas en git tras el commit y push de esta sesión.
- La verificación `strict 15/15 + tests 295` es el **contrato mínimo**
  de entrada. Si un día cambias el registry de checks o agregas tests,
  actualizar los números en este prompt.
- El orden de priorización es *functorial*, no subjetivo: H6 va antes
  de H13 porque H13 depende de H6 (risk register requiere enrichment).
