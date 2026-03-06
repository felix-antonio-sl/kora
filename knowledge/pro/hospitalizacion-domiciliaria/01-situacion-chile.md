---
_manifest:
  urn: "urn:pro:kb:hodom-situacion-chile"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-03"
    source: "Informe Técnico MINSAL/DEIS: Estado y Situación de la Hospitalización Domiciliaria en Chile 2024-2026"
version: "1.3.0"
status: draft
tags: [hospitalizacion-domiciliaria, chile, politica-salud, fonasa, isapre, grd, epidemiologia, normativa, financiamiento, salud-digital, cuidados-paliativos, telemedicina]
lang: es
---

# Hospitalización Domiciliaria en Chile — Situación 2024-2026

## 1. Contexto epidemiológico y déficit estructural

**Presión demográfica**: envejecimiento poblacional + prevalencia ECNT generan demanda creciente sobre red hospitalaria tradicional. OMS y OPS documentan incremento sostenido en carga de morbimortalidad.

**Déficit camas**: Chile 2 camas/1.000 hab (o 2,1 según estimaciones) vs promedio OCDE 4,7 — brecha estructural histórica.

**Recurso humano**: Chile 2,5 médicos y 2,7 enfermeras por 1.000 hab vs OCDE 3,5 médicos y 8,8 enfermeras.

**Dotación camas país**: total aprox. 37.548 camas — 67% públicas (24.983) + 33% privadas (12.565). RM concentra ~50% camas privadas; resto del país participación privada desciende a 21%; Aysén: 0% camas privadas. SSMOc a inicios 2021: solo 1,1 camas/1.000 hab.

**Evolución HD**: de estrategia de contingencia pandémica (SARS-CoV-2) a modelo estructural consolidado — pilar asistencial integrado en lineamientos MINSAL 2024-2026. Durante pandemia: hospitales sin HD fueron forzados a aperturar unidades con rapidez; unidades existentes maximizaron coberturas de urgencia.

**Definición operativa HD**: alternativa a atención cerrada tradicional; cuidados clínicos de rango hospitalario en domicilio del paciente; equivalencia funcional en calidad y cantidad mediante equipo multiprofesional, monitorización constante e intervenciones terapéuticas complejas.

**Estrategias duales**: evitación de ingreso (admission avoidance) + alta precoz (early discharge).

**Ref**: DEIS/MINSAL 2024; OMS; OPS; DS 1/2022; Norma Técnica HD 2024.

## 1.3 Recomendaciones estratégicas

1. **Integración sociosanitaria y protección cuidador informal**: coordinación mandatoria HD ↔ Chile Cuida ↔ SENAMA; derivación bidireccional; educación continua y soporte psicológico al cuidador; prevención "síndrome del cuidador".
2. **Mitigación brecha territorial mediante telesalud**: interconsultas vía Hospital Digital; destinación profesionales PAO a equipos HD en hospitales comunitarios zonas aisladas.
3. **Escalamiento salud digital y logística clínica**: estándar nacional georreferenciación y enrutamiento vehicular (modelo Sótero del Río); interoperabilidad total FHIR; FCE en domicilio; monitoreo remoto IoT signos vitales; diagnóstico predictivo.
4. **Estandarización Score de Complejidad**: validación técnica externa multicéntrica; aplicabilidad nacional; alinear transferencia recursos financieros según intensidad real de cuidados.

## 2. Marco regulatorio vigente

| Norma | Tipo | Alcance |
|-------|------|---------|
| DS 1/2022 MINSAL | Decreto | Reglamento establecimientos HD — requisitos operacionales |
| Norma Técnica HD (2024) | Norma Técnica | Directrices funcionamiento HD; exigencias infraestructura; manuales obligatorios |
| Norma Técnica 243 (mayo 2025) | Norma Técnica | Taxonomía complejidad hospitalaria: Comunitarios, Provinciales, Regionales/Institutos; HD rol transversal en todos los niveles |
| Ley 20.584 | Ley | Derechos y deberes pacientes; consentimiento informado expreso y firmado |
| Ley 19.628 | Ley | Protección datos sensibles; ficha clínica como dato sensible; custodia mínimo 15 años; exime creación de duplicados si existen informes originales de procedimientos |
| Ley 21.688 | Ley | Interoperabilidad fichas clínicas |

**Posición normativa**: HD definida como modalidad asistencial equivalente a atención cerrada — no es atención ambulatoria de baja complejidad. HD transversal: adultos, pediatría, ginecoobstetricia, salud mental, cuidados paliativos.

**Ref**: DS 1/2022; Norma Técnica HD 2024; NT 243 mayo 2025; Ley 20.584; Ley 19.628; Ley 21.688.

## 3. Criterios de elegibilidad y modelo operativo

### 3.1 Criterios clínicos de inclusión

- Patologías agudas, subagudas o crónicas reagudizadas
- Estabilidad hemodinámica: riesgo vital controlado, no requiere UCI ni vigilancia intensiva continua
- Diagnóstico médico definido + plan terapéutico acotado
- Estancias estimadas: 5-10 días promedio, máximo absoluto 30 días
- Requiere habitualmente ≥2 intervenciones activas: terapia IV/SC diaria, kinesioterapia motora/respiratoria, oxigenoterapia, curaciones avanzadas, ajuste diario fármacos
- Patologías index habituales: IC descompensada, EPOC reagudizado, infecciones respiratorias/urinarias/tejidos blandos tributarias de antibioticoterapia parenteral, manejo postquirúrgico, cuidados paliativos oncológicos (GES-4)

### 3.2 Criterios sociales de inclusión

- Red de apoyo efectiva: cuidador informal disponible como co-terapeuta (capacidad física, cognitiva, disposición)
- Consentimiento informado del paciente y cuidador
- Entorno domiciliario habitable: luz, agua potable, telecomunicaciones, accesibilidad territorial
- Domicilio dentro del radio de cobertura geográfica del prestador/hospital base

### 3.3 Criterios absolutos de exclusión

| Categoría | Criterio |
|-----------|---------|
| Clínica | Inestabilidad sin diagnóstico claro ni plan terapéutico definido |
| Clínica | Descompensación psiquiátrica severa |
| Clínica | Requerimiento vigilancia intensiva continua (UCI) / monitorización hemodinámica invasiva |
| Clínica | Cirugía mayor / reintervención quirúrgica inminente |
| Clínica | Dolor crónico difícil manejo sin patología aguda corregible |
| Clínica | Insuficiencias orgánicas terminales que superen capacidad equipo domiciliario |
| Clínica | Paciente suficientemente estable para manejo ambulatorio (no pertinente HD) |
| Social | Ausencia de cuidador efectivo |
| Social | Negativa a firmar consentimiento informado |
| Social | Nula adherencia indicaciones médicas |
| Social | Entorno domiciliario inhabitable (sanitario, eléctrico, cobertura geográfica) |

**Ref**: DS 1/2022; Norma Técnica HD 2024.

## 4. Indicadores de producción 2019-2024

| Indicador | 2019 | 2024 | Variación |
|-----------|------|------|-----------|
| Pacientes atendidos (nacional) | 70.687 | 166.707 | +135% |
| Días-cama generados (días persona atendidos) | — | 1.432.000 | — |
| Camas virtuales diarias equiv. | — | 3.923 | — |
| Fallecimientos intra-programa | — | 3.683 | 5% personas atendidas |
| Promedio días estada HD | — | 11±3 días | — |

**Score de Categorización de Complejidad (SCC)**: herramienta cuantitativa y objetiva; clasifica diariamente según visitas clínicas/día, procedimientos invasivos (vías venosas, sondas), requerimiento O2.

| Nivel SCC | Puntaje |
|-----------|---------|
| Básico | 0-2 |
| Intermedio | 3-5 |
| Complejo | 6+ |

**Distribución SCC (SSMOc)**:

| Año | Básicas | Intermedias | Complejas |
|-----|---------|-------------|-----------|
| 2018 | 39% | 31% | 30% |
| 2024 | 9% | 42% | 50% |

**Datos SSMOc (2024)**:
- Tasa de ocupación HD: 91% (±3)
- Tasa de reingreso a hospitalización tradicional: 4,1% (41/1.000 atendidos)
- Tasa reingreso osciló entre 2±2 y 6±1 según hospital base de derivación
- Mortalidad intra-programa: → ver §4 tabla indicadores (3.683 fallecimientos = 5% personas atendidas)

**Fuente datos**: DEIS, formulario REM A21 Sección C.

**Ref**: DEIS/MINSAL 2024; SSMOc datos operativos 2018-2024.

## 5. Recursos humanos e infraestructura

### 5.1 Dirección Técnica (DT)

| Requisito | Especificación |
|-----------|---------------|
| Perfil | Médico Cirujano |
| Experiencia | 2 años clínicos mínimo |
| Formación | Postítulo/postgrado gestión en salud + IAAS (mínimo 80 horas, vigencia 5 años) + RCP/DEA |
| Jornada | Mínimo 22 horas semanales presenciales en recinto base |
| Plan sucesión | Reemplazante temporal designado con mismos requisitos mínimos |

### 5.2 Coordinación operativa

| Requisito | Especificación |
|-----------|---------------|
| Perfil | Profesional de salud (habitualmente enfermería) |
| Experiencia | ≥5 años experiencia clínica |
| Formación | Postítulo/postgrado gestión en salud + IAAS 80 horas (vigencia 5 años) + soporte vital básico |

### 5.3 Equipo multiprofesional

| Rol | Requisitos clave |
|-----|----------------|
| Médicos atención directa | Habilitación Superintendencia de Salud |
| Médicos reguladores | Habilitación + competencias regulación |
| Enfermería, Kinesiología | Certificaciones vigentes; kinesiólogos ≥2 años experiencia + soporte vital básico |
| HD pediátrica | Médico especialista pediatría o médico general con ≥2 años experiencia en servicios pediátricos |
| HD psiquiátrica | Médico especialista psiquiatría o médico general con ≥2 años experiencia en unidades salud mental |

**Inducción obligatoria**: 44 horas teórico-prácticas para personal nuevo.

**Plan Anual de Capacitación (PAC)**: actualización IAAS; RCP básico + DEA; humanización; trato usuario.

### 5.4 Infraestructura base (Norma Técnica HD 2024)

- Sistemas de comunicación telefónica/radial con grabación continua o registro auditable
- Soporte informático
- Sistemas de respaldo de energía eléctrica
- Áreas REAS: manejo transitorio residuos especiales; bodega almacenamiento con control temperatura y cadena de frío

### 5.5 Gestión de riesgos y bioseguridad

- REAS: procedimiento retiro/transporte/eliminación residuos biológicos domicilio (DS 6/2009); bodega con control temperatura y cadena de frío
- Prevención caídas: protocolos específicos para entorno domiciliario; barandillas laterales con protección; iluminación nocturna; higiene y lubricación piel (prevención úlceras por presión)
- Emergencias: plan respuesta con rescate médico, comunicación 24/7 telefónica/radial con grabación continua o registro auditable
- Protocolo actuación frente a agresiones al equipo de salud en terreno
- Equipamiento mínimo terreno: monitorización PA, FC, FR, SpO2

**Ref**: DS 1/2022; DS 6/2009; Norma Técnica HD 2024.

## 6. Arquitectura financiera

### 6.1 Sistema público (FONASA)

| Mecanismo | Descripción | Estado |
|-----------|-------------|--------|
| MAI (Modalidad Atención Institucional) | Financiamiento histórico tradicional — asignación presupuestaria centralizada; gratuito tramos A y B + mayores 60 años | Vigente, en transición |
| GRD (Grupos Relacionados por Diagnóstico) | Pago por egreso; HD imputable como egreso hospitalario; pesos relativos (Outliers/Inliers); incorporación reciente Traiguén, Puerto Aysén, Peñaflor y Ancud | En expansión: 80 hospitales en 2026 |
| MCC (Modalidad Cobertura Complementaria) | Ley N° 21.674; NT 238; código 0201408 "Día Cama HD Baja Complejidad"; tramos B, C y D; prima complementaria voluntaria; permite a beneficiarios FONASA acceder a prestadores privados con protección financiera; arancel incluye teleconsultas médicas, enfermería, telerehabilitación kinesiológica, insumos y medicamentos generales | Vigente desde 2024-2025 |

**Presupuesto MINSAL 2026**: >30 billones pesos; aumento real 5,6% respecto año anterior; aumento histórico 30% acumulado desde 2022. Glosas específicas para normalización días-cama y ventilación domiciliaria (pacientes electrodependientes, liberación cupos UCI).

### 6.2 Sistema privado (ISAPRE)

| Mecanismo | Descripción |
|-----------|-------------|
| Planes complementarios | Bonificación HD con auditoría de pertinencia médica |
| CAEC (Cobertura Adicional Enfermedades Catastróficas) | Financia 100% tras deducible; HD excluida por regla general |

**Excepciones CAEC (Circular IF N° 7)** — 3 criterios copulativos:
1. Paciente debe estar previamente hospitalizado de manera convencional y requerir continuidad de tratamiento activo
2. Médico tratante prescriptor debe ser distinto e independiente al médico supervisor/director técnico de empresa proveedora HD
3. Isapre debe autorizar pertinencia y derivar formalmente a prestador HD perteneciente a su red CAEC

**Justificación restricción CAEC**: prevenir riesgo moral — evitar que seguros catastróficos financien cuidados crónicos de larga data, residencias geriátricas encubiertas o servicios de enfermería básica sin nivel de riesgo catastrófico.

**Ref**: NT 238 MINSAL; Ley 21.674; Circular IF N° 7 Superintendencia Salud; Ley de Presupuestos 2026.

## 7. Sector privado

### 7.1 Prestadores especializados

| Prestador | Perfil |
|-----------|--------|
| Home Medical Clinic (HMC) | >25 años experiencia; >27.000 pacientes atendidos; Ficha Electrónica en domicilio conectada a Central de Enfermería 24h; Medical Hilfe (unidad pediátrica intensiva); alianza rescate médico HELP S.A. |
| GrupoSalud CHBS (Clínica Hogar Buena Salud) | Cobertura nacional: equipos en todas capitales regionales; implementación HD <4 días hábiles; cartera: terminales, ventilación, clínica neurológica (ACV, TEC, lesiones medulares) |
| Clínica Universidad de los Andes | Pioneros HD Chile; RM (Las Condes, Lo Barnechea, Vitacura); estancias promedio 10 días, máximo 30; terapias IV, oxigenoterapia, curaciones avanzadas; excluye: patologías salud mental descompensadas y dependencias severas sin cuidador efectivo |
| Domihealth | Orientado adulto mayor; EPOC, demencia; capacidad diagnóstica domiciliaria: radiografías portátiles, ecografías, Doppler |

### 7.2 Ranking Merco Salud Chile 2025

Instrumento de reputación corporativa, auditado por KPMG. Combina indicadores objetivos de desempeño clínico + percepción de profesionales médicos, directivos y equipos de salud.

- Clínica Alemana de Santiago: líder en 18 servicios clínicos (incl. ortopedia y traumatología)
- RedSalud Elqui (Coquimbo) y RedSalud Mayor Temuco (Araucanía): reconocidas entre centros con mejor reputación nacional

### 7.3 Alianzas público-privadas y licitaciones

**Licitaciones 2026**: $57.804 millones compra estratégica FONASA para prestaciones NO GES y Sistema de Acceso Priorizado (SAP); ~15.000 cirugías al sector privado (HD privada asume manejo postoperatorio temprano / alta precoz).

MCC: incentiva clínicas privadas a ofrecer cupos HD para beneficiarios FONASA (→ código 0201408, ver §6.1).

**GES-4 oncológico**: prestadores como Oncovida activan HD para analgesia compleja, hidratación parenteral y soporte multidisciplinario en final de vida (→ plazos y copagos GES-4: ver §9.1).

**Ref**: Merco Salud Chile 2025; Ley Presupuestos 2026; NT 238.

## 8. Salud digital e interoperabilidad

| Componente | Descripción |
|------------|-------------|
| Telemonitorización | IoT + wearables + FCE móvil — datos en tiempo real desde domicilio |
| Telemedicina | Representará ~30% de interacciones sanitarias para 2026 |
| Georreferenciación | Hospital Sótero del Río: piloto iniciado a fines de 2025; >156.000 atenciones HD 2024; programa "Juégatela por la Innovación" (MINSAL, Corfo, CENS, Pro Salud Chile); plataforma Raylex; enrutamiento dinámico en tiempo real (tráfico, clima, seguridad ruta, especialidad médica requerida) |
| Interoperabilidad | HL7 FHIR: comunicación bidireccional HD ↔ APS ↔ centros de referencia; Ley 21.688 interoperabilidad fichas clínicas |
| IA predictiva | Diagnóstico precoz de descompensaciones + algoritmos asignación de rutas vehiculares |

**MCC arancel incluye**: teleconsultas médicas, teleconsultas enfermería, telerehabilitación kinesiológica.

**Ref**: Piloto Sótero del Río / Raylex; Ley 21.688; NT HCE/Interoperabilidad MINSAL; HL7 FHIR.

## 9. Poblaciones especiales

### 9.1 Oncológicos y cuidados paliativos (GES-4)

- GES N° 4: "Alivio del dolor y cuidados paliativos por cáncer avanzado"
- Cualquier edad, diagnóstico confirmado, independiente de estadio
- Inicio tratamiento: máximo 5 días desde confirmación diagnóstica
- Copago: 0% FONASA; 20% Isapres
- Prestaciones: medicamentos (analgesia compleja, opioides, hidratación parenteral), insumos, exámenes
- Equipo multiprofesional obligatorio: médicos, enfermeras, psicólogos, trabajadores sociales
- Técnica COPE para cuidadores: Creatividad, Optimismo, Planificación, Información de Expertos
- Soporte estructurado al duelo familiar post-fallecimiento; umbral duelo patológico: síntomas incapacitantes >6 meses

### 9.2 Geriátricos y dependencia severa

**Chile Cuida** presupuesto 2026: $54.801 millones (23,6% crecimiento respecto 2025); 100 Centros Comunitarios de Cuidados a nivel nacional; continuidad programa "Chile te Cuida" (respiro cuidadoras no remuneradas).

**SENAMA Cuidados Domiciliarios** presupuesto 2026: $3.580 millones (94% crecimiento acumulado en cuatrienio). Dirigido a: mayores 60 años, dependencia moderada o severa, 60% más vulnerable del Registro Social de Hogares, sin cuidador principal. Provisión asistentes apoyo domiciliario; retrasa institucionalización.

### 9.3 Infanto-juvenil

- HD pediátrica: médico especialista pediatría o médico general con ≥2 años experiencia pediátrica
- Sector privado: Medical Hilfe (HMC) — infecciones respiratorias agudas, neurorehabilitación pediátrica, ventilación mecánica invasiva domiciliaria
- Cuidador primario (padres) como co-terapeuta: capacitación en reanimación básica, manejo ostomías, administración fármacos IV
- Abordaje salud mental infanto-juvenil ante familiar en fase terminal

**Ref**: GES-4 MINSAL; Chile Cuida; SENAMA; Ley Presupuestos 2026; Norma Técnica HD 2024.

## 10. Brechas y desafíos estratégicos

| Brecha | Descripción | Plan propuesto |
|--------|-------------|----------------|
| Inequidad territorial | HD alta/mediana complejidad concentrada en zonas urbanas metropolitanas; déficit en regiones rurales/extremas | Expansión hospitales comunitarios; telemedicina; PAO zonas extremas |
| Cuidador informal | "Síndrome del Cuidador": estrés, ansiedad, carga de vigilancia transferida a familias | Integración sociosanitaria + apoyo formal del Estado (Chile Cuida + SENAMA) |
| Estandarización SCC | Score Complejidad validado localmente (SSMOc) sin escalabilidad nacional formal | Validación externa multicéntrica + correlación con desenlaces clínicos duros |
| Trazabilidad financiera GRD | Imputación incorrecta CMBD (CIE-10/CIE-9MC) → subvaloración egresos HD → desfinanciamiento hospitales comunitarios | Protocolos GRD específicos HD; integración SCC con sistemas información GRD |
| Formación especialistas | Déficit médicos especialistas en regiones | Glosa 52 Ley Presupuestos 2026: informe técnico formación/retención especialistas; PAO zonas extremas |
| Plan Acción 2026-2030 | Consolidación definitiva modelo domiciliario como pilar permanente del sistema | Plan Gubernamental 2026-2030 MINSAL |

**Ref**: DEIS/MINSAL 2024; NT 243 mayo 2025; Ley Presupuestos 2026 (Glosa 52).

## Anexo A: Fichas indicadores REM para HD

**Fuente datos**: DEIS, formulario REM A21 Sección C.

| Ficha | Indicador | Definición | Dato 2024 |
|-------|-----------|-----------|-----------|
| N°1 | Personas atendidas HD | Total pacientes (traspasos + ingresos mes) | → ver §4 |
| N°2 | Días persona atendidos (días cama HD) | Sumatoria días hospitalización por paciente | → ver §4 |
| N°3 | Camas estimadas (capacidad diaria) | Días persona / 365 | → ver §4 |
| N°4 | Tasa reingreso | Reingresos a hosp. tradicional / personas atendidas × 100 | → ver §4 |
| N°5 | Visitas domiciliarias promedio | Total visitas / personas atendidas | ~13 visitas estándar esperado por caso |
| N°6 | Indicadores complementarios | Ocupación, promedio días estada, fallecidos no esperados | → ver §4 |

## Anexo B: Consentimiento informado HD

Estructura estandarizada — 5 dominios (Ley 20.584; DS 1/2022):

1. **Identificación de las partes**: paciente (nombre, RUT, fecha nacimiento, domicilio, previsión) + cuidador/tutor (nombre, RUT, parentesco)
2. **Declaración información clínica**: diagnóstico principal, plan terapéutico, tiempo estimado estadía (promedio 10 días, máximo 30), riesgos/beneficios/alternativas
3. **Compromisos cuidador/paciente**: mantener habitabilidad (luz, agua, conectividad); presencia continua cuidador; autorizar ingreso equipo clínico al domicilio
4. **Certificación entrega documentación**: Carta Derechos y Deberes (Ley 20.584); mecanismo interposición reclamos; resumen clínico en domicilio (diagnósticos, evolución, cuidados, teléfonos emergencia)
5. **Firmas**: paciente (si estado cognitivo/clínico lo permite) + cuidador/tutor + profesional salud ingresante + lugar, fecha, hora

**Protocolos urgencia domiciliaria**:
- Emergencia clínica: alerta continua, triage, rescate médico SAMU/ambulancia
- Manejo de caídas: evaluar contusiones, riesgo fracturas espontáneas, traumatismos; técnicas seguras levantamiento paciente sin lesiones secundarias
- Voluntades anticipadas y órdenes de no reanimar (paliativos GES-4): prevención obstinación terapéutica; directrices médicas claras en ficha clínica domiciliaria; coordinación con SAMU para alertar que domicilio corresponde a paciente paliativo subsidiario de manejo proporcional (analgesia y confort sobre maniobras invasivas)
- Agresiones al equipo: evaluación entorno, evacuación, georreferenciación

## Anexo C: Análisis territorial brechas cobertura

**Metodología**: 3 anillos concéntricos cobertura:
- Cobertura 1 (Local): misma comuna del hospital base
- Cobertura 2 (Adyacente): comunas con bordes territoriales compartidos
- Cobertura 3 (No adyacente): población lejana o derivada desde otras regiones

**Análisis clúster K-Means**: 177 hospitales públicos, 5 clases:

| Clase | n | Perfil | Cobertura local | Cobertura adyacente |
|-------|---|--------|----------------|---------------------|
| 1 | 32 | Media variabilidad; Calama a Coyhaique; alta/mediana complejidad urbana | 57,6% | 23,7% |
| 2 | 15 | Media baja variabilidad; capitales regionales/áreas metropolitanas | 64,4% | 23,6% |
| 3 | 112 | Muy baja variabilidad; Tocopilla a Cabo de Hornos; hospitales comunitarios; alta ruralidad/zonas extremas | 81,9% | — |
| 4 | 4 | Alta variabilidad; referencia nacional | 41,2-47,1% | alta proporción adyacentes/no adyacentes |
| 5 | 14 | Muy alta variabilidad; referencia nacional (RM, Biobío, Valparaíso, Araucanía) | 41,2-47,1% | hasta 16,5% no adyacente |

**Implicancias planificación**: focalizar telemedicina en 112 hospitales Clase 3; priorizar PAO macrozonas baja densidad camas; escalar modelo georreferenciación Raylex/Sótero del Río a nivel nacional.

## Anexo D: Glosario

| Acrónimo | Definición |
|----------|-----------|
| CAEC | Cobertura Adicional para Enfermedades Catastróficas — beneficio Isapres; financia tras deducible; excluye HD por regla general salvo excepciones calificadas |
| CMBD | Conjunto Mínimo Básico de Datos — codificación CIE-10 (diagnósticos) y CIE-9MC (procedimientos) para clasificación GRD |
| GES | Garantías Explícitas en Salud — acceso, oportunidad, calidad y protección financiera para problemas de salud específicos |
| GRD | Grupos Relacionados por Diagnóstico — sistema clasificación pacientes; pago por resolución integral episodio; Peso Relativo × precio base |
| HD | Hospitalización Domiciliaria — modalidad asistencial alternativa a atención cerrada; cuidados rango hospitalario en domicilio |
| IAAS | Infecciones Asociadas a la Atención de Salud — curso prevención ≥80 horas, vigencia 5 años; exigido para DT y coordinación enfermería |
| Inliers/Outliers | Clasificación duración episodio bajo GRD; Inliers = estadía dentro rangos normalidad; Outliers Superiores = estadía excesiva → carencias pago |
| IoT/Wearables | Dispositivos salud portátiles; telemonitorización constantes vitales (FC, SpO2, PA, temperatura) |
| MCC | Modalidad Cobertura Complementaria — Ley 21.674; tramos B, C, D FONASA; prima voluntaria; red prestadores privados (→ código arancel y detalle prestaciones: ver §6.1) |
| SCC | Score Categorización Complejidad — Básico (0-2), Intermedio (3-5), Complejo (6+); visitas/día, O2, procedimientos invasivos |
