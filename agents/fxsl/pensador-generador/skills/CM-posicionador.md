---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:pensador-generador-cm-posicionador:2.0.0"
  type: "bootstrap_skill"
---

## Proposito

Establecer posicion dialectica completa antes de operar. Integra MBT: contexto (C1-C4), praxis (B1-B4) y posicion clasica (escala/perspectiva/rol).

## Input/Output

- **Input:** Problema o solicitud del usuario, contexto disponible
- **Output:** Posicion dialectica completa: contexto evaluado, praxis definida, posicion seleccionada

## Procedimiento

1. CONTEXTO (C1-C4):
   - C1-RECURSOS: tiempo, equipo, herramientas disponibles
   - C2-PROPOSITO: explorar <-> especificar, comunicar <-> computar, temporal <-> permanente
   - C3-DOMINIO: conocido <-> novedoso, estable <-> volatil, simple <-> complejo
   - C4-CULTURA: formal <-> informal, agil <-> planificado, tolerante <-> critico
2. PRAXIS (B1-B4):
   - B1-ALCANCE: incluir <-> omitir (que entra, que se excluye)
   - B2-AUDIENCIA: experto <-> novato, fidelidad <-> utilidad
   - B3-ESTRATEGIA: top-down <-> bottom-up, analisis <-> sintesis
   - B4-COMPLETITUD: completar <-> entregar, foco <-> contexto
3. POSICION CLASICA:
   - ESCALA: Micro (precision) <-> Macro (coherencia sistemica)
   - PERSPECTIVA: Usuario / Sistema / Implementador / Critico
   - ROL: Analista / Generador / Critico / Integrador
4. SENALES DE CAMBIO: Si analisis no avanza -> otra escala. Si perspectiva no revela -> rotar.

## Signature Output

Tabla con dimensiones evaluadas (C1-C4, B1-B4, Escala, Perspectiva, Rol) y seleccion justificada para cada una.
