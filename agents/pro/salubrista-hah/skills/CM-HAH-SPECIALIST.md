---
_manifest:
  urn: urn:pro:skill:salubrista-hah-hah-specialist:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-HAH-SPECIALIST

## Proposito
Resolver el componente de Hospitalizacion Domiciliaria (HD / HaH) dentro del sistema de hospitalizacion integrado: elegibilidad, operaciones, direccion tecnica, continuidad hospital-domicilio y evidencia. Foco operativo: asistir a Direcciones Tecnicas HD y a la conduccion hospitalaria con criterios, brechas, prioridades y trazabilidad normativa accionable; si el caso viene explicitamente enmarcado en un establecimiento, aterrizar alli el analisis. La normativa y los benchmarks especificos deben extraerse del corpus vigente y, si dependen de vigencia o cifras actuales, verificarse con `web_search` antes de afirmarlos como hechos cerrados.

## Input/Output
- **Input:** subruta: "Eligibility"|"Operations"|"Director"|"Continuity"|"Evidence", problema: string, contexto: object
- **Output:** HAHResult { subruta, análisis, criterios_evaluados: [], recomendaciones: [], trazabilidad_normativa: [], alertas: [], disclaimer }

## Procedimiento
### Sub-ruta A — ELIGIBILITY (criterios ingreso/egreso y pertinencia de modalidad)

1. RESOLVER via `kb_route` los temas normativos de ingreso/egreso HD y recuperar con `knowledge_retrieval` el reglamento base y la norma tecnica pertinentes; si la consulta es de implementacion local del Director Tecnico, complementar con direccion tecnica.
2. RECUPERAR knowledge_retrieval sobre los URNs resueltos y usar ese contenido normativo como baseline antes de evaluar el caso.

**INGRESO** — Verificar los criterios normativos vigentes de ingreso HD y justificar por que HD es la modalidad mas apropiada dentro del continuo hospital-domicilio. Contrastar al menos:

| # | Criterio | Preguntas de verificación |
|---|----------|--------------------------|
| 1 | Perfil de gravedad | ¿Patología aguda o crónico reagudizado que requiere cuidados de intensidad hospitalaria? |
| 2 | Alternativa a cama | ¿Sin HD el paciente requeriría permanencia en atención cerrada? |
| 3 | Condición clínica estable | ¿Equilibrio de funciones vitales que permite traslado seguro al domicilio? |
| 4 | Indicación médica formal | ¿Indicación médica + control médico planificado + plan terapéutico integral? |
| 5 | Condiciones sanitarias domicilio | ¿Agua potable, electricidad, espacio para equipos, posibilidad de aislamientos? |
| 6 | Red de apoyo | ¿Familiar o tutor presente que acompañe y actúe como nexo de comunicación? |
| 7 | Consentimiento informado | ¿Firmado por paciente/representante? + Carta Derechos/Deberes + formulario reclamos |

TIPOLOGIA: clasificar paciente (agudo / crónico reagudizado / condición estable) segun la definicion recuperada del corpus.
RIESGO: identificar criterio mas fragil. Declarar condicion explicita si marginal.
CONTINUIDAD: explicitar articulacion con hospital de origen, equipo HD, cuidador y ruta de rescate.

**EXCLUSION** — Verificar criterios normativos vigentes de exclusion y rescate:
- Inestabilidad hemodinámica / signos vitales fluctuantes / riesgo descompensación → soporte vital avanzado o UPC → EXCLUIR
- Baja complejidad resoluble ambulatoriamente (art. 3: modalidad ambulatoria excluida de regulación HD) → EXCLUIR
- Domicilio sin servicios básicos o sin cuidador responsable → EXCLUIR
- Negativa a consentimiento informado (Ley 20.584) → EXCLUIR

**EGRESO**:
- Alta médica: derivación formal a red ambulatoria + cierre documental en ficha
- Reingreso hospitalario: pérdida condición clínica estable → traslado expedito con soporte vital básico continuo
- Fallecimiento en domicilio: certificación médica, retiro dispositivos, apoyo familiares

### Sub-ruta B — OPERATIONS (gestion clinica y logistica de la unidad HD)

1. RESOLVER via `kb_route` los temas de direccion tecnica, operacion HD y norma tecnica pertinente, y recuperar el contenido con `knowledge_retrieval`.
2. RECUPERAR knowledge_retrieval sobre los URNs resueltos y usar ese contenido como baseline operativo antes de evaluar la unidad.

**Pase de visita diario**:
- Signos vitales: PA + FC + FR + SatO2 → registro en ficha
- Evaluación respuesta terapéutica por cada profesional según rol
- Revisión dispositivos invasivos si aplica (funcionalidad + complicaciones)
- Detección precoz descompensación (→ criterio reingreso)
- Educación cuidador: signos alarma, cuidados actualizados
- Actualización Resumen Clínico en Domicilio (tratamientos + evolución 24h)

**Dispositivos invasivos** — protocolo por tipo:
- VVP: asepsia, fijación, evaluación diaria flebitis, tiempos recambio
- CVC: técnica estéril curación, manipulación lúmenes, administración medicamentos/NP (riesgo CLABSI)
- CUP: técnica aséptica, fijación anti-trauma, circuito cerrado, educación tutor (riesgo CAUTI)
- TQT/TET: aspiración secreciones, curación estoma, recambio cánulas — riesgo vital: O2 + aspiración obligatorios en terreno

**IAAS domiciliaria**:
- Precauciones estándar + aislamientos (contacto/gotitas/respiratorio) adaptados a domicilio
- EPP: inventario en bodega base + dotación en cada vehículo
- Educación cuidadores: higiene de manos, manejo dispositivos, signos alarma infección

**REAS**:
- Segregación: contenedores rígidos corto-punzante + bolsas normadas en domicilio
- Transporte bioseguro: sellados en vehículo, prevenir volcamientos
- Almacenamiento: área exclusiva en base (autorización sanitaria si aplica)
- Eliminación: convenio vigente con empresa autorizada (obligatorio)

**Gestión farmacéutica**:
- Cadena de frío ininterrumpida; monitoreo temperatura/humedad
- 3 vías según tipo prestador: farmacia propia / botiquín autorizado / convenio farmacia comunitaria
- Trazabilidad: entrega/despacho registrado en ficha clínica

**Logística de ruta**:
- Protocolo ruta única: flujograma diario base → domicilios; frecuencia y tipo profesional por visita
- Cálculo simultaneidad: DT debe calcular equipos simultáneos en terreno → cada vehículo porta equipamiento mínimo
- Comunicaciones 24/7: sistema telefónico/radial permanente; trazabilidad de llamadas (fecha, hora, nombres, derivación)

**Emergencia clinica**:
- Competencias de RCP/DEA, equipamiento y protocolos segun la norma vigente recuperada del corpus
- Monitor signos vitales en cada vehículo; O2 si aplica
- Comunicación 24/7 hábil e inhábil; Resumen Clínico en Domicilio disponible para SAMU
- Reingreso: traslado expedito + soporte vital básico continuo
- Plan contingencia cortes energía prolongados (aprobado DT)

**Seguridad personal en terreno**:
- Protocolo agresiones (obligatorio, aprobado DT)
- Evaluación preventiva entorno: animales peligrosos, conflictos familiares, inseguridad barrial
- Entorno hostil grave → criterio egreso inmediato + reingreso hospitalario
- Respaldo laboral: Ley 16.744 (atención médica + psicológica + denuncia)

**Registros obligatorios**:
- Ficha clínica (DS 41/2012): sistema encriptado o sala física exclusiva; acceso restringido equipo clínico
- Protocolo evolución en ficha: registro cada visita (SV, intervenciones, respuesta)
- Protocolo gestión interconsulta: solicitud, respuesta especialista, modificaciones plan — en ficha
- Resumen Clínico en Domicilio: físico en vivienda; actualización obligatoria post-visita
- Consentimiento informado + Carta Derechos/Deberes + formulario reclamos
- Encuestas satisfacción usuaria: obligatorias, registradas en ficha

**Entrega de turno** (SBAR u equivalente):
- Estado de cada paciente ingresado
- Pendientes: exámenes, muestras, interconsultas, recetas
- Articulación ruta del día: dotación vehicular, equipos, monitores

### Sub-ruta C — DIRECTOR (cargo Director Tecnico)

1. RESOLVER via `kb_route` los temas de direccion tecnica, reglamento base y norma tecnica HD, y recuperar el contenido con `knowledge_retrieval`.
2. RECUPERAR knowledge_retrieval sobre los URNs resueltos y usar ese contenido como baseline del cargo antes de emitir obligaciones o brechas.

**Requisitos legales cargo DT**:
- Extraer y citar desde el corpus vigente los requisitos formales del cargo
- Verificar habilitacion profesional, formacion, experiencia, dedicacion y otros requisitos exigibles por la norma vigente

**Responsabilidad legal**:
- **A. Técnico-clínico**: aprobación exclusiva y actualización permanente de todos los manuales y protocolos; supervisión calidad/riesgos/IAAS; supervisión egreso clínico
- **B. Administrativo-organizacional**: Manual de Organización Interna; sistema comunicación trazable; resguardo fichas clínicas; responsabilidad final sobre habilitaciones del equipo (art. 14)
- **C. Frente a SEREMI**: preparación permanente para fiscalizaciones; notificación inmediata de cambio de DT (art. 10)

**Plan de sucesion**:
- Designación formal por escrito del reemplazante
- Requisitos del reemplazante: extraer y citar equivalencia exigida por la norma vigente
- Notificación inmediata a SEREMI + carpeta completa con certificados

**Manuales obligatorios**:
- Manual de Organización Interna: organigrama, roles, turnos, reglamento higiene
- Manuales de protocolos clínicos: todos aprobados exclusivamente por DT
- PAC (Plan Anual de Capacitacion): verificar contenidos y exigencias vigentes en el corpus
- Protocolo comunicación urgencias (hábil e inhábil)
- Protocolo agresiones en terreno
- Plan contingencia cortes de energía

**RRHH bajo responsabilidad DT**:
- Listado actualizado personal con habilitaciones (art. 14): a disposición permanente de SEREMI
- Verificar: inscripción Superintendencia; IAAS vigente; RCP vigente; experiencia acreditada
- HD pediatrica/psiquiatrica: verificar exigencias especificas vigentes en el corpus
- Si el contexto esta explicitamente enmarcado en un establecimiento: traducir estos requisitos a matriz de cumplimiento local, brechas priorizadas, responsables y evidencia documental exigible para fiscalizacion

### Sub-ruta D — CONTINUITY (transicion hospital-domicilio y rescate)

1. RESOLVER via `kb_route` los temas de articulacion hospital-domicilio, modelo HaH de alta complejidad y requisitos tecnicos pertinentes, y recuperar el contenido con `knowledge_retrieval`.
2. RECUPERAR knowledge_retrieval sobre los URNs resueltos y usar ese contenido como baseline antes de emitir recomendaciones.

**Trayectoria integrada**:
- Ingreso a HD desde hospital: criterios clinicos, administrativos y de capacidad
- Plan de egreso precoz: objetivos, ventana de transicion, pendientes criticos
- Resumen de alta / traslado: informacion minima, medicamentos, examenes, alarmas, contacto 24/7
- Coordinacion con APS, rehabilitacion, paliativos u otros dispositivos cuando corresponda
- Ruta de rescate y reingreso: gatillos, responsable de activacion, circuito de traslado
- Cierre del episodio domiciliario: criterios de egreso, seguimiento postalta y prevencion de reingreso evitable

**Riesgos de continuidad**:
- ruptura de informacion
- cuidador insuficientemente preparado
- retraso en rescate
- duplicidad o vacio de responsabilidades
- desalineacion entre capacidad hospitalaria y capacidad HD

### Sub-ruta E — EVIDENCE (evidencia internacional y situacion local)

1. RESOLVER via `kb_route` el tema de evidencia y benchmarks HaH, y recuperar el contenido con `knowledge_retrieval`.
2. RECUPERAR knowledge_retrieval sobre el URN resuelto y usar ese contenido como baseline antes de complementar con evidencia externa.
3. SI necesario → web_search para evidencia actualizada.

**Johns Hopkins HaH Program (Leff et al.)**:
- Referente fundacional para criterios de admision, vias clinicas y estructura del modelo
- Extraer del corpus o verificar por web los outcomes y limites relevantes antes de citarlos como benchmark

**Cochrane Review (Shepperd et al.)**:
- Usar como base para sintetizar efectividad comparada, satisfaccion y limitaciones de la evidencia
- Verificar por web si la pregunta depende de actualizaciones o metaanalisis mas recientes

**CMS AHCAH (EE.UU.)**:
- Usar como referencia regulatoria y operacional solo tras verificar vigencia y estado actual
- No fijar cifras o plazos regulatorios sin validacion web cuando sean relevantes para la respuesta

**Tendencias internacionales**:
- RPM/IoT: telemonitorización continua; FDA Digital Health Framework
- Neural-HaH: IA para detección temprana deterioro clínico
- SNF-at-Home: extensión HaH a cuidados post-agudos (skilled nursing)
- ACOs con HaH integrada: valor longitudinal, no episódico

**Benchmarks Chile**:
- Resolver via `kb_route` el tema de situacion Chile y recuperar con `knowledge_retrieval` datos DEIS, produccion y brechas actuales

## Signature Output
| Campo | Tipo | Descripción |
|-------|------|-------------|
| subruta | string | Eligibility / Operations / Director / Continuity / Evidence |
| análisis | string | Diagnóstico del problema con evidencia/normativa |
| criterios_evaluados | object[] | Solo Eligibility: {criterio, cumple: bool, observacion} |
| recomendaciones | string[] | Con fuente (DS art. / DE Cap. / evidencia) |
| trazabilidad_normativa | string[] | Normativa citada con artículo específico |
| alertas | string[] | Criterios frágiles o riesgos identificados |
| disclaimer | string | "Outputs son apoyo analítico. DS 1/2022 y DE 31/2024 oficiales prevalecen ante cualquier contradicción." |
