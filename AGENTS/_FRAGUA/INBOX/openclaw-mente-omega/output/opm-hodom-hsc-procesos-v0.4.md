# Modelo OPM — HODOM HSC
# Arquitectura de Procesos Integrada

Versión: 0.4
Fecha: 2026-04-09
Estado: integración estructural

Propósito de esta versión: integrar el trabajo de `v0.1`, `v0.2` y `v0.3` en una sola arquitectura procesual coherente, separando con mayor claridad:
- capa asistencial episódica,
- capa de coordinación y regulación,
- capa de observabilidad y reporte.

Esta versión sigue siendo un borrador de alta densidad conceptual, no todavía el modelo local definitivo.

## Convención de evidencia

- [N] Normativa HODOM
- [S] Sistema/repositorio HSC (`hdos-app`, `hdos`)
- [M] Modelo OPM previo
- [H] Hipótesis pendiente de validación local

## Fuentes base de esta versión

### Normativa
- [N] `01-reglamento-hodom-ds1-2022.md`
- [N] `02-decreto-exento-31-2024-aprueba-norma-tecnica.md`
- [N] `03-norma-tecnica-hodom-2024.md`

### Sistema HSC
- [S] `hdos-app/README.md`
- [S] `hdos-app/docs/specs/00-INDICE.md`
- [S] `hdos-app/docs/specs/01-diseno-sistema-operativo-hodom-hsc.md`
- [S] `hdos-app/docs/specs/13-portal-paciente-mvp.md`
- [S] `hdos/README.md`

### Artefactos previos
- [M] `opm-hodom-normativo-v1.0.md`
- [M] `opm-hodom-model-v2.5.md`
- [M] `opm-hodom-hsc-procesos-v0.1.md`
- [M] `opm-hodom-hsc-procesos-v0.2.md`
- [M] `opm-hodom-hsc-procesos-v0.3.md`

---

# 1. Síntesis ejecutiva de modelado

La HODOM HSC aparece ya no como un simple servicio de visitas domiciliarias, sino como un sistema socio-técnico con tres planos simultáneos:

1. **Asistencia episódica**
   - transforma un caso derivado en un episodio clínico con plan, ejecución, monitoreo y egreso.

2. **Coordinación y regulación**
   - transforma intención clínica en territorialidad ejecutable y absorbe incertidumbre por comunicación y resolución remota.

3. **Observabilidad y gobierno operativo**
   - transforma actividad asistencial en información consolidada, trazable y reportable.

La arquitectura correcta del modelo debe respetar esos tres planos, porque en HSC están ya insinuados a la vez por la normativa, por el diseño funcional del sistema y por los módulos reales implementados. [N][S][M]

---

# 2. Clasificación del sistema

**Tipo:** Socio-técnico. [N][S][M]

**Justificación resumida:**
- agentes humanos clínicos, técnicos, administrativos y directivos,
- infraestructura, vehículos, comunicaciones, registros, botiquín/equipamiento,
- capa informatical densa: ficha, agenda, llamadas, REM, portal,
- relación fuerte con red asistencial, regulación y SEREMI.

---

# 3. SD integrado — Nivel 0

## 3.1 Sistema

**Sistema de Hospitalización Domiciliaria del Hospital de San Carlos** [S][H]

## 3.2 Proceso principal

**EN:** *Domiciliary Hospitalizing* [N][M]
**ES:** *Hospitalizar en Domicilio* [N][M]

## 3.3 Beneficiario principal

**Grupo de Pacientes** [N][M]

## 3.4 Atributo de valor principal

**Condición Clínica**: `agudo-reagudizado` → `recuperado` [N][M]

## 3.5 OPL-ES del SD

```opl
**Sistema de Hospitalización Domiciliaria del Hospital de San Carlos** exhibe *Hospitalizar en Domicilio*.
**Grupo de Pacientes** exhibe **Condición Clínica**.
**Condición Clínica** puede estar `agudo-reagudizado` o `recuperado`.
Estado `agudo-reagudizado` de **Condición Clínica** es inicial.
Estado `recuperado` de **Condición Clínica** es final.
*Hospitalizar en Domicilio* cambia **Condición Clínica** de `agudo-reagudizado` a `recuperado`.
**Equipo de Salud** maneja *Hospitalizar en Domicilio*.
```

---

# 4. SD1 integrado — Capa asistencial episódica

## 4.1 Regla de integración

Se limpió el backbone original de `v0.1` en dos sentidos:
- se mantienen en SD1 los procesos que pertenecen al arco clínico-operacional del episodio,
- se deja explícito que algunos procesos ya rozan observabilidad/gobernanza y más adelante podrán migrar o duplicarse en SD3. [M]

## 4.2 SD1 maestro integrado

```opl
SD se refina por descomposición de *Hospitalizar en Domicilio* en SD1.
*Hospitalizar en Domicilio* se descompone en *Evaluar Elegibilidad*, *Admitir Episodio*, *Planificar Atención Interdisciplinaria*, *Programar Visitas y Rutas*, *Ejecutar Atención Domiciliaria*, *Regular Atención a Distancia*, *Monitorear Evolución Clínica*, *Gestionar Comunicación Clínica*, *Egresar Episodio*, *Realizar Seguimiento Post-Egreso* y *Tributar Producción y REM*, en esa secuencia general.
```

## 4.3 Lectura de SD1 por bloques

### Bloque A — Entrada
- *Evaluar Elegibilidad*
- *Admitir Episodio*

### Bloque B — Programación
- *Planificar Atención Interdisciplinaria*
- *Programar Visitas y Rutas*

### Bloque C — Ejecución y absorción de variabilidad
- *Ejecutar Atención Domiciliaria*
- *Regular Atención a Distancia*
- *Gestionar Comunicación Clínica*

### Bloque D — Juicio clínico y cierre
- *Monitorear Evolución Clínica*
- *Egresar Episodio*
- *Realizar Seguimiento Post-Egreso*

### Bloque E — Observabilidad derivada
- *Tributar Producción y REM*

---

# 5. Objetos canónicos transversales del sistema

Esta tabla no representa todavía el catálogo definitivo del modelo completo. Representa los objetos que ya emergen como columna vertebral transversal del sistema. [M][S]

| Objeto | Rol estructural | Capas donde aparece | Evidencia |
|--------|------------------|---------------------|-----------|
| **Episodio de Hospitalización Domiciliaria** | unidad operativa principal | admisión, ejecución, egreso, REM | [S][H] |
| **Ficha Clínica** | memoria clínica longitudinal | admisión, atención, monitoreo, egreso | [N][S][M] |
| **Condición Clínica** | atributo de valor principal | SD, monitoreo, egreso | [N][M] |
| **Plan de Atención** | puente entre decisión clínica y ejecución | planificación, agenda, atención | [N][S][H] |
| **Visita Domiciliaria** | unidad mínima de ejecución territorial | agenda, atención, regulación | [S][H] |
| **Ruta Diaria** | forma logística de territorialización | agenda, contingencia | [S][M] |
| **Llamado Clínico** | unidad mínima de regulación remota | llamadas, regulación, trazabilidad | [N][S][H] |
| **Decisión de Continuidad** | objeto de juicio clínico recurrente | monitoreo, egreso | [M][H] |
| **Estado de Hospitalización** | indicador formal de curso del episodio | admisión, egreso | [N][M] |
| **Epicrisis** | objeto de cierre clínico | egreso, contrarreferencia | [N][M] |
| **REM A21** | salida estadística consolidada | reporte, observabilidad | [S][H] |
| **Cupo Consolidado** | indicador de capacidad operativa | censo, REM, gestión | [S][H] |

## 5.1 Insight

Estos objetos muestran que el sistema no está organizado simplemente alrededor de personas y prestaciones. Está organizado alrededor de artefactos de continuidad, decisión, territorialización y cierre. [S][M]

---

# 6. Separación de capas: asistencial vs coordinación vs observabilidad

## 6.1 Capa asistencial pura

Procesos cuyo propósito inmediato es transformar la situación clínica del paciente:
- *Evaluar Elegibilidad*
- *Planificar Atención Interdisciplinaria*
- *Ejecutar Atención Domiciliaria*
- *Monitorear Evolución Clínica*
- *Egresar Episodio*
- *Realizar Seguimiento Post-Egreso*

## 6.2 Capa de coordinación y regulación

Procesos cuyo propósito inmediato es hacer ejecutable, segura o resoluble la asistencia:
- *Admitir Episodio*
- *Programar Visitas y Rutas*
- *Regular Atención a Distancia*
- *Gestionar Comunicación Clínica*

## 6.3 Capa de observabilidad y reporte

Procesos cuyo propósito inmediato es volver visible, comparable y gobernable la operación:
- *Tributar Producción y REM*

## 6.4 Consecuencia modelística

Esta separación sugiere que el modelo completo tenderá naturalmente a dos grandes diagramas descendientes:
- SD1 asistencial-operativo
- SD3 gobernanza/observabilidad

Por ahora, `Tributar Producción y REM` permanece en SD1 por cercanía con el cierre episódico, pero estructuralmente ya pide una migración parcial a una capa de gobierno. [M][H]

---

# 7. OPL-ES integrado del backbone

```opl
*Hospitalizar en Domicilio* se descompone en *Evaluar Elegibilidad*, *Admitir Episodio*, *Planificar Atención Interdisciplinaria*, *Programar Visitas y Rutas*, *Ejecutar Atención Domiciliaria*, *Regular Atención a Distancia*, *Monitorear Evolución Clínica*, *Gestionar Comunicación Clínica*, *Egresar Episodio*, *Realizar Seguimiento Post-Egreso* y *Tributar Producción y REM*, en esa secuencia general.

*Admitir Episodio* se descompone en *Registrar Ingreso*, *Abrir Ficha Clínica*, *Registrar Origen de Derivación*, *Elaborar Diagnóstico Social*, *Entregar Documentación Inicial* y *Coordinar con Derivador*, en esa secuencia.

*Programar Visitas y Rutas* se descompone en *Construir Agenda Clínica*, *Asignar Profesional*, *Asignar Móvil*, *Secuenciar Ruta* y *Reprogramar Contingencia*, en esa secuencia operativa.

*Regular Atención a Distancia* se descompone en *Recibir Llamado Clínico*, *Evaluar Motivo de Consulta*, *Entregar Indicación Remota*, *Escalar a Visita Presencial*, *Activar Derivación Urgente* y *Registrar Regulación*, en esa secuencia.

*Monitorear Evolución Clínica* se descompone en *Evaluar Signos Vitales*, *Actualizar Resumen Clínico Domiciliario*, *Categorizar Riesgo*, *Evaluar Respuesta Terapéutica* y *Decidir Continuidad o Egreso*, en esa secuencia.

*Egresar por Alta Médica*, *Egresar por Reingreso Hospitalario*, *Egresar por Fallecimiento*, *Egresar por Renuncia Voluntaria* y *Egresar por Alta Disciplinaria* son *Egresar Episodio*.

*Tributar Producción y REM* se descompone en *Consolidar Ingresos*, *Consolidar Altas*, *Consolidar Días-Persona*, *Consolidar Visitas por Profesión*, *Consolidar Cupos*, *Generar REM A21* y *Validar Consistencia Estadística*, en esa secuencia.
```

---

# 8. Tabla de tensiones abiertas

| Tensión | Descripción | Estado |
|--------|-------------|--------|
| Episodio vs paciente | el sistema funciona por episodio, pero parte de la normativa habla en clave de paciente | asumida, bien encaminada |
| Comunicación clínica | podría permanecer como macroproceso o redistribuirse entre regulación, portal y egreso | abierta |
| REM en SD1 o SD3 | operativamente nace del episodio, estructuralmente pertenece al gobierno | abierta |
| Objetivos por disciplina | está bien conceptualmente, pero falta anclaje empírico fino | abierta |
| Categoría de riesgo | parece necesaria, pero falta definición local más dura | abierta |
| Portal paciente/cuidador | hoy aparece por comunicación, pero aún no como submodelo propio | abierta |

---

# 9. Hallazgos fuertes que ya no conviene perder

## 9.1 La unidad real del dominio es el episodio

Esto ya no parece una hipótesis débil. Todo empuja hacia ahí:
- la ficha por estadía,
- el módulo `ficha/[stayId]`,
- el flujo admisión → atención → egreso → REM,
- la necesidad de cierre clínico y estadístico.

## 9.2 La agenda es clínica, no solo logística

En HODOM, programar una visita es parte del cuidado. La agenda traduce prioridad clínica a presencia territorial.

## 9.3 La llamada es acto clínico potencial

La atención remota no es un accesorio telefónico. Puede gatillar resolución, visita o derivación urgente.

## 9.4 El REM es parte de la ontología operativa

No es un apéndice administrativo. Es una transformación real del sistema sobre sus propios datos de actividad.

---

# 10. Próxima secuencia autónoma recomendada

Después de esta v0.4, la continuación natural es:

1. producir `v0.5` dedicada a **SD3 — Gobernar Sistema HODOM HSC**
2. mover allí explícitamente:
   - control de cupos,
   - calidad y seguridad,
   - consistencia estadística,
   - capacitación,
   - protocolos,
   - autorización sanitaria,
   - auditoría de llamadas y registros
3. dejar una frontera más limpia entre sistema asistencial y sistema de gobierno
4. luego producir una `v1.0 local` mucho más estable

---

# 11. Veredicto provisional

Con esta integración, el modelo deja de parecer una suma de procesos sueltos.

Empieza a aparecer como una arquitectura real:
- episódica,
- territorial,
- regulada,
- remotamente sensible,
- y autoobservable.

Ese ya es un marco de diseño serio para una HODOM moderna.
