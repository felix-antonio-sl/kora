---
_manifest:
  urn: urn:gn:kb:bpmn-d03-gestion-ipr
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: "GORE Ñuble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- bpmn
- ipr
- gestion-publica
- gn
lang: es
---

# BPMN D03: Gestión de Intervenciones Públicas Regionales (IPR)

## Metadatos del Dominio

| Atributo | Valor |
| :--- | :--- |
| ID | DOM-IPR |
| Criticidad | Crítica |
| Dueño | Jefatura DIPIR |
| Procesos | 9 (P0–P7 + modificaciones) |
| Subprocesos | ~25 |

## Mapa General: Ciclo de Vida IPR

Pre-Fase (P0) → P1 Ingreso y Admisibilidad → P2 Evaluación Técnico-Económica → P3 Financiamiento → P4 Formalización → P5 Ejecución y Supervisión ↔ P6 Modificaciones → P7 Cierre y Evaluación Ex Post

## P0: Selector de Vías de Financiamiento

**Tipo:** Pre-Fase (Decisión Estratégica). Orienta la selección de vía antes de formulación.

### Matriz de Decisión

| Vía | Tipo IPR | Ejecutor | Monto | Condición clave |
| :--- | :--- | :--- | :--- | :--- |
| FRIL | Proyecto | Municipalidad | < 5.000 UTM | Infraestructura menor |
| Circular 33 | Proyecto | Variable | Variable | Conservación, ANF, estudios |
| FRPD | Ambos | Habilitado | Variable | Foco productivo/innovación |
| SNI General | Proyecto | Variable | Variable | Default |
| 8% FNDR | Actividad | Privado s/f lucro | Variable | Concurso |
| Glosa 06 | Programa | GORE | Variable | Ejecución directa |
| Transferencia | Programa | Entidad pública | Variable | ITF interno |

### Árbol de Decisión

- Propósito principal = Activo Durable → PROYECTO
  - Municipio + < 5.000 UTM → FRIL
  - Conservación/ANF/Estudio → Circular 33
  - Foco productivo → FRPD
  - Default → SNI General
- Propósito principal = Servicio/Prestación → PROGRAMA
  - Privado sin fines de lucro → 8% FNDR
  - GORE → Glosa 06
  - Entidad Pública → Transferencia
  - Foco productivo → FRPD

## P1: Ingreso, Pertinencia y Admisibilidad

**Subprocesos:** Recepción, CDR, Admisibilidad Documental.

### Flujo

1. Entidad Externa prepara postulación
2. Oficina de Partes: recepcionar y registrar
3. DIPIR: registrar en sistema
4. CDR: evaluar pertinencia estratégica → ¿Pre-admisible?
   - No → inadmisible
   - Sí → continúa
5. Analista Preinversión: revisión documental exhaustiva
6. Estado de admisibilidad:
   - Admisible → avanza a P2
   - Con Observaciones → subsanación en plazo → si OK, admisible; si no, inadmisible
   - Inadmisible → fin

### Roles

| Rol | Responsabilidad |
| :--- | :--- |
| Oficina de Partes | Recepcionar, registrar, derivar |
| Jefatura DIPIR | Registrar, convocar CDR |
| CDR | Evaluar pertinencia estratégica |
| Analista Preinversión | Revisión documental exhaustiva |

## P2: Evaluación Técnico-Económica

**Tracks:** A (SNI), B (Glosa 06), C (Simplificadas), D (Transferencias).

### Asignación de Track

| Track | Tipo de Iniciativa |
| :--- | :--- |
| A: SNI/MDSF | Proyecto IDI |
| B: Glosa 06/DIPRES | Programa GORE |
| C: Vías Simplificadas | FRIL/FRPD/C33/8% |
| D: ITF Interno | Transferencia a Entidad Pública |

### Track A: SNI/MDSF

1. Revisión interna GORE, verificar RIS aplicable
2. Cargar en BIP/Carpeta Digital
3. Oficio a MDSF
4. MDSF evalúa (5+10 días)
5. RATE: RS (aprobado) / FI (subsanar en 60 días, reitera evaluación) / OT (rechazado)

### Track B: Glosa 06

1. Perfil MML → Diseño MML
2. DIPRES/SES evalúa → RF / FI / OT

### Track C: Vías Simplificadas

- FRIL: Postular GESDOC+BIP → Admisibilidad → Evaluación técnica → RS (60 días)
- FRPD: Formulario online → Adm. Administrativa → Adm. Técnica/Ranking → Evaluación GORE → RS
- Circular 33: GESDOC+BIP → Admisibilidad → Revisión técnica → RS/FI/OT

### Track D: Transferencias

1. Postulación GESDOC → Admisibilidad DAE → Evaluación MML → ITF Interno

## P3: Obtención de Financiamiento

**Rutas:** A (Sin CORE), B (Con CORE).

### Criterios para Acuerdo CORE

| Condición | Requiere CORE |
| :--- | :--- |
| Monto > 7.000 UTM | Sí |
| Nuevo programa/proyecto | Sí |
| Aumento costo ≤ 10% (tope 7.000 UTM) | No |
| Uso 3% emergencia (Glosa 14) | No |
| Regularización de ingresos | No |

### Ruta A (Sin CORE)

1. Solicitar CDP → DAF emite CDP → Instrucción a Dpto. Presupuesto

### Ruta B (Con CORE)

1. Preparar carpeta CORE
2. Envío formal al CORE
3. Votación CORE → ¿Aprobado?
   - Sí → Certificado Acuerdo CORE → Solicitar creación presupuestaria
   - No → rechazado

## P4: Formalización

**Subprocesos:** Actos, Convenio, Devengo.

### Flujo

1. Financiamiento aprobado
2. Según tipo de modificación:
   - Interna → Resolución GORE
   - Afecta Partida 31 → Solicitud a DIPRES
3. Visaciones internas (DAF, DIPIR, Jurídica)
4. Firma Gobernador/a
5. Control externo (DIPRES/CGR)
6. Elaborar Convenio de Transferencia → Revisión Jurídica → Firma GORE + Entidad Receptora
7. Resolución aprobatoria
8. Programar transferencias

### Regla de Devengo

| Tipo de Receptor | Momento del Devengo |
| :--- | :--- |
| Privados y Municipios | Convenio tramitado |
| Servicios Públicos | Al aprobar rendición |

## P5: Ejecución y Supervisión

**Subprocesos:** Inicio, Licitación, Seguimiento.

### Flujo de Inicio

1. Chequeo documentación técnica
2. Reunión de coordinación GORE-UT
3. Carpeta de seguimiento

### Flujo de Licitación (si aplica)

1. Bases y publicación en Mercado Público
2. Adjudicación → Contrato → Entrega terreno/Orden de inicio

### Seguimiento

- Visitas a terreno
- Revisión de informes de avance
- Estados de Pago
- Actualizar BIP
- Monitoreo financiero SIGFE
- Comité de seguimiento

### Hitos de Control

| Hito | Responsable |
| :--- | :--- |
| Inicio de obra | UT / ITO |
| Avances periódicos | Supervisor GORE |
| Recepción provisoria | UT |
| Recepción definitiva | UT |

## P6: Modificaciones en Ejecución

**Subprocesos:** Solicitud, Evaluación, Tramitación.

### Flujo

1. Detectar necesidad → UT prepara informe técnico → Oficio formal al GORE
2. Supervisor GORE analiza → ¿Altera objetivo?
   - Sí → rechazar
   - No → verificar umbrales → ¿Requiere CORE/SNI?
     - Sí → tramitar como nueva aprobación
     - No → aprobar internamente
3. Convenio modificatorio

## P7: Cierre Técnico-Financiero y Evaluación Ex Post

**Subprocesos:** Cierre Técnico, Cierre Financiero, Evaluación Ex Post.

### Cierre Técnico

1. Recepción provisoria → período de garantía → recepción definitiva → informe final técnico

### Cierre Financiero

1. Rendición final SISREC → Revisión DAF → ¿Saldos pendientes?
   - Sí → Reintegro → Resolución cierre convenio
   - No → Resolución cierre convenio
2. Devolución de garantías

### Evaluación Ex Post

1. Selección muestra → Estudio evaluativo → Lecciones aprendidas

## Sistemas Involucrados

| Sistema | Fases de Uso |
| :--- | :--- |
| SYS-BIP-SNI | P1, P2, P5, P7 |
| SYS-GESDOC | P1, P2 |
| SYS-SIGFE | P3, P4, P5, P7 |
| SYS-SISREC | P7 |

## Normativa Aplicable

| Norma | Alcance |
| :--- | :--- |
| LOC 19.175 | Competencias GORE |
| Ley de Presupuestos | Glosa 06, 14, 16 |
| Instructivo SUBDERE FRIL | Track C |
| Circular 33 MDSF | Track C |
| Resolución 30/2015 CGR | Rendiciones |
| Normas SNI/MDSF | Track A |

## Referencias Cruzadas

| Dominio | Vínculo |
| :--- | :--- |
| D02 Ciclo Presupuestario | CDP, modificaciones, SIGFE |
| D08 Rendiciones | Cierre financiero, SISREC |
| D01 Actos Administrativos | Resoluciones, Convenios |
