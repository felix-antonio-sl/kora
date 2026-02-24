---
_manifest:
  urn: "urn:kora:skill:guardian-pedagogical-adapter:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-PEDAGOGICAL-ADAPTER

## Proposito

Adaptar la explicacion del framework KORA al nivel del usuario (NOVATO | INTERMEDIO | AVANZADO) con analogias y ejemplos apropiados al dominio.

## Procedimiento

1. Evaluar nivel del usuario: vocabulario usado, preguntas formuladas, familiaridad con conceptos KORA
2. Seleccionar profundidad apropiada: NOVATO (conceptos basicos, analogias cotidianas) | INTERMEDIO (mecanismos, ejemplos reales) | AVANZADO (fundamentos categoricos, edge cases)
3. Construir explicacion con analogia del dominio del usuario cuando se conoce (gobierno, software, logistica)
4. Agregar ejemplo concreto del ecosistema KORA que ilustra el concepto
5. Formular pregunta de verificacion de comprension al final
6. Si no comprende: cambiar angulo de la analogia y repetir desde paso 3

## Output

Explicacion adaptada al nivel con analogia + ejemplo KORA + pregunta de verificacion. Estructura progresiva: concepto → analogia → ejemplo → verificacion.
