---
title: "kora/curator workspace"
summary: "Mapa operativo y modelo de memoria del workspace del agente curator"
read_when:
  - "Auditar o mantener el workspace de kora/curator"
  - "Necesitar contexto rapido sobre estructura, memoria y contrato operativo"
---

# kora/curator

Workspace del agente curador del corpus KORA. Su dominio es el ciclo de vida de artefactos de conocimiento: disenar, koraficiar, cristalizar, auditar, editar, reparar, mejorar y deprecar, manteniendo fidelidad, trazabilidad y SSOT.

## Mapa del workspace

- `AGENTS.md`: FSM, reglas duras, retencion multi-turno y wiring.
- `SOUL.md`: identidad fenomenologica, tono y paradigma cognitivo.
- `USER.md`: perfil operador, rutinas y preferencias de output.
- `TOOLS.md`: interfaz semantica permitida para resolver, leer, escribir y validar artefactos.
- `config.json`: KBs permitidas, tools autorizadas y limites operativos.
- `skills/`: capacidades CM-* especializadas por fase del ciclo de vida.
- `MEMORY.md`: memoria durable del workspace.
- `memory/`: logs diarios de contexto episodico.

## Contrato operativo

- Scope: solo curaduria de artefactos KORA/MD y KORA/Spec-MD.
- Fuera de scope: specs fundacionales, agentes y catalogo.
- Invariantes: `FS=100%`, objetivo `CR>1.5`, pipeline `inbox -> source -> drafts -> knowledge`, politica `SSOT`.
- Estilo de salida: Markdown en `es-CL`, citas con nombre oficial, reportes de auditoria en tabla, metricas `FS` y `CR` visibles.

## Memoria

- `MEMORY.md` se usa para hechos estables: decisiones persistentes, limites operativos, preferencias y acuerdos de trabajo que deban sobrevivir a la sesion.
- `memory/YYYY-MM-DD.md` se usa para hechos fechados: cambios recientes, hallazgos, contexto episodico y proximos pasos.
- La memoria no reemplaza artefactos KORA: no guardar conocimiento del corpus aqui salvo lo estrictamente operacional para correr el agente.

## Mantenimiento

- Si cambia el comportamiento estable del agente, actualizar `AGENTS.md` y `MEMORY.md` juntos.
- Si se aplica un cambio relevante al workspace, registrarlo tambien en el log diario correspondiente.
- Mantener la documentacion de memoria corta, operativa y sin duplicacion innecesaria.
