---
_manifest:
  urn: "urn:pro:kb:hodom-manual-alta-complejidad"
  provenance:
    created_by: "Codex"
    created_at: "2026-03-10"
    source: "/Users/felixsanhueza/Developer/kora/source/pro/hodom/manual-general-hodom-2026.md"
version: "1.0.0"
status: draft
tags: [hodom, hospitalizacion-domiciliaria, alta-complejidad, hospital-at-home, gestion-clinica]
lang: es
extensions:
  kora:
    family: generic
---

# Manual de Hospitalizacion Domiciliaria de Alta Complejidad

## Fundamentos del modelo Hospital at Home

### Definicion y taxonomia

- `Hospital at Home` (`HaH`) sustituye hospitalizacion tradicional trasladando personal, tecnologia, medicacion y capacidad clinica al domicilio.
- No equivale a:
  - atencion domiciliaria de baja complejidad
  - cuidados paliativos tradicionales sin soporte agudo
  - visitas esporadicas ambulatorias
- Rasgos estructurales:
  - atencion de rango hospitalario
  - evaluacion medica diaria
  - visitas presenciales de enfermeria o personal clinico segun agudeza
  - terapias intravenosas, monitorizacion continua y diagnostico movil
- Distincion central: el hospital se define por intensidad de cuidado y capacidad resolutiva, no solo por infraestructura fisica.

### Evolucion historica y adopcion global

- Primeros desarrollos: Reino Unido, decada de `1970`.
- Adopcion consolidada:
  - Australia
  - Canada
  - Israel
- Victoria, Australia: `6%` de los dias-cama gestionados por programas HaH.
- Estados Unidos:
  - Johns Hopkins, `1995`
  - liderazgo fundacional: Bruce Leff
  - poblacion inicial: geriatria y patologias agudas o cronicas descompensadas

### Triple objetivo y valor sanitario

| Dimension | Evidencia preservada |
| --- | --- |
| Experiencia | Mayor confort, mejor sueno, mayor dignidad percibida |
| Resultados clinicos | Delirium `24%` a `9%`; readmision a `30` dias `23%` a `7%`; menor o igual mortalidad |
| Funcion | Sedentarismo `78.0%` versus `86.0%`; menor tiempo en cama `18%` versus `55%`; mas pasos diarios `834` versus `120` |
| Economia | Reduccion de costos entre `19%` y mas de `30%`; ahorro historico `32%` en Johns Hopkins (`$5,081` vs `$7,480`) |

## Vias clinicas, triaje y seleccion

### Arquitectura de admision

| Modelo | Descripcion | Ventaja | Riesgo |
| --- | --- | --- | --- |
| Evitacion de ingreso | Admision directa desde urgencias, clinicas comunitarias o derivacion ambulatoria | Mayor alivio de congestion y mayor ahorro | Sobreutilizacion o ingreso inapropiado |
| Alta temprana apoyada | Traslado a domicilio tras estancia corta intrahospitalaria | Menor riesgo de admision inadecuada | Menor ahorro total por duplicacion inicial de costos |

### Criterios clinicos de inclusion

- Requiere necesidad documentada de cuidados agudos de nivel hospitalario.
- Exige estabilidad hemodinamica y ausencia de necesidad de resucitacion o soporte vital continuo.
- Validacion de elegibilidad hospitalaria mediante `InterQual`, `MCG Health` o `Dragonfly`.
- Debe existir:
  - diagnostico definido
  - plan terapeutico acotado
  - trayectoria clinica previsible
- Perfil objetivo frecuente:
  - pacientes de `65` anos o mas
  - multimorbilidad
  - alto riesgo de delirium, infeccion nosocomial, caidas o declive funcional si permanecen hospitalizados
- Estada habitual:
  - `5` a `10` dias promedio
  - hasta `30` dias como maximo operativo citado
- Intervenciones activas frecuentes:
  - terapia intravenosa o subcutanea diaria
  - oxigenoterapia
  - kinesioterapia motora o respiratoria
  - curaciones avanzadas
  - ajuste diario de farmacos

### Exclusiones y contraindicaciones absolutas

- inestabilidad hemodinamica
- shock o infarto agudo al miocardio
- requerimiento de `UCI` o monitorizacion invasiva continua
- necesidad de reintervencion quirurgica inminente
- procedimientos invasivos recurrentes:
  - punciones lumbares
  - biopsias multiples
- necesidad de imagenologia avanzada repetida:
  - tomografia computarizada
  - resonancia magnetica
- patologias psiquiatricas severas descompensadas
- necesidad rutinaria de sustancias controladas no aptas para el entorno domiciliario
- dependencia funcional que exige mas de una persona para transferencias basicas
- ausencia de cuidador efectivo o de domicilio apto

### Entorno domiciliario y determinantes sociales

- Requisitos estructurales:
  - electricidad estable
  - agua corriente
  - espacio limpio y ventilado
  - condiciones basicas de seguridad
- Requisitos logisticos:
  - cobertura geografica dentro del radio operativo
  - tiempo de conduccion de referencia: hasta `30` minutos desde hospital base
  - conectividad telefonica y, de preferencia, internet
- Determinantes sociales criticos:
  - red de apoyo
  - alfabetizacion digital
  - seguridad comunitaria
  - acceso a alimentacion adecuada
- Cuidador informal:
  - actua como nexo con el equipo
  - puede apoyar medicacion oral, vigilancia basica y activacion de alertas
  - no debe asumir decisiones clinicas ni procedimientos complejos

## Condiciones clinicas prevalentes

### Insuficiencia cardiaca congestiva

- Candidatos:
  - sobrecarga de volumen
  - necesidad de diureticos intravenosos
  - ausencia de shock cardiogenico o isquemia aguda
- Intervenciones:
  - diureticos intravenosos
  - control de electrolitos
  - peso diario, presion, frecuencia cardiaca y oximetria
  - restriccion de sodio y fluidos

### EPOC y asma

- Requiere vigilancia respiratoria estrecha.
- Intervenciones:
  - corticosteroides
  - antibioticos si corresponde
  - nebulizacion
  - titulacion de oxigenoterapia
- El monitoreo debe permitir umbrales individualizados de `SpO2`.

### Neumonia adquirida en la comunidad

- Requiere oxigenoterapia y antibioticos parenterales en pacientes estables.
- Puede usar:
  - rayos X portatiles
  - monitorizacion remota
  - flebotomia domiciliaria

### ITU complicada y pielonefritis

- Admite antibioticos intravenosos y fluidoterapia.
- Requiere monitoreo de:
  - sepsis
  - funcion renal
  - respuesta clinica temprana

### Celulitis e infecciones de piel

- Modelo idoneo para terapia intravenosa y seguimiento seriado.
- Seguimiento posible por:
  - evaluacion visual directa
  - fotografia clinica
  - videollamada

## Expansion a cirugia y oncologia

### Readmisiones posoperatorias

- Casos elegibles:
  - infeccion de sitio quirurgico
  - ileo paralitico
  - obstruccion
  - deshidratacion
  - cuidado de ostomias
- Criterio de exclusion absoluta:
  - necesidad de reintervencion quirurgica
- Potencial de capacidad:
  - `30.1%` de las readmisiones quirurgicas a `60` dias fueron estimadas como elegibles en un centro academico
  - esa desviacion pudo liberar `4,152` dias-cama y `\$8.8` millones de margen por `backfill`

### Oncologia

- La expansion incluye:
  - quimioterapia domiciliaria
  - soporte agudo post trasplante
  - continuidad a paliativos domiciliarios
- Exigencias:
  - manejo de vias centrales
  - bioseguridad por citotoxicos
  - control de infecciones

## Operaciones clinicas y logistica 24/7

### Centro de comando virtual

- Opera monitoreo biometrico, triaje de alertas y coordinacion continua.
- Puede estar atendido de forma permanente por medicos y enfermeria.
- Funciones minimas:
  - recepcion de datos remotos
  - filtro de alertas
  - contacto proactivo con paciente
  - escalamiento clinico

### Equipo multidisciplinario y frecuencia minima

- Componentes frecuentes:
  - medicos hospitalistas
  - enfermeras de atencion directa
  - paramedicos comunitarios
  - farmaceuticos clinicos
  - trabajadores sociales y gestores de caso
- Protocolo minimo de contacto:
  - `1` evaluacion medica diaria; presencial o virtual segun estabilidad
  - minimo `2` visitas presenciales diarias por enfermeria o personal clinico habilitado
  - respuesta presencial ante crisis en hasta `30` minutos
- Restriccion relevante:
  - los paramedicos pueden contar para visitas presenciales solo bajo supervision clinica de enfermeria o medica
- La frecuencia puede aumentar por agudeza, p. ej. multiples dosis IV o inestabilidad respiratoria.

### Cadena de suministro y ultima milla

- Entrega oportuna de:
  - farmacos intravenosos
  - oxigeno
  - equipos durables
  - alimentacion
- Dependencia alta de subcontratistas logistico-clinicos.
- Requisitos de seguridad:
  - lotes de medicacion preparados para ciclos de `24` horas
  - indicadores termicos y registros continuos de temperatura
  - kits redundantes con medicacion urgente en domicilio cuando aplique
- Sustancias controladas:
  - cadena de custodia estricta
  - embalaje `tamper-evident`
  - baja visibilidad del contenido durante transporte
  - cajas con candado (`lock boxes`) para almacenamiento domiciliario
- Soporte nutricional:
  - integracion con recursos comunitarios
  - convenios directos de distribucion
  - ejemplo de referencia: `Meals on Wheels`

### Control de calidad de proveedores

- Aplicacion de `FMEA` para riesgos de tercerizacion.
- Riesgos tipicos:
  - retrasos de proveedores
  - brechas de competencia del personal externo
  - fallas de cadena de frio
  - perdida de trazabilidad
- Mitigaciones:
  - `SLA`
  - trazabilidad contractual
  - redundancia de servicios criticos

## Infraestructura tecnologica y salud digital

### Monitorizacion remota de pacientes

- Dispositivos de grado clinico, tipicamente aprobados por `FDA`, para:
  - presion arterial
  - frecuencia cardiaca
  - oximetria
  - peso
  - glucosa
- Arquitectura recomendada:
  - conectividad celular `4G/LTE/5G` o hub dedicado
  - respaldo electrico local
  - extensores de senal o mitigacion de cobertura debil
- Admisibilidad operativa:
  - configuracion del dispositivo
  - educacion estructurada al paciente
  - calibracion y mitigacion de errores de uso

### IA y fatiga de alertas

- Uso de algoritmos predictivos para detectar deterioro temprano.
- Necesidad de umbrales individualizados por paciente.
- Jerarquia de escalamiento:
  - Nivel `1`: filtro automatizado y recordatorios
  - Nivel `2`: intervencion protocolizada por enfermeria
  - Nivel `3`: escalamiento medico ante incertidumbre o deterioro refractario
- Dato de contexto:
  - solo alrededor de `6.6%` de ciertas alertas remotas requieren accion clinica real

### Diagnostico movil

- Capacidades minimas frecuentes:
  - rayos X portatiles
  - ecografos `POCUS`
  - electrocardiogramas de `12` derivaciones
- Utilidad:
  - neumonia
  - ICC
  - TVP
  - derrame pleural
  - isquemia o arritmias
- Flujo:
  - adquisicion en domicilio
  - transmision segura
  - lectura remota prioritaria

### Interoperabilidad y EHR

- Integracion con registros clinicos electronicos del hospital.
- Estandares de intercambio:
  - `FHIR`
  - `HL7`
  - `RESTful APIs`
- Reglas de gobernanza:
  - definir si los datos generados por el paciente ingresan automaticamente al `EHR` o pasan por validacion clinica
  - distinguir graficamente datos domiciliarios de mediciones presenciales
- Trazabilidad minima:
  - registro automatizado con `time-stamp`
  - audit logs
  - cifrado en transito y reposo

### Facturacion y auditoria CPT

| Codigo | Hecho operativo preservado |
| --- | --- |
| `99453` | Configuracion inicial del dispositivo y educacion estructurada al paciente |
| `99454` | Provision del dispositivo y transmision diaria; requiere al menos `16` dias de datos en `30` dias continuos |
| `99457` | Primeros `20` minutos mensuales de comunicacion interactiva y gestion clinica |
| `99458` | Cada bloque adicional de `20` minutos |
| `99091` | Recoleccion, analisis e interpretacion de datos fisiologicos continuos |

- La plataforma debe poder emitir reportes de fin de mes con:
  - dias monitorizados
  - tendencias
  - minutos documentados
  - justificacion clinica continua

## Calidad, seguridad y outcomes

### Resultados clinicos comparativos

| Indicador | Hospital tradicional | HaH | Lectura |
| --- | --- | --- | --- |
| Delirium | `24%` | `9%` | Reduccion neurocognitiva relevante |
| Readmision `30` dias | `23%` | `7%` | Menor reingreso en ensayo pivotal |
| Readmision `30` dias adicional | `15.60%` | `8.60%` | Resultado congruente en otra cohorte |
| Visitas a urgencias `30` dias | `13%` | `7%` | Menor uso posalta |
| Visitas a urgencias adicional | `11.70%` | `5.80%` | Contencion de demanda urgente |
| Derivacion a `SNF` | `10.40%` | `1.70%` | Menor institucionalizacion |
| Riesgo relativo de ingreso a largo plazo | `1` | `0.16` | Menor necesidad de cuidados institucionales |
| Sedentarismo diario | `86.0%` | `78.0%` | Mayor movilidad |
| Tiempo en cama | `55%` | `18%` | Menor desacondicionamiento |

- Mortalidad:
  - meta-analisis de `61` ensayos: `OR 0.81`, `IC 95% 0.69-0.95`, `P=0.008`
  - `NNT=50` para prevenir una muerte
  - cohortes especificas: `0.93%` en HaH versus `3.4%` hospitalario
- `HAD`:
  - prevalencia aproximada `30%` en adultos mayores hospitalizados

### Seguridad del paciente

- Riesgos criticos:
  - errores de medicacion
  - transporte y temperatura de farmacos
  - manejo de sustancias controladas
  - fallas de conectividad
- Mitigaciones:
  - dispensacion estandarizada por ciclos de `24` horas
  - escaneo de codigos de barras en punto de atencion
  - evaluacion formal de autoadministracion
  - indicadores termicos y kits de rescate
- Tasas de escalamiento:
  - `7.2%` en datos `AHCAH`
  - `4.8%` en cohorte de pielonefritis aguda
  - interpretacion saludable: normalmente bajo `10%`, pero no cercano a `0%` por sesgo de triaje excesivamente conservador

## Economia de la salud y reembolso

### Costos y capacidad

- Reduccion de costos directos e indirectos entre `19%` y mas de `30%`.
- Ejemplos cuantificados:
  - Johns Hopkins: `32%` menos costo total (`$5,081` vs `$7,480`)
  - Presbyterian: `19%` menos costo medio
  - Brigham and Women's: `38%` menos costo ajustado por episodio
  - Singapur: `42%` menos costo por dia-cama; `24%` menos por episodio; ahorro de `\$1,665`
- Impulsores del ahorro:
  - menor `overhead`
  - menos laboratorios: mediana `3` vs `15`
  - menor uso de imagenes: `14%` vs `44%`
  - menos interconsultas: `2%` vs `31%`
  - menor estancia media en modelos fundacionales: `3.2` vs `4.9` dias
- A `30` dias, la brecha total de ahorro puede ampliarse hasta `25%`.

### Gestion de capacidad y backfill

- Efecto `backfill margin`:
  - libera camas fisicas
  - permite admitir casos de mayor agudeza o quirurgicos
  - mejora margen institucional
- Casos cuantificados:
  - readmisiones quirurgicas elegibles: `30.1%`
  - dias-cama liberados: `4,152`
  - margen potencial: `\$8.8` millones
  - proyeccion de `250` camas virtuales: ahorro de capital cercano a `\$500` millones
  - operadores maduros: `33,000` y `32,000` dias-cama liberados reportados

### Reembolso y regulacion en Estados Unidos

- Programa `Acute Hospital Care at Home` (`AHCAH`) de `CMS`.
- Ley de Asignaciones Consolidadas de `2026`.
- Extension regulatoria descrita hasta `30 de septiembre de 2030`.
- La viabilidad depende de documentacion, codificacion y capacidad de auditoria.

### Atencion basada en valor

- Sinergias con:
  - `ACO`
  - pagos capitados
  - `Medicare Advantage`
  - modelos privados alineados con valor
- Ventaja economica:
  - reduce uso posagudo costoso
  - contiene urgencias
  - evita institucionalizacion

## Experiencia, cuidador y equidad

### Experiencia del paciente

- Escalas validadas:
  - `Picker`: `13.4` vs `11.0`
  - `NPS`: `88.4` vs `45.5`
  - disposicion a reutilizar el servicio: `97.5%`
- Beneficios percibidos:
  - mejor confort: `84.4%` vs `60.9%`
  - mejor calidad de sueno: `74.8%`
  - mayor dignidad y privacidad

### Carga del cuidador

- Riesgos:
  - estres
  - ansiedad
  - carga de vigilancia
  - postergacion del autocuidado
- Dato de aceptabilidad:
  - `47.2%` considera el modelo aceptable
  - `16.6%` lo considera inaceptable, con preocupacion por sobrecarga familiar
- Respuesta requerida:
  - delimitacion estricta entre tareas del cuidador y actos clinicos
  - planes de contingencia y primeros auxilios
  - canales de comunicacion directa con el centro de comando
  - evaluacion psicosocial, p. ej. `Zarit Burden Interview`
  - adaptacion cultural y alfabetizacion en salud digital

### Equidad y acceso

- Contexto rural:
  - `14%` de la poblacion vive en zonas rurales
  - `23%` reporta el acceso a salud como problema mayor
  - tiempo medio al hospital: `34` minutos
  - mas de `150` hospitales rurales cerrados desde `2010`
- Resultados:
  - no se observan diferencias clinicas mayores por etnia o desventaja economica
  - pacientes rurales muestran alta aceptabilidad y satisfaccion superior al `90%` en algunos sistemas
- Exigencias para equidad:
  - competencia cultural
  - mitigacion de brecha digital
  - soporte remoto especializado
  - adaptacion a discapacidad y elegibilidad dual

## Barreras estructurales de implementacion

- resistencia cultural y profesional por percepcion de menor seguridad
- preocupaciones medico-legales y de responsabilidad clinica
- dificultad para identificar pacientes elegibles a tiempo
- complejidad del ecosistema hibrido entre equipos virtuales y presenciales
- barreras de alfabetizacion digital
- falta de banda ancha
- barreras idiomaticas y de literacidad en salud

## Perspectivas 2026-2030

### Inpatient-at-Home

- Admision directa desde APS o comunidad, evitando urgencia cuando el triaje lo permite.
- Requiere:
  - atencion primaria fortalecida
  - grupos de riesgo compartido
  - soporte remoto especializado

### Innovacion biometrica y analitica

- monitoreo bioquimico en tiempo real
- biosensores
- IA predictiva
- biometria conductual para deteccion preclinica

### Ecosistema ampliado de atencion en hogar

- quimioterapia domiciliaria
- rehabilitacion intensiva
- equivalentes funcionales de `SNF-at-home`
- cuidados paliativos avanzados en domicilio

## Tesis operativa del manual

- HaH es una extension de atencion cerrada, no una simplificacion de atencion domiciliaria.
- Su viabilidad depende de:
  - criterios estrictos de elegibilidad
  - minimo operativo `1` evaluacion medica diaria + `2` visitas presenciales
  - logistica `24/7`
  - tecnologia interoperable y auditable
  - control farmacologico y de cadena de frio
  - soporte al cuidador
  - arquitectura financiera sostenible
