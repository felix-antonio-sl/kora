---
_manifest:
  urn: "urn:fxsl:skill:tester-coverage-reporter:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-COVERAGE-REPORTER

## Proposito
Calcula y reporta cobertura de tests por criterio de aceptacion, por componente y por tipo. Identifica gaps: ACs sin tests, componentes sin integracion, paths no cubiertos.

## Input/Output
- **Input:** Resultados de ejecucion (output de CM-TEST-EXECUTOR) + historias con ACs + mapa de componentes
- **Output:** Reporte de cobertura: {cobertura_por_ac, cobertura_por_componente, cobertura_por_tipo, gaps[], recomendaciones[]}

## Procedimiento

### Paso 1: Mapear ACs a tests
- Listar todos los ACs de las historias en scope.
- Para cada AC, buscar tests que lo cubren (por naming convention, por tag, por mapping explicito).
- Clasificar: AC_CUBIERTO (tiene al menos 1 test que pasa), AC_PARCIAL (tiene test pero falla), AC_DESCUBIERTO (no tiene test).
- Calcular: cobertura_ac = AC_CUBIERTO / AC_TOTAL * 100.

### Paso 2: Mapear componentes a tests
- Listar componentes del sistema (desde ARCHITECTURE.md o inferido de estructura de archivos).
- Para cada componente, contar tests por tipo:
  - Unitarios: tests que cubren logica interna del componente.
  - Integracion: tests que cubren boundaries del componente con otros.
  - Aceptacion: tests de AC que involucran este componente.
- Identificar componentes con 0 tests de integracion → gap critico.

### Paso 3: Calcular cobertura por tipo
- Contar tests por tipo: {unit: N, acceptance: N, integration: N}.
- Calcular proporcion: unit/total, acceptance/total, integration/total.
- Evaluar balance: si acceptance = 0 y hay ACs → gap critico.

### Paso 4: Identificar gaps
- **Gap tipo A (critico):** AC sin ningun test → listar AC_ID + descripcion.
- **Gap tipo B (critico):** Componente con boundaries sin test de integracion → listar componente + boundaries.
- **Gap tipo C (advertencia):** Tests que fallan consistentemente → posible test fragil o defecto no resuelto.
- **Gap tipo D (informativo):** Componentes con solo tests unitarios, sin aceptacion ni integracion.
- Priorizar gaps: A > B > C > D.

### Paso 5: Generar recomendaciones
- Por cada gap tipo A: "Generar test de aceptacion para AC [id]: [descripcion]."
- Por cada gap tipo B: "Generar test de integracion para boundary [from→to]."
- Por cada gap tipo C: "Investigar test fragil: [test_name]. Posible causa: [hipotesis]."
- Estimar esfuerzo: cantidad de tests faltantes por tipo.

### Paso 6: Emitir reporte
- Tabla de cobertura por AC.
- Tabla de cobertura por componente.
- Resumen de cobertura por tipo.
- Lista de gaps priorizada.
- Recomendaciones con esfuerzo estimado.

## Invariantes
- Todo AC DEBE aparecer en el reporte (cubierto o descubierto).
- Gaps tipo A (AC sin test) son siempre criticos. No se toleran.
- El reporte no modifica tests ni codigo. Solo diagnostica.
- Datos basados en ultima ejecucion de suite (requiere CM-TEST-EXECUTOR previo).

## Signature Output
```
## Cobertura por AC
| AC  | Historia | Tests | Status     |
|-----|----------|-------|------------|
| AC1 | STORY-1  | 2     | CUBIERTO   |
| AC2 | STORY-1  | 1     | CUBIERTO   |
| AC3 | STORY-2  | 0     | DESCUBIERTO|

## Cobertura por Componente
| Componente     | Unit | Acceptance | Integration | Total |
|----------------|------|------------|-------------|-------|
| ProductService | 8    | 2          | 3           | 13    |
| OrderService   | 5    | 1          | 0           | 6     |

## Cobertura por Tipo
| Tipo        | Count | % del Total |
|-------------|-------|-------------|
| Unit        | 30    | 71.4%       |
| Acceptance  | 8     | 19.0%       |
| Integration | 4     | 9.5%        |

## Gaps (priorizado)
1. [CRITICO] AC3 (STORY-2) sin test de aceptacion
2. [CRITICO] OrderService sin test de integracion (boundary→PaymentGateway)
3. [ADVERTENCIA] test_order_timeout falla intermitentemente

## Recomendaciones
- Generar 1 test aceptacion para AC3
- Generar 2 tests integracion para OrderService boundaries
- Investigar test_order_timeout (posible non-determinism)
```
