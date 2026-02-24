---
_manifest:
  urn: "urn:kora:agent-bootstrap:cartographer-cm-layer-designer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Disenar arquitectura de capas de abstraccion para el modelo de datos, asegurando que dependencias solo fluyan hacia arriba.

## Input/Output

- **Input:** Patrones aplicados y clasificacion ontologica desde S-ELEVAR
- **Output:** Arquitectura de capas con elementos asignados y regla de dependencia verificada

## Procedimiento

1. Definir 4 capas estandar:
   - **Layer 0 — META:** Lo que describe al sistema mismo. Cambia solo con filosofia. Ej: story, entity, role, process.
   - **Layer 1 — REFERENCE:** Vocabularios controlados. Cambia infrecuentemente. Ej: domain, category, status.
   - **Layer 2 — CORE:** Entidades de negocio. El corazon del dominio. Ej: org, person, ipr, agreement.
   - **Layer 3 — TRANSACTIONAL:** Eventos y mediciones. Alta volumetria, append-only. Ej: event, magnitude, audit_log.
2. Asignar cada elemento del modelo a su capa
3. Verificar regla de dependencia: cada capa solo referencia misma capa o superiores. Nunca abajo.
4. IF violacion detectada → reorganizar o crear vista intermedia

## Signature Output

```
**Arquitectura de Capas**:
| Capa | Nombre | Elementos | Freq Cambio |
|------|--------|-----------|-------------|
| 0 | META | [lista] | Filosofico |
| 1 | REFERENCE | [lista] | Infrecuente |
| 2 | CORE | [lista] | Dominio |
| 3 | TRANSACTIONAL | [lista] | Alto volumen |
**Dependencias**: [verificadas/violaciones encontradas]
```
