---
_manifest:
  urn: urn:gn:kb:mecanismos-matriz-decision
  provenance:
    created_by: kora/curator
    created_at: '2026-03-16'
    source: ssot-mecanismos v1.1.1 + ssot-ipr-lifecycle v1.2.1 + selector-ipr v1.0.0
version: 1.0.0
status: published
tags:
- mecanismos
- financiamiento
- arbol-decision
- tracks
- fril
- frpd
- sni
- c33
- glosa06
- subvencion-8
- gore-nuble
lang: es
extensions:
  gn:
    family: guide
relations:
  cites:
  - urn:gn:kb:guia-circular-33-sts
  - urn:gn:kb:guia-fril-2025-sts
  - urn:gn:kb:guia-frpd-nuble
  - urn:gn:kb:guia-idi-sni-sts
  - urn:gn:kb:guia-programas-directos-gore
  - urn:gn:kb:instructivo-subvencion-8-2025-sts
  - urn:gn:kb:transferencia-ppr
---


# Matriz Unificada de Mecanismos de Financiamiento — GORE Ñuble

## Resumen

Vista comparativa consolidada de los 7 mecanismos de financiamiento del GORE Ñuble. Árbol de decisión canónico (7 pasos), tabla unificada mecanismo × track × evaluador × dictamen, catálogo de costos y plazos, restricciones cruzadas, bifurcación FRPD, niveles de proporcionalidad SNI y plazos de evaluación por track. Complementa las 7 guías individuales por mecanismo con comparaciones cruzadas imposibles de obtener por separado.

---

## Árbol de decisión canónico (7 pasos)

### Paso 1 — Naturaleza de la IPR

¿Crea activo físico durable? → Sí: PROYECTO (S31/S33). No: PROGRAMA (S24).

### Paso 2 — FRIL

Si PROYECTO: ¿Monto < 4.545 UTM + ejecutor municipal? → Sí: **FRIL** (Track C).

### Paso 3 — Circular 33

Si PROYECTO no-FRIL: ¿Es conservación/reposición/ANF/estudio del giro? → Sí: **C33** (Track B).

### Paso 4 — SNI General

Si PROYECTO estándar (no FRIL, no C33): → **SNI** (Track A).

### Paso 5 — Glosa 06

Si PROGRAMA: ¿Ejecución directa GORE? → Sí: **Glosa 06** (Track D1).

### Paso 6 — Transferencia o Subv8

Si PROGRAMA con ejecución por terceros: ¿Concurso 8% FNDR? → Sí: **Subv8** (Track E1). No: **Transferencia PPR** (Track D2).

### Paso 7 — FRPD

Routing especial: FRPD ingresa por concurso de elegibilidad, luego bifurca post-selección:

| Línea FRPD | Evaluación posterior | Derivación |
|------------|---------------------|-----------|
| CTCI (Ciencia/Tecnología/Conocimiento/Innovación) | Exenta evaluación ex-ante | Directa a formalización |
| Fomento — Proyecto | Requiere evaluación SNI/MDSF | → Track A |
| Fomento — Programa | Requiere evaluación PPR | → Track D1 |

---

## Tabla unificada de mecanismos

| Track | Mecanismo | Fuente | Subtítulo | Evaluador | Dictamen | Modo ejecución | Tipo IPR |
|-------|-----------|--------|-----------|-----------|----------|----------------|----------|
| A | SNI General | FNDR | S31 | MDSF | RS (Recomendación Satisfactoria) | Directa GORE / Terceros | Proyecto |
| B | Circular 33 | — | S31 | MDSF/GORE | AD (Admisibilidad) | Directa GORE | Proyecto |
| C | FRIL | FNDR | S33 | GORE (DIPIR) | AT (Aprobación Técnica) | Municipalidad | Proyecto |
| D1 | Glosa 06 | — | S24 | DIPRES/SES | RF (Recomendación Favorable) | Directa GORE | Programa |
| D2 | Transferencia PPR | — | S24 | GORE (Comité/DAE) | ITF (Informe Técnico Favorable) | Entidad pública | Programa |
| E1 | Subvención 8% | FNDR | S24 | GORE (Comisión) | Puntaje/Ranking | OSC/Municipio | Programa |
| E2 | FRPD | FRPD | S31/S33 | ANID/CORFO/GORE | Elegibilidad + RS/RF | Inst. habilitada | Productivo |

---

## Catálogo unificado — Costo, ejecutor, plazo

| Track | Costo típico | Ejecutor | Plazo ejecución | Modo ejecución |
|-------|-------------|----------|----------------|----------------|
| A — SNI | >15.000 UTM | GORE/Terceros | 12-36 meses | Directa o transferencia |
| B — C33 | Variable | GORE | Variable | Directa |
| C — FRIL | <4.545 UTM (Ñuble) | Municipalidad | 12-18 meses | Transferencia |
| D1 — Glosa 06 | Variable | GORE (directo) | 8-12 meses | Directa |
| D2 — Transfer | <$15M típico | Entidad pública | 8-12 meses | Transferencia |
| E1 — Subv8 | <$8M | OSC/Municipio | 8-9 meses | Transferencia |
| E2 — FRPD | Variable | Inst. habilitada | ≤30 meses | Según línea |

---

## Restricciones operativas cruzadas

| Mecanismo | Restricción | Consecuencia |
|-----------|------------|--------------|
| FRIL | Fraccionamiento de obras prohibido | Rechazo postulación |
| FRIL | Plazo licitación 90 días | Caducidad asignación |
| Glosa 06 | Admin GORE max 5% monto total | Rechazo DIPRES |
| Transfer (D2) | Honorarios max 5% monto total | Ajuste o rechazo |
| Subv8 | Rendiciones pendientes en SISREC | Inhabilidad total (bloqueo Art. 18 Res. 30 CGR) |
| C33 | Cofinanciamiento ANF ≥20% | Requisito habilitante |
| FRPD | Garantía privados >1.000 UTM: 5% total + 90d post-término | Requisito habilitante |

### Restricciones transversales (Glosa 03)

Prohibido usar recursos de inversión regional para: préstamos, gastos en personal o bienes/servicios de consumo de entidades receptoras, constituir/efectuar aportes/comprar sociedades. Aplica a todos los mecanismos.

---

## Niveles de proporcionalidad SNI (4)

Aplica a Track A. El rigor de evaluación se adapta a la magnitud del proyecto.

| Nivel | Umbral | Etapas preinversionales |
|-------|--------|------------------------|
| 0 | < 5.000 UTM | Solo Ejecución (exención evaluación) |
| 1 | Baja complejidad | Perfil → Ejecución |
| 2 | Estándar | Perfil → Prefactibilidad → Ejecución |
| 3 | Alta complejidad | Idea → Perfil → Prefactibilidad → Factibilidad → Ejecución |

Indicadores económicos obligatorios: VAN (≥0), TIR (≥TSD), VAC (menor preferido), CAE (menor preferido). TSD 2025: 5,5%.

---

## Resultados de evaluación (10)

| Código | Nombre completo | Track |
|--------|----------------|-------|
| RS | Recomendación Satisfactoria | A (SNI) |
| FI | Falta Información | A (SNI) |
| OT | Objetado Técnicamente | A (SNI) |
| AD | Admisible | B (C33), C (FRIL) |
| RF | Recomendación Favorable | D1 (Glosa 06) |
| ITF | Informe Técnico Favorable | D2 (Transfer) |
| AT | Aprobación Técnica | C (FRIL) |
| Elegible | Elegible (FRPD/FIC) | E2 (FRPD) |
| NV | No Viable | Transversal |
| Puntaje | Puntaje (concursos) | E1 (Subv8), E2 (FRPD) |

Vigencia RS: 3 años presupuestarios consecutivos (año obtención + 2 siguientes). Si no se identifica presupuesto, RS caduca y requiere re-evaluación.

---

## Plazos de evaluación por proceso

| Proceso | Plazo | Responsable |
|---------|-------|-------------|
| Admisibilidad MDSF (Track A) | 10 días hábiles | MDSF |
| Análisis técnico-económico (Track A) | 45-90 días típico | MDSF |
| Respuesta a observaciones FI/OT | 60 días hábiles | Institución patrocinadora |
| Identificación presupuestaria post-RS | 20 días hábiles | DIPRES |
| Admisibilidad FRIL (Track C) | 5 días | DIPIR |
| Evaluación técnica FRIL (Track C) | 60 días | DIPIR |
| Subsanación FRIL | 30 días | Municipalidad |
| Licitación FRIL | 45 días | Municipalidad |
| Toma de Razón CGR | 15 días hábiles (no perentorio) | CGR |
| Postulación C33 (Track B) | Hasta 31 de octubre | GORE |

---

## Categorías FRIL (12)

| Grupo | Código | Nombre | Exención límite comunal |
|-------|--------|--------|:----------------------:|
| A — Desarrollo Territorial | A1 | Integración Rural | No |
| | A2 | Acceso al Agua | Sí |
| | A3 | Vial | Sí |
| B — Servicios | B1 | Edificación Pública | No |
| | B2 | Gestión Riesgos | No |
| | B3 | Seguridad | No |
| C — Desarrollo Social y Económico | C1 | Inclusión | No |
| | C2 | Género | No |
| | C3 | Turismo | No |
| D — Medio Ambiente | D1 | Deportes | No |
| | D2 | Áreas Verdes | No |
| | D3 | Sustentabilidad | No |

Máximo 5 proyectos por comuna (A2/A3 exentos). Monto mínimo M$100. Umbral máximo 4.545 UTM (Ñuble, incluye 10% variacional).

---

## Fondos temáticos Subvención 8% (7)

| Fondo | Techo |
|-------|-------|
| Cultura | $5M |
| Deporte | $5M |
| Social | $5,5M |
| Seguridad Ciudadana | $8M |
| Medio Ambiente | $5M |
| Adulto Mayor | $4M |
| Género | $6,5M |

Asignación directa excepcional: ≤10% del fondo, previo acuerdo CORE (Res. 72/2025 DIPRES). Pagaré notarial 100% monto + 18 meses vigencia. Unicidad: max 1 iniciativa por institución (excepciones: Cultura/Deporte 2da de Representación; Colaboradores Mejor Niñez múltiples residencias).

---

## FRPD — Detalle concurso

### Admisibilidad (6 criterios)

- Max 2 iniciativas por postulante
- Plazo ejecución ≤30 meses
- Cobertura regional (21 comunas) o territorial justificado
- Max remuneraciones 30%
- Min 1 profesional local (residente en Ñuble)
- Gastos admin max 5% (Art. 25 Ley 21.796)

### Ponderación evaluación técnica

| Criterio | Peso |
|----------|------|
| Mérito Innovador | 40% |
| Coherencia Regional (ERD) | 30% |
| Coherencia Componentes | 20% |
| Coherencia Global | 10% |

Elegibilidad mínima: 5 puntos promedio ponderado. Aprobación CORE: >7.000 UTM. Sectores prioritarios 2025: Atracción de Inversiones, Desarrollo Empresarial, Turismo y Medioambiente, Energía y Conectividad.

---

## Certificados de pertinencia sectorial

| Tipo proyecto | Servicio emisor | Organismo |
|--------------|----------------|-----------|
| Infraestructura deportiva | IND | Mindep |
| Infraestructura sanitaria | Servicio de Salud regional | Minsal |
| Vialidad rural (caminos) | Dirección de Vialidad | MOP |
| Vialidad urbana (pavimentación) | SERVIU | MINVU |
| Edificación pública | SERVIU | MINVU |
| Estudios del giro (S22) | DIPRES (autorización) | Hacienda |

---

## Guías individuales por mecanismo

| Track | URN guía detallada |
|-------|--------------------|
| A — SNI | [urn:gn:kb:guia-idi-sni-sts](urn:gn:kb:guia-idi-sni-sts) |
| B — C33 | [urn:gn:kb:guia-circular-33-sts](urn:gn:kb:guia-circular-33-sts) |
| C — FRIL | [urn:gn:kb:guia-fril-2025-sts](urn:gn:kb:guia-fril-2025-sts) |
| D1 — Glosa 06 | [urn:gn:kb:guia-programas-directos-gore](urn:gn:kb:guia-programas-directos-gore) |
| D2 — Transfer | [urn:gn:kb:transferencia-ppr](urn:gn:kb:transferencia-ppr) |
| E1 — Subv8 | [urn:gn:kb:instructivo-subvencion-8-2025-sts](urn:gn:kb:instructivo-subvencion-8-2025-sts) |
| E2 — FRPD | [urn:gn:kb:guia-frpd-nuble](urn:gn:kb:guia-frpd-nuble) |
