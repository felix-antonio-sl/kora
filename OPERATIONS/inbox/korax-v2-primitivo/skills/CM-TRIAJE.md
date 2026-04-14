---
_manifest:
  urn: urn:korvo:skill:korax-triaje:1.0.0
  type: lazy_load_endofunctor
---

## Proposito
Protocolo de procesamiento del buffer (Módulo 2 PCA). Procesa items sin triajear desde INBOX.md hacia sus destinos GTD.

## Input/Output
- **Input:** items: Item[] (sin procesar en INBOX.md)
- **Output:** result: TriageResult {procesados, eliminados, incubados, comprometidos, waiting}

## Procedimiento
### Rama Asistida (delegation_scope: none)

1. Por cada item en INBOX.md, presentar al operador.
2. Preguntar destino:
   - (1) Basura → eliminar
   - (2) Incubar → SOMEDAY.md
   - (3) Waiting → WAITING.md (enviar mensaje primero)
   - (4) Comprometer → asignar Modo + Timebox → NEXT.md
3. Korax **NO DEBE** sugerir destino (INV-02).
4. Al finalizar: reportar conteos.
5. Si regla_50 aplica (>50% eliminados), recordar al operador que ajuste filtro mental de captura.

### Rama Autónoma (delegation_scope ⊇ triage)

1. Por cada item en INBOX.md, aplicar heurísticas aprendidas del historial del operador.
2. Clasificar según patrones de decisión previos: frecuencia de destino por tipo de item, contextos recurrentes, umbrales de incubación.
3. Ejecutar triaje completo sin intervención del operador.
4. **DEBE** registrar cada decisión con justificación (pattern match usado).
5. **DEBE** reportar resultados completos al siguiente contacto con el operador.

## Signature Output
```
📊 Triaje completado:
- Procesados: {n}
- Eliminados: {n}
- Incubados: {n}
- Comprometidos: {n}
- Waiting: {n}
Buffer vacío ✓
```
