# Modelo OPM — HODOM HSC
# Arquitectura de Procesos

Versión: 0.2
Fecha: 2026-04-09
Estado: refinamiento formal focalizado

Alcance de esta versión: formalizar tres macroprocesos críticos del backbone HODOM HSC:
- *Admitir Episodio*
- *Programar Visitas y Rutas*
- *Regular Atención a Distancia*

Esta versión no cierra aún el modelo completo. Busca aumentar corrección estructural y utilidad de ingeniería sobre los puntos donde HSC parece diferenciarse más de un modelo normativo genérico.

## Convención de evidencia

- [N] Normativa HODOM
- [S] Sistema/repositorio HSC (`hdos-app`, `hdos`)
- [M] Modelo OPM previo
- [H] Hipótesis pendiente de validación local

## Fuentes usadas

### Normativa
- [N] `01-reglamento-hodom-ds1-2022.md`
- [N] `02-decreto-exento-31-2024-aprueba-norma-tecnica.md`
- [N] `03-norma-tecnica-hodom-2024.md`

### Sistema y diseño HSC
- [S] `hdos-app/README.md`
- [S] `hdos-app/docs/specs/00-INDICE.md`
- [S] `hdos-app/docs/specs/01-diseno-sistema-operativo-hodom-hsc.md`
- [S] `hdos-app/docs/specs/13-portal-paciente-mvp.md`
- [S] `hdos/README.md`

### Modelos previos
- [M] `opm-hodom-normativo-v1.0.md`
- [M] `opm-hodom-model-v2.5.md`
- [M] `opm-hodom-hsc-procesos-v0.1.md`

---

## 1. Decisión de arquitectura de esta versión

Se mantiene el backbone de `v0.1`, pero se formaliza en profundidad solo donde hoy hay mayor densidad operativa y mayor valor modelador:

1. **Admisión episódica**
2. **Programación territorial-operativa**
3. **Regulación clínica remota**

Razón:
- [S] son módulos explícitos o inferidos directamente del sistema HSC (`admision`, `agenda`, `llamadas`)
- [N] están fuertemente anclados en la norma
- [M] son puntos donde un modelo normativo estándar suele quedarse corto

---

# 2. SD1.2 — *Admitir Episodio*

## 2.1 Criterio de modelado

Se modela el ingreso no solo como formalización de paciente, sino como creación y activación de un **episodio clínico-operativo**. [S][M]

Esto es más correcto para HSC porque:
- [S] la app trabaja con `stayId` y ficha longitudinal por estadía
- [S] el diseño del sistema explicita que la unidad del dominio es el episodio
- [N] el ingreso genera formulario, consentimiento, ficha, diagnóstico social y trazabilidad derivadora

## 2.2 Tabla de elementos

| Tipo | Nombre | Esencia | Afiliación | Estados | Evidencia |
|------|--------|---------|------------|---------|-----------|
| Proceso | *Admitir Episodio* | Informatical | Sistémico | — | [S][M] |
| Proceso | *Registrar Ingreso* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Abrir Ficha Clínica* | Informatical | Sistémico | — | [N][S][H] |
| Proceso | *Registrar Origen de Derivación* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Elaborar Diagnóstico Social* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Entregar Documentación Inicial* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Coordinar con Derivador* | Informatical | Sistémico | — | [N][S][M] |
| Objeto | **Episodio de Hospitalización Domiciliaria** | Informatical | Sistémico | `registrado`, `activo`, `cerrado` | [S][H] |
| Objeto | **Ficha Clínica** | Informatical | Sistémico | `abierta`, `cerrada` | [N][S][M] |
| Objeto | **Formulario de Ingreso** | Informatical | Sistémico | — | [N][M] |
| Objeto | **Origen de Derivación** | Informatical | Sistémico | `hospitalización`, `urgencia`, `atención primaria`, `ambulatorio`, `ley de urgencia`, `gestión de camas` | [N][M] |
| Objeto | **Diagnóstico Social** | Informatical | Sistémico | — | [N][M] |
| Objeto | **Consentimiento Informado** | Informatical | Sistémico | `sin firmar`, `firmado` | [N][M] |
| Objeto | **Carta de Derechos y Deberes** | Informatical | Sistémico | `pendiente de entrega`, `entregada` | [N][M] |
| Objeto | **Documento Inicial de Cuidados** | Informatical | Sistémico | — | [N][H] |
| Objeto | **Registro de Coordinación con Derivador** | Informatical | Sistémico | — | [M] |
| Objeto | **Establecimiento Derivador** | Físico | Ambiental | — | [N][M] |
| Objeto | **Sistema de Comunicación** | Físico | Sistémico | — | [N][S][M] |
| Objeto | **Personal Administrativo** | Físico | Sistémico | — | [N][M] |
| Objeto | **Trabajador Social** | Físico | Sistémico | — | [N][M] |
| Objeto | **Enfermero Clínico** | Físico | Sistémico | — | [N][M] |
| Objeto | **Profesional Coordinador** | Físico | Sistémico | — | [N][M] |

## 2.3 Tabla de enlaces

| Tipo | Origen | Destino | Plantilla | Evidencia |
|------|--------|---------|-----------|-----------|
| In-zooming | *Admitir Episodio* | 6 subprocesos | RF6 | [M] |
| Result | *Registrar Ingreso* | **Formulario de Ingreso** | T2 | [N][M] |
| Result (state-specified) | *Registrar Ingreso* | **Episodio de Hospitalización Domiciliaria** en `registrado` | TS2 | [S][H] |
| Agent | **Personal Administrativo** | *Registrar Ingreso* | H1 | [M][N] |
| Result (state-specified) | *Abrir Ficha Clínica* | **Ficha Clínica** en `abierta` | TS2 | [N][S][H] |
| Effect (input-output) | *Abrir Ficha Clínica* | **Episodio de Hospitalización Domiciliaria** | TS3 | [S][H] |
| Result | *Registrar Origen de Derivación* | **Origen de Derivación** | T2 | [N][M] |
| Result | *Elaborar Diagnóstico Social* | **Diagnóstico Social** | T2 | [N][M] |
| Agent | **Trabajador Social** | *Elaborar Diagnóstico Social* | H1 | [N][M] |
| Effect (input-output) | *Entregar Documentación Inicial* | **Carta de Derechos y Deberes** | TS3 | [N][M] |
| Instrument (state-specified) | *Entregar Documentación Inicial* | **Consentimiento Informado** en `firmado` | HS2 | [N][M] |
| Result | *Entregar Documentación Inicial* | **Documento Inicial de Cuidados** | T2 | [N][H] |
| Agent | **Enfermero Clínico** | *Entregar Documentación Inicial* | H1 | [N][M] |
| Instrument | *Coordinar con Derivador* | **Establecimiento Derivador** | H2 | [N][M] |
| Instrument | *Coordinar con Derivador* | **Sistema de Comunicación** | H2 | [N][S][M] |
| Result | *Coordinar con Derivador* | **Registro de Coordinación con Derivador** | T2 | [M] |
| Agent | **Profesional Coordinador** | *Coordinar con Derivador* | H1 | [N][M] |

## 2.4 OPL-ES

```opl
SD1 se refina por descomposición de *Admitir Episodio* en SD1.2.
*Admitir Episodio* se descompone en *Registrar Ingreso*, *Abrir Ficha Clínica*, *Registrar Origen de Derivación*, *Elaborar Diagnóstico Social*, *Entregar Documentación Inicial* y *Coordinar con Derivador*, en esa secuencia.

**Episodio de Hospitalización Domiciliaria** puede estar `registrado`, `activo` o `cerrado`.
Estado `registrado` de **Episodio de Hospitalización Domiciliaria** es inicial.

*Registrar Ingreso* genera **Formulario de Ingreso**.
*Registrar Ingreso* genera **Episodio de Hospitalización Domiciliaria** en `registrado`.
**Personal Administrativo** maneja *Registrar Ingreso*.

**Ficha Clínica** puede estar `abierta` o `cerrada`.
Estado `abierta` de **Ficha Clínica** es inicial.
Estado `cerrada` de **Ficha Clínica** es final.
*Abrir Ficha Clínica* genera **Ficha Clínica** en `abierta`.
*Abrir Ficha Clínica* cambia **Episodio de Hospitalización Domiciliaria** de `registrado` a `activo`.

**Origen de Derivación** puede estar `hospitalización`, `urgencia`, `atención primaria`, `ambulatorio`, `ley de urgencia` o `gestión de camas`.
*Registrar Origen de Derivación* genera **Origen de Derivación**.

*Elaborar Diagnóstico Social* genera **Diagnóstico Social**.
**Trabajador Social** maneja *Elaborar Diagnóstico Social*.

**Carta de Derechos y Deberes** puede estar `pendiente de entrega` o `entregada`.
Estado `pendiente de entrega` de **Carta de Derechos y Deberes** es inicial.
Estado `entregada` de **Carta de Derechos y Deberes** es final.
*Entregar Documentación Inicial* cambia **Carta de Derechos y Deberes** de `pendiente de entrega` a `entregada`.
*Entregar Documentación Inicial* requiere **Consentimiento Informado** en `firmado`.
*Entregar Documentación Inicial* genera **Documento Inicial de Cuidados**.
**Enfermero Clínico** maneja *Entregar Documentación Inicial*.

*Coordinar con Derivador* requiere **Establecimiento Derivador**.
*Coordinar con Derivador* requiere **Sistema de Comunicación**.
*Coordinar con Derivador* genera **Registro de Coordinación con Derivador**.
**Profesional Coordinador** maneja *Coordinar con Derivador*.
```

## 2.5 Insight de modelado

La admisión HSC no es un mero trámite documental. Es la transición donde un caso elegible se convierte en episodio activo, trazable y coordinado. [S][M]

---

# 3. SD1.4 — *Programar Visitas y Rutas*

## 3.1 Criterio de modelado

Se modela como proceso propio, separado de planificación clínica. [S][N][M]

Justificación:
- [S] existe módulo `agenda/`
- [N] la NT exige protocolo de programación de rutas y visitas
- [M] la logística no debe quedar absorbida por el plan terapéutico porque tiene semántica operacional distinta

## 3.2 Tabla de elementos

| Tipo | Nombre | Esencia | Afiliación | Estados | Evidencia |
|------|--------|---------|------------|---------|-----------|
| Proceso | *Programar Visitas y Rutas* | Informatical | Sistémico | — | [S][N][M] |
| Proceso | *Construir Agenda Clínica* | Informatical | Sistémico | — | [S][H] |
| Proceso | *Asignar Profesional* | Informatical | Sistémico | — | [S][M] |
| Proceso | *Asignar Móvil* | Informatical | Sistémico | — | [S][H] |
| Proceso | *Secuenciar Ruta* | Informatical | Sistémico | — | [S][M] |
| Proceso | *Reprogramar Contingencia* | Informatical | Sistémico | — | [S][H] |
| Objeto | **Agenda Clínica** | Informatical | Sistémico | `borrador`, `activa`, `reprogramada` | [S][H] |
| Objeto | **Visita Domiciliaria** | Informatical | Sistémico | `pendiente`, `asignada`, `realizada`, `fallida`, `cancelada` | [S][H] |
| Objeto | **Ruta Diaria** | Informatical | Sistémico | `borrador`, `asignada`, `ejecutada`, `reprogramada` | [S][M] |
| Objeto | **Profesional de Salud** | Físico | Sistémico | — | [N][S][H] |
| Objeto | **Vehículo de Transporte** | Físico | Sistémico | `disponible`, `asignado`, `fuera de servicio` | [N][S][M] |
| Objeto | **Contingencia Operacional** | Informatical | Sistémico | `ausente`, `presente` | [S][H] |
| Objeto | **Plan de Atención** | Informatical | Sistémico | `activo` | [N][S][H] |
| Objeto | **Profesional Coordinador** | Físico | Sistémico | — | [N][M] |
| Objeto | **Conductor** | Físico | Sistémico | — | [S][H] |

## 3.3 Tabla de enlaces

| Tipo | Origen | Destino | Plantilla | Evidencia |
|------|--------|---------|-----------|-----------|
| In-zooming | *Programar Visitas y Rutas* | 5 subprocesos | RF6 | [M] |
| Instrument (state-specified) | *Construir Agenda Clínica* | **Plan de Atención** en `activo` | HS2 | [N][S][H] |
| Result | *Construir Agenda Clínica* | **Agenda Clínica** | T2 | [S][H] |
| Result | *Construir Agenda Clínica* | **Visita Domiciliaria** | T2 | [S][H] |
| Agent | **Profesional Coordinador** | *Construir Agenda Clínica* | H1 | [N][M] |
| Effect (input-output) | *Asignar Profesional* | **Visita Domiciliaria** | TS3 | [S][H] |
| Instrument | *Asignar Profesional* | **Profesional de Salud** | H2 | [S][H] |
| Agent | **Profesional Coordinador** | *Asignar Profesional* | H1 | [N][M] |
| Effect (input-output) | *Asignar Móvil* | **Vehículo de Transporte** | TS3 | [S][H] |
| Instrument | *Asignar Móvil* | **Ruta Diaria** | H2 | [S][M] |
| Agent | **Profesional Coordinador** | *Asignar Móvil* | H1 | [S][M] |
| Effect (input-output) | *Secuenciar Ruta* | **Ruta Diaria** | TS3 | [S][M] |
| Result | *Secuenciar Ruta* | **Ruta Diaria** en `asignada` | TS2 | [S][M] |
| Agent | **Conductor** | *Secuenciar Ruta* | H1 | [S][H] |
| Condition | **Contingencia Operacional** en `presente` | *Reprogramar Contingencia* | HC2 | [S][H] |
| Effect (input-output) | *Reprogramar Contingencia* | **Agenda Clínica** | TS3 | [S][H] |
| Effect (input-output) | *Reprogramar Contingencia* | **Ruta Diaria** | TS3 | [S][H] |
| Agent | **Profesional Coordinador** | *Reprogramar Contingencia* | H1 | [N][S][M] |

## 3.4 OPL-ES

```opl
SD1 se refina por descomposición de *Programar Visitas y Rutas* en SD1.4.
*Programar Visitas y Rutas* se descompone en *Construir Agenda Clínica*, *Asignar Profesional*, *Asignar Móvil*, *Secuenciar Ruta* y *Reprogramar Contingencia*, en esa secuencia operativa.

**Agenda Clínica** puede estar `borrador`, `activa` o `reprogramada`.
Estado `borrador` de **Agenda Clínica** es inicial.

**Visita Domiciliaria** puede estar `pendiente`, `asignada`, `realizada`, `fallida` o `cancelada`.
Estado `pendiente` de **Visita Domiciliaria** es inicial.

*Construir Agenda Clínica* requiere **Plan de Atención** en `activo`.
*Construir Agenda Clínica* genera **Agenda Clínica**.
*Construir Agenda Clínica* genera **Visita Domiciliaria**.
**Profesional Coordinador** maneja *Construir Agenda Clínica*.

**Profesional de Salud** es físico.
*Asignar Profesional* requiere **Profesional de Salud**.
*Asignar Profesional* cambia **Visita Domiciliaria** de `pendiente` a `asignada`.
**Profesional Coordinador** maneja *Asignar Profesional*.

**Vehículo de Transporte** puede estar `disponible`, `asignado` o `fuera de servicio`.
Estado `disponible` de **Vehículo de Transporte** es inicial.
*Asignar Móvil* requiere **Ruta Diaria**.
*Asignar Móvil* cambia **Vehículo de Transporte** de `disponible` a `asignado`.
**Profesional Coordinador** maneja *Asignar Móvil*.

**Ruta Diaria** puede estar `borrador`, `asignada`, `ejecutada` o `reprogramada`.
Estado `borrador` de **Ruta Diaria** es inicial.
*Secuenciar Ruta* cambia **Ruta Diaria** de `borrador` a `asignada`.
**Conductor** maneja *Secuenciar Ruta*.

**Contingencia Operacional** puede estar `ausente` o `presente`.
Estado `ausente` de **Contingencia Operacional** es inicial.
*Reprogramar Contingencia* ocurre si **Contingencia Operacional** está en `presente`, de lo contrario *Reprogramar Contingencia* se omite.
*Reprogramar Contingencia* cambia **Agenda Clínica** de `activa` a `reprogramada`.
*Reprogramar Contingencia* cambia **Ruta Diaria** de `asignada` a `reprogramada`.
**Profesional Coordinador** maneja *Reprogramar Contingencia*.
```

## 3.5 Insight de modelado

La programación territorial es el puente entre la intención clínica y la capacidad real de ejecución. Sin este proceso, HODOM queda modelado como clínica abstracta sin territorio. [S][M]

---

# 4. SD1.6 — *Regular Atención a Distancia*

## 4.1 Criterio de modelado

Se modela como macroproceso distinto de atención presencial y distinto de simple comunicación. [N][S][M]

Justificación:
- [N] el médico regulador puede atender a distancia con alcance clínico equivalente
- [N] la unidad debe tener sistema telefónico/radial 24/7 con trazabilidad
- [S] la app tiene módulo `llamadas/`
- [M] la regulación remota tiene lógica clínica propia: recepción, juicio, resolución, escalamiento y registro

## 4.2 Tabla de elementos

| Tipo | Nombre | Esencia | Afiliación | Estados | Evidencia |
|------|--------|---------|------------|---------|-----------|
| Proceso | *Regular Atención a Distancia* | Informatical | Sistémico | — | [N][S][M] |
| Proceso | *Recibir Llamado Clínico* | Informatical | Sistémico | — | [N][S][H] |
| Proceso | *Evaluar Motivo de Consulta* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Entregar Indicación Remota* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Escalar a Visita Presencial* | Informatical | Sistémico | — | [S][H] |
| Proceso | *Activar Derivación Urgente* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Registrar Regulación* | Informatical | Sistémico | — | [N][S][M] |
| Objeto | **Llamado Clínico** | Informatical | Sistémico | `recibido`, `triageado`, `cerrado` | [N][S][H] |
| Objeto | **Motivo de Consulta** | Informatical | Sistémico | `administrativo`, `clínico`, `urgente` | [S][H] |
| Objeto | **Indicación Remota** | Informatical | Sistémico | — | [N][M] |
| Objeto | **Decisión de Escalamiento** | Informatical | Sistémico | `resolver remoto`, `visita presencial`, `derivación urgente` | [M][H] |
| Objeto | **Registro de Regulación** | Informatical | Sistémico | — | [N][S][M] |
| Objeto | **Sistema Telefónico** | Físico | Sistémico | — | [N][M] |
| Objeto | **Médico Regulador** | Físico | Sistémico | — | [N][M] |
| Objeto | **Enfermero Clínico** | Físico | Sistémico | — | [N][M] |
| Objeto | **Paciente/Cuidador** | Físico | Ambiental | — | [N][S][H] |
| Objeto | **Visita Domiciliaria** | Informatical | Sistémico | `pendiente`, `asignada`, `realizada`, `urgente` | [S][H] |
| Objeto | **Derivación Urgente** | Informatical | Sistémico | `activada` | [N][M] |

## 4.3 Tabla de enlaces

| Tipo | Origen | Destino | Plantilla | Evidencia |
|------|--------|---------|-----------|-----------|
| In-zooming | *Regular Atención a Distancia* | 6 subprocesos | RF6 | [M] |
| Instrument | *Recibir Llamado Clínico* | **Sistema Telefónico** | H2 | [N][M] |
| Instrument | *Recibir Llamado Clínico* | **Paciente/Cuidador** | H2 | [N][S][H] |
| Result (state-specified) | *Recibir Llamado Clínico* | **Llamado Clínico** en `recibido` | TS2 | [N][S][H] |
| Effect (input-output) | *Evaluar Motivo de Consulta* | **Motivo de Consulta** | TS3 | [S][H] |
| Agent | **Médico Regulador** | *Evaluar Motivo de Consulta* | H1 | [N][M] |
| Agent | **Enfermero Clínico** | *Evaluar Motivo de Consulta* | H1 | [N][H] |
| Result | *Entregar Indicación Remota* | **Indicación Remota** | T2 | [N][M] |
| Result (state-specified) | *Entregar Indicación Remota* | **Decisión de Escalamiento** en `resolver remoto` | TS2 | [M][H] |
| Agent | **Médico Regulador** | *Entregar Indicación Remota* | H1 | [N][M] |
| Result (state-specified) | *Escalar a Visita Presencial* | **Visita Domiciliaria** en `urgente` | TS2 | [S][H] |
| Result (state-specified) | *Escalar a Visita Presencial* | **Decisión de Escalamiento** en `visita presencial` | TS2 | [M][H] |
| Agent | **Enfermero Clínico** | *Escalar a Visita Presencial* | H1 | [S][H] |
| Result (state-specified) | *Activar Derivación Urgente* | **Derivación Urgente** en `activada` | TS2 | [N][M] |
| Result (state-specified) | *Activar Derivación Urgente* | **Decisión de Escalamiento** en `derivación urgente` | TS2 | [M][H] |
| Agent | **Médico Regulador** | *Activar Derivación Urgente* | H1 | [N][M] |
| Result | *Registrar Regulación* | **Registro de Regulación** | T2 | [N][S][M] |
| Agent | **Médico Regulador** | *Registrar Regulación* | H1 | [N][M] |

## 4.4 OPL-ES

```opl
SD1 se refina por descomposición de *Regular Atención a Distancia* en SD1.6.
*Regular Atención a Distancia* se descompone en *Recibir Llamado Clínico*, *Evaluar Motivo de Consulta*, *Entregar Indicación Remota*, *Escalar a Visita Presencial*, *Activar Derivación Urgente* y *Registrar Regulación*, en esa secuencia.

**Llamado Clínico** puede estar `recibido`, `triageado` o `cerrado`.
Estado `recibido` de **Llamado Clínico** es inicial.

*Recibir Llamado Clínico* requiere **Sistema Telefónico**.
*Recibir Llamado Clínico* requiere **Paciente/Cuidador**.
*Recibir Llamado Clínico* genera **Llamado Clínico** en `recibido`.

**Motivo de Consulta** puede estar `administrativo`, `clínico` o `urgente`.
*Evaluar Motivo de Consulta* cambia **Motivo de Consulta** de `clínico` a `urgente`.
**Médico Regulador** maneja *Evaluar Motivo de Consulta*.
**Enfermero Clínico** maneja *Evaluar Motivo de Consulta*.

**Decisión de Escalamiento** puede estar `resolver remoto`, `visita presencial` o `derivación urgente`.
*Entregar Indicación Remota* genera **Indicación Remota**.
*Entregar Indicación Remota* genera **Decisión de Escalamiento** en `resolver remoto`.
**Médico Regulador** maneja *Entregar Indicación Remota*.

*Escalar a Visita Presencial* genera **Visita Domiciliaria** en `urgente`.
*Escalar a Visita Presencial* genera **Decisión de Escalamiento** en `visita presencial`.
**Enfermero Clínico** maneja *Escalar a Visita Presencial*.

*Activar Derivación Urgente* genera **Derivación Urgente** en `activada`.
*Activar Derivación Urgente* genera **Decisión de Escalamiento** en `derivación urgente`.
**Médico Regulador** maneja *Activar Derivación Urgente*.

*Registrar Regulación* genera **Registro de Regulación**.
**Médico Regulador** maneja *Registrar Regulación*.
```

## 4.5 Insight de modelado

La regulación a distancia no es solo una llamada. Es un mini-sistema clínico de triage, juicio, resolución y escalamiento. Si se la modela como simple comunicación, se pierde su peso asistencial real. [N][S][M]

---

# 5. Síntesis transversal de esta v0.2

## 5.1 Qué mejoró respecto a v0.1

- se pasó de backbone discursivo a tres submodelos más formales
- aparecen objetos operativos explícitos
- aparecen estados operativos relevantes
- aparecen agents, instruments, results y effects
- la unidad episodio empieza a quedar modelada de manera seria

## 5.2 Qué sigue flojo aún

- faltan tablas de enlaces y elementos para el resto del backbone
- aún hay hipótesis no validadas con BD y pantallas reales
- hay que limpiar mejor qué va en SD1 y qué sube a gobernanza/observabilidad
- el proceso de monitoreo aún no está formalizado al mismo nivel

## 5.3 Tensión central que emerge

HODOM HSC no se deja reducir a “atención clínica en casa”.

Lo que el sistema realmente hace es esto:
- convierte un caso derivado en un episodio gestionado,
- transforma planes en territorialidad ejecutable,
- y absorbe incertidumbre clínica a través de regulación remota y escalamiento.

Eso es mucho más interesante y mucho más exigente que una ficha con visitas.

---

# 6. Siguiente paso recomendado

Avanzar a `v0.3` formalizando estos tres bloques:

1. *Monitorear Evolución Clínica*
2. *Egresar Episodio*
3. *Tributar Producción y REM*

Razón:
- cerrarían el arco completo episodio → control → salida → observabilidad
- permitirían separar definitivamente capa asistencial de capa de reporte
- ahí se juega buena parte de la calidad, trazabilidad y capacidad de gestión directiva
