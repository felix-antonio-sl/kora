# Modelo OPM — HODOM HSC
# Arquitectura de Procesos

Versión: 0.3
Fecha: 2026-04-09
Estado: refinamiento formal ampliado

Alcance de esta versión: formalizar tres bloques adicionales del backbone HODOM HSC para cerrar el arco operativo episodio → monitoreo → salida → observabilidad:
- *Monitorear Evolución Clínica*
- *Egresar Episodio*
- *Tributar Producción y REM*

Esta versión se apoya sobre `v0.2` y asume su backbone vigente.

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
- [M] `opm-hodom-hsc-procesos-v0.2.md`

---

# 1. Decisión de arquitectura de esta versión

La v0.3 formaliza los tres macroprocesos que terminan de revelar el carácter directivo y operacional de HODOM HSC:

1. el sistema no solo atiende, sino que **monitorea**
2. no solo monitorea, sino que **cierra episodios por causal**
3. no solo cierra episodios, sino que **se hace visible estadísticamente y rinde cuenta**

Este paso era necesario porque, sin estos tres bloques, el modelo quedaba demasiado centrado en admisión, agenda y llamadas, y aún no mostraba cómo la unidad se gobierna a sí misma a través de la producción de información clínica y estadística. [S][M]

---

# 2. SD1.7 — *Monitorear Evolución Clínica*

## 2.1 Criterio de modelado

Se modela como proceso separado de la ejecución terapéutica. [N][M]

Justificación:
- [N] la normativa exige control clínico, monitoreo de signos vitales y continuidad segura
- [M] en los modelos previos, el monitoreo ya aparecía como loop específico
- [S] el sistema HSC tiene ficha longitudinal, tablero de censo y alertas, lo que sugiere una capa explícita de evaluación continua

## 2.2 Tabla de elementos

| Tipo | Nombre | Esencia | Afiliación | Estados | Evidencia |
|------|--------|---------|------------|---------|-----------|
| Proceso | *Monitorear Evolución Clínica* | Informatical | Sistémico | — | [N][M][S] |
| Proceso | *Evaluar Signos Vitales* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Actualizar Resumen Clínico Domiciliario* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Categorizar Riesgo* | Informatical | Sistémico | — | [S][H] |
| Proceso | *Evaluar Respuesta Terapéutica* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Decidir Continuidad o Egreso* | Informatical | Sistémico | — | [M][H] |
| Objeto | **Signos Vitales** | Informatical | Sistémico | `en rango`, `alterados`, `críticos` | [N][H] |
| Objeto | **Resumen Clínico Domiciliario** | Informatical | Sistémico | `actualizado` | [N][M] |
| Objeto | **Categoría de Riesgo** | Informatical | Sistémico | `estable`, `en observación`, `inestable` | [S][H] |
| Objeto | **Respuesta Terapéutica** | Informatical | Sistémico | `favorable`, `insuficiente`, `desfavorable` | [M][H] |
| Objeto | **Decisión de Continuidad** | Informatical | Sistémico | `continuar tratamiento`, `ajustar plan`, `proceder egreso`, `escalar` | [M][H] |
| Objeto | **Condición Clínica** | Informatical | Sistémico | `agudo-reagudizado`, `recuperado` | [N][M] |
| Objeto | **Equipo de Salud** | Físico | Sistémico | — | [N][M] |
| Objeto | **Equipamiento Médico** | Físico | Sistémico | — | [N][M] |
| Objeto | **Ficha Clínica** | Informatical | Sistémico | `abierta`, `cerrada` | [N][S][M] |

## 2.3 Tabla de enlaces

| Tipo | Origen | Destino | Plantilla | Evidencia |
|------|--------|---------|-----------|-----------|
| In-zooming | *Monitorear Evolución Clínica* | 5 subprocesos | RF6 | [M] |
| Instrument | *Evaluar Signos Vitales* | **Equipamiento Médico** | H2 | [N][M] |
| Result | *Evaluar Signos Vitales* | **Signos Vitales** | T2 | [N][H] |
| Agent | **Equipo de Salud** | *Evaluar Signos Vitales* | H1 | [N][M] |
| Result | *Actualizar Resumen Clínico Domiciliario* | **Resumen Clínico Domiciliario** | T2 | [N][M] |
| Instrument | *Actualizar Resumen Clínico Domiciliario* | **Ficha Clínica** | H2 | [N][S][M] |
| Agent | **Equipo de Salud** | *Actualizar Resumen Clínico Domiciliario* | H1 | [N][M] |
| Effect (input-output) | *Categorizar Riesgo* | **Categoría de Riesgo** | TS3 | [S][H] |
| Instrument | *Categorizar Riesgo* | **Signos Vitales** | H2 | [N][H] |
| Agent | **Equipo de Salud** | *Categorizar Riesgo* | H1 | [S][H] |
| Effect (input-output) | *Evaluar Respuesta Terapéutica* | **Respuesta Terapéutica** | TS3 | [M][H] |
| Instrument | *Evaluar Respuesta Terapéutica* | **Condición Clínica** | H2 | [N][M] |
| Instrument | *Evaluar Respuesta Terapéutica* | **Resumen Clínico Domiciliario** | H2 | [N][M] |
| Agent | **Equipo de Salud** | *Evaluar Respuesta Terapéutica* | H1 | [N][M] |
| Effect (input-output) | *Decidir Continuidad o Egreso* | **Decisión de Continuidad** | TS3 | [M][H] |
| Instrument | *Decidir Continuidad o Egreso* | **Categoría de Riesgo** | H2 | [S][H] |
| Instrument | *Decidir Continuidad o Egreso* | **Respuesta Terapéutica** | H2 | [M][H] |
| Agent | **Equipo de Salud** | *Decidir Continuidad o Egreso* | H1 | [M][H] |

## 2.4 OPL-ES

```opl
SD1 se refina por descomposición de *Monitorear Evolución Clínica* en SD1.7.
*Monitorear Evolución Clínica* se descompone en *Evaluar Signos Vitales*, *Actualizar Resumen Clínico Domiciliario*, *Categorizar Riesgo*, *Evaluar Respuesta Terapéutica* y *Decidir Continuidad o Egreso*, en esa secuencia.

**Signos Vitales** puede estar `en rango`, `alterados` o `críticos`.
*Evaluar Signos Vitales* requiere **Equipamiento Médico**.
*Evaluar Signos Vitales* genera **Signos Vitales**.
**Equipo de Salud** maneja *Evaluar Signos Vitales*.

*Actualizar Resumen Clínico Domiciliario* requiere **Ficha Clínica**.
*Actualizar Resumen Clínico Domiciliario* genera **Resumen Clínico Domiciliario**.
**Equipo de Salud** maneja *Actualizar Resumen Clínico Domiciliario*.

**Categoría de Riesgo** puede estar `estable`, `en observación` o `inestable`.
*Categorizar Riesgo* requiere **Signos Vitales**.
*Categorizar Riesgo* cambia **Categoría de Riesgo** de `estable` a `en observación`.
**Equipo de Salud** maneja *Categorizar Riesgo*.

**Respuesta Terapéutica** puede estar `favorable`, `insuficiente` o `desfavorable`.
*Evaluar Respuesta Terapéutica* requiere **Condición Clínica**.
*Evaluar Respuesta Terapéutica* requiere **Resumen Clínico Domiciliario**.
*Evaluar Respuesta Terapéutica* cambia **Respuesta Terapéutica** de `insuficiente` a `favorable`.
**Equipo de Salud** maneja *Evaluar Respuesta Terapéutica*.

**Decisión de Continuidad** puede estar `continuar tratamiento`, `ajustar plan`, `proceder egreso` o `escalar`.
*Decidir Continuidad o Egreso* requiere **Categoría de Riesgo**.
*Decidir Continuidad o Egreso* requiere **Respuesta Terapéutica**.
*Decidir Continuidad o Egreso* cambia **Decisión de Continuidad** de `continuar tratamiento` a `proceder egreso`.
**Equipo de Salud** maneja *Decidir Continuidad o Egreso*.
```

## 2.5 Insight de modelado

Aquí aparece la diferencia entre “hacer visitas” y “operar una unidad”.

La unidad no solo ejecuta prestaciones. Produce juicios clínicos recurrentes sobre estabilidad, riesgo, respuesta y continuidad. Ese juicio recurrente es lo que vuelve posible el egreso seguro y el uso racional de cupos. [N][S][M]

---

# 3. SD1.9 — *Egresar Episodio*

## 3.1 Criterio de modelado

Se mantiene la tipología normativa de egresos, pero se la reescribe en clave de episodio. [N][M]

Razón:
- [N] las causales están claramente definidas por el reglamento
- [S] el sistema implementado tiene módulo `egreso/`
- [M] el nivel correcto de refinamiento aquí es unfolding por especialización

## 3.2 Tabla de elementos

| Tipo | Nombre | Esencia | Afiliación | Estados | Evidencia |
|------|--------|---------|------------|---------|-----------|
| Proceso | *Egresar Episodio* | Informatical | Sistémico | — | [N][S][M] |
| Proceso | *Egresar por Alta Médica* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Egresar por Reingreso Hospitalario* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Egresar por Fallecimiento* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Egresar por Renuncia Voluntaria* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Egresar por Alta Disciplinaria* | Informatical | Sistémico | — | [N][M] |
| Proceso | *Emitir Epicrisis* | Informatical | Sistémico | — | [N][S][H] |
| Proceso | *Cerrar Ficha Clínica* | Informatical | Sistémico | — | [N][S][H] |
| Objeto | **Episodio de Hospitalización Domiciliaria** | Informatical | Sistémico | `activo`, `egresado`, `cerrado` | [S][H] |
| Objeto | **Estado de Hospitalización** | Informatical | Sistémico | `activa`, `egresado` | [N][M] |
| Objeto | **Condición Clínica** | Informatical | Sistémico | `agudo-reagudizado`, `recuperado` | [N][M] |
| Objeto | **Epicrisis** | Informatical | Sistémico | `emitida` | [N][M] |
| Objeto | **Ficha Clínica** | Informatical | Sistémico | `abierta`, `cerrada` | [N][S][M] |
| Objeto | **Establecimiento de Atención Cerrada** | Físico | Ambiental | — | [N][M] |
| Objeto | **Consentimiento Informado** | Informatical | Sistémico | `sin firmar`, `firmado` | [N][M] |
| Objeto | **Director Técnico** | Físico | Sistémico | — | [N][M] |
| Objeto | **Médico de Atención Directa** | Físico | Sistémico | — | [N][M] |
| Objeto | **Vehículo de Transporte** | Físico | Sistémico | — | [N][M] |

## 3.3 Tabla de enlaces

| Tipo | Origen | Destino | Plantilla | Evidencia |
|------|--------|---------|-----------|-----------|
| Unfolding | *Egresar Episodio* | 5 especializaciones | RF7 | [M] |
| Effect (input-output) | *Egresar por Alta Médica* | **Condición Clínica** | TS3 | [N][M] |
| Effect (input-output) | *Egresar por Alta Médica* | **Estado de Hospitalización** | TS3 | [N][M] |
| Effect (input-output) | *Egresar por Alta Médica* | **Episodio de Hospitalización Domiciliaria** | TS3 | [S][H] |
| Agent | **Médico de Atención Directa** | *Egresar por Alta Médica* | H1 | [N][M] |
| Effect (input-output) | *Egresar por Reingreso Hospitalario* | **Estado de Hospitalización** | TS3 | [N][M] |
| Instrument | *Egresar por Reingreso Hospitalario* | **Establecimiento de Atención Cerrada** | H2 | [N][M] |
| Instrument | *Egresar por Reingreso Hospitalario* | **Vehículo de Transporte** | H2 | [N][M] |
| Agent | **Médico de Atención Directa** | *Egresar por Reingreso Hospitalario* | H1 | [N][M] |
| Effect (input-output) | *Egresar por Fallecimiento* | **Estado de Hospitalización** | TS3 | [N][M] |
| Agent | **Médico de Atención Directa** | *Egresar por Fallecimiento* | H1 | [N][M] |
| Effect (input-output) | *Egresar por Renuncia Voluntaria* | **Estado de Hospitalización** | TS3 | [N][M] |
| Instrument (state-specified) | *Egresar por Renuncia Voluntaria* | **Consentimiento Informado** en `firmado` | HS2 | [N][M] |
| Agent | **Médico de Atención Directa** | *Egresar por Renuncia Voluntaria* | H1 | [N][M] |
| Effect (input-output) | *Egresar por Alta Disciplinaria* | **Estado de Hospitalización** | TS3 | [N][M] |
| Agent | **Director Técnico** | *Egresar por Alta Disciplinaria* | H1 | [N][M] |
| Result | *Emitir Epicrisis* | **Epicrisis** | T2 | [N][S][H] |
| Effect (input-output) | *Cerrar Ficha Clínica* | **Ficha Clínica** | TS3 | [N][S][H] |
| Effect (input-output) | *Cerrar Ficha Clínica* | **Episodio de Hospitalización Domiciliaria** | TS3 | [S][H] |

## 3.4 OPL-ES

```opl
SD1 se refina por despliegue de *Egresar Episodio* en SD1.9.
*Egresar por Alta Médica*, *Egresar por Reingreso Hospitalario*, *Egresar por Fallecimiento*, *Egresar por Renuncia Voluntaria* y *Egresar por Alta Disciplinaria* son *Egresar Episodio*.

**Episodio de Hospitalización Domiciliaria** puede estar `activo`, `egresado` o `cerrado`.
**Estado de Hospitalización** puede estar `activa` o `egresado`.
Estado `activa` de **Estado de Hospitalización** es inicial.
Estado `egresado` de **Estado de Hospitalización** es final.

*Egresar por Alta Médica* cambia **Condición Clínica** de `agudo-reagudizado` a `recuperado`.
*Egresar por Alta Médica* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Alta Médica* cambia **Episodio de Hospitalización Domiciliaria** de `activo` a `egresado`.
**Médico de Atención Directa** maneja *Egresar por Alta Médica*.

*Egresar por Reingreso Hospitalario* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Reingreso Hospitalario* requiere **Establecimiento de Atención Cerrada**.
*Egresar por Reingreso Hospitalario* requiere **Vehículo de Transporte**.
**Médico de Atención Directa** maneja *Egresar por Reingreso Hospitalario*.

*Egresar por Fallecimiento* cambia **Estado de Hospitalización** de `activa` a `egresado`.
**Médico de Atención Directa** maneja *Egresar por Fallecimiento*.

*Egresar por Renuncia Voluntaria* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Renuncia Voluntaria* requiere **Consentimiento Informado** en `firmado`.
**Médico de Atención Directa** maneja *Egresar por Renuncia Voluntaria*.

*Egresar por Alta Disciplinaria* cambia **Estado de Hospitalización** de `activa` a `egresado`.
**Director Técnico** maneja *Egresar por Alta Disciplinaria*.

*Emitir Epicrisis* genera **Epicrisis**.
*Cerrar Ficha Clínica* cambia **Ficha Clínica** de `abierta` a `cerrada`.
*Cerrar Ficha Clínica* cambia **Episodio de Hospitalización Domiciliaria** de `egresado` a `cerrado`.
```

## 3.5 Insight de modelado

El egreso no es un único acto. Es una familia de cierres posibles del episodio, con una separación muy fuerte entre autoridad clínica y autoridad institucional. Ese punto importa mucho para dirección técnica. [N][M]

---

# 4. SD1.11 — *Tributar Producción y REM*

## 4.1 Criterio de modelado

Se modela como proceso propio y explícito. [S][H]

Justificación:
- [S] `rem/` existe como módulo explícito en la app y se describe como REM A21 automático
- [S] el diseño del sistema da gran peso a observabilidad operativa
- [N] aunque el DS no habla en detalle de REM, la operación pública HODOM está materialmente sometida a producción estadística y rendición de actividad

## 4.2 Tabla de elementos

| Tipo | Nombre | Esencia | Afiliación | Estados | Evidencia |
|------|--------|---------|------------|---------|-----------|
| Proceso | *Tributar Producción y REM* | Informatical | Sistémico | — | [S][H] |
| Proceso | *Consolidar Ingresos* | Informatical | Sistémico | — | [S][H] |
| Proceso | *Consolidar Altas* | Informatical | Sistémico | — | [S][H] |
| Proceso | *Consolidar Días-Persona* | Informatical | Sistémico | — | [S][H] |
| Proceso | *Consolidar Visitas por Profesión* | Informatical | Sistémico | — | [S][H] |
| Proceso | *Consolidar Cupos* | Informatical | Sistémico | — | [S][H] |
| Proceso | *Generar REM A21* | Informatical | Sistémico | — | [S][H] |
| Proceso | *Validar Consistencia Estadística* | Informatical | Sistémico | — | [S][H] |
| Objeto | **Ingreso Consolidado** | Informatical | Sistémico | — | [S][H] |
| Objeto | **Alta Consolidada** | Informatical | Sistémico | — | [S][H] |
| Objeto | **Día-Persona Consolidado** | Informatical | Sistémico | — | [S][H] |
| Objeto | **Visita por Profesión Consolidada** | Informatical | Sistémico | — | [S][H] |
| Objeto | **Cupo Consolidado** | Informatical | Sistémico | `programado`, `usado`, `disponible` | [S][H] |
| Objeto | **REM A21** | Informatical | Sistémico | `generado`, `validado` | [S][H] |
| Objeto | **Regla de Consistencia Estadística** | Informatical | Sistémico | — | [S][H] |
| Objeto | **Referente REM** | Físico | Sistémico | — | [S][H] |
| Objeto | **Base de Datos HODOM** | Informatical | Sistémico | — | [S][H] |

## 4.3 Tabla de enlaces

| Tipo | Origen | Destino | Plantilla | Evidencia |
|------|--------|---------|-----------|-----------|
| In-zooming | *Tributar Producción y REM* | 7 subprocesos | RF6 | [M] |
| Instrument | *Consolidar Ingresos* | **Base de Datos HODOM** | H2 | [S][H] |
| Result | *Consolidar Ingresos* | **Ingreso Consolidado** | T2 | [S][H] |
| Instrument | *Consolidar Altas* | **Base de Datos HODOM** | H2 | [S][H] |
| Result | *Consolidar Altas* | **Alta Consolidada** | T2 | [S][H] |
| Instrument | *Consolidar Días-Persona* | **Base de Datos HODOM** | H2 | [S][H] |
| Result | *Consolidar Días-Persona* | **Día-Persona Consolidado** | T2 | [S][H] |
| Instrument | *Consolidar Visitas por Profesión* | **Base de Datos HODOM** | H2 | [S][H] |
| Result | *Consolidar Visitas por Profesión* | **Visita por Profesión Consolidada** | T2 | [S][H] |
| Instrument | *Consolidar Cupos* | **Base de Datos HODOM** | H2 | [S][H] |
| Effect (input-output) | *Consolidar Cupos* | **Cupo Consolidado** | TS3 | [S][H] |
| Result | *Generar REM A21* | **REM A21** en `generado` | TS2 | [S][H] |
| Instrument | *Generar REM A21* | **Ingreso Consolidado** | H2 | [S][H] |
| Instrument | *Generar REM A21* | **Alta Consolidada** | H2 | [S][H] |
| Instrument | *Generar REM A21* | **Día-Persona Consolidado** | H2 | [S][H] |
| Instrument | *Generar REM A21* | **Visita por Profesión Consolidada** | H2 | [S][H] |
| Instrument | *Generar REM A21* | **Cupo Consolidado** | H2 | [S][H] |
| Agent | **Referente REM** | *Generar REM A21* | H1 | [S][H] |
| Instrument | *Validar Consistencia Estadística* | **Regla de Consistencia Estadística** | H2 | [S][H] |
| Effect (input-output) | *Validar Consistencia Estadística* | **REM A21** | TS3 | [S][H] |
| Agent | **Referente REM** | *Validar Consistencia Estadística* | H1 | [S][H] |

## 4.4 OPL-ES

```opl
SD1 se refina por descomposición de *Tributar Producción y REM* en SD1.11.
*Tributar Producción y REM* se descompone en *Consolidar Ingresos*, *Consolidar Altas*, *Consolidar Días-Persona*, *Consolidar Visitas por Profesión*, *Consolidar Cupos*, *Generar REM A21* y *Validar Consistencia Estadística*, en esa secuencia.

*Consolidar Ingresos* requiere **Base de Datos HODOM**.
*Consolidar Ingresos* genera **Ingreso Consolidado**.

*Consolidar Altas* requiere **Base de Datos HODOM**.
*Consolidar Altas* genera **Alta Consolidada**.

*Consolidar Días-Persona* requiere **Base de Datos HODOM**.
*Consolidar Días-Persona* genera **Día-Persona Consolidado**.

*Consolidar Visitas por Profesión* requiere **Base de Datos HODOM**.
*Consolidar Visitas por Profesión* genera **Visita por Profesión Consolidada**.

**Cupo Consolidado** puede estar `programado`, `usado` o `disponible`.
*Consolidar Cupos* requiere **Base de Datos HODOM**.
*Consolidar Cupos* cambia **Cupo Consolidado** de `programado` a `usado`.

**REM A21** puede estar `generado` o `validado`.
*Generar REM A21* requiere **Ingreso Consolidado**.
*Generar REM A21* requiere **Alta Consolidada**.
*Generar REM A21* requiere **Día-Persona Consolidado**.
*Generar REM A21* requiere **Visita por Profesión Consolidada**.
*Generar REM A21* requiere **Cupo Consolidado**.
*Generar REM A21* genera **REM A21** en `generado`.
**Referente REM** maneja *Generar REM A21*.

*Validar Consistencia Estadística* requiere **Regla de Consistencia Estadística**.
*Validar Consistencia Estadística* cambia **REM A21** de `generado` a `validado`.
**Referente REM** maneja *Validar Consistencia Estadística*.
```

## 4.5 Insight de modelado

El REM no es un residuo administrativo del sistema. Es una segunda vida del episodio: la actividad clínica se vuelve visible, comparable, financiable y gobernable solo cuando logra pasar a producción consolidada. [S][H]

---

# 5. Síntesis estructural de la v0.3

Con `v0.2` y `v0.3` juntas, el backbone HODOM HSC ya tiene formalizados estos seis macroprocesos críticos:

1. *Admitir Episodio*
2. *Programar Visitas y Rutas*
3. *Regular Atención a Distancia*
4. *Monitorear Evolución Clínica*
5. *Egresar Episodio*
6. *Tributar Producción y REM*

Esto permite ver el sistema como un ciclo completo:

- un caso entra y se vuelve episodio,
- el episodio se territorializa,
- absorbe variabilidad por regulación remota,
- se monitorea y redecide,
- termina por causal,
- y luego reaparece como dato de producción.

---

# 6. Qué emerge ahora con fuerza

## 6.1 La HODOM HSC tiene dos salidas

No solo egresa pacientes.
También egresa información consolidada.

Eso significa que la unidad no solo produce cuidado. Produce también verdad operativa sobre sí misma.

## 6.2 El episodio tiene dos cierres

- cierre clínico-operacional: egreso y cierre de ficha
- cierre estadístico: consolidación y validación REM

Si uno de los dos falla, la unidad queda incompleta.

## 6.3 Dirección técnica necesita ver ambos planos

No basta con mirar evolución clínica.
Hay que mirar también:
- continuidad,
- saturación de cupos,
- reingresos,
- actividad por profesión,
- trazabilidad de llamadas,
- capacidad real ejecutada vs capacidad programada.

---

# 7. Próximos pasos, sin preguntar demasiado

La secuencia autónoma correcta después de esta v0.3 sería:

1. producir `v0.4` integrando estos 6 bloques en un solo documento coherente
2. construir una tabla de objetos canónicos transversales del sistema
3. separar formalmente SD1 asistencial de SD3 gobernanza/observabilidad
4. alinear el modelo con entidades reales de BD y módulos UI
5. producir una versión “canónica local” más limpia y menos hipotética

---

# 8. Veredicto provisional

La HODOM HSC ya no aparece aquí como “hospitalización en domicilio” a secas.

Aparece como lo que realmente parece ser:

un sistema episódico, territorial, regulado, remotamente sensible y estadísticamente autoobservable.

Ese ya es un salto de comprensión importante.
