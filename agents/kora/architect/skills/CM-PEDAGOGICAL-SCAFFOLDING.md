---
_manifest:
  urn: "urn:kora:skill:architect-pedagogical-scaffolding:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-PEDAGOGICAL-SCAFFOLDING

## Proposito

Guiar el aprendizaje del framework KORA mediante progresion estructurada, conectando conocimiento previo del usuario con conceptos nuevos del ecosistema.

## Procedimiento

1. Evaluar nivel del usuario: NOVATO (primera exposicion) | INTERMEDIO (conoce spec, no domina) | AVANZADO (construye agentes, necesita edge cases)
2. Conectar con conocimiento previo: identificar analogia del dominio del usuario (documentacion tecnica, YAML conocido, agentes previos)
3. Introducir concepto con ejemplo concreto del ecosistema KORA (no abstracto)
4. Establecer progresion: concepto actual → aplicacion → siguiente concepto relacionado
5. Verificar comprension con pregunta practica: "¿Como aplicarias esto a tu caso?"
6. Si no comprende: cambiar analogia, simplificar, agregar otro ejemplo
7. Registrar conceptos dominados para no repetirlos en turnos siguientes

## Output

Explicacion progresiva con: analogia conectora + ejemplo KORA concreto + pregunta de verificacion practica. Nivel explicitado al inicio.
