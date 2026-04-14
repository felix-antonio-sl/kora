---
_manifest:
  urn: urn:fxsl:skill:neriomath-posicionador:1.2.0
  type: lazy_load_endofunctor
---

## Proposito
Establecer posicion dialectica completa antes de operar. Integra MBT (contexto C1-C4, praxis B1-B4), diagnostico de escala causal (micro/meso/macro) y posicion clasica (perspectiva/rol). Alimenta escala al motor para cross-index tension-escala.

## Input/Output
- **Input:** Problema o solicitud del usuario, clase de activacion
- **Output:** Posicion dialectica: contexto evaluado, praxis definida, escala causal diagnosticada (con señal para cross-index), perspectiva y rol seleccionados

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
3. ESCALA CAUSAL:
   - Diagnosticar si el problema fue planteado en escala micro, meso o macro
   - No asumir que la escala percibida es la escala causal
   - Proponer intervenir donde exista mayor palanca causal
   - Emitir escala diagnosticada como señal para el motor: el cross-index tension-escala filtrara tensiones MBT por productividad segun esta escala
4. POSICION CLASICA:
   - PERSPECTIVA: Usuario / Sistema / Implementador / Critico
   - ROL: Analista / Generador / Critico / Integrador
5. SENALES DE CAMBIO: Si analisis no avanza -> otra escala. Si perspectiva no revela -> rotar.
6. PUNTOS CIEGOS: Que perspectivas no estoy tomando? Que escalas estoy ignorando?
7. En CLASE-2: modo compacto — evaluar solo dimensiones relevantes. En CLASE-3: evaluacion completa.

## Signature Output
Tabla con dimensiones evaluadas (C1-C4, B1-B4, Escala causal, Perspectiva, Rol) y seleccion justificada. Escala causal emitida como señal para cross-index. En modo compacto: solo dimensiones activas.
