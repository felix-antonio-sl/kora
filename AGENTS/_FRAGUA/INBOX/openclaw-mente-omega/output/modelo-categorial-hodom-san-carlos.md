# Modelo Categórico del Dominio de Hospitalización Domiciliaria — Hospital de San Carlos

**Versión:** 4.1  
**Fecha:** 2026-03-31  
**Convención de composición:** `g ∘ f` se lee right-to-left (estándar matemático): primero `f`, luego `g`. Los comentarios en línea siguen esta misma convención.  
**Fuentes integradas:**
- Modelo OPM HoDom (SD–SD9)
- Esquema operacional `ingresos_hodom` v1.0
- Especificación REM A21 C.1
- Manual REM 2026 (MINSAL/DEIS) — definiciones conceptuales y operacionales oficiales
- Proyecto de Implementación Permanente HODOM HSC (BIP 40059567-0)
- Enlace HoDom–APS (protocolo postrados)
- Pipeline de migración (README, 30 archivos fuente, 1698 episodios, 1231 pacientes)
- Formularios clínicos: Registro Enfermería diario, Hoja Ingreso Kinesiología, Registro Curaciones
- Presentación Enlace HODOM-APS HSC
- **[v3]** Hoja Ingreso Enfermería HODOM HSC (formulario de admisión con checklist y examen físico)
- **[v3]** Registro Visita Equipo HODOM / Ciclo Vital (planilla real de signos vitales — 15 columnas)
- **[v3]** Consentimiento Informado Hospitalización Domiciliaria HSC 2026
- **[v4]** Formularios de Postulación 2025 y 2026 (Google Form → XLSX)
- **[v4]** Canasta HODOM (Resolución Exenta, 24 prestaciones con código MAI)
- **[v4]** Consolidado Atenciones Diarias 2026 (368 días, serie temporal)
- **[v4]** Entrega Turno Kinesiología (106 hojas) y Enfermería (3 muestras)
- **[v4]** Cartera de Servicios HSC (Res. Exenta N°1.206)
- **[v4b]** Registro Trabajo Social, Registro Llamadas, Programación Diaria
- **[v4b]** Contraste FHIR R5 + Corpus HaH internacional (113 fuentes)

**Método:** Integración categórica — estático + dinámico + observacional  
**Clasificación:** `integration` con componentes `static` y `dynamic`  
**Convención de marcadores de versión:** Los marcadores `[v3]`, `[v4]`, `[v4b]`, `[v4.1]` aparecen solo en elementos que fueron adiciones o correcciones significativas respecto a la versión anterior. La ausencia de marcador indica contenido original (v1-v2). Los marcadores se preservan como trazabilidad de evolución del modelo.

---

## 1. Posicionamiento del Problema

### 1.1 Qué es este modelo

Una formalización categórica exhaustiva del dominio de Hospitalización Domiciliaria del Hospital de San Carlos Dr. Benicio Arzola Medina. Describe la estructura de datos, la dinámica de procesos y los mecanismos de observación estadística como un sistema integrado de categorías conectadas por functores.

### 1.2 Para qué sirve

- **Especificación:** Define con precisión qué entidades, relaciones, restricciones y transiciones existen en el dominio, eliminando ambigüedades entre fuentes.
- **Integración:** Conecta el registro operacional individual, la dinámica de procesos clínico-administrativos, y el reporte estadístico (REM) como proyecciones formales de una misma realidad.
- **Auditoría:** Identifica déficits estructurales en el esquema de datos actual y en los formularios en uso.
- **Diseño:** Sirve como base para un esquema relacional normalizado que sostenga las operaciones y derive el REM por query.

### 1.3 Tesis estructural

**El episodio de hospitalización domiciliaria (EpisodioHD) es la acción-clave-primaria del dominio.** No es un atributo del paciente ni del establecimiento. Es la unidad indexadora sobre la cual se definen estados, transiciones, observaciones clínicas, visitas, planes, egresos y agregaciones estadísticas. Todo lo demás se define por su relación morfológica con el episodio.

Esta tesis está respaldada categóricamente por el framework action-as-primary-key: la estructura rica reside en los morfismos (acciones sobre el episodio), no en los objetos aislados (paciente, domicilio, equipo).

### 1.4 Contexto institucional

- **Establecimiento:** Hospital de San Carlos, segundo en complejidad en Ñuble. 130 camas de dotación. Centro de referencia de la red norte (10 comunas).
- **Estado actual:** HoDom operando desde junio 2023 por campaña/compra de servicio. Proyecto BIP 40059567-0 busca implementación permanente.
- **Capacidad:** 20-25 cupos diarios. Promedio 8 días de estada. Meta: ~900 pacientes/año.
- **Radio de cobertura:** 20 km desde el hospital. Comunas: San Carlos, San Nicolás, Ñiquén, San Fabián y sectores rurales.
- **Población objetivo:** ~67.000 adultos (≥18 años) de 4 comunas.
- **Evidencia empírica (2023-2025):**
  - 2023: 307 ingresos, 280 altas, 13 fallecidos esperados, 0 no esperados, 16 reingresos, 5.148 visitas
  - 2024: 843 ingresos, 850 altas, 16 fallecidos esperados, 0 no esperados, 28 reingresos, 11.562 visitas
  - 2025: 598 ingresos, 629 altas, 7 fallecidos esperados, 0 no esperados, 28 reingresos, 9.428 visitas
- **Indicador crítico:** Oportunidad de hospitalización ≤12h cayó de 97% (2019) a 47% (2025). Índice ocupacional medicina/cirugía/traumatología consistentemente >90%.

---

## 2. Arquitectura de Categorías

El dominio se formaliza como seis categorías interrelacionadas (más dos categorías derivadas: C_compartido y C_integrado, definidas por el pushout en §4.5):

```
                          C_inst
                       (institucional)
                            │
                       contextualiza
                            ↓
C_form ──tensión──→      C_proc
(formularios)          (procesos)
  │                        │
  │extraer            F_proc│
  │                        ↓
  └──────────────→      C_op      ←──── C_migr
                   (operacional)      (migración)
                            │
                       F_REM │
                            ↓
                          C_rem
                        (reporte)
```

**Nota [v4.1]:** C_form y C_proc están en tensión: los formularios reales capturan más variables que las modeladas en el proceso normativo (ej: 12 variables de ciclo vital vs 4 en OPM). La flecha `tensión` indica que C_form revela brechas en C_proc.

| Categoría | Fuentes | Función |
|-----------|---------|---------|
| C_op | Esquema ingresos_hodom, definiciones operacionales | Núcleo: registro individual de episodios, pacientes, visitas, recursos |
| C_proc | Modelo OPM (SD–SD9), Orientación Técnica, DS N°1 | Dinámica normativa: estados, transiciones, agentes, precondiciones |
| C_rem | Manual REM 2026, Especificación REM A21 C.1 | Observación: agregados estadísticos mensuales |
| C_inst | Proyecto Implementación, Enlace APS, datos empíricos | Contexto institucional: capacidad, dotación, cobertura, red |
| C_form | Registro Enfermería, Hoja Kinesiología, Registro Curaciones | Formularios clínicos: estructura real de captura de datos en terreno |
| C_migr | Pipeline migración (README), 30 CSV fuente | Datos reales: 1698 episodios, 1231 pacientes, estrategias de identidad |

---

## 3. Categoría Operacional C_op

### 3.1 Objetos

#### 3.1.1 Objetos nucleares

| Objeto | Tipo | Identidad | Descripción |
|--------|------|-----------|-------------|
| `Paciente` | entidad | `rut` (formato chileno, validado por dígito verificador) | Individuo con atributos demográficos. Separado del episodio: relación 1:N |
| `EpisodioHD` | acción-entidad | `id_registro` (surrogate) + `(rut, fecha_ingreso)` (natural) | Unidad central: un ingreso–estancia–egreso. Porta estados, planes, transiciones |
| `Domicilio` | entidad-ambiental | `(direccion, comuna)` | Lugar donde ocurre la hospitalización. Porta condiciones evaluables |
| `Postulacion` | pre-entidad | `nro_postulacion` | **[v3]** Objeto formal previo al episodio. Existe desde la evaluación, antes del ingreso. Fuente: Hoja Ingreso Enfermería campo "Nro. Postulación" |
| `Cuidador` | entidad | `(rut_cuidador, nombre)` | Familiar responsable. **[v3]** CI 2026 registra RUT del cuidador + parentesco. Precondición de elegibilidad |
| `EquipoSalud` | agregado | `id_equipo` | Conjunto estructurado de profesionales asignado al programa |
| `Profesional` | entidad | `rut_profesional` | Miembro individual con rol tipado |

#### 3.1.2 Objetos de plan y tratamiento

| Objeto | Tipo | Estados | Descripción |
|--------|------|---------|-------------|
| `PlanTerapeutico` | artefacto-estado | borrador → activo → completado | Programa de tratamiento del episodio |
| `PlanCuidadosEnfermeria` | artefacto-estado | borrador → activo → completado | Derivado del plan terapéutico |
| `RecetaMedica` | artefacto | — | Prescripción farmacológica |
| `ProgramaVisitas` | artefacto | — | Calendario de visitas domiciliarias |
| `RutaTransporte` | artefacto | — | Logística de desplazamiento |

#### 3.1.3 Objetos de registro clínico (derivados de formularios reales)

| Objeto | Tipo | Fuente | Campos capturados |
|--------|------|--------|-------------------|
| `RegistroClinico` | supertipo | — | Tipo abstracto. Codominio de `genera_registro`. Subtipos: RegistroEnfermeria, IngresoKinesiologia, RegistroCuraciones, ResumenClinicoDomiciliario, RegistroCicloVital, RegistroTelesalud |
| `Visita` | evento | Todos los formularios | fecha, profesional, episodio |
| `IngresoEnfermeria` | evaluación-ingreso | **[v3]** Hoja Ingreso Enfermería HODOM HSC | Nro. Postulación, fechas (ingreso/egreso/visita_ingreso), servicio_origen, checklist (7 ítems Si/No/NA), examen_fisico (6 dominios enum), historia clínica (antecedentes, medicamentos crónicos, valores exámenes), examen segmentario (12 regiones), diagnóstico enfermería, plan atención enfermería, profesional_responsable_ingreso + profesional_responsable_VD |
| `RegistroCicloVital` | observación-serie | **[v3]** Registro Visita Equipo HODOM | **15 columnas por fila:** Fecha, PA, FC, FR, T°, SAT%, HGT, EVA, Glasgow, Edema, Diuresis, Deposiciones, Invasivos, Observaciones_Visita, Responsable. Este es el formulario real de monitoreo diario — una fila por visita |
| `RegistroEnfermeria` | observación-diaria | Registro Enfermería diario HODOM HSC | narrativa clínica, medicamentos (dosis, dilución, vía, nro_dosis), plan de enfermería (lista intervenciones), invasivos (fecha_instalación, cambio, signos_infección/flebitis), firma |
| `IngresoKinesiologia` | evaluación | Hoja Kinesiología | ant_morbidos, diagnostico_medico, funcionalidad_previa, conciencia, barthel, tiempo_reposo, farmacos, asistencias, evaluación_motora, evaluación_respiratoria, dependencia_kinesica_motora, dependencia_kinesica_respiratoria, objetivos, indicación |
| `RegistroCuraciones` | procedimiento | Registro Curaciones | fecha, lugar/grado, exudación/cantidad, tipo_tejido, caracteristicas/tamaño, aposito_1, aposito_2, observaciones, responsable |
| `CategoriaPaciente` | estado-derivado | Modelo OPM SD1.5 | mejorando / estable / deteriorándose |
| `DecisionContinuidad` | decisión | Modelo OPM SD1.5 | continuar_tratamiento / proceder_egreso |
| `ResumenClinicoDomiciliario` | artefacto | Visita médica | Registro de cada visita médica |
| `RegistroTelesalud` | artefacto | Regulación a distancia | Registro de atención remota |
| `FichaClinica` | artefacto-continuo | Manual REM | Instrumento central de registro clínico |

#### 3.1.4 Objetos de ingreso y egreso

| Objeto | Tipo | Estados | Descripción |
|--------|------|---------|-------------|
| `EstadoElegibilidad` | estado | pendiente → elegible / no_elegible | Resultado de evaluación de ingreso |
| `ConsentimientoInformado` | artefacto-estado | sin_firmar → aceptado / rechazado | **[v3]** Documento con estructura formal: identificación (paciente RUT + cuidador RUT + CESFAM + teléfonos), 6 cláusulas informativas, decisión binaria ACEPTO/RECHAZO, firma + parentesco. Establece constraints operativos del episodio (ver PE-12 a PE-15) |
| `FormularioIngreso` | artefacto | — | Registro administrativo de entrada |
| `InformeSocial` | artefacto | — | Evaluación socioeconómica |
| `CartaDerechosDeberes` | artefacto | — | Documento entregado al paciente |
| `Epicrisis` | artefacto | — | Documento de cierre. Generado en todo egreso |
| `EncuestaSatisfaccion` | artefacto | — | Evaluación post-egreso |
| `ProtocoloFallecimiento` | artefacto | — | Solo en egreso por fallecimiento |
| `DeclaracionRetiro` | artefacto | — | Solo en renuncia voluntaria |
| `CondicionExclusion` | restricción | ausente / presente | Coproducto de 5 causales |
| `EstadoHospitalizacion` | estado | postulado → elegible / no_elegible → activo → planificado → en_tratamiento → pre_egreso → egresado | Estado principal del episodio. `no_elegible` es estado terminal. Enum completo alineado con transiciones §5.2 y diagrama §5.3 |

#### 3.1.5 Objetos de contexto y clasificación

| Objeto | Tipo | Identidad | Descripción |
|--------|------|-----------|-------------|
| `Establecimiento` | entidad | código DEIS | Hospital, CESFAM u otro establecimiento de la red. Codominio de `derivado_de` |
| `CESFAM` | entidad (subtipo de Establecimiento) | código DEIS | Centro de salud familiar. Codominio de `pertenece_cesfam`, `enlace_aps`, `epicrisis_a_aps` |
| `RadioCobertura` | valor | distancia en km | Distancia del domicilio al hospital. Invariante: ≤20 km para HSC |
| `RolProfesional` | enum | — | `{medico, enfermera, tecnico_enfermeria, matrona, kinesiologo, psicologo, fonoaudiologo, trabajador_social, terapeuta_ocupacional}`. Codominio de `tipo_profesional` |
| `Profesional_APS` | entidad (subtipo de Profesional) | `rut_profesional` | Profesional del nivel primario que participa en derivaciones APS → HoDom. Subtipado: `Profesional_APS ↪ Profesional` (monomorfismo) |
| `GestoraEncargada` | entidad (subtipo de Profesional) | `rut_profesional` | Enfermera gestora que media entre servicio derivador y HoDom. Asigna y coordina el ingreso. Subtipado: `GestoraEncargada ↪ Profesional` |

#### 3.1.6 Objetos de recurso

| Objeto | Tipo | Invariantes |
|--------|------|-------------|
| `EquipamientoMedico` | recurso | Estado mantención vigente, autorización sanitaria autorizada |
| `VehiculoTransporte` | recurso | 3 móviles disponibles (dato HSC) |
| `InsumoClinico` | recurso-consumible | Se consume en cuidados de enfermería |
| `Medicamento` | recurso-consumible | Se consume en administración |
| `SistemaComunicacion` | recurso | Teléfono, sistema informático |
| `InfraestructuraAdministrativa` | recurso-agregado | Ver descomposición SD3 |
| `SistemaDocumental` | recurso-informático | Protocolos, manuales, procedimientos |

### 3.2 Morfismos fundamentales

```
-- Relaciones nucleares
pertenece_a     : EpisodioHD → Paciente              -- 1 episodio = 1 paciente. 1 paciente = N episodios
ocurre_en       : EpisodioHD → Domicilio              -- 1 episodio = 1 domicilio
asignado_a      : EpisodioHD → EquipoSalud            -- equipo responsable
tiene_plan      : EpisodioHD → PlanTerapeutico         -- plan terapéutico activo
tiene_pce       : EpisodioHD → PlanCuidadosEnfermeria  -- derivado del plan terapéutico
cuidador_de     : Cuidador → EpisodioHD               -- cuidador asociado
derivado_de     : EpisodioHD → Establecimiento         -- hospital/servicio derivador

-- Relaciones de visita
visita_de       : Visita → EpisodioHD                  -- cada visita pertenece a un episodio
realizada_por   : Visita → Profesional                 -- profesional que ejecuta
genera_registro : Visita → RegistroClinico             -- cada visita produce un registro tipado (supertipo de RegistroEnfermeria, IngresoKinesiologia, RegistroCuraciones, ResumenClinicoDomiciliario, RegistroCicloVital)

-- Relaciones de equipo
rol_en          : Profesional → EquipoSalud            -- composición del equipo
tipo_profesional: Profesional → RolProfesional         -- enum de rol

-- Relaciones de domicilio
reside_en       : Paciente → Domicilio                 -- domicilio del paciente
en_radio        : Domicilio → RadioCobertura           -- ≤20 km del hospital (invariante HSC)
pertenece_cesfam: Domicilio → CESFAM                   -- enlace con APS

-- Relaciones de formulario clínico
tiene_reg_enf   : Visita → RegistroEnfermeria          -- cuando visita es de enfermería
tiene_reg_kine  : Visita → IngresoKinesiologia         -- cuando visita es de kinesiología (ingreso)
tiene_reg_cur   : Visita → RegistroCuraciones          -- cuando visita incluye curación
tiene_sv        : Visita → RegistroCicloVital           -- en toda visita clínica (ver §4.3 ObservacionCicloVital)

-- Relaciones de derivación inter-nivel
enlace_aps      : CESFAM → EpisodioHD                  -- derivación desde APS (programa postrados)
informe_medico  : Profesional_APS → EpisodioHD         -- informe médico resumido de derivación
epicrisis_a_aps : EpisodioHD → CESFAM                  -- contrarreferencia al egreso
```

### 3.3 Composiciones relevantes

```
-- Observar al paciente: tiene_sv⁻¹ (registro → visita), luego visita_de (visita → episodio), luego pertenece_a (episodio → paciente)
observar_paciente = pertenece_a ∘ visita_de ∘ tiene_sv⁻¹

-- Plan del paciente: vía episodio activo
plan_del_paciente = tiene_plan ∘ (pertenece_a⁻¹ |_{estado=activo})

-- Registro clínico completo del episodio: unión de todos los registros de visitas
historia_clinica(e) = ⋃{genera_registro(v) | v ∈ visita_de⁻¹(e)}

-- Continuidad APS: derivación → episodio → egreso → contrarreferencia
flujo_aps = epicrisis_a_aps ∘ egresar ∘ ingresar ∘ enlace_aps

-- Visitas por profesional para REM: 
visitas_por_tipo(e) = {(tipo_profesional(realizada_por(v)), count) | v ∈ visita_de⁻¹(e)}
```

### 3.4 Path Equations (restricciones conmutativas)

**PE-1: Consistencia domicilio**
```
ocurre_en(e) = reside_en(pertenece_a(e)) ∨ ocurre_en(e) = domicilio_cuidador(cuidador_de⁻¹(e))
-- El domicilio del episodio coincide con el domicilio del paciente o, excepcionalmente,
-- con el del cuidador (familiar responsable). El caso habitual es igualdad estricta.
-- NOTA [v4.1]: no hay evidencia empírica HSC de episodios en domicilio de terceros,
-- pero la estructura lo permite por diseño del CI (firma cuidador con dirección propia).
```

**PE-2: Consistencia temporal**
```
estado(e) = EGRESADO ⟹ fecha_egreso(e) ≥ fecha_ingreso(e)
estado(e) = ACTIVO ⟹ fecha_egreso(e) = null
dias_estada(e) = fecha_egreso(e) - fecha_ingreso(e)
-- Fuente: constraint del esquema operacional + definición REM 2026
```

**PE-3: Derivación del plan de enfermería**
```
tiene_pce(e) = derivar_pce(tiene_plan(e))
-- El PCE se construye a partir del plan terapéutico, no independientemente (SD1.3)
```

**PE-4: Visita dentro del episodio**
```
∀ v ∈ visita_de⁻¹(e): fecha(v) ∈ [fecha_ingreso(e), fecha_egreso(e) ∨ hoy]
```

**PE-5: Radio de cobertura (invariante HSC)**
```
en_radio(ocurre_en(e)) ≤ 20 km
-- El domicilio debe estar dentro del radio de 20 km desde el hospital
```

**PE-6: Congruencia de identidad del paciente**
```
edad(p, e) = floor((fecha_ingreso(e) - fecha_nacimiento(p)) / 365.25)
-- Edad calculada al momento del ingreso, con ajuste de cumpleaños.
-- Fuente: constraint del esquema + dato de migración: 71 correcciones rut/fecha_nacimiento invertidos
```

**PE-7: Previsión Fonasa o PRAIS**
```
prevision(pertenece_a(e)) ∈ {FONASA_A, FONASA_B, FONASA_C, FONASA_D, PRAIS}
-- Criterio de ingreso explícito del HSC (presentación enlace APS)
```

**PE-8: Consistencia REM personas atendidas**
```
personas_atendidas_mes(m) = personas_activas_mes_anterior(m-1) + ingresos(m) - egresos(m) - fallecidos(m)
-- Definición operacional REM 2026: "incluye pacientes traspasados del mes anterior y los ingresos del mes actual"
```

**PE-9: Consistencia REM origen derivación**
```
∀ componente: sum(origen_derivacion) = total_por_rango_etario
-- Regla de consistencia R.1 del REM A21 C.1.1
```

**PE-10: Consistencia REM cupos**
```
cupos_utilizados ≤ cupos_programados
cupos_disponibles = cupos_programados - cupos_utilizados
-- Reglas R.1 y R.2 del REM A21 C.1.3
```

**PE-11: Cierre de ficha clínica**
```
estado(e) = EGRESADO ⟹ ficha_clinica(e).cerrada = true
-- Principio de registro clínico REM 2026: "fichas no cerradas impiden extracción estadística"
```

**PE-12: Cobertura temporal (constraint del CI 2026)** [v3]
```
∀ v ∈ visita_de⁻¹(e): hora(v) ∈ [08:00, 19:00]
-- CI 2026: "un equipo de salud lo visitará de lunes a domingo en horario diurno 
-- (entre las 08:00 horas a 19:00 horas)"
-- CORRECCIÓN v3: El proyecto decía L-V. El CI dice L-D. 
-- Los enfermeros en cuarto turno cubren L-D. Los médicos diurnos solo L-V.
-- Contradicción entre fuentes resuelta por el CI como documento legal vinculante.
-- NOTA: La cobertura L-D es del sistema (al menos enfermería y kine visitan),
-- no de cada profesional individual. Médico y fono solo L-V (ver §6.2).
```

**PE-13: Estadía máxima (constraint del CI 2026)** [v3]
```
dias_estada(e) ≤ 8
-- CI 2026: "la estadía máxima en Hospitalización Domiciliaria es por 6 a 8 días"
-- NOTA: El promedio empírico HSC es 8 días. El CI establece 6-8 como máximo.
-- Si dias_estada > 8: requiere derivación a CESFAM o ambulatorio.
-- Contradicción: dato empírico 2023 muestra dias_persona/personas = 4037/307 = 13.1 días promedio.
-- Esto indica que PE-13 no se cumple estrictamente en la práctica.
```

**PE-14: Protocolo de emergencia fuera de horario (constraint del CI 2026)** [v3]
```
emergencia(e) ∧ hora ∉ [08:00, 17:00] L-J ∨ [08:00, 16:00] V ⟹ 
  acudir(SAPU) ∨ acudir(UEH) ∨ llamar(SAMU_131)
-- CI 2026: "En caso de complicaciones, solicitar orientación al teléfono 42 2586292 
-- en horario hábil L-J 08-17, V 08-16. Si riesgo: SAPU, UEH o SAMU 131."
-- Implicancia: existe una ventana sin cobertura (19:00-08:00 y fines de semana para consulta).
-- Las visitas son L-D 08:00-19:00, pero la línea de consulta es solo L-V horario hábil.
```

**PE-15: Barthel pareado ingreso-egreso** [v3]
```
barthel_ingreso(e) ∈ [0..100] ∧ barthel_egreso(e) ∈ [0..100]
-- Hoja Ingreso Enfermería: campos "PTJE. INGRESO" y "PTJE. EGRESO"
-- El Barthel se captura obligatoriamente al inicio Y al final del episodio.
-- Esto define una observación pareada: Δ_barthel = barthel_egreso - barthel_ingreso
-- Δ_barthel > 0 indica mejoría funcional del episodio.
```

**PE-16: Postulación precede episodio** [v3]
```
∀ e ∈ EpisodioHD: ∃ p ∈ Postulacion: p.nro = nro_postulacion(e) ∧ fecha(p) ≤ fecha_ingreso(e)
-- La postulación es un objeto formal que existe antes del episodio.
-- El checklist de ingreso (IngresoEnfermeria) está indexado por nro_postulacion.
```

---

## 4. Construcciones Universales

### 4.1 Wide Pullback: Elegibilidad

La elegibilidad para ingreso a HoDom es un **wide pullback** (límite de un diagrama con 8 flechas convergentes) — el episodio solo se instancia si convergen simultáneamente todas las precondiciones:

```
Elegibilidad = eq(cond_clinica, cuidador, cond_domicilio, consentimiento, 
                  no_exclusion, prevision, radio_cobertura, mayor_18)

donde:
  cond_clinica       : Paciente → {agudo_reagudizado, recuperado}    -- debe ser agudo/reagudizado
  cuidador           : Domicilio → {disponible, no_disponible}       -- debe ser disponible
  cond_domicilio     : Domicilio → {adecuada, inadecuada}            -- debe ser adecuada
  consentimiento     : Paciente → {firmado, sin_firmar}              -- debe ser firmado
  no_exclusion       : Paciente → {ausente, presente}                -- debe ser ausente
  prevision          : Paciente → Prevision                          -- debe ser Fonasa o PRAIS
  radio_cobertura    : Domicilio → {cumple, no_cumple}               -- debe cumplir (≤20 km)
  mayor_18           : Paciente → Bool                               -- debe ser verdadero
```

El wide pullback `E ↪ Paciente × Domicilio` selecciona exactamente los pares donde las ocho condiciones convergen al valor requerido. Solo sobre este subobjeto se puede construir el morfismo `ingresar: E → EpisodioHD`.

**Criterios de ingreso confirmados por fuentes HSC:**
- Mayor de 18 años (presentación enlace APS)
- Previsión Fonasa o PRAIS (presentación enlace APS)
- Familiar o cuidador responsable (presentación enlace APS)
- Condiciones sanitarias básicas (presentación enlace APS)
- Radio de 20 km (proyecto implementación + presentación)

**Condiciones de exclusión como coproducto negado (SD8):**
```
CondicionExclusion = InestabilidadClinica + DiagnosticoNoEstablecido 
                   + SaludMentalDescompensada + PrestacionNoListada 
                   + AltaDisciplinariaPrevia

no_exclusion = ¬(∃ componente presente en CondicionExclusion)
```

**Patologías elegibles confirmadas (proyecto HSC):**
- Pielonefritis aguda
- ITU multirresistente sin compromiso hemodinámico
- NAC o infecciones respiratorias IAAS sin insuficiencia respiratoria aguda
- Celulitis
- Patologías crónicas descompensadas: EPOC, Asma, LCFA, ICC
- Pacientes quirúrgicos estables con tratamientos EV, curaciones avanzadas, atención kinésica/fonoaudiológica
- Patologías cerebrovasculares
- TVP confirmada u otra que requiera ajuste anticoagulante
- Rehabilitación neurológica, motora, respiratoria, deglutoria

### 4.2 Coproducto: Motivo de Egreso

El egreso es un **coproducto** de cinco variantes mutuamente excluyentes, validado por dos fuentes independientes (modelo OPM SD1.6 + manual REM 2026):

```
MotivoEgreso = AltaMedica + ReingresoHospitalario + Fallecimiento 
             + RenunciaVoluntaria + AltaDisciplinaria

con inyecciones canónicas:
  ι₁ : AltaMedica           → MotivoEgreso
  ι₂ : ReingresoHospitalario → MotivoEgreso
  ι₃ : Fallecimiento         → MotivoEgreso
  ι₄ : RenunciaVoluntaria    → MotivoEgreso
  ι₅ : AltaDisciplinaria     → MotivoEgreso
```

**Refinamiento de Fallecimiento (nuevo, desde REM 2026):**

```
Fallecimiento = FallecidoEsperado + FallecidoNoEsperado

FallecidoEsperado: "paciente ingresa a HoDom con objetivo de fallecer en domicilio 
                    favoreciendo el vínculo con su entorno familiar"
FallecidoNoEsperado: "paciente ingresa con objetivo de cumplir plan terapéutico 
                      que favorezca su recuperación; fallece de forma inesperada"
```

**Nota empírica HSC:** En los 3 años de operación, cero fallecidos no esperados. Todos los fallecimientos han sido de tipo esperado (cuidados paliativos domiciliarios).

**Tabla de precondiciones, artefactos y agentes por variante:**

| Variante | Precondición | Genera | Agente | Definición REM 2026 |
|----------|-------------|--------|--------|---------------------|
| AltaMedica | cond_clinica = recuperado | Epicrisis | MédicoAD | "completan plan terapéutico (alta clínica y administrativa)" |
| ReingresoHospitalario | inestabilidad_clinica = presente | Epicrisis | MédicoAD | "por condición de salud inesperada o no programada debe reingresar a cama de dotación" |
| FallecidoEsperado | — | Epicrisis + ProtocoloFallecimiento | MédicoAD | "ingresa con objetivo de fallecer en domicilio" |
| FallecidoNoEsperado | — | Epicrisis + ProtocoloFallecimiento | MédicoAD | "fallece de forma inesperada" |
| RenunciaVoluntaria | consentimiento | Epicrisis + DeclaracionRetiro | — | No definido explícitamente en REM |
| AltaDisciplinaria | adherencia = no_adherente | Epicrisis | DirectorTécnico | "alta disciplinaria, según lo señalado en la Orientación Técnica" |

**Propiedad universal:** todo morfismo que salga de un egreso se factoriza a través del coproducto — no existen egresos fuera de estas variantes. El REM confirma: "no se considera un Egreso Hospitalario porque no hace uso de una cama de dotación."

### 4.3 Producto: Observación Clínica por Visita (Registro Ciclo Vital)

**[v3] CORRECCIÓN MAYOR.** El producto de signos vitales del modelo v2 era incompleto. El formulario real "Registro Visita Equipo HODOM" (Ciclo Vital) revela 15 columnas: 12 variables clínicas + 3 metadatos (Fecha, Observaciones_Visita, Responsable). El producto modela las 12 variables clínicas:

```
ObservacionCicloVital = PA × FC × FR × Temperatura × SaturacionO2 × HGT × EVA 
                      × Glasgow × Edema × Diuresis × Deposiciones × EstadoInvasivos

con proyecciones:
  π_PA       : OCV → PresionArterial          -- hemodinámico
  π_FC       : OCV → FrecuenciaCardiaca        -- hemodinámico
  π_FR       : OCV → FrecuenciaRespiratoria    -- respiratorio
  π_Temp     : OCV → Temperatura               -- [v3] NO estaba en modelo OPM ni en v2
  π_SpO2     : OCV → SaturacionOxigeno         -- respiratorio
  π_HGT      : OCV → Hemoglucotest             -- [v3] metabólico. NO en modelo OPM
  π_EVA      : OCV → EscalaVisualAnalogica     -- [v3] dolor. NO en modelo OPM
  π_Glasgow  : OCV → EscalaGlasgow             -- [v3] neurológico. NO en modelo OPM
  π_Edema    : OCV → EstadoEdema               -- [v3] NO en modelo OPM
  π_Diuresis : OCV → VolumenDiuresis           -- [v3] renal/hídrico. NO en modelo OPM
  π_Deposiciones : OCV → EstadoDeposiciones    -- [v3] gastrointestinal. NO en modelo OPM
  π_Invasivos: OCV → EstadoDispInvasivos       -- [v3] seguimiento de dispositivos
```

**Dimensiones de monitoreo que emergen del formulario real:**

| Dimensión | Variables | En modelo OPM | En esquema operacional |
|-----------|-----------|---------------|----------------------|
| Hemodinámica | PA, FC | Sí (SD1.5) | No |
| Respiratoria | FR, SpO2 | Sí (SD1.5) | No |
| Térmica | T° | No | No |
| Metabólica | HGT | No | No |
| Dolor | EVA | No | No |
| Neurológica | Glasgow | No | No |
| Hídrica | Edema, Diuresis | No | No |
| Gastrointestinal | Deposiciones | No | No |
| Dispositivos | Invasivos | Parcial (enfermería) | No |

**Implicancia:** El modelo OPM solo modelaba 4 de las 12 variables que realmente se capturan. El esquema operacional no captura ninguna. La brecha entre la práctica clínica real y la representación formal es mucho mayor de lo que el modelo v2 estimaba.

**Producto reducido para kinesiología (se mantiene):**

```
SignosVitales_Kine = PA × FR × FC × SatO2 × LitrosO2
-- Fuente: Hoja Ingreso Kinesiología, campo "CSV"
-- Subproducto de ObservacionCicloVital (sin T°, HGT, EVA, Glasgow, etc.)
```

### 4.4 Pullback: Visita como encuentro

```
        Visita ────→ Profesional
          │              │
          ↓              ↓
      EpisodioHD ──→ EquipoSalud
```

La visita existe solo cuando el profesional pertenece al equipo que atiende el episodio. El pullback garantiza integridad referencial.

**Tipos de visita según profesional (confirmado por REM 2026 + datos HSC):**

| Profesional | Registra | Datos HSC | Año |
|-------------|----------|-----------|-----|
| Médico | Visita médica → ResumenClínicoDomiciliario | 1.280 visitas | 2024 |
| Enfermera | Registro Enfermería → RegistroEnfermeria | 4.688 visitas | 2024 |
| Kinesiólogo | Hoja Kinesiología → IngresoKinesiologia / seguimiento | 3.195 visitas | 2024 |
| Fonoaudiólogo | Evaluación deglutoria/habla | 1.279 visitas | 2024 |
| Trabajador Social | Informe Social | 1.120 visitas | 2024 |
| Técnico Enfermería | Apoyo enfermería → procedimientos | 422 visitas | 2025 |
| Matrona | — | No reportado en HSC |
| Psicólogo | — | No reportado en HSC |
| Terapeuta Ocupacional | — | No reportado en HSC |

**Nota:** El REM lista 9 tipos de profesional. HSC opera con 6 (incluyendo TENS desde 2025). La diferencia es pérdida de información en F_REM: HSC no tiene matronas, psicólogos ni terapeutas ocupacionales asignados a HoDom.

### 4.5 Pushout: Integración de fuentes

```
    C_compartido ────→ C_op
         │                │
         ↓                ↓
      C_rem  ─────────→ C_integrado
```

`C_compartido = {Paciente, Episodio, Egreso, Profesional, Domicilio, Establecimiento}`

El pushout identifica conceptos que aparecen en ambos lados:
- Un ingreso en C_op (registro individual) y un conteo en C_rem (agregado) son la misma realidad a diferente granularidad.
- Un profesional en C_op (individuo con RUT) y un tipo de profesional en C_rem (categoría de visita) son la misma entidad colapsada.

### 4.6 Limit: Registro de Enfermería como producto con secciones

El formulario real de enfermería del HSC tiene estructura de **producto con secciones dependientes:**

```
RegistroEnfermeria = NarrativaClinica × TablaMedicamentos × PlanEnfermeria × TablaInvasivos

TablaMedicamentos = List(Medicamento × DosisIndicada × Dilucion × Via × NroDosis)
PlanEnfermeria = List(Intervencion)
TablaInvasivos = List(TipoInvasivo × FechaInstalacion × CambioInvasivo × SignosInfeccion × Observaciones)
```

Cada sección es una proyección del registro total. El producto garantiza que toda visita de enfermería captura las cuatro secciones simultáneamente.

### 4.7 Limit: Ingreso Kinesiología como producto evaluativo

```
IngresoKinesiologia = Antecedentes × EstadoActual × EvaluacionMotora × EvaluacionRespiratoria 
                    × DependenciaKinesica × Objetivos × Indicacion

Antecedentes = Nombre × Edad × AntMorbidos × DiagnosticoMedico × FuncionalidadPrevia × CSV
EstadoActual = Conciencia × Barthel × TiempoReposo × Farmacos × Asistencias × SignosVitales
DependenciaKinesica = DependenciaMotora × DependenciaRespiratoria
```

**CSV (Control de Signos Vitales)** mencionado como campo en el formulario. Esto confirma la existencia de un subobjeto SignosVitales embebido en múltiples formularios.

---

## 5. Modelo Dinámico: Coalgebra del Episodio

### 5.1 El episodio como F-coalgebra

```
c : EstadoEpisodio → F(EstadoEpisodio)

donde F(U) = Observacion × (Accion → U)
```

**Tipo Accion (dominio de la función de transición):**

```
Accion = Derivar_APS + Evaluar_Elegibilidad + Ingresar + Planificar 
       + Ejecutar + Monitorear + Egresar

-- Coproducto de 7 variantes. Cada inyección tiene precondiciones que restringen 
-- su dominio efectivo (ver §5.2 para precondiciones de cada transición).
-- En un estado dado, solo un subconjunto de acciones es habilitado.
```

**Estado interno (carrier set U):**

```
EstadoEpisodio = EstadoHospitalizacion × CondicionClinica × EstadoPlanTerapeutico 
               × EstadoPCE × ConocimientoAutocuidado × DependenciaKinesica
               × EstadoInvasivos × EstadoHeridas × EstadoConciencia × EstadoPsiquico
               × EstadoNutritivo × NivelAutocuidado

donde:
  EstadoHospitalizacion    ∈ {postulado, elegible, no_elegible, activo, planificado, en_tratamiento, pre_egreso, egresado}    -- [v3] +postulado. [v4.1] +no_elegible (estado terminal). pre_egreso = DecisionContinuidad = proceder_egreso
  CondicionClinica         ∈ {agudo_reagudizado, recuperado}
  EstadoPlanTerapeutico    ∈ {borrador, activo, completado}
  EstadoPCE                ∈ {borrador, activo, completado}
  ConocimientoAutocuidado  ∈ {insuficiente, suficiente}
  DependenciaKinesica      ∈ {motora: Level, respiratoria: Level}
  EstadoInvasivos          ∈ {List(TipoInvasivo × EstadoInfeccion)}    -- [v3] TipoInvasivo ∈ {SNG,CVC,PICC,OSTOMIA,CUP,VVP}
  EstadoHeridas            ∈ {List(TipoLesion × GradoCuracion)}       -- [v3] TipoLesion ∈ {LPP,PIE_DIABETICO,HERIDA_OP,OTRA}
  EstadoConciencia         ∈ {consciente, orientado, vigil, desorientado, somnoliente, soporoso, coma}  -- [v3] del IngresoEnfermería
  EstadoPsiquico           ∈ {agitado, agresivo, angustiado, inquieto, tranquilo}                       -- [v3]
  EstadoNutritivo          ∈ {obeso, sobrepeso, eutrofico, enflaquecido}                                -- [v3]
  NivelAutocuidado         ∈ {autovalente, semidependiente, postrado}                                   -- [v3]
```

**Observaciones (lo expuesto externamente):**

```
Observacion = ObservacionCicloVital × CategoriaPaciente × DecisionContinuidad × Barthel

donde:
  ObservacionCicloVital ∈ PA × FC × FR × T° × SpO2 × HGT × EVA × Glasgow 
                        × Edema × Diuresis × Deposiciones × ObsDispInvasivos   -- [v3] 12 variables reales
  -- NOTA [v4.1]: ObsDispInvasivos es la proyección observable del estado interno EstadoInvasivos.
  -- El isomorfismo π_invasivos ≅ obs_invasivos se cumple: no hay información oculta en esta dimensión.
  -- Para las demás dimensiones del carrier, la observación es una proyección parcial (lossy).
  CategoriaPaciente     ∈ {mejorando, estable, deteriorandose}
  DecisionContinuidad   ∈ {continuar_tratamiento, proceder_egreso}
  Barthel               ∈ [0..100]    -- observación pareada ingreso/egreso (PE-15)
```

### 5.2 Transiciones como morfismos de acción

```
derivar_aps : EstadoProgPostrados → EstadoPreIngreso
    -- NUEVO: derivación desde APS (programa postrados)
    -- precondición: informe médico resumido del médico APS
    -- precondición: datos de dirección, familiar responsable, contacto
    -- canal: correo electrónico institucional

evaluar_elegibilidad : EstadoPreIngreso → EstadoElegible
    -- precondición: wide pullback de elegibilidad (8 condiciones)
    -- efecto: EstadoElegibilidad: pendiente → elegible
    -- efecto: RedApoyo: insuficiente → verificada
    -- efecto: CondicionDomicilio: inadecuada → adecuada
    -- agentes: MédicoAD (condición clínica), TrabajadorSocial (domicilio, red apoyo), 
    --          EnfermeroClínico (consentimiento)

ingresar : EstadoElegible → EstadoActivo
    -- precondición: consentimiento = firmado
    -- efecto: EstadoHospitalizacion := activo
    -- genera: FormularioIngreso, CartaDerechosDeberes, DocumentoIndicacionesCuidado
    -- genera: InformeSocial (diagnóstico social)
    -- agentes: PersonalAdministrativo (registro), TrabajadorSocial (diagnóstico social),
    --          EnfermeroClínico (documentación), ProfesionalCoordinador (coordinación derivador)

planificar : EstadoActivo → EstadoPlanificado
    -- efecto: PlanTerapeutico := borrador → activo
    -- efecto: PlanCuidadosEnfermeria := borrador → activo
    -- genera: ProgramaVisitas, RutaTransporte
    -- agentes: MédicoAD (plan terapéutico), EnfermeroClínico (PCE),
    --          ProfesionalCoordinador (visitas), PersonalAdministrativo (rutas)

ejecutar : EstadoPlanificado → EstadoEnTratamiento
    -- precondición: PlanTerapeutico = activo, PCE = activo
    -- acciones paralelas (confirmadas por RRHH proyecto HSC):
    --   visitas médicas (Médico 44hrs L-V)
    --   cuidados enfermería (4 enfermeros cuarto turno, 2 TENS cuarto turno)
    --   terapia kinesiológica (2 kinesiólogos cuarto turno + 1 diurno)
    --   administración medicamentos
    --   educación paciente/cuidador
    --   regulación a distancia (médico regulador - no en HSC actual)
    --   fonoaudiología (1 fonoaudiólogo diurno L-V)
    --   curaciones (enfermería)
    -- NUEVO: programa postrados APS continúa curaciones crónicas y cambios de invasivos

monitorear : EstadoEnTratamiento → EstadoEnTratamiento | EstadoPreEgreso
    -- genera: SignosVitales, CategoriaPaciente, DecisionContinuidad
    -- actualiza: FichaClinica
    -- si DecisionContinuidad = continuar_tratamiento: loop (promedio 8 días)
    -- si DecisionContinuidad = proceder_egreso: transición

egresar : EstadoPreEgreso → EstadoFinal
    -- efecto: EstadoHospitalizacion := egresado
    -- efecto: PlanTerapeutico := completado
    -- efecto: PCE := completado
    -- genera: Epicrisis (siempre) + artefactos según variante del coproducto
    -- genera: EncuestaSatisfaccion
    -- NUEVO: epicrisis se envía a CESFAM de origen (contrarreferencia)
```

### 5.3 Diagrama de estado

```
[Postulado] ──→ [Elegible] ──→ [Activo] ──→ [Planificado] ──→ [En Tratamiento]
     │                                                               │    ↑
     ↓                                                               │    │
[No Elegible]                                                        └────┘
                                                                   monitorear
                                                                 (loop ~8 días)
                                                                      │
                                                                      ↓
                                                              [Pre-Egreso] ──→ [Egresado]
                                                                                    │
                                                                                    ↓
                                                                          [Seguimiento Post-Egreso]
                                                                          (llamadas, contrarreferencia)
                                                                          Estado terminal extendido.
                                                                          No genera nuevas transiciones
                                                                          clínicas — solo observaciones
                                                                          de seguimiento (§16.12).
```

**Estados terminales:** `No Elegible` y `Egresado` son terminales respecto a transiciones clínicas. `Egresado` admite un subestado extendido de seguimiento post-egreso (llamadas telefónicas, contrarreferencia APS) que no modifica el episodio pero genera actividad registrable (ver §16.12).

**Nota sobre la entrada al flujo:** El estado `Postulado` absorbe tanto la derivación desde APS (programa postrados) como la postulación directa desde servicios hospitalarios (formulario Google §16.2). La evaluación de elegibilidad (wide pullback §4.1) es el gate que transiciona a `Elegible` o termina en `No Elegible`.

**Nuevo estado "Derivación APS":** incorporado desde el protocolo de enlace con programa de postrados. No estaba en el modelo v1.

### 5.4 Equivalencia observacional de episodios

Dos episodios `e₁`, `e₂` son **bisimilares** si existe una relación `R` tal que `(e₁, e₂) ∈ R` y para toda acción `a ∈ Accion`: si `e₁` puede transicionar vía `a` a `e₁'` produciendo observación `o`, entonces `e₂` puede transicionar vía `a` a algún `e₂'` produciendo la misma observación `o`, con `(e₁', e₂') ∈ R` — y simétricamente. Esto es más fuerte que equivalencia de traza (mismas secuencias de observaciones), porque exige matching paso a paso.

La bisimilaridad es relevante para la equivalencia entre perfiles de episodios: dos episodios con distinta composición de equipo o domicilio son bisimilares si todo paso de monitoreo de uno puede ser igualado por el otro, preservando observaciones y acciones habilitadas.

**Evidencia observacional HSC (no bisimulación formal):** La tasa de reingreso ≈3-4% y cero fallecidos no esperados sugieren **equivalencia observacional de outcomes** entre episodios HoDom HSC y hospitalizaciones cerradas para el perfil de patologías atendidas. Esta es una comparación estadística de resultados, no una bisimulación formal — requeriría matching paso a paso de transiciones para ser demostrada categóricamente. Sin embargo, la evidencia es suficiente para sostener la tesis clínica del modelo.

---

## 6. Categoría de Agentes y Roles

### 6.1 Equipo de Salud — estructura real HSC

Confirmado por el proyecto de implementación (tabla RRHH):

```
EquipoSalud_HSC = MedicoGeneral_44hrs × MedicoGeneral_22hrs × EnfermeraCoordinadora 
                × TrabajadoraSocial × Fonoaudiologa × Conductores(4_cuarto_turno + 1_diurno)
                × Administrativo × Enfermeros(4_cuarto_turno) × TENS(2_cuarto_turno)
                × Kinesiologos(2_cuarto_turno + 1_diurno)
```

**Diferencia con modelo OPM (SD2):** El modelo OPM incluye roles que HSC no tiene actualmente:
- Director Técnico: existe a nivel del hospital pero no dedicado a HoDom
- Profesional Coordinador: rol cubierto por la Enfermera Coordinadora
- Médico Regulador: no presente en HSC (no hay regulación a distancia formal)
- Kinesiólogo, Trabajador Social, Personal Administrativo: confirmados

**Costo operacional anual:** CLP $344.518.110 (dato proyecto BIP 40059567-0)

### 6.2 Cobertura temporal

| Tipo | Jornada | Cobertura |
|------|---------|-----------|
| Diurno (médico, enfermera coord., kine, TS, fono, conductor, admin) | 44 hrs L-V | 08:00-17:00 L-V |
| Cuarto turno (enfermeros, TENS, kinesiólogos, conductores) | 08:00-20:00 | Largo-largo-libre-libre (L-D). **Nota [v4.1]:** la ventana 19:00-20:00 se destina a retorno a base, documentación y cierre de turno — no se programan visitas en ese bloque (PE-12 establece visitas hasta 19:00) |

**[v3] Contradicción entre fuentes resuelta:**
- El **proyecto de implementación** dice cobertura L-V para diurnos.
- El **CI 2026** dice visitas "de lunes a domingo en horario diurno (08:00 a 19:00)".
- El **cuarto turno** cubre L-D con rotación largo-largo-libre-libre.

**Resolución:** El CI es el documento legal vinculante con el paciente. La cobertura real de visitas es **L-D 08:00-19:00** (por cuarto turno). Los profesionales diurnos (médico, TS, fono) solo cubren L-V. Los fines de semana la atención es reducida a enfermería, TENS, kinesiólogos y conductores en cuarto turno.

**Implicancia coalgebraica:** El sistema HoDom HSC opera en dos modos:
- **Modo L-V** (equipo completo): todas las transiciones posibles.
- **Modo fin de semana** (cuarto turno): solo monitoreo, administración de medicamentos y cuidados de enfermería. No se pueden ejecutar transiciones que requieran médico (evaluar elegibilidad, decidir continuidad, egresar por alta médica).

Esto define un **autómata con restricción temporal**: el conjunto de acciones disponibles depende del día de la semana.

### 6.3 Enlace con APS — nuevo actor

```
Profesional_APS ↪ Profesional    -- subtipo (monomorfismo). Ver §3.1.5. Médico del programa postrados del CESFAM
Enfermera_Coord_HODOM ↪ Profesional    -- Melissa Sepúlveda (dato HSC)
Medico_Gestor_HODOM ↪ Profesional    -- Luis Mera Saltos (dato HSC)

enlace_protocolo:
  1. Programa Postrados identifica descompensación/enfermedad aguda
  2. Médico APS elabora informe médico resumido
  3. Envío a HODOM por correo institucional + datos (dirección, familiar, contacto)
  4. Contacto enfermera coordinadora HODOM ↔ enfermera programa postrados
  5. Médico HODOM evalúa caso → acepta/rechaza
  6. Si acepta: tratamiento comienza al día siguiente
  7. Verificar disponibilidad de cupo (≤20 cupos)
  
  Distribución de responsabilidad durante episodio:
  - HODOM: administración tratamiento, evaluación médica, exámenes, radiografías
  - Programa Postrados APS: continúa curaciones crónicas y cambios de invasivos
  
  Al egreso: epicrisis médica enviada por vía formal a APS
```

Esta distribución de responsabilidad es un **coproducto de responsabilidades** sobre el mismo paciente: HoDom y APS actúan en paralelo sobre dominios disjuntos.

---

## 7. Funtor de Observación F_REM: C_op → C_rem

### 7.1 Definición formal

```
F_REM : C_op → C_rem
```

Construido desde las definiciones conceptuales y operacionales oficiales del Manual REM 2026.

**Sobre objetos — C.1.1 Personas Atendidas:**

| C_op | C_rem componente | Transformación | Definición REM 2026 |
|------|-----------------|----------------|---------------------|
| EpisodioHD ingresado en mes | ingresos | count por dimensión | "número de pacientes que ingresan al Programa en el período (mes)" |
| EpisodioHD activo en mes (traspasos + ingresos) | personas_atendidas | count distintos | "total de pacientes atendidos. Incluye traspasados del mes anterior y los ingresos del mes actual" |
| sum(dias_estada por paciente en mes) | dias_persona | sum | "total de días de HD por cada paciente atendido en el período" |
| EpisodioHD con alta médica o disciplinaria | altas | count | "número de personas que egresan: completan plan terapéutico o alta disciplinaria" |
| EpisodioHD con fallecimiento esperado | fallecidos_esperados | count | "ingresa con objetivo de fallecer en domicilio" |
| EpisodioHD con fallecimiento no esperado | fallecidos_no_esperados | count | "fallece de forma inesperada" |
| EpisodioHD con reingreso | reingresos_hospitalizacion | count | "por condición de salud inesperada debe reingresar a cama de dotación" |

**Sobre objetos — C.1.2 Visitas Realizadas:**

| C_op | C_rem | Transformación |
|------|-------|----------------|
| Visita por tipo profesional | RegistroVisitas | count por enum profesional |

**Sobre objetos — C.1.3 Cupos:**

| C_op | C_rem componente | Definición REM 2026 |
|------|-----------------|---------------------|
| Capacidad instalada diaria | cupos_programados | "número de personas que pueden ser atendidas en domicilio en forma diaria (oferta)" |
| Pacientes atendidos en mes | cupos_utilizados | "uso de la capacidad instalada" |
| Cupos diarios no ocupados (sum mensual) | cupos_disponibles | "sumatoria mensual de cupos diarios disponibles" |

**Desagregación de cupos (confirmada REM 2026):**
- Total cupos
- Cupos campaña invierno adicionales
- Cupos campaña invierno
- Cupos pediátricos (hasta 17 años 11 meses 29 días)
- Cupos adultos (18+ años)
- Cupos salud mental

**Sobre morfismos — dimensiones de desagregación:**

```
F_REM(pertenece_a ∘ edad)     → rango_etario: {<15, 15_19, >=20}
    -- Manual REM 2026 define 3 rangos para C.1.1: "menores de 15, 15 a 19, 20 y más".
    -- NOTA HISTÓRICA: especificaciones previas usaban 4 rangos (<15, 15_19, 20_59, ≥60). Corregido en v4.1.

F_REM(pertenece_a ∘ sexo)     → sexo: {masculino, femenino}

F_REM(derivado_de)            → origen_derivacion: {APS, urgencia, hospitalizacion, 
                                 ambulatorio, ley_urgencia, UGCC}
    -- REM 2026 precisa: APS, Unidad de Emergencia Hospitalaria, 
    --   Áreas de hospitalización, Ambulatorio (CDT, hospital de día),
    --   Ley de Urgencia, UGCC

F_REM(realizada_por ∘ rol_en) → tipo_profesional ∈ {medico, enfermera, tecnico_enfermeria,
                                 matrona, kinesiologo, psicologo, fonoaudiologo, 
                                 trabajador_social, terapeuta_ocupacional}
```

### 7.2 Functor Information Loss — declaración exhaustiva

**FIL-1: Pérdida de cruce dimensional.**
Las dimensiones rango_etario, sexo y origen_derivacion son ortogonales y no se cruzan. No es posible recuperar "mujeres ≥60 derivadas de urgencia" desde C_rem.

**FIL-2: Pérdida de identidad individual.**
El funtor colapsa EpisodioHD a conteos — no hay morfismo inverso.

**FIL-3: Pérdida de temporalidad intra-mes.**
Eje temporal implícitamente mensual. Fecha exacta se pierde.

**FIL-4: Pérdida de identificador organizacional.**
El REM no porta un identificador explícito de establecimiento en la estructura de dato. Se asume por contexto de envío y código DEIS.

**FIL-5: Ambigüedad personas_atendidas vs ingresos.**
Un paciente con dos ingresos en el mes cuenta como 1 persona atendida y 2 ingresos. La convención operacional no está completamente formalizada en el REM.

**FIL-6: Invariante débil en totales.**
`total ≥ suma(sexo)` es desigualdad, no igualdad. Registros incompletos rompen conmutatividad exacta.

**FIL-7: Pérdida de patología/diagnóstico (NUEVO).**
El REM C.1 no registra diagnóstico ni CIE-10 del episodio. El esquema operacional tiene `diagnostico_egreso` como string libre. La información clínica se pierde completamente en el funtor.

**FIL-8: Pérdida del índice funcional (NUEVO).**
Barthel se captura en el esquema operacional y en el formulario de kinesiología, pero no tiene dimensión en el REM. La dependencia funcional del paciente se pierde.

**FIL-9: Pérdida de tipo de cupo (NUEVO).**
HSC opera con cupos indiferenciados (adulto general). El REM distingue cupos por campaña invierno, pediátricos, adultos y salud mental. Si HSC no diferencia, el reporte a DEIS es incompleto.

**FIL-10: Pérdida de la variable pueblos originarios y migrantes (NUEVO).**
El REM A21 C.2.3 (asistencia ventilatoria) incluye desagregación por pueblos originarios y migrantes. C.1 no la incluye explícitamente, pero el esquema operacional tiene `nacionalidad`. No hay mapeo formal entre nacionalidad y la variable migrante del REM.

### 7.3 Principios basales del registro estadístico (REM 2026)

El funtor F_REM opera bajo cuatro principios declarados por DEIS:

1. **Territorialidad:** La prestación se registra donde se realiza, con código DEIS.
2. **Normativo:** El dato debe cumplir definiciones conceptuales subyacentes.
3. **Temporalidad:** El registro ocurre en el período en que se produce la actividad.
4. **Calidad:** Los registros deben ser revisados regularmente para identificar errores.

Principio adicional: **Cierre de ficha clínica.** "Fichas no cerradas impiden extracción estadística." Esto significa que el funtor F_REM solo actúa sobre episodios con ficha cerrada — episodios sin cierre son invisibles para el REM.

---

## 8. Funtor F_proc: C_proc → C_op

### 8.1 Pérdida de información

**FPIL-1: Pérdida de paralelismo.**
OPM especifica ejecución paralela. El registro operacional aplana a secuencia temporal.

**FPIL-2: Pérdida del agente específico.**
OPM tipifica roles. El registro puede no capturar qué individuo ejecutó.

**FPIL-3: Colapso de granularidad.**
OPM tiene 6+ niveles de refinamiento. Esquema operacional: tabla plana.

**FPIL-4: Pérdida de cobertura temporal (NUEVO).**
OPM no modela restricción horaria. HSC opera 08:00-20:00 sin nocturna. Las transiciones nocturnas no existen en el sistema real.

**FPIL-5: Pérdida de distribución de responsabilidad APS-HoDom (NUEVO).**
El protocolo de enlace establece que APS mantiene curaciones crónicas y cambios de invasivos durante el episodio HoDom. El modelo OPM no captura esta concurrencia inter-nivel. El esquema operacional tampoco: no hay campo que registre qué parte de la atención la hace APS vs HoDom.

---

## 9. Categoría de Migración C_migr

### 9.1 Datos reales del pipeline

La migración procesó 30 archivos CSV fuente con los siguientes resultados:

```
Filas válidas leídas:           2998
Episodios deduplicados:         1698
Filas descartadas por duplicado: 1300
Pacientes deduplicados:         1231
```

### 9.2 Estrategias de identidad del paciente

El pipeline revela un problema categórico fundamental: **la identidad del paciente no es uniforme.**

```
patient_key_strategy ∈ {rut, nombre_fecha, nombre_contacto}

Distribución:
  rut:              1653 episodios (97.4%) — RUT válido por dígito verificador
  nombre_fecha:     39 episodios (2.3%)   — sin RUT válido, clave = nombre + fecha_nacimiento
  nombre_contacto:  6 episodios (0.3%)    — sin RUT válido ni fecha, clave = nombre + contacto
```

**Correcciones detectadas:**
- 71 episodios con RUT y fecha_nacimiento invertidos (swap)
- 40 episodios con RUT rechazado por validación

**Implicancia categórica:** La identidad `id(Paciente) = rut` no es completa. El 2.6% de los episodios requiere claves alternativas. Esto significa que la inyección `Paciente ↪ Set` (por RUT) tiene un kernel no trivial — hay pacientes que no se pueden identificar unívocamente por la clave canónica.

### 9.3 Esquema PostgreSQL generado

El pipeline generó un DDL con tablas staging:
- `hodom_pacientes_staging`: dimensión de pacientes
- `hodom_episodios_staging`: tabla de episodios normalizada

Esta estructura ya implementa la separación Paciente/Episodio que el esquema operacional original no tenía.

---

## 10. Estructura de Formularios Clínicos C_form

### 10.1 Hoja de Ingreso Enfermería HODOM HSC

**El formulario de admisión más rico del dominio.** Estructura formal:

```
IngresoEnfermeria {
  -- CABECERA
  nro_postulacion: Int                    -- FK a Postulacion. Identifica el pre-ingreso
  fecha_ingreso_hodom: Date
  fecha_egreso_hodom: Date                -- se llena al egreso (observación pareada)
  fecha_visita_ingreso_domiciliaria: Date -- puede diferir de fecha_ingreso
  servicio_origen: String                 -- mapea a origen_derivacion_REM
  
  -- IDENTIFICACIÓN PACIENTE
  nombre: String
  rut: String
  direccion: String
  edad: Int
  alergias: String
  cesfam_inscrito: String                 -- FK a CESFAM → clave para contrarreferencia
  diagnostico_ingreso: String             -- diagnóstico al ingreso (no al egreso)
  barthel_ingreso: Int[0..100]
  barthel_egreso: Int[0..100]             -- OBSERVACIÓN PAREADA
  
  -- IDENTIFICACIÓN CUIDADOR
  nombre_familiar_responsable: String
  rut_familiar_responsable: String        -- [v3] El cuidador tiene RUT formal
  telefonos: List(String)
  
  -- CHECKLIST DE INGRESO (7 ítems booleanos)
  checklist: {
    firma_consentimiento: Si|No|NA        -- PE: debe ser Si
    bienvenida_educacion: Si|No|NA
    familiar_presente: Si|No|NA           -- PE: debe ser Si
    interconsultas_pendientes: Si|No|NA
    medicamentos_despachados: Si|No|NA
    portador_invasivos: Si|No|NA          -- si Si: especificar tipo
    tipo_invasivos: String                -- SNG, CVC, PICC LINE, OSTOMIAS, CUP, VVP, etc.
    lesiones_piel: Si|No|NA
    tipo_lesion: LPP|PIE_DIABETICO|HERIDA_OP|OTRA
  }
  
  -- TRATAMIENTOS ACTIVOS
  tratamientos: List {
    dia: Date
    dosis: String
    via: String
  }
  
  -- EXAMEN FÍSICO DE INGRESO (enums cerrados)
  examen_fisico: {
    estado_conciencia: Consciente|Orientado|Vigil|Desorientado|Somnoliente|Soporoso|Coma
    estado_psiquico: Agitado|Agresivo|Angustiado|Inquieto|Tranquilo
    lenguaje: Atingente_estructurado|Disartrico|Balbuceo|Afasico
    estado_piel: {color: String, hidratacion: String}
    estado_nutritivo: Obeso|Sobrepeso|Eutrofico|Enflaquecido
    autocuidado: Autovalente|Semidependiente|Postrado
  }
  
  -- HISTORIA CLÍNICA
  antecedentes_morbidos_quirurgicos: Text
  medicamentos_cronicos: Text
  historia_ingreso: Text
  valores_examenes: Text
  
  -- EXAMEN FÍSICO SEGMENTARIO (12 regiones)
  examen_segmentario: {
    cabeza: Text, cuello: Text, pupilas: Text, torax: Text,
    escleras: Text, abdomen: Text, oidos: Text, eess: Text,
    boca: Text, eeii: Text, dentadura: Text, genitales: Text
  }
  
  -- DIAGNÓSTICO Y PLAN
  diagnostico_enfermeria: String
  plan_atencion_enfermeria: Text
  profesional_responsable_ingreso: String    -- firma y timbre
  profesional_responsable_vd: String         -- firma y timbre
}
```

**Hallazgos categóricos [v3]:**

1. **Nro. Postulación** confirma la existencia de `Postulacion` como objeto formal pre-episodio. El morfismo `postulacion_de: EpisodioHD → Postulacion` ahora tiene evidencia documental.

2. **Examen físico con enums cerrados** — 6 dominios con valores discretos predefinidos. Esto es un **producto de enums**, no texto libre. Categóricamente más rico que lo que el modelo OPM captura.

3. **Barthel pareado** (ingreso + egreso en el mismo formulario) confirma PE-15. Permite medir el resultado del episodio como Δ_barthel.

4. **Checklist como testigo de verificación** — los 7 ítems del checklist son una verificación en el momento del ingreso de que el wide pullback de elegibilidad se cumplió. El checklist es el testigo documental del wide pullback.

5. **Tipo de invasivos** listados explícitamente: SNG, CVC, PICC LINE, OSTOMIAS, CUP, VVP. Esto define un enum cerrado de dispositivos invasivos que el modelo anterior tenía como string libre.

6. **Lesiones de piel tipadas**: LPP, PIE DIABÉTICO, HERIDA OP., OTRA. Otro enum que categoriza las lesiones que dan origen a los registros de curaciones.

### 10.2 Registro Visita Equipo HODOM (Ciclo Vital)

**La planilla real de monitoreo diario.** Una fila por visita:

```
RegistroCicloVital {
  nombre_paciente: String        -- cabecera del formulario
  registros: List {              -- una fila por visita/día
    fecha: Date
    pa: String                   -- presión arterial
    fc: Int                      -- frecuencia cardíaca
    fr: Int                      -- frecuencia respiratoria
    temperatura: Float           -- [v3] T° — NO en modelo OPM
    saturacion: Float            -- SAT%
    hgt: Float                   -- [v3] hemoglucotest — NO en modelo OPM
    eva: Int                     -- [v3] escala visual analógica dolor — NO en modelo OPM
    glasgow: Int                 -- [v3] escala de coma Glasgow — NO en modelo OPM
    edema: String                -- [v3] presencia/grado edema — NO en modelo OPM
    diuresis: String             -- [v3] volumen/características diuresis — NO en modelo OPM
    deposiciones: String         -- [v3] características deposiciones — NO en modelo OPM
    invasivos: String            -- estado de dispositivos invasivos
    observaciones_visita: Text   -- narrativa libre
    responsable: String          -- profesional que registra
  }
}
```

**Hallazgo crítico:** Este formulario es la fuente primaria de la serie temporal clínica del episodio. Cada fila es una observación que alimenta la coalgebra del episodio. El modelo OPM solo modelaba PA, FC, FR y SpO2 (4 de 12 variables). La realidad clínica captura T°, HGT, EVA, Glasgow, Edema, Diuresis y Deposiciones que son invisibles para el modelo formal.

### 10.3 Consentimiento Informado HODOM HSC 2026

```
ConsentimientoInformado_2026 {
  -- IDENTIFICACIÓN
  nombre_usuario: String
  cedula_identidad: String       -- RUT paciente
  cesfam: String
  nombre_cuidador: String
  cedula_cuidador: String        -- RUT cuidador
  telefonos: List(String)
  
  -- CLÁUSULAS INFORMATIVAS (6)
  clausula_1: "visitas L-D 08:00-19:00"           -- constraint PE-12
  clausula_2: "profesionales: Médico, Enfermera, TENS, Kinesiólogos, Fonoaudióloga"
              + "registros audiovisuales consentidos"
  clausula_3: "complicaciones → tel 42 2586292 L-J 08-17, V 08-16"
              + "riesgo → SAPU, UEH, SAMU 131"    -- constraint PE-14
  clausula_4: "estadía máxima 6-8 días"            -- constraint PE-13
  clausula_5: "post-alta: CESFAM o UEH ambulatoria"
  clausula_6: "EPP por COVID-19"                   -- vestigio pandemia. Candidata a eliminación en próxima revisión del CI
  
  -- DECISIÓN
  decision: ACEPTO | RECHAZO
  fecha: Date
  firma_usuario_o_cuidador: String
  relacion_parentesco: String
}
```

**Constraints operativos derivados del CI:**

| Constraint | Valor | Impacto en el modelo |
|------------|-------|---------------------|
| Cobertura visitas | L-D 08:00-19:00 | Corrige PE-12. Más amplio que L-V del proyecto |
| Estadía máxima | 6-8 días | PE-13. Pero dato empírico 2023 muestra ~13 días promedio |
| Línea de orientación | L-J 08-17, V 08-16 | Ventana sin cobertura de consulta: noches y fines de semana |
| Escalada emergencia | SAPU → UEH → SAMU 131 | Protocolo de seguridad fuera de horario |
| Registros audiovisuales | Consentidos | Habilitación legal para telesalud |
| Post-alta | CESFAM o UEH ambulatoria | Contrarreferencia obligatoria |

**Contradicción detectada [v3]:** El CI dice "estadía máxima 6-8 días". Los datos empíricos 2023 muestran un promedio de 13.1 días (4037 días-persona / 307 personas). En 2024: 6508/1077 = 6.0 días. En 2025: 5480/751 = 7.3 días. El constraint de 6-8 días se cumple en 2024-2025 pero no en 2023 (periodo inicial). Esto indica que la restricción se formalizó después de la experiencia de 2023.

### 10.4 Registro de Enfermería diario HODOM HSC

**Estructura real del formulario (de seguimiento, no de ingreso):**

```
RegistroEnfermeria {
  identificacion: Nombre × RUT
  temporal: Fecha × Hora
  narrativa: Text           -- descripción clínica libre (7 líneas)
  medicamentos: List {
    medicamento: String
    dosis_indicada: String
    dilucion: String
    via: String
    nro_dosis: Int
  }
  plan_enfermeria: List(String)    -- 9 items máximo en formulario
  invasivos: List {
    tipo: String
    fecha_instalacion: Date
    cambio_invasivo: String
    signos_infeccion: String       -- "(o flebitis)" — nota del formulario
    observaciones: String
  }
}
```

**Relación con IngresoEnfermería [v3]:** El Registro diario es el seguimiento; la Hoja de Ingreso es la evaluación inicial. El IngresoEnfermería se llena una vez por episodio. El RegistroEnfermería se llena en cada visita de enfermería. Son dos formularios distintos con relación 1:N dentro del mismo episodio.

### 10.5 Hoja de Ingreso Kinesiología HODOM HSC

```
IngresoKinesiologia {
  evaluador: String
  fecha: Date
  antecedentes: {
    nombre: String
    edad: Int
    ant_morbidos: Text
    diagnostico_medico: String
    funcionalidad_previa: String
    csv: SignosVitales          -- "Registro CSV: PA FR FC SAT O2 LTS"
  }
  estado_actual: {
    conciencia: String
    barthel: Int[0..100]
    tiempo_reposo: String
    farmacos: Text
    asistencias: Text
  }
  evaluacion: {
    motora: Text
    respiratoria: Text
  }
  dependencia_kinesica: {
    motora_ingreso: String
    respiratoria_ingreso: String
  }
  objetivos: Text
  indicacion: Text
  observaciones: Text
}
```

### 10.6 Registro de Curaciones

```
RegistroCuraciones {
  nombre_paciente: String
  tipo_curacion: String
  registros: List {
    fecha: Date
    lugar_grado: String
    exudacion_cantidad: String
    tipo_tejido: String
    caracteristicas_tamano: String
    aposito_primario: String
    aposito_secundario: String
    observaciones_responsable: String
  }
}
```

**Observación categórica:** El registro de curaciones no tiene RUT ni identificador de episodio. Solo nombre. Esto rompe la composición `RegistroCuraciones → Episodio → Paciente` — la FK al episodio debe ser inferida por nombre + contexto temporal.

---

## 11. Red Asistencial como Categoría de Contexto

### 11.1 Estructura de la red HSC

```
RedAsistencial_HSC = {
  Hospital_San_Carlos: Establecimiento(130 camas, complejidad media-alta)
  CESFAM: {
    San_Carlos_JDT: CESFAM
    San_Carlos_TB: CESFAM
    San_Fabian: CESFAM
    San_Gregorio: CESFAM    -- Ñiquén
    San_Nicolas: CESFAM
    Ninhue: CESFAM
    Quirihue: Consultorio_Adosado
    Cobquecura: CESFAM
    Trehuaco: CESFAM
    Nipas: CESFAM           -- Ránquil
  }
  Postas: [lista por comuna]
  EMR: [estaciones médicas rurales]
  CECOSF: {Valle_Hondo, Cachapoal}
}
```

### 11.2 Morfismos de derivación en la red

```
derivar_urgencia  : UEH_HSC → EpisodioHD
derivar_hosp      : ServicioClinico_HSC → EpisodioHD
derivar_aps       : CESFAM → EpisodioHD               -- protocolo enlace postrados
derivar_ambulatorio: CAE_HSC → EpisodioHD
derivar_ley_urg   : ExternoRedNuble → EpisodioHD      -- ley de urgencia (Parral, Talca, Chillán)
derivar_ugcc      : UGCC → EpisodioHD

contrarreferir    : EpisodioHD → CESFAM                -- epicrisis al egreso
```

**Nota empírica:** El proyecto HSC menciona usuarios de Parral (Región del Maule) y Chillán que consultan espontáneamente en urgencias. Estos pacientes pueden ser derivados a HoDom si su domicilio está dentro del radio de 20 km — lo cual es poco probable para los de Talca/Parral. Esto genera un caso límite del wide pullback de elegibilidad.

---

## 12. Gestión del Sistema como Endofunctores de Mantenimiento

Los procesos de gestión (SD6) no actúan directamente sobre episodios sino sobre las precondiciones estructurales:

```
GestionarAutorizacionSanitaria : EstadoAutorizacion pendiente → autorizado
    -- agente: DirectorTecnico + SEREMI
    -- invariante: si autorización vencida, wide pullback de elegibilidad falla globalmente

GestionarMantencionEquipos     : EstadoMantencion vencido → vigente
    -- agente: DirectorTecnico
    -- DATO HSC: equipamiento solicitado por $59.661.078 incluye:
    --   3 oxímetros Massimo Rad 5, 3 DEA, 10 colchones antiescaras,
    --   4 electroestimuladores, 4 pirómetros, 3 ECG portátil, 3 monitores multiparámetros

GestionarCapacitacion          : CumplimientoCapacitacion no_cumple → cumple
    -- plan anual: IAAS, SVB, inducción, humanización del cuidado

GestionarCadenaAbastecimiento  : nivel_insumos bajo → suficiente
    -- incluye: farmacia/botiquín autorizado, bodega de insumos

GestionarResiduos              : residuos sin procesar → procesados
    -- protocolo cortopunzantes, cumplimiento REAS
```

Estos son **endofunctores de mantenimiento** sobre C_op: no crean ni destruyen episodios, pero mantienen las invariantes del sistema. Si alguna falla, el sistema entero se degrada.

---

## 13. Mapeo Esquema Operacional → Modelo Categórico

### 13.1 Correspondencia campo → objeto/morfismo

| Campo esquema | Objeto categórico | Rol | Observación nueva |
|---------------|-------------------|-----|-------------------|
| id_registro | id(EpisodioHD) | identidad surrogate | — |
| estado | EstadoHospitalizacion | subestado coalgebraico | {ACTIVO, EGRESADO} |
| fecha_ingreso | timestamp(ingresar) | marca temporal | — |
| fecha_egreso | timestamp(egresar) | marca temporal | null si ACTIVO (PE-2) |
| dias_estada | distancia temporal | morfismo derivado | PE-2 |
| motivo_egreso | MotivoEgreso | inyección del coproducto | String libre → debe ser enum 5+1 |
| nombres, apellidos | atributos Paciente | — | — |
| sexo | atributo Paciente | dimensión REM | {M, F} |
| edad | atributo Paciente | dimensión REM | Clasificable a rango_etario |
| fecha_nacimiento | atributo Paciente | verificación PE-6 | 71 swaps detectados |
| rut | id(Paciente) | identidad natural | 97.4% válidos, 2.6% requiere clave alternativa |
| barthel | observación funcional | Barthel index | [0..100]. También en formulario kinesiología |
| prevision | atributo administrativo | PE-7 | Debe ser Fonasa/PRAIS |
| servicio_origen | derivado_de | morfismo derivación | Debe mapear a 6 categorías REM |
| usuario_o2 | necesidad clínica | atributo episodio | Vinculado a C.2 (asistencia ventilatoria) |
| requerimiento_hodom_o2 | necesidad clínica | atributo episodio | Vinculado a C.2 |
| categorizacion | CategoriaPaciente | estado derivado | — |
| diagnostico_egreso | atributo Epicrisis | artefacto egreso | String libre, debería ser CIE-10 |
| domicilio, comuna | id(Domicilio) | identidad natural | — |
| cesfam | referencia APS | morfismo a CESFAM | Clave para contrarreferencia |
| nro_contacto | canal comunicación | operacional | — |
| nacionalidad | atributo Paciente | potencial dim. REM | Sin mapeo formal a "migrante" |
| enfermeria, kinesiologia, fonoaudiologia | tipo visita requerida | booleano → subobjeto plan | Insuficiente: debería ser conteo, no booleano |

### 13.2 Déficits estructurales — actualización

| # | Déficit | Severidad | Impacto |
|---|---------|-----------|---------|
| D1 | Paciente y Episodio fundidos en una tabla | CRÍTICO | Viola separación de objetos. Pipeline de migración ya lo corrigió |
| D2 | Ausencia de entidad Visita | CRÍTICO | Impide construir F_REM para C.1.2 (visitas por profesional) |
| D3 | Ausencia de SignosVitales como entidad | ALTO | Se capturan en papel (formularios) pero no en el esquema |
| D4 | Motivo egreso como string libre | ALTO | No tipado como enum del coproducto 5+1 variantes |
| D5 | Sin timestamps de transiciones intermedias | MEDIO | Solo ingreso y egreso. Sin traza de elegibilidad, planificación |
| D6 | Sin FK al equipo/profesional asignado | ALTO | Impide construir el pullback de Visita |
| D7 | Sin registro de elegibilidad | MEDIO | Condiciones evaluadas no quedan persistidas |
| D8 | Sin tabla de cupos | ALTO | Impide generar C.1.3 del REM |
| D9 | Sin distinción fallecido esperado/no esperado | ALTO | REM 2026 lo exige. Esquema no lo tiene |
| D10 | Sin campo pueblos originarios | BAJO | No requerido para C.1 pero sí para C.2 |
| D11 | Formulario curaciones sin ID paciente/episodio | MEDIO | Rompe composición. Solo tiene nombre |
| D12 | Registro enfermería sin signos vitales estructurados | MEDIO | Se capturan en narrativa libre o en kinesiología |
| D13 | Sin campo rango_etario REM | BAJO | Derivable de edad, pero mapeo difiere: REM 2026 dice 3 rangos, no 4 |
| D14 | Sin mapeo servicio_origen → origen_derivacion_REM | ALTO | String libre sin correspondencia formal a las 6 categorías |
| D15 | Sin registro de enlace APS | NUEVO/ALTO | El protocolo postrados-HoDom no deja traza estructurada |
| D16 | **[v3]** Ciclo vital en papel — 12 variables clínicas sin digitalizar | CRÍTICO | T°, HGT, EVA, Glasgow, Edema, Diuresis, Deposiciones no existen en ningún esquema digital |
| D17 | **[v3]** Nro. Postulación sin FK en esquema | ALTO | El objeto Postulacion no tiene tabla ni campo en el esquema operacional |
| D18 | **[v3]** Examen físico de ingreso sin digitalizar | MEDIO | 6 dominios con enums cerrados que quedan solo en papel |
| D19 | **[v3]** Checklist de ingreso sin persistencia | MEDIO | El testigo documental del wide pullback de elegibilidad no se registra digitalmente |
| D20 | **[v3]** RUT del cuidador no registrado en esquema | MEDIO | El CI captura RUT cuidador + parentesco, pero el esquema no tiene campo |
| D21 | **[v3]** Constraint estadía máxima no enforced | ALTO | CI dice 6-8 días, datos 2023 muestran ~13 días promedio |
| D22 | **[v3]** Diagnóstico de ingreso vs egreso | MEDIO | IngresoEnfermería tiene "diagnóstico de ingreso", esquema solo tiene "diagnóstico de egreso". Son dos observaciones distintas del mismo episodio |

---

## 14. Riesgos y Tensiones No Resueltas

### 14.1 Tensión entidad vs evento en EpisodioHD

El episodio es simultáneamente entidad (tiene estado, duración) y evento compuesto (tiene inicio, acciones, fin). El esquema actual lo trata como entidad estática. Si se necesita trazabilidad de cada acción dentro del episodio, se requiere un event log.

**Recomendación:** Mantener EpisodioHD como entidad con event log adjunto. Las visitas y registros clínicos son el event log natural.

### 14.2 Tensión token vs type en Profesional

OPM tipifica roles. HSC tiene individuos concretos. Para el pullback de Visita se necesitan tokens. Esto ya está parcialmente resuelto en los formularios (campo "evaluador" en kinesiología, "responsable" en curaciones) pero no en el esquema de datos.

### 14.3 Riesgo de drift entre C_proc y C_op

El modelo OPM describe el proceso normativo. El esquema operacional registra lo que ocurre. Los datos empíricos HSC muestran drift específico:
- No hay médico regulador ni regulación a distancia formal
- No hay matronas, psicólogos ni terapeutas ocupacionales en el equipo
- No hay cobertura nocturna (el OPM no lo restringe)
- El enlace APS opera sin protocolo formal registrado en el sistema

### 14.4 Riesgo de pérdida en F_REM

**Mapeos no formalizados:**
- ¿Cómo se mapea `servicio_origen` del esquema a las 6 categorías del REM?
- ¿Cómo se cuentan cupos si no hay tabla de capacidad?
- ¿Cómo se distingue fallecido esperado de no esperado si el campo no existe?
- Los 3 rangos etarios del REM 2026 ("<15", "15-19", "20+") no coinciden con los 4 de la especificación previa ("<15", "15-19", "20-59", "≥60")

### 14.5 Riesgo de datos en papel vs digital

Los formularios clínicos (enfermería, kinesiología, curaciones) se llenan en papel. Estos datos no fluyen al esquema operacional digital. Esto significa que:
- Una parte significativa de la información clínica (medicamentos administrados, invasivos, curaciones, evaluación kinésica) no es consultable ni agregable.
- El funtor F_REM para visitas opera sobre conteos, pero la riqueza clínica se pierde.
- El esquema operacional es una proyección empobrecida no solo del modelo categórico sino de la propia práctica clínica.

### 14.6 Tensión cupos permanentes vs campaña (NUEVO)

HSC opera actualmente por compra de servicio/campaña de invierno, pero el proyecto BIP busca implementación permanente. Esto significa que el objeto `Cupos` tiene dos regímenes:
- Campaña: cupos temporales, financiamiento acotado
- Permanente: cupos fijos, financiamiento base

El REM distingue "cupos" de "cupos adicionales campaña invierno". Si HSC transiciona a permanente, los cupos dejan de ser "campaña" pero el REM sigue pidiendo esa desagregación.

---

## 15. Recomendaciones Estructurales

### 15.1 Esquema relacional normalizado (priorizado)

1. **Separar Paciente de EpisodioHD** (relación 1:N). El pipeline de migración ya lo hizo.
2. **Agregar tabla Visita** con FK a EpisodioHD y Profesional. Campos: fecha, hora, tipo_profesional, duracion.
3. **Agregar tabla RegistroClinico** polimórfica o tipada, hija de Visita. Subcategorías: enfermería, kinesiología, curación, médica.
4. **Tipar MotivoEgreso** como enum: `{alta_medica, reingreso_hospitalario, fallecido_esperado, fallecido_no_esperado, renuncia_voluntaria, alta_disciplinaria}`.
5. **Agregar tabla Elegibilidad** como checklist booleana por episodio.
6. **Agregar tabla Cupos** con campos: fecha, tipo_cupo, programados, utilizados.
7. **Crear catálogo OrigenDerivacion** mapeado a las 6 categorías REM.
8. **Agregar campo cesfam_referencia** para traza de enlace APS.
9. **Agregar SignosVitales** como tabla hija de Visita (PA, FC, FR, SpO2, LtsO2).

### 15.2 Digitalización de formularios

10. **Digitalizar Registro Ciclo Vital** como tabla de serie temporal: 12 columnas numéricas/categóricas por visita. Prioridad máxima — contiene las variables clínicas más ricas del dominio. [v3]
11. **Digitalizar IngresoEnfermería** como entidad de admisión: checklist (7 booleanos), examen físico (6 enums), Barthel pareado, Nro. Postulación como FK. [v3]
12. **Digitalizar Registro Enfermería diario** como entidad de seguimiento vinculada a Visita.
13. **Digitalizar Ingreso Kinesiología** con campos tipados (Barthel, dependencia, CSV).
14. **Agregar ID paciente/episodio a Registro Curaciones.**
15. **Crear tabla Postulación** como entidad pre-episodio con Nro. Postulación. [v3]
16. **Registrar RUT del cuidador** como campo en tabla Cuidador o en IngresoEnfermería. [v3]

### 15.3 Artefactos de integración

17. **Definir vistas SQL que implementen F_REM** como queries sobre C_op normalizado.
18. **Implementar PE-8, PE-9, PE-10 como constraints o validaciones** en la capa de datos.
19. **Crear tabla de mapeo servicio_origen → origen_derivacion_REM.**
20. **Implementar PE-13 (estadía máxima) como alerta**, no como constraint duro — la práctica real excede el CI en casos justificados. [v3]
21. **Registrar diagnóstico de ingreso** además del de egreso — son dos observaciones distintas del mismo episodio. [v3]

---

## 16. [v4] Refinamiento desde Registros Operacionales Legacy

### 16.1 Inventario de fuentes legacy procesadas

| Fuente | Tipo | Contenido | Filas/Sheets | Hallazgo principal |
|--------|------|-----------|-------------|-------------------|
| Formulario Postulación 2025 | Google Form → XLSX | Solicitudes de ingreso a HoDom | ~600+ filas | El ingreso real es vía formulario Google. La postulación es digital, no papel |
| Formulario Postulación 2026 | Google Form → XLSX | Solicitudes de ingreso 2026 | 141 filas (ene-mar 2026) | Schema evolucionó: +USUARIO_O2, +GESTORA_ENCARGADA, +EPICRISIS_CON_IND_MEDICA; −COVID, −AISLAMIENTO, −NRO_CASA |
| Canasta HODOM | Resolución Exenta | Catálogo oficial de prestaciones con código MAI | 24 prestaciones | Define el coproducto formal de servicios autorizados |
| Consolidado Atenciones Diarias | Agregado operacional | Conteo diario de visitas por tipo profesional | 368 días (2026-01-01 a 2027-01-03) | Serie temporal de producción. Fuente directa para F_REM C.1.2 |
| Entrega Turno Kinesiología | Planilla XLSX diaria | Estado de cada paciente desde kinesiología | 106 hojas (días) | Revela campos: COBERTURA {INGRESO/CONTROL/ALTA}, REGISTRO FC {KTR/KTM/R+M} |
| Entrega Turno Enfermería | Documentos Word | Handoff clínico entre turnos de enfermería | 3 muestras (sep-oct 2025, ene 2026) | La tabla más rica del dominio: 7 columnas clínicas por paciente + tabla de altas/ingresos |
| Cartera de Servicios HSC | Resolución Exenta N°1.206 | Cartera completa del hospital por servicio | 13 hojas (sin hoja HoDom dedicada) | HoDom no tiene hoja propia — opera bajo estructura de Atención Cerrada |

### 16.2 Objeto Postulación — estructura real confirmada

La postulación NO es un formulario en papel. Es un **Google Form** que alimenta una hoja de cálculo compartida. Esto es la fuente primaria de datos de ingreso al sistema.

```
Postulacion_2026 {
  timestamp: DateTime                         -- marca temporal del envío
  nombres: String
  apellidos: String
  rut: String                                 -- formato 9999999-9
  prevision: String                           -- FONASA (A/B/C/D) o PRAIS
  fecha_nacimiento: Date
  edad: Int
  sexo: {HOMBRE, MUJER}
  servicio_origen_solicitud: Enum             -- ver catálogo abajo
  diagnostico_egreso: String                  -- diagnóstico del servicio derivador
  direccion: String
  cesfam_inscrito: String                     -- FK a CESFAM
  celular: String
  prestacion_solicitada: String               -- texto libre con combinaciones
  epicrisis_con_indicacion_medica: URL        -- link a Google Drive
  gestora_encargada: String                   -- enfermera gestora asignada
  usuario_o2: Boolean                         -- [v4] campo nuevo 2026
}
```

**Catálogo real de servicios de origen (2026):**
```
ServicioOrigen ∈ {MEDICINA, CIRUGÍA, TMT (traumatología), UE (urgencia), 
                  UTI, CMI (cuidados medios), CAE, GINE, PEDIATRÍA, URA, OTRO}
```

Esto corrige el modelo anterior: los servicios reales de derivación son **internos al hospital**, no las 6 categorías del REM (APS, urgencia, hospitalización, ambulatorio, ley_urgencia, UGCC). El mapeo `servicio_origen → origen_derivacion_REM` requiere una tabla de conversión:

```
Mapeo servicio_origen → REM:
  UE          → urgencia
  MEDICINA    → hospitalizacion
  CIRUGÍA     → hospitalizacion
  TMT         → hospitalizacion
  UTI         → hospitalizacion
  CMI         → hospitalizacion
  CAE         → ambulatorio
  GINE        → hospitalizacion
  PEDIATRÍA   → hospitalizacion
  URA         → urgencia (?)
  OTRO        → requiere clasificación manual
  APS (si existe) → APS
```

**Evolución del schema 2025 → 2026:**

| Eliminado en 2026 | Agregado en 2026 | Renombrado |
|-------------------|-------------------|------------|
| COVID19? | USUARIO DE O2 | APELLIDO PATERNO+MATERNO → APELLIDOS |
| AISLAMIENTO? | EPICRISIS CON IND MÉDICA (URL) | NOMBRE POSTULANTE → GESTORA ENCARGADA |
| NRO. DE CASA | GESTORA ENCARGADA | DAU/EPICRISIS → EPICRISIS CON IND MÉDICA |
| CELULAR 2 | — | CELULAR 1 → CELULAR |
| Antecedentes complementarios | — | — |

**Implicancia categórica:** El schema de la postulación evoluciona anualmente. Esto es un problema de **schema evolution** que requiere migración Delta (Δ). La categoría C_migr debe incluir un funtor de migración entre versiones del formulario.

### 16.3 Objeto EntregaTurno — la tabla más rica del dominio

**La entrega de turno de enfermería es el verdadero estado operacional del sistema.** Cada handoff captura el snapshot completo de todos los pacientes activos:

```
EntregaTurnoEnfermeria {
  enfermero_turno: String                     -- EU que entrega
  fecha: Date
  
  pacientes: List {
    nombre_paciente: String
    edad: Int
    diagnostico: String                       -- texto abreviado clínico
    tto_ev_cs_ca: String                     -- tratamientos activos
    invasivos_o2: String                     -- dispositivos + oxígeno
    rhb: String                              -- rehabilitación requerida
    observaciones: Text                      -- estado clínico narrativo
    pendientes: Text                         -- acciones por completar
  }
  
  movimientos: {
    altas: List { nombre, fecha, observaciones }
    ingresos: List { nombre, fecha, diagnostico }
  }
}
```

**Hallazgos de los datos reales:**

1. **TTO EV / CS / CA** son abreviaturas operacionales:
   - TTO EV = tratamiento endovenoso (con esquema: droga dosis/total, ej "ERTA 4/7", "CEF 5/7")
   - CS = curación simple
   - CA = curación avanzada
   - Formato típico: "CA 05.01" = curación avanzada programada para el día 5 de enero

2. **Invasivos codificados:** VVP (vía venosa periférica) con calibre y días ("VVP 22 D5" = calibre 22, día 5), CUP (catéter urinario permanente) con número, SNG (sonda nasogástrica)

3. **RHB tipada:** KTM (kinesiología motora), KTR (kinesiología respiratoria), FONO (fonoaudiología). Combinaciones: "KTM + FONO", "KTR + FONO"

4. **Observaciones contienen estado clínico real:**
   - "AISL. X GOTITAS + CONTACTO" = aislamiento por gotitas y contacto
   - "ING MEDICO OK" = ingreso médico completado
   - "ACTIVAR GES AL ALTA" = gestión GES pendiente
   - "NTP LUNES Y JUEVES" = nutrición parenteral días específicos
   - "VM INGRESO OK 29-12" = visita médica de ingreso completada

5. **Pendientes revelan la cola de trabajo:**
   - "FIRMA CONSENTIMIENTO INFORMADO" = CI pendiente (viola condición `consentimiento = firmado` del wide pullback §4.1)
   - "VERIFICAR HORA CARDIO EN 3 SEMANAS" = coordinación con especialidades
   - "EGRESO MÉDICO" = alta pendiente de firma médica
   - "EXÁMENES 05.01" = laboratorio programado

**Entrega de turno kinesiología** — estructura diferente pero complementaria:

```
EntregaTurnoKine {
  kinesiologo_entrega: String
  kinesiologo_recibe: String
  fecha: Date
  
  pacientes: List {
    nombre: String
    rut: String                              -- kinesiología SÍ registra RUT
    cobertura: {INGRESO, CONTROL, ALTA}      -- tipo de atención del día
    diagnostico: String
    observaciones: String                    -- intervención kinésica realizada
    hora_atencion: Time
    ayuno: String                            -- hora última ingesta (para respiratorio)
    registro_fc: {KTR, KTM, R+M}            -- tipo de ficha kinésica
  }
}
```

**Campo COBERTURA** — este es un enum operacional que mapea a estados del episodio:
```
INGRESO → primera visita kine del episodio (genera IngresoKinesiologia)
CONTROL → visita de seguimiento (genera registro de evolución)
ALTA    → última visita kine (cierra componente kinésico del plan)
```

**Campo REGISTRO FC** codifica el tipo de intervención:
```
KTR = kinesiología respiratoria (ficha respiratoria)
KTM = kinesiología motora (ficha motora)
R+M = ambas intervenciones en la misma visita
```

### 16.4 Canasta de Prestaciones — coproducto formal de servicios

La Canasta HODOM define **24 prestaciones autorizadas** con código MAI (Modalidad de Atención Institucional). Esto es el catálogo formal que determina qué puede hacer HoDom:

```
Prestacion = DiaCama + ConsultaMedica + ControlEnfermera + ControlTENS 
           + ControlFonoaudiologo + AtencionKine + ReanimacionCPR 
           + SaturacionO2 + IntubacionSNG + VaciamientoFecaloma
           + InstilacionVesical + VaciamientoVesical + InstalacionSondaVesical
           + Hemoglucotest + CuracionSimple + AdministracionMedicamentos
           + InstalacionViaVenosa + TomaMuestras + CuracionAvanzada
           + TtoUlceraVenosaTipo1 + TtoUlceraVenosaTipo3 
           + CuracionQuemadosMenos5 + CuracionQuemadosMas5

con atributos:
  codigo_mai: String    -- ej: "0201010", "01 01 001", "s/c" (sin código)
  tipo_eph: "EPH"       -- Estándar de Prestaciones Hospitalarias
  estamento: String      -- Cama Básica | Cama Básica/Media
```

**Implicancia categórica:** La canasta es un **coproducto cerrado** — HoDom solo puede ejecutar estas 24 prestaciones. Cualquier otro procedimiento requiere derivación al hospital. Las prestaciones sin código MAI ("s/c") son servicios que se ejecutan pero no están formalizados en el arancel.

**Cruce prestaciones × formulario de postulación:**
El campo `prestacion_solicitada` del formulario usa texto libre que combina prestaciones de la canasta:
```
"TTO EV"                          → AdministracionMedicamentos + InstalacionViaVenosa
"CURACIÓN"                        → CuracionSimple | CuracionAvanzada
"KTM"                             → AtencionKine (motora)
"KINE RESPIRATORIA"               → AtencionKine (respiratoria)
"REHABILITACIÓN (KINE + FONO)"    → AtencionKine + ControlFonoaudiologo
"TTO EV + CURACION"               → combinación
"EXAMENES DE CONTROL"             → TomaMuestras
```

El mapeo es N:M — una postulación puede solicitar múltiples prestaciones, y una prestación puede ser solicitada en múltiples postulaciones.

### 16.5 Consolidado de Atenciones Diarias — serie temporal para F_REM

```
ConsolidadoDiario {
  fecha: Date
  enfermero: Int      -- conteo de atenciones de enfermería del día
  kinesiologo: Int    -- conteo de atenciones kinesiología
  fonoaudiologo: Int  -- conteo de atenciones fonoaudiología
  medico: Int         -- conteo de atenciones médicas
  tecnico: Int        -- conteo de atenciones TENS
}
```

**368 días de datos** (2026-01-01 a 2027-01-03). **NOTA [v4.1]:** El rango temporal excede la fecha del documento (2026-03-31). Los datos post-marzo 2026 provienen de la fuente original sin depurar — probablemente son registros proyectados o preexistentes en la planilla fuente. Tratar los datos posteriores a la fecha del documento como no verificados. Esta tabla es el insumo directo para generar la sección C.1.2 del REM (Visitas Realizadas).

**Patrones observados en los datos:**
- Enfermero: visitas todos los días (L-D). Rango 6-15 por día.
- Kinesiólogo: visitas todos los días. Rango 6-10 por día.
- Fonoaudiólogo: solo algunos días (0 en fines de semana y algunos L-V). Rango 0-8.
- Médico: solo algunos días (0 en fines de semana y algunos L-V). Rango 0-7.
- Técnico: irregular, 0 la mayoría de los días. Rango 0-2.

**Esto confirma PE-12 (cobertura L-D):** Enfermería y kinesiología atienden todos los días. Médico y fonoaudióloga solo días hábiles (con excepciones). TENS es un recurso escaso e irregular.

### 16.6 Gestora Encargada — nuevo rol formal

El formulario 2026 introduce `GESTORA ENCARGADA` como campo explícito. Los datos revelan al menos 7 personas distintas en este rol:

```
GestoraEncargada ∈ {MELISSA SEPULVEDA, MELISSA RIVERA, HELEN LOPEZ, 
                    PIA VASQUEZ, CAMILA BUSTAMANTE, DORIS GONZALEZ, ANASTASIA}
```

Este rol NO aparece en el modelo OPM (SD2) ni en el organigrama formal del proyecto. Es un rol operacional que media entre el servicio derivador y HoDom:
- Recibe la postulación
- Evalúa elegibilidad inicial
- Asigna al paciente
- Coordina el ingreso

Categóricamente, la gestora es un **agente del morfismo `evaluar_elegibilidad`** que no estaba modelado.

### 16.7 Nuevos morfismos descubiertos

```
-- Postulación digital
postula_via_form    : Postulacion → GoogleForm           -- la postulación es digital
asignada_a_gestora  : Postulacion → GestoraEncargada     -- gestora asignada
tiene_epicrisis_url : Postulacion → URL_GoogleDrive      -- epicrisis adjunta como link

-- Prestaciones
requiere_prestacion : EpisodioHD → List(Prestacion)      -- prestaciones solicitadas
prestacion_codigo   : Prestacion → CodigoMAI             -- código arancel

-- Turno
turno_de           : EntregaTurno → Profesional           -- profesional que entrega
recibe             : EntregaTurno → Profesional           -- profesional que recibe
snapshot_pacientes : EntregaTurno → List(EstadoPaciente)  -- estado de cada paciente activo
movimientos_dia    : EntregaTurno → (List(Alta) × List(Ingreso))  -- altas e ingresos del turno

-- Kinesiología operacional
tipo_cobertura_kine : VisitaKine → {INGRESO, CONTROL, ALTA}
tipo_registro_kine  : VisitaKine → {KTR, KTM, R_M}
hora_ayuno         : VisitaKine → (Time × Time_ayuno)     -- para procedimientos respiratorios
```

### 16.8 Nuevas path equations

**PE-17: Prestación dentro de canasta** [v4]
```
∀ p ∈ requiere_prestacion(e): p ∈ Canasta_HODOM ∨ p.tipo = 'sin_codigo_MAI'
-- Solo se pueden ejecutar las 24 prestaciones autorizadas de la canasta.
-- Excepción: prestaciones sin código MAI (ej: NTP/nutrición parenteral) se ejecutan
-- pero no están formalizadas en el arancel. Esta excepción aplica igualmente en PE-24.
```

**PE-18: Consolidado diario = sum visitas** [v4]
```
∀ fecha d, ∀ tipo t: consolidado(d, t) = count(visitas donde fecha=d ∧ tipo_profesional=t)
-- El consolidado debe ser derivable de las visitas individuales
```

**PE-19: Movimientos de turno = transiciones del día** [v4]
```
altas_turno(d) ⊆ {e | egresar(e).fecha = d}
ingresos_turno(d) ⊆ {e | ingresar(e).fecha = d}
-- Los movimientos registrados en el turno deben corresponder a transiciones reales
```

**PE-20: Cobertura kine mapea a estado episodio** [v4]
```
cobertura_kine(v) = INGRESO ⟹ ∄ v' ∈ visitas_kine(episodio(v)): v' < v
cobertura_kine(v) = ALTA ⟹ ∄ v' ∈ visitas_kine(episodio(v)): v' > v
-- INGRESO es la primera visita kine, ALTA es la última
```

### 16.9 Déficits estructurales adicionales

| # | Déficit | Severidad | Impacto |
|---|---------|-----------|---------|
| D23 | **[v4]** Gestora Encargada no modelada formalmente | ALTO | Rol operacional crítico sin entidad en el schema ni en OPM |
| D24 | **[v4]** Prestación solicitada como texto libre | ALTO | Debería ser FK a Canasta HODOM con código MAI |
| D25 | **[v4]** Epicrisis como URL a Google Drive | MEDIO | Documento clínico almacenado fuera del sistema. Sin estructura ni FK |
| D26 | **[v4]** Schema de postulación evoluciona sin control | ALTO | Drift anual sin migración formal. 2025→2026 perdió campos relevantes |
| D27 | **[v4]** Entrega de turno no digitalizada estructuralmente | CRÍTICO | La tabla más rica del dominio está en Word/Excel sin FK a episodios |
| D28 | **[v4]** Consolidado diario no vinculado a visitas individuales | ALTO | Conteos manuales sin trazabilidad a registros fuente |
| D29 | **[v4]** Múltiples gestoras sin normalización de nombres | MEDIO | "MELISSA SEPULVEDA", "melissa sepulveda meriño", "MELISSA SEPULVEDA MERIÑO" son la misma persona |
| D30 | **[v4]** Diagnóstico en texto libre abreviado | ALTO | "PNA", "ACV", "EPOC EXACERBADO" sin codificación CIE-10 |
| D31 | **[v4]** Servicio origen interno vs categoría REM sin mapeo | ALTO | 11 servicios internos deben mapear a 6 categorías REM |

### 16.10 Hallazgos para la futura estructura de datos

**Prioridad 1 — Tabla de Postulaciones:**
```sql
CREATE TABLE postulacion (
  id SERIAL PRIMARY KEY,
  timestamp_envio TIMESTAMPTZ NOT NULL,
  paciente_rut VARCHAR(12) REFERENCES paciente(rut),
  servicio_origen VARCHAR(20) NOT NULL,  -- enum de 11 servicios
  origen_derivacion_rem VARCHAR(20),     -- enum de 6 categorías REM (derivado)
  diagnostico_texto TEXT,
  diagnostico_cie10 VARCHAR(10),         -- TO DO: codificar
  prestaciones_solicitadas TEXT[],       -- array de códigos MAI
  gestora_rut VARCHAR(12) REFERENCES profesional(rut),
  epicrisis_url TEXT,
  usuario_o2 BOOLEAN DEFAULT FALSE,
  estado_postulacion VARCHAR(20) DEFAULT 'pendiente'  -- pendiente/aceptada/rechazada
);
```

**Prioridad 2 — Tabla de Prestaciones (Canasta):**
```sql
CREATE TABLE prestacion_canasta (
  id SERIAL PRIMARY KEY,
  codigo_mai VARCHAR(20),               -- puede ser 's/c'
  nombre TEXT NOT NULL,
  estamento VARCHAR(30),                -- Cama Básica | Cama Básica/Media
  tipo_eph VARCHAR(10) DEFAULT 'EPH',
  activa BOOLEAN DEFAULT TRUE
);
```

**Prioridad 3 — Tabla de Entregas de Turno:**
```sql
CREATE TABLE entrega_turno (
  id SERIAL PRIMARY KEY,
  fecha DATE NOT NULL,
  tipo VARCHAR(20) NOT NULL,            -- enfermeria | kinesiologia
  profesional_entrega VARCHAR(12) REFERENCES profesional(rut),
  profesional_recibe VARCHAR(12) REFERENCES profesional(rut)
);

CREATE TABLE entrega_turno_paciente (
  id SERIAL PRIMARY KEY,
  entrega_turno_id INT REFERENCES entrega_turno(id),
  episodio_id INT REFERENCES episodio(id),
  diagnostico_abreviado TEXT,
  tto_activo TEXT,                      -- tratamientos en curso
  invasivos TEXT,                       -- dispositivos activos
  rehabilitacion TEXT,                  -- KTM/KTR/FONO
  observaciones TEXT,
  pendientes TEXT,
  -- para kine:
  cobertura VARCHAR(10),               -- INGRESO/CONTROL/ALTA
  hora_atencion TIME,
  tipo_registro VARCHAR(5)             -- KTR/KTM/R+M
);

CREATE TABLE movimiento_turno (
  id SERIAL PRIMARY KEY,
  entrega_turno_id INT REFERENCES entrega_turno(id),
  tipo VARCHAR(10) NOT NULL,           -- ALTA | INGRESO
  episodio_id INT REFERENCES episodio(id),
  fecha DATE,
  observaciones TEXT
);
```

**Prioridad 4 — Consolidado Diario (vista materializada):**
```sql
CREATE MATERIALIZED VIEW consolidado_diario AS
SELECT 
  fecha,
  COUNT(*) FILTER (WHERE tipo_profesional = 'enfermero') AS enfermero,
  COUNT(*) FILTER (WHERE tipo_profesional = 'kinesiologo') AS kinesiologo,
  COUNT(*) FILTER (WHERE tipo_profesional = 'fonoaudiologo') AS fonoaudiologo,
  COUNT(*) FILTER (WHERE tipo_profesional = 'medico') AS medico,
  COUNT(*) FILTER (WHERE tipo_profesional = 'tecnico') AS tecnico
FROM visita
GROUP BY fecha;
-- Esto reemplaza el conteo manual actual y genera C.1.2 del REM
```

### 16.11 [v4b] Registro Trabajo Social — rol en elegibilidad confirmado

```
RegistroTrabajoSocial {
  fecha: Date
  nombre: String
  apellidos: String
  diagnostico: String
  motivo_consulta: Enum {
    EVALUACION_SOCIAL,
    EVALUACION_INGRESO_HODOM,      -- participa en el wide pullback de elegibilidad
    ORIENTACION_SOCIAL,
    VISITA_SOCIAL_SEGUIMIENTO
  }
  actividad_complementaria: Enum {
    ENTREVISTA_CON_FAMILIAR,
    COORDINACION_CON_RED,          -- coordinación con otros establecimientos
    CONTACTO_TELEFONICO_SEGUIMIENTO,
    PESQUIZA_SERVICIOS_CLINICOS    -- búsqueda activa de candidatos en servicios
  }
  duracion_visita: String          -- "15 MINUTOS", "30 MINUTOS", "1 HORA"
  resultado: {INGRESA, NO_INGRESA} -- decisión de elegibilidad social
}
```

**Hallazgo categórico:** Trabajo Social no solo evalúa condiciones del domicilio y red de apoyo (como dice el modelo OPM). También hace **pesquisa activa** en servicios clínicos — busca candidatos para HoDom dentro del hospital. Esto es un morfismo nuevo:

```
pesquisar : ServicioClinico → List(Candidato)
-- Trabajo Social genera el flujo de entrada al wide pullback de elegibilidad
-- No solo evalúa: también descubre
```

El campo `resultado = {INGRESA, NO_INGRESA}` confirma que la evaluación social es un **gate** del wide pullback — si Trabajo Social dice NO_INGRESA, el episodio no se crea independientemente de la condición clínica.

### 16.12 [v4b] Registro de Llamadas — regulación a distancia real

```
RegistroLlamada {
  fecha: Date
  hora: Time
  duracion: Duration              -- "HH:MM:SS"
  nro_telefono: String
  motivo: String                  -- texto libre: "RESULTADO EX", "SEGUIMIENTO", etc.
  usuario_hodom: String           -- nombre del paciente
  nombre_familiar: String         -- familiar contactado
  estado_paciente: {ACTIVO, EGRESADO}
  tipo_llamada: {EMITIDA, RECIBIDA}
  funcionario_hd: String          -- profesional que llama/recibe
  observaciones: Text
}
```

**Datos:** 7 meses (julio 2024 — enero 2025). Esto confirma la existencia de `RegistroTelesalud` del modelo OPM pero con estructura diferente a la supuesta.

**Hallazgo:** Las llamadas se hacen también a pacientes EGRESADOS (campo ACT/EGR). Esto implica un **seguimiento post-egreso** que no está modelado en el ciclo de vida del episodio. El episodio "terminado" sigue generando actividad.

```
seguimiento_post_egreso : EpisodioEgresado → List(Llamada)
-- Morfismo que extiende el ciclo de vida más allá del estado "egresado"
```

### 16.13 [v4b] Programación Diaria — ProgramaVisitas real

La planilla real de programación diaria (dato 31.03.2026) tiene estructura más rica que la modelada originalmente. Consta de **cuatro zonas** estructuralmente distintas:

```
ProgramacionDiaria {
  fecha: Date
  
  -- ZONA 1: Rutas con conductor, hora y profesionales asignados
  rutas_asignadas: List {
    conductor: String              -- ANDRES | SERVANDO | CRISTOPHER (3 conductores = 3 rutas)
    hora: Time                     -- hora programada de la visita
    medico: String | null          -- nombre (ej: CARABALLO)
    fonoaudiologo: String | null   -- nombre (ej: M.JOSÉ)
    kinesiologo: String | null     -- nombre (ej: BRAYAN)
    enfermera: String | null       -- nombre (ej: LAURA)
    tens: String | null            -- nombre
    paciente: String               -- nombre completo del paciente
    prestacion_programada: String  -- código(s) de prestación: CA, CS, TTO EV, KTM, KTR, FONO, NTP, VM INGRESO, VM EGRESO
    direccion: String              -- dirección completa con localidad
    telefono: String               -- uno o más números de contacto
  }
  
  -- ZONA 2: Visitas de enfermería sin ruta asignada
  -- Profesionales van por su cuenta o se asignan dinámicamente a conductor con disponibilidad
  visitas_enfermeria_sin_ruta: List {
    paciente: String
    prestacion_programada: String  -- TTO EV, CA, CS, etc.
    direccion: String
    telefono: String
  }
  
  -- ZONA 3: Visitas de kine/fono sin ruta asignada
  visitas_rehab_sin_ruta: List {
    paciente: String
    prestacion_programada: String  -- KTM, KTR, FONO, combinaciones
    direccion: String
    telefono: String
  }
  
  -- ZONA 4: Visitas sueltas (ingresos, egresos, procedimientos especiales)
  visitas_adicionales: List {
    paciente: String
    prestacion_programada: String  -- TTO EV + VM INGRESO, CA, KTM + EV FONO, etc.
    direccion: String
    telefono: String
  }
}
```

**Estructura real (dato 31.03.2026):**
- 3 conductores: ANDRES, CRISTOPHER, SERVANDO — cada uno con su ruta
- Visitas en ruta programadas con hora específica (08:00, 09:30, 11:00, etc.)
- Cada visita indica qué profesionales van: la enfermera LAURA cubre la mayoría, BRAYAN (kine) y M.JOSÉ (fono) se asignan a pacientes específicos
- 35 hojas = 35 días del mes

**Hallazgos categóricos de la planilla real:**

1. **Prestación codificada por visita.** Cada fila lleva la prestación a ejecutar usando códigos operacionales que mapean a la canasta §16.4:

```
Código operacional → Prestación / Artefacto generado

  -- Prestaciones de tratamiento
  CA                → CuracionAvanzada (canasta §16.4)
  CS                → CuracionSimple (canasta §16.4)
  TTO EV            → AdministracionMedicamentos + InstalacionViaVenosa (canasta §16.4)
  EV                → InstalacionViaVenosa | AdministracionMedicamentos (canasta §16.4)
  NTP               → Nutrición parenteral (sin código MAI directo en canasta)
  
  -- Prestaciones de rehabilitación
  KTM               → AtencionKine modalidad motora (canasta §16.4)
  KTR               → AtencionKine modalidad respiratoria (canasta §16.4)
  FONO              → ControlFonoaudiologo (canasta §16.4)
  
  -- Marcadores de transición de estado del episodio
  VM INGRESO        → ConsultaMedica (primera visita médica) → transición `ingresar` (§5.2)
  VM EGRESO         → ConsultaMedica (última visita médica) → transición `egresar` (§5.2), genera Epicrisis
  
  -- Marcadores de ingreso por disciplina (primera visita de cada profesional)
  ING ENF           → genera IngresoEnfermeria (§10.1): checklist, examen físico, Barthel, plan enfermería
  ING KTR           → genera IngresoKinesiologia (§10.5) modalidad respiratoria: evaluación, dependencia, objetivos
  ING KTM           → genera IngresoKinesiologia (§10.5) modalidad motora: evaluación, Barthel, dependencia
```

Las combinaciones son frecuentes: "KTM + FONO", "CA + VM EGRESO", "TTO EV + VM INGRESO", "KTM + EV FONO", "ING ENF + VM INGRESO", "ING KTR + EV FONO". Un paciente puede requerir múltiples prestaciones en la misma visita.

2. **La admisión es una secuencia multi-profesional, no un evento atómico.** El dato del 31/03/2026 muestra un ingreso real (SYLVIA PALACIOS MORALES) programado como dos filas el mismo día:
   - Fila 1: `ING ENF + VM INGRESO` → enfermera hace IngresoEnfermeria + médico hace primera visita
   - Fila 2: `ING KTR + EV FONO` → kinesiólogo hace IngresoKinesiologia + fonoaudiólogo evalúa
   
   Esto significa que la transición `ingresar` (§5.2) se ejecuta como un **fan-out** de visitas de ingreso por disciplina, coordinadas en la programación del mismo día. Categóricamente:

```
ingresar(e) = VM_INGRESO(e) ∧ ING_ENF(e) ∧ (ING_KTR(e) ∨ ING_KTM(e))?
-- El ingreso médico (VM INGRESO) es obligatorio
-- El ingreso de enfermería (ING ENF) es obligatorio (genera checklist §10.1)
-- El ingreso kinésico es condicional a la prestación solicitada
-- Todos se programan para el mismo día
```

3. **VM INGRESO / VM EGRESO como marcadores de transición de estado.** La programación etiqueta explícitamente qué visitas médicas corresponden a transiciones del ciclo de vida del episodio:
   - `VM INGRESO` → transición `ingresar` (§5.2): el médico realiza la primera evaluación domiciliaria
   - `VM EGRESO` → transición `egresar` (§5.2): el médico cierra el episodio y genera Epicrisis
   Esto conecta la programación diaria con la coalgebra del episodio de forma directa.

3. **Un paciente puede aparecer múltiples veces en el mismo día.** Ejemplo del 31/03: MARIA LUZ ALARCÓN tiene CA (zona 2, enfermería) + KTM+CA (zona 3, kine). NORMA HERNÁNDEZ tiene CS (zona 2) + KTM (zona 3). Esto significa que un paciente puede recibir N visitas/día de profesionales distintos, cada una con su prestación. El conteo diario del consolidado (§16.5) refleja visitas, no pacientes.

4. **Dos modos de asignación logística:**
   - **Con ruta** (zona 1): conductor + hora + profesionales asignados. El conductor determina la ruta geográfica y transporta al equipo.
   - **Sin ruta** (zonas 2-4): visitas listadas por paciente y prestación, sin conductor ni hora. Posiblemente asignadas dinámicamente al conductor con disponibilidad, o profesionales que se desplazan por su cuenta.

5. **Dirección + teléfono como dato operacional.** Cada entrada de la programación porta la dirección completa y teléfono(s) del paciente. La ruta es un artefacto logístico completo, no solo un calendario.

**Hallazgo categórico:** La programación diaria es el **producto fibrado** real del dominio:

```
ProgramacionDiaria = ∏_{paciente ∈ activos} (hora? × equipo_asignado? × conductor? × prestacion × direccion × telefono)
```

Los campos `hora`, `equipo_asignado` y `conductor` son opcionales (nullable) — solo las visitas en ruta los tienen. La prestación, dirección y teléfono siempre están presentes.

Cada fila con ruta es un pullback: (profesional, paciente, hora, conductor) donde el conductor determina la ruta geográfica y la hora determina el orden de visitas. Tres conductores = tres rutas paralelas.

Esto confirma que el **VehiculoTransporte** del modelo OPM se operacionaliza como 3 rutas diarias con conductor asignado, y que la asignación profesional-paciente varía día a día según necesidad clínica.

### 16.14 [v4b] Nuevos morfismos y PE

```
-- Trabajo Social
pesquisar         : TrabajadorSocial × ServicioClinico → List(Candidato)
evaluar_social    : TrabajadorSocial × Candidato → {INGRESA, NO_INGRESA}

-- Llamadas
llamar            : Profesional × (Paciente | Familiar) → Llamada
seguir_post_egreso: Profesional × EpisodioEgresado → Llamada

-- Programación
programar_dia     : ProfesionalCoordinador × Date → ProgramacionDiaria
asignar_ruta      : Conductor × List(Paciente) → Ruta
prestacion_prog   : FilaProgramacion → List(Prestacion)     -- prestación(es) programada(s) por visita
marca_transicion  : FilaProgramacion → {VM_INGRESO, VM_EGRESO, null}  -- etiqueta de transición de estado
```

**PE-21: Evaluación social gate del wide pullback** [v4b]
```
∀ e ∈ EpisodioHD: ∃ eval ∈ RegistroTrabajoSocial: 
  eval.paciente = pertenece_a(e) ∧ eval.resultado = INGRESA
-- No se crea episodio sin evaluación social positiva
```

**PE-22: Programación diaria cubre activos** [v4b]
```
∀ d, ∀ p activo en d: ∃ fila ∈ ProgramacionDiaria(d): fila.paciente = p
-- Todo paciente activo aparece en la programación del día (al menos una visita)
```

**PE-23: VM INGRESO/EGRESO implica transición de estado** [v4b]
```
marca_transicion(fila) = VM_INGRESO ⟹ ∃ e: ingresar(e).fecha = fila.fecha
marca_transicion(fila) = VM_EGRESO ⟹ ∃ e: egresar(e).fecha = fila.fecha
-- Las visitas médicas de ingreso y egreso marcadas en la programación 
-- deben corresponder a transiciones reales del episodio
```

**PE-24: Prestación programada dentro de canasta** [v4b]
```
∀ fila ∈ ProgramacionDiaria: ∀ p ∈ prestacion_prog(fila): p ∈ Canasta_HODOM ∨ p.tipo = 'sin_codigo_MAI'
-- Las prestaciones programadas deben estar en la canasta §16.4
-- Excepción: NTP (nutrición parenteral) no tiene código MAI directo
```

**PE-25: Ingreso como fan-out multi-profesional** [v4b]
```
∀ e ∈ EpisodioHD: ∃ d = fecha_ingreso(e):
  ∃ fila₁ ∈ Prog(d): fila₁.paciente = pertenece_a(e) ∧ VM_INGRESO ∈ prestacion_prog(fila₁)
  ∧ ∃ fila₂ ∈ Prog(d): fila₂.paciente = pertenece_a(e) ∧ ING_ENF ∈ prestacion_prog(fila₂)
-- Todo episodio tiene al menos VM INGRESO + ING ENF programados el día de ingreso
-- Las visitas de ingreso por disciplina adicional (ING KTR, ING KTM) son condicionales
```

### 16.15 [v4b] Dimensión Espacial-Temporal: Telemetría GPS + Análisis Operacional

**Fuentes integradas:**
- Reporte GPS Wialon: drives/stops de 3 vehículos (PFFF57, RGHB14, SUV TZXS94), ene–mar 2026
- Análisis operacional cruzado (XLSX 7 hojas): 1.574 visitas programadas, 7.587 eventos GPS, 145 direcciones geocodificadas, 194 asignaciones bloque-vehículo, 1.895 anomalías

**Estructura del dataset operacional:**

```
TelemetriaOperacional {
  planned_visits: List {                    -- 1.574 filas
    visita_programada_id: String            -- ej: "2026-01-31_31.01_002"
    fecha: Date
    bloque_diario: String                   -- ej: "2026-01-31_B01" (ruta del día)
    lider_bloque: String                    -- conductor asignado
    hora_programada: Time
    profesionales: {medico?, fono?, kine?, enfermera?, tens?}
    paciente: String
    paciente_id: String                     -- ej: "PAC-087" (ID normalizado)
    tipo_visita: String                     -- código prestación: KTM, KTR, CA, TTO EV, VM INGRESO, etc.
    direccion: String
    direccion_normalizada: String
    lat: Float?
    lon: Float?
    geocode_quality: {alta, media, sin_match}
  }
  
  gps_events: List {                        -- 7.587 filas
    event_id: String
    stop_id: String?                        -- solo para paradas
    device: String                          -- PFFF57 | RGHB14 | SUV TZXS94
    tipo_evento: {Detenido, Movimiento}
    inicio: DateTime
    fin: DateTime
    duracion_seg: Int
    lat: Float?                             -- solo paradas
    lon: Float?                             -- solo paradas
    distancia_km: Float?                    -- solo movimientos
    vel_max_kph: Int?
    vel_media_kph: Int?
    candidate_stop: Bool                    -- ¿candidato a visita domiciliaria?
    base_stop: Bool                         -- ¿parada en la base hospitalaria?
  }
  
  visit_matches: List {                     -- 1.574 filas (1:1 con planned)
    visita_programada_id: String
    stop_id: String?                        -- GPS stop matcheado
    distance_m: Float?                      -- distancia entre dirección y GPS stop
    delta_min: Float?                       -- diferencia temporal programado vs real
    confianza_match: {alta, media, sin_match}
  }
  
  daily_vehicle_summary: List {             -- 226 filas (vehículo × día)
    fecha: Date
    dispositivo: String
    visitas_programadas: Int
    visitas_matcheadas_alta: Int
    visitas_matcheadas_media: Int
    visitas_sin_match: Int
    km_totales: Float
    tiempo_movimiento_min: Float
    tiempo_detenido_min: Float
    paradas_extra: Int                      -- paradas >10min no asociadas a visita ni base
    tiempo_detenido_no_asistencial_min: Float
    salida_primera: DateTime?
    llegada_ultima: DateTime?
    cumplimiento_pct: Float?
    km_por_visita_programada: Float?
  }
  
  geocoded_addresses: List {                -- 145 direcciones únicas
    direccion_normalizada: String
    lat: Float
    lon: Float
    calidad_geocoder: {alta, media}
  }
}
```

**Hallazgos categóricos de la telemetría:**

1. **Match programación ↔ GPS = 87%.** De las 1.574 visitas programadas, el 87% tiene correspondencia con paradas GPS reales. Esto valida que la programación diaria (§16.13) refleja la operación real con alta fidelidad.

2. **Productividad real = 39.2% de la jornada formal.** Sobre 12h de jornada formal (08:00-20:00), solo 4.7h son productivas (23.1% en terreno + 16.1% en movimiento). El 35.6% de la jornada no se opera (17:30-20:00 sin actividad de ruta).

3. **Capacidad ociosa trimestral = 1.818 horas.** El bloque 17:30-20:00 no genera visitas detectables. Esto es una holgura temporal, no kilométrica — los vehículos usan 74-81% de su límite de km pero solo el 64% de su ventana temporal.

4. **3 vehículos con perfiles diferenciados:**

| Vehículo | Km/día | Visitas/día | % tiempo en base | Disponibilidad |
|----------|--------|-------------|-----------------|----------------|
| PFFF57 | 73.9 | 9.3 | 36.0% | L-D |
| RGHB14 | 81.2 | 8.8 | 38.3% | L-D |
| SUV TZXS94 | 63.2 | 5.6 | 42.0% | **L-V** |

El SUV opera solo L-V, lo que reduce la capacidad de fines de semana a 2 móviles. Los conductores de cuarto turno cubren L-D; el conductor diurno solo L-V.

5. **Velocidades >100 kph detectadas en rutas rurales.** Esto es un riesgo de seguridad no modelado anteriormente.

6. **Pacientes geocodificados:** 145 direcciones únicas geocodificadas con calidad variable (alta, media, sin_match). Esto habilita análisis de cobertura geográfica real vs radio teórico de 20 km (PE-5).

7. **Paradas extra (anomalías):** 1.895 paradas >10 min no asociadas a visitas programadas ni a base hospitalaria. Posibles causas: trámites, compras, paradas no programadas. Fuente de ineficiencia no capturada en el modelo de programación.

**Nuevos morfismos:**

```
-- Telemetría
gps_track_of    : VehiculoTransporte × Date → List(GPSEvent)
match_visita    : VisitaProgramada × GPSEvent → VisitaMatch
geocode         : Direccion → (Lat × Lon × Calidad)
productividad   : VehiculoTransporte × Date → (km_totales × tiempo_movimiento × tiempo_terreno × tiempo_base × visitas_realizadas)
```

**Nuevas path equations:**

**PE-26: Geocodificación de domicilio habilita PE-5** [v4b]
```
∀ e ∈ EpisodioHD: geocode(ocurre_en(e)).calidad ∈ {alta, media} ⟹ 
  haversine(geocode(ocurre_en(e)), coord_hospital) ≤ 20 km
-- La verificación de PE-5 (radio ≤20 km) se puede automatizar cuando la dirección está geocodificada
```

**PE-27: Match GPS valida ejecución de visita** [v4b]
```
∀ v ∈ VisitaProgramada: match_visita(v).confianza ∈ {alta, media} ⟹ 
  ∃ stop ∈ GPSEvent: haversine(stop.coord, geocode(v.direccion)) ≤ 500m 
  ∧ |stop.inicio - v.hora_programada| ≤ 120 min
-- Una visita se considera ejecutada si hay una parada GPS cercana en tiempo y espacio
```

**Nuevos déficits:**

| # | Déficit | Severidad | Impacto |
|---|---------|-----------|---------|
| D36 | **[v4b]** Bloque 17:30-20:00 sin operación de ruta | ALTO | 1.818 horas/trimestre de capacidad vehicular no utilizada. La holgura es temporal, no kilométrica |
| D37 | **[v4b]** Velocidades >100 kph en rutas rurales sin protocolo de seguridad vial | MEDIO | Riesgo de seguridad para el equipo y los pacientes transportados |
| D38 | **[v4b]** Paradas extra no trazables (1.895 anomalías en 83 días) | MEDIO | Paradas >10 min sin asociación a visitas programadas ni a base. Causa desconocida |
| D39 | **[v4b]** SUV disponible solo L-V, reduce capacidad fin de semana a 2/3 | MEDIO | Impacto en cobertura de fines de semana. Alineado con PE-12 (cobertura L-D) |

### 16.16 [v4b] Fuentes estratégicas del Director Técnico

Los documentos de la Dirección Técnica (presentación Marp, guión, consolidado estratégico, marco de rol DT) aportan al modelo las siguientes piezas no capturadas previamente:

1. **Dato de oportunidad de hospitalización ≤12h** ya estaba en §1.4 pero ahora con serie completa: 96.8% (2019) → 69.5% (2022) → 61.0% (2023) → 54.9% (2024) → **40.6%** (2025). Caída de 56 puntos en 6 años. Esto es el driver institucional de HODOM.

2. **Perfil demográfico de pacientes** con dato exacto: edad promedio 70.1 años, 35% ≥80 años, 87.6% FONASA A+B, 54.4% mujeres. Diagnósticos frecuentes: ITU 12.2%, neumonía 11.0%, ACV 3.5%. Origen: medicina 42.7%, urgencia 32.0%, traumatología 9.4%. Prestaciones core: TTO EV ~45%, kinesiología ~40%, curaciones ~10%.

3. **Rol dual DT + médico regulador** — el Director Técnico es simultáneamente autoridad clínica, regulador operativo de flujo de casos, responsable normativo y conductor del equipo. Esto formaliza un agente que el modelo OPM no tenía: `DirectorTecnico` como agente de los morfismos `evaluar_elegibilidad`, `planificar`, `monitorear` y `egresar`, y como responsable de la instancia de regulación clínica diaria.

4. **Horizonte H1 (sin recursos adicionales):** capacidad recuperable de ~24 a ~36-40 visitas/día (+50-67%) activando bloque tardío, escalonando almuerzo, adelantando salida y optimizando asignación territorial. Esta es la variable de acción inmediata que conecta la telemetría (§16.15) con la capacidad del sistema.

---

## 17. Brechas de Diseño desde Contraste Internacional [v4b]

El contraste del modelo contra HL7 FHIR R5 y el corpus de evidencia HaH internacional (113 fuentes) reveló brechas y oportunidades que modifican el inventario de déficits y las recomendaciones del modelo.

### 17.1 Brechas absorbidas como déficits

| # | Brecha | Origen | Severidad | Acción en el modelo |
|---|--------|--------|-----------|---------------------|
| D32 | **[v4b]** Remote Patient Monitoring (RPM) no modelado | Corpus HaH: sensores biofísicos, parches torácicos, wearables son componente activo en intervenciones HaH efectivas. FHIR: `Device` + `DeviceDefinition` con UDI. El modelo usa `SistemaComunicacion` genérico (§3.1.6) que no captura monitoreo remoto continuo | 🔴 ALTA | Agregar `DispositivoMonitoreoRemoto` como subtipo de recurso en §3.1.6. Extender el producto de `ObservacionCicloVital` (§4.3) con canal de captura: {presencial, RPM}. Agregar morfismo `captura_rpm: DispositivoRPM × Paciente → ObservacionCicloVital` |
| D33 | **[v4b]** Sin distinción Admission Avoidance (AA) vs Early Supported Discharge (ESD) | Corpus HaH: meta-análisis priorizan AA sobre ESD por mejores outcomes y costos. El modelo trata todo episodio como homogéneo. El campo `servicio_origen` (§16.2) distingue procedencia pero no el modelo de hospitalización | 🟡 MEDIA | Agregar atributo `modelo_hd: {admision_evitada, alta_precoz}` en `EpisodioHD` (§3.1.1). El mapeo: derivación desde UE/APS → AA; derivación desde servicios clínicos → ESD |
| D34 | **[v4b]** Sin medición estandarizada de outcomes clínicos | Corpus HaH: mortalidad 30d/90d, reingresos 30d, LOS, EQ-5D-5L, escalación. El modelo captura `CategoriaPaciente` y `Barthel` pero no métricas de resultado del episodio a nivel de programa | 🔴 ALTA | Agregar `OutcomeMeasurement` como proceso de gobernanza (extensión §12) con indicadores: tasa de fallecimiento no anticipado (ref: 0.36% MedPAC), tasa de escalación (ref: 7.2%), reingresos 30d, Δ_barthel agregado |
| D35 | **[v4b]** Sin evaluación de determinantes sociales (SDOH) | Corpus HaH: evidencia de que HaH puede amplificar inequidades. §16.11 confirma que Trabajo Social evalúa condiciones de ingreso, pero no captura SDOH estructurados (inseguridad alimentaria, habitacional, digital) | 🟡 MEDIA | Extender `RegistroTrabajoSocial` (§16.11) con dimensiones SDOH. Fuente FHIR: alineación con Gravity Project |

### 17.2 Fortalezas confirmadas del modelo frente a evidencia internacional

| Fortaleza | Detalle |
|-----------|---------|
| Marco regulatorio permanente | Chile (DS 1/2022 + NT 2024) tiene marco legal estable. EE.UU. depende de waivers congresionales (CMS AHCAH expiró sept 2025). El wide pullback de elegibilidad (§4.1) con 8 condiciones es más formal que cualquier modelo del corpus |
| Distinción fallecido esperado/no esperado | El coproducto §4.2 modela esto nativamente. La mayoría de estudios internacionales reportan mortalidad agregada sin distinguir intención paliativa |
| Capacidad instalada como variable de gestión | El funtor F_REM §7 captura cupos programados/utilizados/disponibles. Sin equivalente estructurado en los modelos internacionales revisados |
| Médico regulador 24/7 en normativa | SD2 del OPM lo incluye como rol (aunque HSC no lo implementa — §14.3). CMS solo exige "conexión audio remota on-demand" sin rol diferenciado |

### 17.3 Mapeo FHIR de objetos nucleares del modelo

El contraste confirma que todo C_op es representable en FHIR R5. Mapeos directos de los objetos nucleares:

| Objeto del modelo | Recurso FHIR R5 | Notas |
|-------------------|-----------------|-------|
| `EpisodioHD` | `EpisodeOfCare` + `Encounter` (class: HH) | Encounter.class = HH (home health). EpisodeOfCare envuelve el episodio completo |
| `Paciente` | `Patient` | Mapeo directo |
| `Domicilio` | `Location` (type: pa = patient's home) | Soporta dirección, coordenadas, accesibilidad |
| `PlanTerapeutico` | `CarePlan` (status: draft → active → completed) | Mapeo directo. Referencia Condition, CareTeam, Goal |
| `EquipoSalud` | `CareTeam` + `PractitionerRole` + `Practitioner` | FHIR descompone hasta el rol individual con período |
| `Visita` | `Encounter` (hijo de EpisodeOfCare) | Cada visita domiciliaria = un Encounter |
| `ObservacionCicloVital` | `Observation` (category: vital-signs) | Perfiles estandarizados para PA, FC, FR, SpO2, T°. HGT, EVA, Glasgow requieren perfiles adicionales |
| `ConsentimientoInformado` | `Consent` | Recurso dedicado (maturity 2) |
| `MotivoEgreso` | `Encounter.dischargeDisposition` | ValueSet extensible para las 5+1 variantes |
| `Epicrisis` | `Composition` (type: discharge summary) | + `DocumentReference` |
| `PrestacionCanasta` | `HealthcareService` + `ChargeItemDefinition` | Código MAI mapeable a ChargeItem |

**Sin equivalente FHIR nativo** (requieren extensions o modelado fuera de FHIR):
- `SistemaDocumental` (protocolos, manuales)
- `CondicionExclusion` (se aproxima con `DetectedIssue` o `PlanDefinition`)
- Cupos programados/disponibles (sin recurso de capacity management)
- Normativa vigente (FHIR no modela regulación legal)
- Procesos de gobernanza §12 (dominio ERP/calidad, no interoperabilidad)

---

## Apéndice A. Tabla Consolidada de Déficits Estructurales

**Convención de numeración:** Los déficits se numeran por versión de adición (D1-D22: v1-v3, D23-D31: v4, D32-D39: v4b). La numeración refleja orden cronológico de descubrimiento, no orden documental. D32-D35 provienen de §17.1 (contraste FHIR/HaH) y D36-D39 de §16.15 (telemetría GPS).

| # | Sección origen | Déficit | Severidad |
|---|----------------|---------|-----------|
| D1 | §13.2 | Paciente y Episodio fundidos en una tabla | CRÍTICO |
| D2 | §13.2 | Ausencia de entidad Visita | CRÍTICO |
| D3 | §13.2 | Ausencia de SignosVitales como entidad | ALTO |
| D4 | §13.2 | Motivo egreso como string libre | ALTO |
| D5 | §13.2 | Sin timestamps de transiciones intermedias | MEDIO |
| D6 | §13.2 | Sin FK al equipo/profesional asignado | ALTO |
| D7 | §13.2 | Sin registro de elegibilidad | MEDIO |
| D8 | §13.2 | Sin tabla de cupos | ALTO |
| D9 | §13.2 | Sin distinción fallecido esperado/no esperado | ALTO |
| D10 | §13.2 | Sin campo pueblos originarios | BAJO |
| D11 | §13.2 | Formulario curaciones sin ID paciente/episodio | MEDIO |
| D12 | §13.2 | Registro enfermería sin signos vitales estructurados | MEDIO |
| D13 | §13.2 | Sin campo rango_etario REM | BAJO |
| D14 | §13.2 | Sin mapeo servicio_origen → origen_derivacion_REM | ALTO |
| D15 | §13.2 | Sin registro de enlace APS | ALTO |
| D16 | §13.2 | Ciclo vital en papel — 12 variables sin digitalizar | CRÍTICO |
| D17 | §13.2 | Nro. Postulación sin FK en esquema | ALTO |
| D18 | §13.2 | Examen físico de ingreso sin digitalizar | MEDIO |
| D19 | §13.2 | Checklist de ingreso sin persistencia | MEDIO |
| D20 | §13.2 | RUT del cuidador no registrado en esquema | MEDIO |
| D21 | §13.2 | Constraint estadía máxima no enforced | ALTO |
| D22 | §13.2 | Diagnóstico de ingreso vs egreso no diferenciado | MEDIO |
| D23 | §16.9 | Gestora Encargada no modelada formalmente | ALTO |
| D24 | §16.9 | Prestación solicitada como texto libre | ALTO |
| D25 | §16.9 | Epicrisis como URL a Google Drive | MEDIO |
| D26 | §16.9 | Schema de postulación evoluciona sin control | ALTO |
| D27 | §16.9 | Entrega de turno no digitalizada estructuralmente | CRÍTICO |
| D28 | §16.9 | Consolidado diario no vinculado a visitas individuales | ALTO |
| D29 | §16.9 | Múltiples gestoras sin normalización de nombres | MEDIO |
| D30 | §16.9 | Diagnóstico en texto libre abreviado | ALTO |
| D31 | §16.9 | Servicio origen interno vs categoría REM sin mapeo | ALTO |
| D32 | §17.1 | RPM no modelado | ALTO |
| D33 | §17.1 | Sin distinción AA vs ESD | MEDIO |
| D34 | §17.1 | Sin medición estandarizada de outcomes clínicos | ALTO |
| D35 | §17.1 | Sin evaluación SDOH estructurada | MEDIO |
| D36 | §16.15 | Bloque 17:30-20:00 sin operación de ruta | ALTO |
| D37 | §16.15 | Velocidades >100 kph sin protocolo de seguridad vial | MEDIO |
| D38 | §16.15 | 1.895 paradas extra no trazables en 83 días | MEDIO |
| D39 | §16.15 | SUV disponible solo L-V, reduce capacidad fin de semana | MEDIO |

**Totales por severidad:** CRÍTICO: 4, ALTO: 17, MEDIO: 14, BAJO: 2. **Total: 39 (sin cambio respecto a v4b).**

---

## 18. Firma

```
Versión: 4.1
Convención de composición: g ∘ f = right-to-left (estándar matemático)
Categorías: C_op, C_proc, C_rem, C_inst, C_form, C_migr, C_compartido, C_integrado
  C_op: registro individual — pacientes, episodios, visitas, formularios, recursos
  C_proc: dinámica normativa — estados, transiciones, agentes, precondiciones (OPM SD–SD9)
  C_rem: observación estadística — agregados mensuales REM A21 C.1
  C_inst: contexto institucional — capacidad, dotación, cobertura, red
  C_form: formularios clínicos — estructura real de captura de datos en terreno
  C_migr: datos reales — 1698 episodios, 1231 pacientes, estrategias de identidad
  C_compartido: objetos que existen en C_op y C_rem simultáneamente
  C_integrado: pushout de C_op y C_rem sobre C_compartido
Objetos en C_op: 56 (nucleares: 7, plan/tratamiento: 5, registro clínico: 12, ingreso/egreso: 12,
                     contexto/clasificación: 6, recurso: 7, postulación/turno/programación: 7)
Morfismos fundamentales: 43 (nucleares: 12, visita: 3, equipo: 2, domicilio: 3, formulario: 4,
                              derivación: 3, postulación: 3, turno: 3, trabajo social: 2,
                              llamadas: 2, programación: 4, telemetría: 2)
Path Equations: 27 (PE-1 a PE-27)
  PE-1  consistencia domicilio
  PE-2  consistencia temporal
  PE-3  derivación del plan de enfermería
  PE-4  visita dentro del episodio
  PE-5  radio de cobertura ≤20 km
  PE-6  congruencia de identidad del paciente
  PE-7  previsión Fonasa o PRAIS
  PE-8  consistencia REM personas atendidas
  PE-9  consistencia REM origen derivación
  PE-10 consistencia REM cupos
  PE-11 cierre de ficha clínica
  PE-12 cobertura temporal L-D 08:00-19:00 [v3]
  PE-13 estadía máxima 6-8 días (contradicción empírica 2023 documentada) [v3]
  PE-14 protocolo emergencia fuera de horario [v3]
  PE-15 Barthel pareado ingreso/egreso [v3]
  PE-16 postulación precede episodio [v3]
  PE-17 prestación dentro de canasta (24 autorizadas) [v4]
  PE-18 consolidado diario = sum visitas por tipo [v4]
  PE-19 movimientos turno = transiciones del día [v4]
  PE-20 cobertura kine mapea a estado episodio [v4]
  PE-21 evaluación social gate del wide pullback [v4b]
  PE-22 programación diaria cubre pacientes activos [v4b]
  PE-23 VM INGRESO/EGRESO implica transición de estado del episodio [v4b]
  PE-24 prestación programada dentro de canasta [v4b]
  PE-25 ingreso como fan-out multi-profesional (VM INGRESO + ING ENF obligatorios el mismo día) [v4b]
  PE-26 geocodificación habilita verificación automática de PE-5 (radio ≤20 km) [v4b]
  PE-27 match GPS valida ejecución de visita programada (500m + 120min) [v4b]
Construcciones universales:
  - Wide pullback: elegibilidad (8 condiciones convergentes) + checklist como testigo documental [v3]
  - Coproducto: egreso (5+1 variantes) con refinamiento fallecimiento esperado/no esperado
  - Coproducto: canasta de prestaciones (24 prestaciones con código MAI) [v4]
  - Producto: observación ciclo vital (12 componentes, corregido desde 5) [v3]
  - Producto: examen físico de ingreso (6 dominios enum) [v3]
  - Pullback: visita como encuentro (profesional × episodio → equipo)
  - Pushout: integración C_op + C_rem sobre C_compartido
  - Limit: registro enfermería como producto con secciones (4 componentes)
  - Limit: ingreso kinesiología como producto evaluativo (7 componentes)
Tipo Accion: coproducto de 7 variantes (Derivar_APS + Evaluar_Elegibilidad + Ingresar + Planificar + Ejecutar + Monitorear + Egresar)
Coalgebra: EstadoEpisodio con 12 subestados [v3]
  EstadoHospitalizacion: {postulado, elegible, no_elegible, activo, planificado, en_tratamiento, pre_egreso, egresado}
  Estados terminales: no_elegible, egresado (egresado admite seguimiento post-egreso extendido)
Functores: F_REM (C_op → C_rem), F_proc (C_proc → C_op)
Functor Information Loss: 10 en F_REM (FIL-1 a FIL-10), 5 en F_proc (FPIL-1 a FPIL-5)
Déficits estructurales: 39 identificados (ver Apéndice A para tabla consolidada)
  CRÍTICO: 4 (D1, D2, D16, D27)
  ALTO: 17 (D3-D4, D6, D8-D9, D14-D15, D17, D21, D23-D24, D26, D28, D30-D32, D34, D36)
  MEDIO: 14 (D5, D7, D11-D12, D18-D20, D22, D25, D29, D33, D35, D37-D39)
  BAJO: 2 (D10, D13)
Fuentes integradas: 27 (ampliado desde 13)
  [v4b] +Telemetría GPS Wialon (3 vehículos, ene-mar 2026, 7.587 eventos)
  [v4b] +Análisis operacional cruzado (1.574 visitas, 145 geocodificaciones, 1.895 anomalías)
  [v4b] +Presentación DT HODOM HSC (Marp, datos de oportunidad hospitalización y perfil pacientes)
  [v4b] +Consolidado estratégico DT HODOM HSC (diagnóstico + 3 horizontes + prioridades)
  [v4b] +Guión presentación equipo DT
  [v4b] +Marco de rol Director Técnico HODOM HSC
Datos empíricos: 2023-2026, 1698 episodios migrados, 1231 pacientes,
                 141 postulaciones 2026, 368 días consolidado, 106 turnos kine,
                 7 meses registro llamadas, 35 días programación diaria,
                 registro trabajo social jun-oct 2023
Contradicciones documentadas: 3 [v3] (PE-12 proyecto vs CI, PE-13 CI vs dato empírico,
                              PE-14 cobertura visitas vs línea de consulta)
                              + schema drift 2025→2026 [v4]
DDL propuesto para estructura target: 4 tablas nuevas [v4]
  postulacion, prestacion_canasta, entrega_turno + hijas, consolidado_diario (vista materializada)
Mapeo FHIR R5: 11 objetos nucleares con correspondencia directa, 5 sin equivalente nativo [v4b]
Telemetría GPS integrada: 7.587 eventos, 1.574 visitas programadas, 87% match programación↔GPS [v4b]
Geocodificación: 145 direcciones únicas de pacientes con coordenadas [v4b]
```
