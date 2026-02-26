---
_manifest:
  urn: urn:gn:kb:bpmn-d06-flota-vehicular
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: "GORE Ñuble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- flota-vehicular
- logistica
- bpmn
- gn
lang: es
---

# BPMN D06: Gestión de Flota Vehicular

## Metadatos del Dominio

| Atributo | Valor |
| :--- | :--- |
| ID | DOM-FLOTA |
| Criticidad | Media |
| Dueño | Jefe Servicios Generales |
| Procesos | 1 proceso, 6 subprocesos |
| Normativa | D.L. 799 (restricción uso vehículos fiscales) |

## Mapa General

S1 Registro de vehículos y conductores → S2 Solicitud y asignación → S3 Bitácora de viaje → S4 Gestión de combustible → S5 Mantención vehicular; S2 también conecta con S6 Siniestros y accidentes.

## S1: Registro de Vehículos y Conductores

### Registro de Vehículos

1. Adquisición de vehículo → registrar en sistema interno
2. Datos requeridos: patente, modelo, año, tipo de combustible
3. Asignar a división/área → inscribir en Registro Automotor

### Registro de Conductores

1. Funcionario solicita autorización
2. Verificar: licencia vigente, clase apropiada, hoja de vida
3. Autorización de Jefe de Servicios Generales
4. Registrar en nómina de conductores habilitados

## S2: Solicitud y Asignación

1. Funcionario ingresa solicitud: fecha/hora, destino, motivo, pasajeros
2. Jefatura directa autoriza
3. Servicios Generales verifica disponibilidad → ¿Disponible?
   - Sí → asignar vehículo y conductor si aplica → entregar llaves y bitácora
   - No → buscar alternativa o reprogramar

## S3: Bitácora de Viaje

**Al recibir el vehículo:**
1. Registrar en bitácora: fecha/hora salida, km inicial, estado del combustible

**Al regresar:**
2. Registrar: fecha/hora llegada, km final, observaciones
3. Firmar bitácora → devolver llaves a Servicios Generales

## S4: Gestión de Combustible

1. Conductor solicita cupón/tarjeta
2. Servicios Generales autoriza
3. Cargar combustible en estación → registrar: litros, monto, km actual
4. Devolver cupón con factura
5. Consolidar consumos mensuales → analizar rendimiento km/litro

## S5: Mantención Vehicular

### Mantención Preventiva

1. Programar según km/tiempo → alertar próxima mantención
2. Agendar con taller → ejecutar mantención → registrar en historial

### Mantención Correctiva

1. Detectar falla → reportar a Servicios Generales
2. Evaluar: taller interno o taller externo → reparar → certificar OK para uso

### Programa de Mantención

| Tipo | Frecuencia | Acciones |
| :--- | :--- | :--- |
| Básica | 5.000 km | Cambio aceite, filtros |
| Intermedia | 15.000 km | Frenos, neumáticos |
| Mayor | 30.000 km | Revisión completa |
| Documentos | Anual | Revisión técnica, permiso de circulación |

## S6: Siniestros y Accidentes

1. Conductor toma medidas inmediatas → llamar a Carabineros → obtener constancia policial
2. Reportar a Servicios Generales → levantar acta de siniestro
3. ¿Daños a terceros?
   - Sí → activar seguro y procedimiento → seguimiento aseguradora → resolución administrativa → determinar responsabilidades
   - No → evaluar daños propios → cotizar reparación → resolución administrativa → determinar responsabilidades

### Información del Acta de Siniestro

| Dato | Descripción |
| :--- | :--- |
| Fecha y hora | Del accidente |
| Lugar | Dirección exacta |
| Conductor | Funcionario a cargo |
| Descripción | Circunstancias |
| Testigos | Identificación |
| Daños | Propios y a terceros |
| N° Parte | Carabineros |

## Restricciones Normativas (D.L. 799)

| Restricción | Detalle |
| :--- | :--- |
| Fines de semana | Prohibido sin autorización especial |
| Uso particular | Prohibido |
| Fuera de la región | Requiere autorización |
| Horario | Jornada laboral (salvo excepciones) |

Incumplimiento genera responsabilidad administrativa y patrimonial.

## Métricas de Control

| Indicador | Fórmula | Meta |
| :--- | :--- | :--- |
| Rendimiento combustible | Km / Litros | > 10 km/lt |
| % Mantención cumplida | Mantenciones OK / Programadas | > 95% |
| Tasa de accidentabilidad | Accidentes / Vehículos | < 5% |
| Disponibilidad flota | Días operativos / Días totales | > 90% |

## Sistemas Involucrados

| Sistema | Función |
| :--- | :--- |
| SYS-SIGAS | Inventario de vehículos |
| Sistema interno de flota | Bitácoras, mantenciones |

## Referencias Cruzadas

| Dominio | Vínculo |
| :--- | :--- |
| D05 Inventarios y AF | Vehículos como activo fijo |
| D04 Compras | Adquisición vehículos, combustible |
