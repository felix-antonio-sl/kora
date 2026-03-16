---
_manifest:
  urn: urn:gn:skill:goreologo-specialist-router:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-SPECIALIST-ROUTER

## Proposito
Determinar si una consulta debe ser derivada a un agente especialista del namespace gn o retenida por goreologo para sintesis cross-domain.

## Input/Output
- **Input:** Consulta clasificada por CM-INTAKE con dimension institucional y tipo identificados
- **Output:** Decision de routing: ROUTE_TO_SPECIALIST(agente) | SYNTHESIZE_CROSS_DOMAIN

## Procedimiento

### Tabla Dominio → Agente Especialista

| Dominio | Agente Especialista | Indicadores |
|---------|---------------------|-------------|
| Derecho administrativo, actos juridicos, dictamenes, toma de razon | gn/asesor-juridico | clasificar acto, redactar resolucion, validar legalidad, tramitar |
| Gestion IPR, formulacion proyectos, evaluacion, rendiciones, inversion estrategica | gn/gestor-ipr-360 | FNDR, FRIL, FRPD, BIP, formular, evaluar, rendir, brechas territoriales |
| Recursos operacionales, presupuesto, contabilidad, RRHH, compras | gn/erp-gore | SIGFE, subtitulos, pagos, compras, personal, activo fijo |
| Vision estrategica, CORE, representacion, prospectiva, ExO-GORE | gn/gobernador-virtual | vision, CORE, mayorias, prospectiva, aceleracion, GORE 4.0 |
| Control gestion, procesos, DMAIC, navegacion social, estructura | gn/dgi-virtual | indicadores, dashboard, BPMN, Lean, ADKAR, Meyer |
| Transformacion digital, TDE, Ley 21.180, plataformas | gn/digitrans | TDE, Ley 21.180, ClaveUnica, SIMPLE, CPAT |
| Coordinacion, visado, supervision, subrogancia | gn/ar-virtual | coordinar divisiones, visar actos, supervisar, subrogar |

### Logica de Decision

1. Clasificar dominios involucrados en la consulta (puede ser 1 o mas).
2. IF single-domain → ROUTE_TO_SPECIALIST: recomendar agente especialista.
3. IF cross-domain (2+ dominios) → SYNTHESIZE_CROSS_DOMAIN: retener en goreologo para sintesis integradora.
4. IF ambiguo → presentar opciones al usuario antes de decidir.

### Criterios de Retencion (goreologo sintetiza)
- Consultas que cruzan marco legal + financiero + operativo
- Preguntas generales sobre "como funciona el GORE"
- Comparaciones entre instrumentos de distintos dominios
- Consultas de induccion o vision panoramica

## Signature Output
Decision: ROUTE_TO_SPECIALIST(gn/agente-slug) con justificacion, o SYNTHESIZE_CROSS_DOMAIN con dominios involucrados identificados.
