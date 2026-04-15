---
_manifest:
  urn: urn:gn:kb:manual-flota-servicios-generales
  provenance:
    created_by: FS
    created_at: '2026-03-15'
    source: Manual 3.1 Administración de Flota Vehicular GORE Ñuble + BPMN D06 Flota
      Vehicular
version: 1.0.0
status: published
tags:
- flota-vehicular
- servicios-generales
- gore-nuble
- logistica
- mantencion
lang: es
extensions:
  gn:
    family: guide
  kora:
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:gn:kb:manual-flota-servicios-generales
---

# Gestion de Flota Vehicular y Servicios Generales — GORE Nuble


## Vision General

Manual operativo que integra la administracion de servicios generales de soporte institucional y la gestion integral de la flota vehicular del GORE Nuble. Cubre servicios externalizados, mantencion de infraestructura, registro y asignacion de vehiculos, bitacora de uso, combustible, mantencion vehicular, siniestros, control documental y reporteria.

| Campo | Valor |
| :--- | :--- |
| Criticidad | Media |
| Dueno funcional | Jefe Servicios Generales |
| Proceso principal | 1 (Gestion de Flota Vehicular) |
| Subprocesos | 6 (Registro, Asignacion, Bitacora, Combustible, Mantencion, Siniestros) |

## Mapa de Procesos

```mermaid
flowchart LR
 subgraph CICLO_FLOTA["Gestion de Flota"]
 S1["Registro; vehiculos"]
 S2["Asignacion; y uso"]
 S3["Bitacora; de viaje"]
 S4["Combustible; y kilometraje"]
 S5["Mantencion; vehicular"]
 S6["Siniestros y; accidentes"]
 end

 S1 --> S2 --> S3 --> S4
 S4 --> S5
 S2 --> S6

 style S1 fill:#2196F3,color:#fff
 style S5 fill:#FF9800,color:#fff
 style S6 fill:#f44336,color:#fff
```

## Servicios Generales

Servicios transversales de apoyo a la operacion institucional:

| Servicio | Alcance |
| :--- | :--- |
| Mantencion de Infraestructura | Edificios, instalaciones, sistemas electricos, sanitarios |
| Aseo y Ornato | Limpieza de oficinas, areas comunes, jardines |
| Seguridad Fisica | Vigilancia, control de acceso, circuito cerrado |
| Cafeteria y Alimentacion | Segun aplicabilidad |
| Correo y Mensajeria | Distribucion interna y externa de correspondencia |
| Gestion de Estacionamientos | Asignacion y control de espacios |

### Organizacion del area

| Rol | Funcion |
| :--- | :--- |
| Jefe de Servicios Generales | Coordinacion integral, supervision del area |
| Supervisores por Area | Mantencion, Aseo, Seguridad |
| Personal Operativo | Funcionarios propios o empresas contratadas |
| Coordinacion con DAF | Contrataciones, pagos, control presupuestario |

### Contratos de servicios externalizados

La mayoria de servicios generales se ejecuta mediante contratos externos:

- **Aseo:** contrato de servicio con empresa especializada.
- **Seguridad:** contrato de vigilancia privada.
- **Mantencion de Areas Verdes:** contrato de jardineria.
- **Mantencion de Ascensores/Equipos:** contratos especializados.

**Administracion de contratos:**

1. Designacion de Administrador del Contrato.
2. Verificacion de cumplimiento de dotaciones y horarios.
3. Libro de novedades para registro de incidencias.
4. Evaluacion periodica del servicio.
5. Aplicacion de multas segun bases contractuales.

## Mantencion de Infraestructura

### Tipos de mantencion

| Tipo | Definicion |
| :--- | :--- |
| Preventiva | Programada para evitar fallas (revisiones periodicas) |
| Correctiva | Reparacion de fallas o danos detectados |
| Emergencia | Atencion inmediata ante situaciones criticas (filtraciones, cortes electricos) |

### Plan de mantencion preventiva

- **Frecuencia de elaboracion:** anual.
- **Base:** inventario de instalaciones y equipos.

Contenido del plan:

- Listado de equipos e instalaciones a mantener.
- Frecuencia de intervencion (mensual, trimestral, anual).
- Responsable de ejecucion (interno o contratista).
- Presupuesto estimado.

Seguimiento mediante calendario de actividades con alertas automaticas.

### Ordenes de trabajo

Instrumento formal para solicitar y documentar intervenciones de infraestructura.

**Generacion:**
- Por usuario (falla reportada).
- Automatica (plan preventivo).

**Contenido:**
- Descripcion del requerimiento.
- Ubicacion y equipo afectado.
- Prioridad (alta, media, baja).
- Fecha de solicitud.

**Asignacion:** a tecnico interno o derivacion a contratista.

**Ejecucion:** registro de trabajos realizados, materiales usados, horas.

**Cierre:** validacion por solicitante + actualizacion de hoja de vida del equipo.

### Control de elementos de seguridad

- Extintores: carga, vencimiento, ubicacion, senaletica.
- Red humeda y seca: pruebas periodicas.
- Iluminacion de emergencia.
- Senaletica de evacuacion.
- Detectores de humo y alarmas.

## Registro de Vehiculos y Conductores

### Restricciones legales de adquisicion

La adquisicion de vehiculos motorizados, a cualquier titulo, requiere autorizacion previa de la Direccion de Presupuestos (DIPRES) cuando su precio supere el monto fijado por dicha direccion (Art. 12 Ley de Presupuestos). Esta restriccion aplica tambien a vehiculos adquiridos via proyectos de inversion.

### Registro de vehiculos

Cada vehiculo institucional debe tener ficha completa:

**Datos de identificacion:**
- Patente.
- Marca, modelo, ano.
- Numero de chasis y motor.
- Color.
- Tipo (sedan, camioneta, minibus, etc.).

**Datos administrativos:**
- Codigo de activo fijo (vinculacion con Manual Activo Fijo).
- Fecha de adquisicion y valor.
- Responsable asignado.
- Centro de costo.

**Documentacion vigente:**
- Permiso de circulacion.
- Revision tecnica.
- Seguro obligatorio (SOAP).
- Seguro automotriz voluntario.

**Equipamiento:**
- Accesorios instalados (GPS, radio, botiquin, extintor).
- Kit de emergencia.

### Registro de conductores

Nomina de funcionarios autorizados para conducir vehiculos institucionales.

**Requisitos:**
- Licencia de conducir vigente (clase apropiada).
- Hoja de vida sin infracciones graves.
- Autorizacion formal (resolucion o memorando).

Control de vencimiento de licencias con alertas.

### Flujo de registro

```mermaid
flowchart TD
 subgraph VEHICULOS["Registro de Vehiculos"]
 A["Adquisicion de; vehiculo"]
 B["Registrar en; sistema interno"]
 C["Datos:; Patente; Modelo; Ano; Tipo combustible"]
 D["Asignar a; division/area"]
 E["Inscribir en; Registro Automotor"]
 end

 subgraph CONDUCTORES["Registro de Conductores"]
 F["Funcionario solicita; autorizacion"]
 G["Verificar:; Licencia vigente; Clase apropiada; Hoja de vida"]
 H["Autorizacion de; Jefe Servicios"]
 I["Registrar en; nomina conductores"]
 end

 A --> B --> C --> D --> E
 F --> G --> H --> I

 style E fill:#2196F3,color:#fff
 style I fill:#4CAF50,color:#fff
```

## Solicitud y Asignacion de Vehiculos

### Procedimiento

1. **Solicitud:** funcionario requiere vehiculo indicando fecha, hora, destino, proposito.
2. **Aprobacion:** jefatura del solicitante autoriza.
3. **Asignacion:** Encargado de Flota verifica disponibilidad y asigna vehiculo + conductor.
4. **Confirmacion:** notificacion al solicitante y conductor.

### Criterios de prioridad

1. Comisiones de servicio oficiales.
2. Actividades del Gobernador y autoridades.
3. Emergencias institucionales.
4. Traslados programados.

> **D.L. 799 — Restriccion de uso:** los vehiculos estatales no pueden circular en dias sabados, domingos ni festivos, salvo autorizacion expresa y fundada por razones de servicio impostergables.

### Flujo de solicitud y asignacion

```mermaid
flowchart TD
 A["Funcionario solicita; vehiculo"] --> B["Ingresar solicitud:; Fecha/hora; Destino; Motivo; Pasajeros"]
 B --> C["Jefatura directa; autoriza"]
 C --> D["Servicios Generales; verifica disponibilidad"]
 D --> E{"Disponible?"}
 E -->|"Si"| F["Asignar vehiculo; y conductor si aplica"]
 E -->|"No"| G["Buscar alternativa; o reprogramar"]
 F --> H["Entregar llaves; y bitacora"]

 style H fill:#4CAF50,color:#fff
```

## Bitacora de Viaje

Registro obligatorio de cada salida.

**Campos:**
- Fecha y hora de salida/retorno.
- Conductor.
- Destino y proposito.
- Kilometraje inicial y final.
- Observaciones (estado del vehiculo, incidentes).

**Modalidad:**
- Digital: registro en sistema o aplicacion movil.
- Fisica: cuaderno en el vehiculo (respaldo).

### Flujo de bitacora

```mermaid
flowchart TD
 A["Recibir vehiculo"] --> B["Registrar en bitacora:; Fecha/hora salida; Km inicial; Estado combustible"]
 B --> C["Realizar viaje"]
 C --> D["Al regresar registrar:; Fecha/hora llegada; Km final; Observaciones"]
 D --> E["Firmar bitacora"]
 E --> F["Devolver llaves; a Servicios Generales"]

 style E fill:#FF9800,color:#fff
```

## Gestion de Combustible y Kilometraje

### Control de combustible

**Tarjeta de combustible:** asignada a cada vehiculo (ej. ServiEstado, Copec).

**Registro de cargas:**
- Fecha y estacion de servicio.
- Litros cargados.
- Monto.
- Kilometraje al momento de carga.

**Analisis de rendimiento:**
- Km/litro por vehiculo.
- Comparacion con estandar del fabricante.
- Alertas por consumos anomalos.

### Control de kilometraje

- Registro mensual del odometro de cada vehiculo.
- Proyeccion de mantenciones segun kilometraje.
- Deteccion de usos no autorizados.

### Flujo de combustible

```mermaid
flowchart TD
 A["Vehiculo requiere; combustible"] --> B["Conductor solicita; cupon/tarjeta"]
 B --> C["Servicios Generales; autoriza"]
 C --> D["Cargar combustible; en estacion"]
 D --> E["Registrar:; Litros; Monto; Km actual"]
 E --> F["Devolver cupon; con factura"]
 F --> G["Consolidar consumos; mensuales"]
 G --> H["Analizar rendimiento; km/litro"]

 style H fill:#9C27B0,color:#fff
```
