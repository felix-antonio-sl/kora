---
_manifest:
  urn: urn:gn:kb:bpmn-d02-ciclo-presupuestario
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: "GORE Ñuble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- presupuesto
- bpmn
- finanzas
- gn
lang: es
---

# BPMN D02: Ciclo Presupuestario Regional

## Metadatos del Dominio

| Atributo | Valor |
| :--- | :--- |
| ID | DOM-PRESUPUESTO |
| Criticidad | Crítica |
| Dueño | DAF (Funcionamiento) / DIPIR (Inversión) |
| Procesos | 5 (P1–P5) + Modificaciones (transversal) |
| Subprocesos | ~15 |

## Mapa General: Ciclo Anual

| Proceso | Período |
| :--- | :--- |
| P1: Formulación | Mayo–Junio (año anterior) |
| P2: Aprobación | Septiembre–Noviembre |
| P3: Distribución | Diciembre–Enero |
| P4: Ejecución | Todo el año |
| P5: Control y Cierre | Diciembre–Enero |
| Modificaciones Presupuestarias | Transversal (durante P4) |

P5 retroalimenta a P1 en el ciclo siguiente.

## P1: Formulación del Presupuesto

**Período:** Mayo–Junio del año anterior.

### Flujo

1. DIPRES emite instructivo y clasificador presupuestario
2. Definir techos preliminares
3. Formulación paralela por áreas:
   - DIPIR: propuesta marco de inversión → cartera proyectos con RS vigente → asignaciones por fuente (FNDR/FRIL/FRPD)
   - DAF: Personal (Subt. 21) → Bienes/Servicios (Subt. 22) → Transferencias (Subt. 24)
4. Consolidación de propuesta
5. Presentación a Gobernador/a
6. Ajustes según prioridades ERD
7. Envío a DIPRES

### Estructura del Presupuesto

| Subtítulo | Concepto | Responsable |
| :--- | :--- | :--- |
| 21 | Personal | DAF |
| 22 | Bienes y Servicios | DAF |
| 24 | Transferencias Corrientes | DAF/DIPIR |
| 29 | Activos No Financieros | DAF |
| 31 | Inversión (Iniciativas) | DIPIR |
| 33 | Transferencias de Capital | DIPIR |

## P2: Aprobación del Presupuesto

Actores: Gobernador/a, CORE, DIPRES, CGR. El presupuesto regional requiere presentación formal y aprobación por estos organismos antes de su distribución.

## P3: Distribución Inicial

Distribución del presupuesto aprobado y carga en SIGFE para habilitar ejecución.

## P4: Ejecución Presupuestaria

Seguimiento continuo de compromisos, devengos y pagos durante el año. Proceso de Modificaciones Presupuestarias actúa como subproceso transversal.

## P5: Control y Cierre del Ejercicio

**Período:** Diciembre–Enero.

### Flujo de Control

1. Control interno (DAF, DIPIR, Unidad de Control)
2. Seguimiento DIPRES mensual
3. Sistema KPIs y alertas tempranas

### Flujo de Cierre (al 31/12)

1. Consolidar información (DAF)
2. Cerrar cuentas en SIGFE
3. Calcular deuda flotante
4. Regularizar deuda flotante
5. Informe de cierre a DIPRES/CGR
6. Evaluar resultados físicos y financieros
7. Informe evaluación ex post (DIPIR)

### Deuda Flotante

Obligaciones devengadas al 31/12 pendientes de pago. Financiamiento: SIC (si suficiente) o SIC + mayor aporte fiscal. Se incorpora en presupuesto año siguiente como primera prioridad de pago.

## Modificaciones Presupuestarias (Transversal)

Proceso que opera durante P4. Requiere Acuerdo CORE según criterios:

| Condición | Requiere CORE |
| :--- | :--- |
| Monto > 7.000 UTM | Sí |
| Nuevo programa/proyecto | Sí |
| Aumento costo ≤ 10% (tope 7.000 UTM) | No |
| Uso 3% emergencia (Glosa 14) | No |
| Regularización de ingresos | No |

## Reportería Oficial

| Reporte | Frecuencia | Destinatario |
| :--- | :--- | :--- |
| Informe Ejecución Mensual | Mensual | DIPRES, CORE |
| Informes por Glosas | Trimestral | Transparencia |
| Cartera de Proyectos | Mensual | Web institucional |
| Acuerdos CORE | 5 días hábiles | Web institucional |

## Sistemas Involucrados

| Sistema | Función |
| :--- | :--- |
| SYS-SIGFE | Gestión financiera central |
| SYS-BIP-SNI | Inversión pública |
| SYS-TRANSPARENCIA | Publicación de información |

## Normativa Aplicable

| Norma | Alcance |
| :--- | :--- |
| LOC 19.175 Art. 72-73 | Competencias presupuestarias |
| Decreto 854/2004 Hacienda | Clasificador presupuestario |
| Ley de Presupuestos (anual) | Marco legal del ejercicio |
| Glosa 14 Partida 31 | 3% emergencias |
| Glosa 16 Partida 31 | Transparencia |
| NICSP-CGR | Contabilidad gubernamental |
| Resolución 30/2015 CGR | Rendiciones |

## Referencias Cruzadas

| Dominio | Vínculo |
| :--- | :--- |
| D03 Gestión IPR | CDP, financiamiento proyectos |
| D08 Rendiciones | Contabilización, SIGFE |
| D04 Compras | Órdenes de compra, contratos |
