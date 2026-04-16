# Modelo OPM — HODOM HSC
# Arquitectura de Procesos

Versión: 0.1
Fecha: 2026-04-09
Estado: borrador estructural de trabajo

Propósito del documento: definir el backbone procesual más correcto para modelar la Hospitalización Domiciliaria del Hospital de San Carlos (HODOM HSC), priorizando procesos, granularidad y trazabilidad de evidencia.

## Convención de evidencia

- [N] Hecho sustentado en normativa HODOM (DS 1/2022, Decreto Exento 31/2024, Norma Técnica 2024)
- [S] Hecho sustentado en sistema/repositorio operativo (`hdos-app`, `hdos`)
- [M] Hecho heredado o afinado desde modelos OPM previos (`opm-hodom-normativo-v1.0`, `opm-hodom-model-v2.5`)
- [H] Hipótesis de modelado razonable, pendiente de validación empírica HSC

## Fuentes efectivamente usadas en esta versión

### Normativa
- [N] `/home/felix/kora/KNOWLEDGE/salud/hodom/normativa/01-reglamento-hodom-ds1-2022.md`
- [N] `/home/felix/kora/KNOWLEDGE/salud/hodom/normativa/02-decreto-exento-31-2024-aprueba-norma-tecnica.md`
- [N] `/home/felix/kora/KNOWLEDGE/salud/hodom/normativa/03-norma-tecnica-hodom-2024.md`

### Modelos previos
- [M] `kv_outbox_mente-omega/opm-hodom-normativo-v1.0.md`
- [M] `kv_outbox_mente-omega/opm-hodom-model-v2.5.md`

### Repositorios y especificaciones de sistema
- [S] `/home/felix/projects/hdos-app/README.md`
- [S] `/home/felix/projects/hdos-app/package.json`
- [S] `/home/felix/projects/hdos-app/docs/specs/00-INDICE.md`
- [S] `/home/felix/projects/hdos-app/docs/specs/01-diseno-sistema-operativo-hodom-hsc.md`
- [S] `/home/felix/projects/hdos-app/docs/specs/13-portal-paciente-mvp.md`
- [S] `/home/felix/projects/hdos/README.md`

---

## 1. Tesis de modelado

1. [N][S][M] La unidad estructural correcta del dominio no es el paciente aislado ni la visita aislada, sino el **Episodio de Hospitalización Domiciliaria**.
2. [N][S][M] HODOM HSC debe modelarse como sistema socio-técnico episódico que integra al mismo tiempo:
   - continuidad clínica hospitalaria en domicilio,
   - coordinación operativa,
   - regulación y comunicación clínica a distancia,
   - registro clínico y documental,
   - coordinación con red,
   - observabilidad estadística y tributación REM.
3. [M][S] Para HSC, el backbone procesual más correcto no es el SD1 normativo corto, sino un tronco procesual expandido, cercano a `v2.5`, pero alineado con la arquitectura de producto real de `hdos-app`.

---

## 2. Clasificación del sistema

**Tipo:** Socio-técnico. [N][M][S]

**Justificación:**
- [N] Combina equipo clínico multidisciplinario, infraestructura, equipamiento, comunicaciones, registros, protocolos y relación regulatoria con SEREMI.
- [S] El sistema implementado contiene módulos clínicos, operativos, telefónicos, de agenda, egreso, portal y REM.
- [M] Requiere modelar función, enablers, ambiente, gobernanza y control de flujo.

---

## 3. SD propuesto — Nivel 0

### 3.1 Proceso principal

**EN:** *Domiciliary Hospitalizing* [N][M]
**ES:** *Hospitalizar en Domicilio* [N][M]

### 3.2 Sistema

**Sistema de Hospitalización Domiciliaria del Hospital de San Carlos** [S][H]

Nota: el nombre organizacional específico HSC es correcto para el modelo local, aunque la semántica base proviene de la normativa general. [N][S]

### 3.3 Beneficiario principal

**Grupo de Pacientes** [N][M]

### 3.4 Atributo de valor principal

**Condición Clínica**: `agudo-reagudizado` → `recuperado` [N][M]

### 3.5 Núcleo OPL-ES del SD

```opl
**Sistema de Hospitalización Domiciliaria del Hospital de San Carlos** exhibe *Hospitalizar en Domicilio*.
**Grupo de Pacientes** exhibe **Condición Clínica**.
**Condición Clínica** puede estar `agudo-reagudizado` o `recuperado`.
Estado `agudo-reagudizado` de **Condición Clínica** es inicial.
Estado `recuperado` de **Condición Clínica** es final.
*Hospitalizar en Domicilio* cambia **Condición Clínica** de `agudo-reagudizado` a `recuperado`.
**Equipo de Salud** maneja *Hospitalizar en Domicilio*.
```

### 3.6 Lectura arquitectónica del SD

- [N] La función normativa sigue siendo recuperación o resolución suficientemente segura del cuadro.
- [S] En HSC esa función ocurre dentro de una operación digitalizada por episodio.
- [M] El SD no debe sobrecargarse con logística, llamadas o REM. Eso se resuelve en SD1 y niveles descendientes.

---

## 4. SD1 propuesto — Tronco procesual maestro

### 4.1 Decisión de arquitectura

Se propone que *Hospitalizar en Domicilio* se refine en **11 procesos**. [N][S][M]

Esto supera en riqueza al normativo corto y expresa mejor la realidad operativa observable en HSC. [S][M]

### 4.2 OPL-ES maestro de SD1

```opl
SD se refina por descomposición de *Hospitalizar en Domicilio* en SD1.
*Hospitalizar en Domicilio* se descompone en *Evaluar Elegibilidad*, *Admitir Episodio*, *Planificar Atención Interdisciplinaria*, *Programar Visitas y Rutas*, *Ejecutar Atención Domiciliaria*, *Regular Atención a Distancia*, *Monitorear Evolución Clínica*, *Gestionar Comunicación Clínica*, *Egresar Episodio*, *Realizar Seguimiento Post-Egreso* y *Tributar Producción y REM*, en esa secuencia general.
```

### 4.3 Sentido de cada proceso del tronco

1. **Evaluar Elegibilidad** [N][M]
   - Resuelve si el caso puede entrar al sistema.
2. **Admitir Episodio** [S][M]
   - Formaliza el episodio como unidad operativa y documental.
3. **Planificar Atención Interdisciplinaria** [N][S][M]
   - Convierte la admisión en programa terapéutico ejecutable.
4. **Programar Visitas y Rutas** [N][S][H]
   - Convierte el plan clínico en agenda territorial realizable.
5. **Ejecutar Atención Domiciliaria** [N][S][M]
   - Realiza atención clínica presencial en domicilio.
6. **Regular Atención a Distancia** [N][S][M]
   - Realiza resolución clínica no presencial vía TIC/llamadas.
7. **Monitorear Evolución Clínica** [N][M]
   - Evalúa respuesta al tratamiento y continuidad.
8. **Gestionar Comunicación Clínica** [N][S][H]
   - Ordena interacciones con cuidador, portal, derivadores y red.
9. **Egresar Episodio** [N][M]
   - Cierra el episodio por causal.
10. **Realizar Seguimiento Post-Egreso** [N][S][M]
   - Observa continuidad y desenlace inmediato post alta.
11. **Tributar Producción y REM** [S][N][H]
   - Materializa la obligación de observabilidad y reporte.

---

## 5. Árbol de refinamiento propuesto

## 5.1 SD1.1 — *Evaluar Elegibilidad*

### OPL-ES propuesto

```opl
SD1 se refina por descomposición de *Evaluar Elegibilidad* en SD1.1.
*Evaluar Elegibilidad* se descompone en *Pesquisar Candidato*, *Recibir Postulación*, *Evaluar Condición Clínica*, *Evaluar Condición del Domicilio*, *Verificar Red de Apoyo*, *Obtener Consentimiento Informado* y *Decidir Elegibilidad*, en esa secuencia.
```

### Lectura
- [N] Los 4 criterios de ingreso normativos deben quedar explícitos.
- [S] En HSC existe flujo de postulación y admisión como módulo propio.
- [M] La decisión final de elegibilidad conviene explicitarla como subproceso y no dejarla difusa.

## 5.2 SD1.2 — *Admitir Episodio*

### OPL-ES propuesto

```opl
SD1 se refina por descomposición de *Admitir Episodio* en SD1.2.
*Admitir Episodio* se descompone en *Registrar Ingreso*, *Abrir Ficha Clínica*, *Registrar Origen de Derivación*, *Elaborar Diagnóstico Social*, *Entregar Documentación Inicial* y *Coordinar con Derivador*, en esa secuencia.
```

### Lectura
- [S] El episodio, no solo el paciente, es la entidad operativa del sistema.
- [N] Consentimiento, ficha, formulario de ingreso, carta de derechos y coordinación derivadora son obligatorios.
- [M] Separar admisión de elegibilidad mejora limpieza causal.

## 5.3 SD1.3 — *Planificar Atención Interdisciplinaria*

### OPL-ES propuesto

```opl
SD1 se refina por descomposición de *Planificar Atención Interdisciplinaria* en SD1.3.
*Planificar Atención Interdisciplinaria* se descompone en *Elaborar Plan Terapéutico*, *Elaborar Plan de Cuidados de Enfermería*, *Definir Objetivos por Disciplina*, *Definir Frecuencia de Visitas*, *Definir Criterios de Monitoreo* y *Activar Plan de Atención*, en esa secuencia.
```

### Lectura
- [N] El plan terapéutico es requisito estructural expreso del sistema.
- [S] La app reconoce prescripción, plan y programación como piezas separadas.
- [H] “Definir Objetivos por Disciplina” probablemente emergerá con más claridad al revisar formularios y fichas reales.

## 5.4 SD1.4 — *Programar Visitas y Rutas*

### OPL-ES propuesto

```opl
SD1 se refina por descomposición de *Programar Visitas y Rutas* en SD1.4.
*Programar Visitas y Rutas* se descompone en *Construir Agenda Clínica*, *Asignar Profesional*, *Asignar Móvil*, *Secuenciar Ruta* y *Reprogramar Contingencia*, en esa secuencia operativa.
```

### Lectura
- [S] `agenda/` es módulo explícito del sistema.
- [N] La norma exige protocolos de programación de rutas y visitas.
- [M] Este proceso no debe esconderse como simple subrutina logística.

## 5.5 SD1.5 — *Ejecutar Atención Domiciliaria*

### OPL-ES propuesto

```opl
SD1 se refina por descomposición de *Ejecutar Atención Domiciliaria* en SD1.5.
*Ejecutar Atención Domiciliaria* se descompone en paralelo *Realizar Visita Médica*, *Realizar Atención de Enfermería*, *Realizar Atención TENS*, *Realizar Terapia Kinesiológica*, *Realizar Intervención Fonoaudiológica*, *Realizar Intervención Social*, *Educar a Paciente y Cuidador* y *Registrar Atención en Ficha*.
```

### Lectura
- [N] Médicos, enfermería, TENS, kinesiólogo y trabajador social tienen anclaje normativo directo.
- [S] El diseño de HSC contempla otras disciplinas y registro longitudinal.
- [H] Fonoaudiología y otras disciplinas pueden quedar como especializaciones opcionales según cartera efectiva.

## 5.6 SD1.6 — *Regular Atención a Distancia*

### OPL-ES propuesto

```opl
SD1 se refina por descomposición de *Regular Atención a Distancia* en SD1.6.
*Regular Atención a Distancia* se descompone en *Recibir Llamado Clínico*, *Evaluar Motivo de Consulta*, *Entregar Indicación Remota*, *Escalar a Visita Presencial*, *Activar Derivación Urgente* y *Registrar Regulación*, en esa secuencia.
```

### Lectura
- [N] Médico regulador y TIC tienen base normativa explícita.
- [S] `llamadas/` existe como módulo propio.
- [N][S] La trazabilidad de llamadas es una exigencia normativa y una necesidad operacional.

## 5.7 SD1.7 — *Monitorear Evolución Clínica*

### OPL-ES propuesto

```opl
SD1 se refina por descomposición de *Monitorear Evolución Clínica* en SD1.7.
*Monitorear Evolución Clínica* se descompone en *Evaluar Signos Vitales*, *Actualizar Resumen Clínico Domiciliario*, *Categorizar Riesgo*, *Evaluar Respuesta Terapéutica* y *Decidir Continuidad o Egreso*, en esa secuencia.
```

### Lectura
- [N] La norma técnica exige monitoreo mínimo de signos vitales.
- [M] Separar monitoreo de ejecución terapéutica mejora semántica del loop.
- [H] La categorización exacta debe amarrarse a reglas clínicas HSC reales.

## 5.8 SD1.8 — *Gestionar Comunicación Clínica*

### OPL-ES propuesto

```opl
SD1 se refina por descomposición de *Gestionar Comunicación Clínica* en SD1.8.
*Gestionar Comunicación Clínica* se descompone en *Coordinar con Hospital Derivador*, *Coordinar con APS*, *Emitir Indicaciones al Cuidador*, *Responder Mensaje del Portal*, *Emitir Documento de Emergencia* y *Trazar Llamado*, en esa secuencia general.
```

### Lectura
- [N] Existe deber de coordinación con derivadores, médico tratante y red.
- [S] El portal agrega mensajería y documento de emergencia.
- [H] Puede que algunas de estas piezas terminen redistribuidas entre regulación, portal y egreso en versiones posteriores.

## 5.9 SD1.9 — *Egresar Episodio*

### OPL-ES propuesto

```opl
SD1 se refina por despliegue de *Egresar Episodio* en SD1.9.
*Egresar por Alta Médica*, *Egresar por Reingreso Hospitalario*, *Egresar por Fallecimiento*, *Egresar por Renuncia Voluntaria* y *Egresar por Alta Disciplinaria* son *Egresar Episodio*.
```

### Lectura
- [N] Las causales normativas ya están bien fijadas.
- [M] Mantener esta parte cerca de `v1.0` y `v2.5` es correcto.
- [S] `egreso/` es módulo explícito en la app.

## 5.10 SD1.10 — *Realizar Seguimiento Post-Egreso*

### OPL-ES propuesto

```opl
SD1 se refina por descomposición de *Realizar Seguimiento Post-Egreso* en SD1.10.
*Realizar Seguimiento Post-Egreso* se descompone en *Ejecutar Llamada de Seguimiento*, *Enviar Contrarreferencia* y *Evaluar Resultado Post-Egreso*, en esa secuencia.
```

### Lectura
- [N] El seguimiento existe en normativa y continuidad de la atención.
- [S] La operación digital necesita este cierre para red y trazabilidad.

## 5.11 SD1.11 — *Tributar Producción y REM*

### OPL-ES propuesto

```opl
SD1 se refina por descomposición de *Tributar Producción y REM* en SD1.11.
*Tributar Producción y REM* se descompone en *Consolidar Ingresos*, *Consolidar Altas*, *Consolidar Días-Persona*, *Consolidar Visitas por Profesión*, *Consolidar Cupos*, *Generar REM A21* y *Validar Consistencia Estadística*, en esa secuencia.
```

### Lectura
- [S] `rem/` existe como módulo explícito y automático.
- [N] La norma no detalla REM, pero la operación pública lo exige materialmente.
- [H] Puede subir a SD3 si se decide separar completamente producción de asistencia.

---

## 6. OPL-ES maestro compacto del sistema HSC

```opl
**Sistema de Hospitalización Domiciliaria del Hospital de San Carlos** exhibe *Hospitalizar en Domicilio*.
*Hospitalizar en Domicilio* se descompone en *Evaluar Elegibilidad*, *Admitir Episodio*, *Planificar Atención Interdisciplinaria*, *Programar Visitas y Rutas*, *Ejecutar Atención Domiciliaria*, *Regular Atención a Distancia*, *Monitorear Evolución Clínica*, *Gestionar Comunicación Clínica*, *Egresar Episodio*, *Realizar Seguimiento Post-Egreso* y *Tributar Producción y REM*, en esa secuencia general.
*Evaluar Elegibilidad* se descompone en *Pesquisar Candidato*, *Recibir Postulación*, *Evaluar Condición Clínica*, *Evaluar Condición del Domicilio*, *Verificar Red de Apoyo*, *Obtener Consentimiento Informado* y *Decidir Elegibilidad*, en esa secuencia.
*Admitir Episodio* se descompone en *Registrar Ingreso*, *Abrir Ficha Clínica*, *Registrar Origen de Derivación*, *Elaborar Diagnóstico Social*, *Entregar Documentación Inicial* y *Coordinar con Derivador*, en esa secuencia.
*Planificar Atención Interdisciplinaria* se descompone en *Elaborar Plan Terapéutico*, *Elaborar Plan de Cuidados de Enfermería*, *Definir Objetivos por Disciplina*, *Definir Frecuencia de Visitas*, *Definir Criterios de Monitoreo* y *Activar Plan de Atención*, en esa secuencia.
*Programar Visitas y Rutas* se descompone en *Construir Agenda Clínica*, *Asignar Profesional*, *Asignar Móvil*, *Secuenciar Ruta* y *Reprogramar Contingencia*, en esa secuencia operativa.
*Ejecutar Atención Domiciliaria* se descompone en paralelo *Realizar Visita Médica*, *Realizar Atención de Enfermería*, *Realizar Atención TENS*, *Realizar Terapia Kinesiológica*, *Realizar Intervención Fonoaudiológica*, *Realizar Intervención Social*, *Educar a Paciente y Cuidador* y *Registrar Atención en Ficha*.
*Regular Atención a Distancia* se descompone en *Recibir Llamado Clínico*, *Evaluar Motivo de Consulta*, *Entregar Indicación Remota*, *Escalar a Visita Presencial*, *Activar Derivación Urgente* y *Registrar Regulación*, en esa secuencia.
*Monitorear Evolución Clínica* se descompone en *Evaluar Signos Vitales*, *Actualizar Resumen Clínico Domiciliario*, *Categorizar Riesgo*, *Evaluar Respuesta Terapéutica* y *Decidir Continuidad o Egreso*, en esa secuencia.
*Gestionar Comunicación Clínica* se descompone en *Coordinar con Hospital Derivador*, *Coordinar con APS*, *Emitir Indicaciones al Cuidador*, *Responder Mensaje del Portal*, *Emitir Documento de Emergencia* y *Trazar Llamado*, en esa secuencia general.
*Egresar por Alta Médica*, *Egresar por Reingreso Hospitalario*, *Egresar por Fallecimiento*, *Egresar por Renuncia Voluntaria* y *Egresar por Alta Disciplinaria* son *Egresar Episodio*.
*Realizar Seguimiento Post-Egreso* se descompone en *Ejecutar Llamada de Seguimiento*, *Enviar Contrarreferencia* y *Evaluar Resultado Post-Egreso*, en esa secuencia.
*Tributar Producción y REM* se descompone en *Consolidar Ingresos*, *Consolidar Altas*, *Consolidar Días-Persona*, *Consolidar Visitas por Profesión*, *Consolidar Cupos*, *Generar REM A21* y *Validar Consistencia Estadística*, en esa secuencia.
```

---

## 7. Decisiones de modelado tomadas en esta versión

1. **Se privilegia el episodio sobre el paciente como unidad operativa.** [S][M]
2. **Se separa la admisión de la elegibilidad.** [M]
3. **Se separa la planificación de la programación logística.** [S][N][M]
4. **Se separa la atención presencial de la regulación remota.** [N][S]
5. **Se explicita la comunicación clínica como macroproceso.** [S][H]
6. **Se explicita la tributación REM como proceso y no solo como output silencioso.** [S][H]

---

## 8. Riesgos y puntos a validar

### Riesgos de sobre-modelado
- [H] Comunicación clínica podría estar demasiado expandida para este nivel.
- [H] REM podría terminar mejor en una capa de gobernanza/observabilidad separada.
- [H] Fonoaudiología y otras disciplinas quizá deban modelarse como opcionales o como colección abierta.

### Puntos de validación empírica HSC
- estructura real del episodio en BD y UI
- flujo exacto de llamadas y regulación
- cómo se registran visitas no efectuadas y contingencias
- cómo se materializa el resumen clínico domiciliario
- reglas reales de categorización y continuidad
- pipeline exacto REM A21

---

## 9. Siguiente paso recomendado

Construir `v0.2` con estas mejoras:

1. agregar **tabla de elementos** para SD y SD1
2. agregar **objetos clave por macroproceso**
3. definir **links procedurales** principales
4. limpiar qué procesos quedan en SD1 y cuáles migran a SD3
5. contrastar este backbone contra formularios y tablas reales de `hdos-app`/`hodom`

---

## 10. Veredicto provisional

Este backbone es, a esta altura del trabajo, la mejor arquitectura procesual disponible para modelar la HODOM del Hospital de San Carlos con foco en procesos.

Es superior al normativo corto porque incorpora:
- territorialidad,
- regulación remota,
- comunicación clínica,
- episodio como unidad,
- agenda/ruta como proceso core,
- observabilidad y REM como parte constitutiva de la operación.

Pero todavía es una **arquitectura procesual candidata**, no el modelo final cerrado.

Necesita una siguiente iteración apoyada en artefactos operacionales reales para pasar de backbone correcto a modelo canónico local.
