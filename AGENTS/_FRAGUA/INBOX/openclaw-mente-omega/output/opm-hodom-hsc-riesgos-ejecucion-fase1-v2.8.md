# HODOM HSC
# Matriz de Riesgos de Ejecución — Fase I

Versión: 2.8
Fecha: 2026-04-09
Estado: matriz inicial de riesgos

Propósito: anticipar los riesgos más probables de implementación de Fase I para proteger coherencia, utilidad y adopción.

Base:
- `opm-hodom-hsc-fase1-plan-tactico-v1.5.md`
- `opm-hodom-hsc-fase1-paquetes-trabajo-v1.6.md`
- `opm-hodom-hsc-adrs-tecnicos-fase1-v2.7.md`

---

## 1. Escala usada

### Probabilidad
- Alta
- Media
- Baja

### Impacto
- Alto
- Medio
- Bajo

---

## 2. Matriz principal

| ID | Riesgo | Probabilidad | Impacto | Señal temprana | Mitigación |
|----|--------|--------------|---------|----------------|------------|
| R1 | Implementar UI antes de cerrar semántica | Alta | Alto | diseños avanzan sin acuerdo clínico | congelar glosario y ADRs antes de desarrollo fuerte |
| R2 | Duplicar lógica en frontend y generar inconsistencias | Alta | Alto | ficha/censo/admisión muestran cosas distintas | centralizar en vistas/contratos comunes |
| R3 | Diseñar un Plan de Atención demasiado complejo al inicio | Media | Alto | el equipo no logra llenarlo ni leerlo rápido | partir con versión mínima y legible |
| R4 | El estado canónico contradice datos históricos actuales | Alta | Alto | episodios “imposibles” o ambiguos | usar vista con bandera de inconsistencia |
| R5 | Riesgo clínico se vuelve decorativo y no cambia operación | Media | Alto | nadie lo usa para priorizar | definir acción mínima por categoría |
| R6 | Sobrecargar la ficha con demasiado contenido nuevo | Media | Medio | usuarios no encuentran lo importante | ubicar bloque alto, breve y jerarquizado |
| R7 | Censo pierde legibilidad por exceso de badges | Media | Medio | coordinación rechaza nueva tabla | intervenir con mínima carga visual |
| R8 | Agenda recibe semántica inmadura demasiado pronto | Media | Medio | equipo desconfía de prioridades nuevas | dejar agenda para consumo ligero tardío |
| R9 | Falta de adopción clínica del Plan de Atención | Media | Alto | se sigue trabajando solo con notas narrativas | validar con casos reales y ajuste rápido |
| R10 | Falta de responsable claro para actualizar riesgo | Alta | Medio | riesgo desactualizado o ausente | asignar responsabilidad y timestamp explícitos |
| R11 | Reporting y estado del episodio quedan desacoplados | Media | Alto | REM no conversa con la operación | incluir chequeo de coherencia temprano |
| R12 | Equipo percibe Fase I como burocracia extra | Media | Alto | resistencia verbal o uso superficial | mostrar beneficio con casos reales y lectura más rápida |
| R13 | Se intenta resolver todo en Fase I | Alta | Alto | backlog se infla y se frena | proteger alcance: plan, estado, riesgo |
| R14 | La semántica nueva no se valida con casos reales | Media | Alto | cierre basado solo en demo técnica | protocolo de validación obligatorio |
| R15 | Se crea estructura de datos nueva sin buena trazabilidad | Media | Medio | nadie sabe de dónde sale plan/riesgo | exigir fuente, responsable y timestamp |

---

## 3. Riesgos críticos a vigilar semanalmente

### R1 — UI antes de semántica
Si esto ocurre, el sistema se vuelve bonito antes de volverse claro.

### R2 — Duplicación de lógica
Si cada pantalla interpreta distinto plan/estado/riesgo, Fase I fracasa aunque el código compile.

### R4 — Contradicción con datos reales
Esto es casi seguro en algún grado. Hay que asumirlo y señalizarlo, no negarlo.

### R9 — No adopción clínica del plan
Si el plan no se vuelve útil de verdad, queda como cascarón.

### R13 — Inflación de alcance
La tentación de meter comunicación, cockpit y portal en esta fase puede romper el foco.

---

## 4. Mitigaciones estructurales

## 4.1 Mitigación de gobierno
- ADRs aprobados
- glosario mínimo congelado
- núcleo decisor con cadencia corta

## 4.2 Mitigación de producto
- backlog priorizado P0/P1/P2
- criterio claro de fuera de alcance
- validación por caso real, no solo por checklist técnica

## 4.3 Mitigación de datos
- contratos de datos comunes
- vistas canónicas compartidas
- banderas de inconsistencia en vez de ocultamiento

## 4.4 Mitigación de adopción
- probar con casos reales del equipo
- mostrar valor en ficha y censo primero
- preferir lectura rápida sobre perfección documental

---

## 5. Riesgos por épica

### Plan de Atención
- exceso de complejidad
- baja adopción
- duplicación con notas existentes

### Estado del Episodio
- mapeo confuso con estados actuales
- mezcla con tipo de egreso
- contradicción entre pantallas

### Riesgo
- falta de confianza clínica
- categoría sin consecuencia operativa
- actualización irregular

---

## 6. Indicadores de deriva del proyecto

Si aparecen estas señales, hay que intervenir:

1. discusiones largas sobre taxonomías antes de probar casos
2. pantallas nuevas sin contrato de datos claro
3. episodios reales que no entran en la nueva semántica
4. coordinación que sigue usando atajos verbales en vez del sistema
5. backlog creciendo más rápido que la validación

---

## 7. Criterio de control ejecutivo

Dirección Técnica y Coordinación deberían preguntar periódicamente:

1. ¿Esto hizo más claro el episodio o solo agregó campos?
2. ¿Esto mejoró la coordinación o solo embelleció la pantalla?
3. ¿Esto redujo ambigüedad o la movió de lugar?
4. ¿Esto ya sirve con casos reales o todavía es una idea técnica?

---

## 8. Veredicto

El mayor riesgo de Fase I no es técnico.

El mayor riesgo es perder foco y producir una capa nueva que parezca orden, pero no cambie realmente la inteligibilidad operativa del sistema.

Por eso la protección central debe ser:

**menos ambición ornamental, más rigor semántico y validación real.**
