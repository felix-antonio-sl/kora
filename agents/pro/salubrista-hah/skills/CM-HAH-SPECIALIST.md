---
_manifest:
  urn: "urn:pro:skill:salubrista-hah-hah-specialist:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-HAH-SPECIALIST

## Propósito
Resolver problemas específicos de Hospitalización Domiciliaria (HD / HaH): criterios de admisión/egreso, gestión operacional, cargo Director Técnico, y evidencia internacional. Norma primaria: DS 1/2022 + DE 31/2024 (Chile). Evidencia base: Johns Hopkins HaH Program, Cochrane/Shepperd, CMS AHCAH. Consultar corpus hodom-* antes que web o modelo.

## I/O

- **Input:** subruta: "Admission"|"Operations"|"Director"|"Evidence", problema: string, contexto: object
- **Output:** HAHResult { subruta, análisis, criterios_evaluados: [], recomendaciones: [], trazabilidad_normativa: [], alertas: [], disclaimer }

## Procedimiento

### Sub-ruta A — ADMISSION (criterios ingreso/egreso)

**INGRESO** — Verificar 7 criterios copulativos (art. 15 DS 1/2022, TODOS deben cumplirse):

| # | Criterio | Preguntas de verificación |
|---|----------|--------------------------|
| 1 | Perfil de gravedad | ¿Patología aguda o crónico reagudizado que requiere cuidados de intensidad hospitalaria? |
| 2 | Alternativa a cama | ¿Sin HD el paciente requeriría permanencia en atención cerrada? |
| 3 | Condición clínica estable | ¿Equilibrio de funciones vitales que permite traslado seguro al domicilio? |
| 4 | Indicación médica formal | ¿Indicación médica + control médico planificado + plan terapéutico integral? |
| 5 | Condiciones sanitarias domicilio | ¿Agua potable, electricidad, espacio para equipos, posibilidad de aislamientos? |
| 6 | Red de apoyo | ¿Familiar o tutor presente que acompañe y actúe como nexo de comunicación? |
| 7 | Consentimiento informado | ¿Firmado por paciente/representante? + Carta Derechos/Deberes + formulario reclamos |

TIPOLOGÍA: clasificar paciente (agudo / crónico reagudizado / condición estable).
RIESGO: identificar criterio más frágil. Declarar condición explícitamente si marginal.

**EXCLUSIÓN** — Verificar criterios (art. 17 DS 1/2022):
- Inestabilidad hemodinámica / signos vitales fluctuantes / riesgo descompensación → soporte vital avanzado o UPC → EXCLUIR
- Baja complejidad resoluble ambulatoriamente (art. 3: modalidad ambulatoria excluida de regulación HD) → EXCLUIR
- Domicilio sin servicios básicos o sin cuidador responsable → EXCLUIR
- Negativa a consentimiento informado (Ley 20.584) → EXCLUIR

**EGRESO**:
- Alta médica: derivación formal a red ambulatoria + cierre documental en ficha
- Reingreso hospitalario: pérdida condición clínica estable → traslado expedito con soporte vital básico continuo
- Fallecimiento en domicilio: certificación médica, retiro dispositivos, apoyo familiares

### Sub-ruta B — OPERATIONS (gestión clínica diaria)

1. CONSULTAR kb_route → `urn:pro:kb:hodom-director-tecnico` (§§ 7-10).

**Pase de visita diario** (obligatorio en cada visita):
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

**IAAS domiciliaria** (RE 60/2022 MINSAL):
- Precauciones estándar + aislamientos (contacto/gotitas/respiratorio) adaptados a domicilio
- EPP: inventario en bodega base + dotación en cada vehículo
- Educación cuidadores: higiene de manos, manejo dispositivos, signos alarma infección

**REAS** (DS 6/2009 MINSAL):
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

**Emergencia clínica**:
- RCP+DEA: todo el personal, mínimo 3h, vigencia 5 años (DE 52/2022 MINSAL)
- Monitor signos vitales en cada vehículo; O2 si aplica
- Comunicación 24/7 hábil e inhábil; Resumen Clínico en Domicilio disponible para SAMU
- Reingreso: traslado expedito + soporte vital básico continuo
- Plan contingencia cortes energía prolongados (aprobado DT)

**Seguridad personal en terreno** (DE 31/2024 Cap. IV):
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

### Sub-ruta C — DIRECTOR (cargo Director Técnico)

1. CONSULTAR kb_route → `urn:pro:kb:hodom-director-tecnico` (§§ 2-5).

**Requisitos legales cargo DT** (art. 9 DS 1/2022):
- Médico cirujano habilitado (inscripción vigente Superintendencia Salud)
- Postítulo/postgrado gestión en salud (IES reconocida)
- Curso IAAS ≥80h, vigencia máxima 5 años
- Experiencia clínica ≥2 años (acreditada con contratos/finiquitos/certificados)
- Jornada mínima 22h semanales en el establecimiento

**Responsabilidad legal** (art. 7 DS 1/2022) — 3 dimensiones:
- **A. Técnico-clínico**: aprobación exclusiva y actualización permanente de todos los manuales y protocolos; supervisión calidad/riesgos/IAAS; supervisión egreso clínico
- **B. Administrativo-organizacional**: Manual de Organización Interna; sistema comunicación trazable; resguardo fichas clínicas; responsabilidad final sobre habilitaciones del equipo (art. 14)
- **C. Frente a SEREMI**: preparación permanente para fiscalizaciones; notificación inmediata de cambio de DT (art. 10)

**Plan de sucesión** (art. 10 DS 1/2022):
- Designación formal por escrito del reemplazante
- Requisitos del reemplazante: idénticos al titular (médico + postgrado + IAAS 80h + 2 años experiencia)
- Notificación inmediata a SEREMI + carpeta completa con certificados

**Manuales obligatorios** (DE 31/2024, mandatado por art. 18 DS 1/2022):
- Manual de Organización Interna: organigrama, roles, turnos, reglamento higiene
- Manuales de protocolos clínicos: todos aprobados exclusivamente por DT
- PAC (Plan Anual de Capacitación): incluye inducción 44h + IAAS + RCP + humanización
- Protocolo comunicación urgencias (hábil e inhábil)
- Protocolo agresiones en terreno
- Plan contingencia cortes de energía

**RRHH bajo responsabilidad DT**:
- Listado actualizado personal con habilitaciones (art. 14): a disposición permanente de SEREMI
- Verificar: inscripción Superintendencia; IAAS vigente; RCP vigente; experiencia acreditada
- HD pediátrica/psiquiátrica: médico especialista o ≥2 años experiencia en servicio de especialidad

### Sub-ruta D — EVIDENCE (evidencia internacional)

1. CONSULTAR kb_route → `urn:pro:kb:hodom-manual-hah`.
2. SI necesario → web_search para evidencia actualizada.

**Johns Hopkins HaH Program (Leff et al.)**:
- Referente global fundacional
- Criterios admisión específicos, vías clínicas estructuradas, outcomes
- Resultados: reducción costos 30-50% vs hospitalización, sin incremento mortalidad

**Cochrane Review (Shepperd et al.)**:
- Evidencia de alta calidad para HaH como alternativa a hospitalización aguda
- Efectividad similar en outcomes clínicos; mayor satisfacción paciente/cuidador
- Reducción de reingresos en ciertos perfiles

**CMS AHCAH (EE.UU.)**:
- Marco regulatorio exenciones reglamentarias; paridad DRG hasta septiembre 2030
- Habilitó >300 hospitales, >100.000 pacientes admitidos
- Estándar de facto para protocolos de seguridad y tecnología RPM

**Tendencias internacionales**:
- RPM/IoT: telemonitorización continua; FDA Digital Health Framework
- Neural-HaH: IA para detección temprana deterioro clínico
- SNF-at-Home: extensión HaH a cuidados post-agudos (skilled nursing)
- ACOs con HaH integrada: valor longitudinal, no episódico

**Benchmarks Chile**:
- Consultar kb_route → `urn:pro:kb:hodom-situacion-chile` para datos DEIS, producción, brechas actuales

## Signature Output

| Campo | Tipo | Descripción |
|-------|------|-------------|
| subruta | string | Admission / Operations / Director / Evidence |
| análisis | string | Diagnóstico del problema con evidencia/normativa |
| criterios_evaluados | object[] | Solo Admission: {criterio, cumple: bool, observacion} |
| recomendaciones | string[] | Con fuente (DS art. / DE Cap. / evidencia) |
| trazabilidad_normativa | string[] | Normativa citada con artículo específico |
| alertas | string[] | Criterios frágiles o riesgos identificados |
| disclaimer | string | "Outputs son apoyo analítico. DS 1/2022 y DE 31/2024 oficiales prevalecen ante cualquier contradicción." |
