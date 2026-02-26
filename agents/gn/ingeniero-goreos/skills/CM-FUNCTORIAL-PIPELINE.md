---
_manifest:
  urn: "urn:gn:skill:ingeniero-goreos-functorial-pipeline:2.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Razonar sobre la cadena completa GORE_OS: Dominio GORE -> Blueprint -> Sistema -> Infra -> Code. Asegurar consistencia end-to-end entre capas.

## Input/Output

- **Input:** Cambio propuesto en cualquier capa GORE_OS
- **Output:** Analisis de impacto en cadena, verificacion de consistencia, acciones requeridas en otras capas

## Procedimiento

1. Identificar capa de origen del cambio:
   - D_GORE: Dominio institucional (Omega v2.6.0: FNDR, FRPD, IPR)
   - D_BLUEPRINT: Especificacion funcional (Dominios, Modulos, US)
   - D_SYSTEM: Arquitectura tecnica (Python, Flask, HTMX)
   - D_INFRA: Contenedores Docker + PostgreSQL/PostGIS
   - D_CODE: Implementacion SQLAlchemy + Jinja2

2. Propagar cambio via functores:
   - Cambio en Dominio -> actualizar Blueprint -> actualizar Sistema -> actualizar Code
   - Cambio en Blueprint -> verificar alineamiento con Dominio -> propagar a Sistema
   - Cambio en Code -> verificar consistencia con Blueprint

3. Evaluar preservacion de estructura:
   - En que categoria GORE_OS estoy trabajando?
   - Que functor traduce a la siguiente capa?
   - Que cambios en capas anteriores afectan esta?
   - El diseno es consistente end-to-end?

4. Aplicar OPM (Omega v2.6.0):
   - Objetos (Nouns): IPR polimorfica (Proyecto vs Programa)
   - Procesos (Verbs): Tracks evaluacion A-E (SNI, Circ33, FRIL, PPR, FRPD)
   - Estados: MCD F0 (Formulacion) -> F1 (Admisibilidad) -> F2 (Evaluacion) -> F3 (Priorizacion) -> F4 (Ejecucion) -> F5 (Cierre)

5. Evaluar impacto sociotecnico:
   - Respeta cultura GORE?
   - Es habilitador (tool) o reemplazo (automation)?
   - Considera carga cognitiva del funcionario?
   - Nivel HAIC: M1 (Sugerencia) a M6 (Autonomo) es adecuado?

## Signature Output

Capa origen + Impacto propagado por capa (tabla) + Acciones requeridas + Verificacion consistencia end-to-end.
