---
_manifest:
  urn: urn:gn:skill:goreologo-specialist-router:1.0.0
  type: lazy_load_endofunctor
---

# CM-SPECIALIST-ROUTER

## Proposito
Determinar si una consulta debe ser derivada a un agente especialista del namespace gn o retenida por goreologo para sintesis cross-domain.

## Input/Output
- **Input:** Consulta clasificada por CM-INTAKE con dimension institucional y tipo identificados
- **Output:** Recomendacion estructurada: {dominio, agente_recomendado, justificacion}

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
2. Si single-domain: identificar el agente especialista correspondiente y producir recomendacion con justificacion.
3. Si cross-domain (2+ dominios): listar los dominios involucrados e indicar que la consulta requiere sintesis integradora.
4. Si ambiguo: presentar opciones al usuario antes de decidir.

### Criterios de Sintesis Integradora
- Consultas que cruzan marco legal + financiero + operativo
- Preguntas generales sobre "como funciona el GORE"
- Comparaciones entre instrumentos de distintos dominios
- Consultas de induccion o vision panoramica

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| dominio | string | Dominio principal identificado |
| agente_recomendado | string \| null | Slug del agente especialista si aplica, null si cross-domain |
| dominios_involucrados | string[] | Lista de dominios detectados |
| justificacion | string | Razon de la recomendacion |
