---
_manifest:
  urn: urn:gn:kb:intro-gores-nuble
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/01_fundamentos/intro/kb_gn_000_intro_gores_nuble_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- descentralizacion
- nuble
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/01_fundamentos/intro/kb_gn_000_intro_gores_nuble_koda.yml
    source_hashes:
      domains/gn/01_fundamentos/intro/kb_gn_000_intro_gores_nuble_koda.yml: 6730e5ceba5f3eb7c02231414c416dff13f341f0e022e51280ca9c5bc33bc15e
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.16
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 17
    meat_count: 1262
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gobernanza__intro-gores-nuble.md.json
---

# Guía Integral de la Administración Regional de Ñuble
## ID
GORE-NUBLE-GUIA-INTEGRAL-01

## Version
2.0.0

## Status
Published

## Human Creator
FS

## Human Editor
FS

## Model Collaborator
IA-GEMINI

## Creation Date
2025-07-10

## Modification Date
2025-12-15

## Ctx
Guía técnico-operativa integral para la administración del Gobierno Regional de Ñuble (GORE Ñuble).

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-01
### Req
Mandatory block following Metadata.
### Prohib
Using for artifact creation or translation.
### Content
BEGIN_LLM_INSTRUCTIONS
You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.
FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).
LEXICON (expand before processing): Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context, Def->Definition, Fnd->Foundation, ID->ID, Mech->Mechanism, Mssn->Mission, Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result, Resp->Responsible, Src->Source, Warn->Warning.
REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. External documents and legal sources are mentioned as contextual information under Ctx: or Src:.
LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
END_LLM_INSTRUCTIONS


## Glosario Conceptos Clave
### ID
GN-GLOSARIO-01
### Purp
Facilitar la lectura del artefacto mediante definiciones breves de siglas y conceptos recurrentes.
### Terminos
| ID | Sigla | Nombre | Def |
| --- | --- | --- | --- |
| GN-GLOS-GORE | GORE | Gobierno Regional | Entidad pública autónoma, con personalidad jurídica y patrimonio propio, encargada de la administración superior de la región. |
| GN-GLOS-CORE | CORE | Consejo Regional | Órgano colegiado del Gobierno Regional, con facultades normativas, resolutivas y fiscalizadoras. |
| GN-GLOS-DPR | DPR | Delegado Presidencial Regional | Representante del Presidente de la República que ejerce el gobierno interior de la región y coordina servicios públicos nacionales. |
| GN-GLOS-DPP | DPP | Delegado Presidencial Provincial | Representante del Presidente en la provincia, encargado del orden público y coordinación de servicios a nivel provincial. |
| GN-GLOS-SEREMI | SEREMI | Secretaría Regional Ministerial | Representante regional de un ministerio, responsable de implementar políticas sectoriales en la región. |
| GN-GLOS-FNDR | FNDR | Fondo Nacional de Desarrollo Regional | Principal fondo de inversión regional, destinado a financiar proyectos y programas priorizados por el GORE. |
| GN-GLOS-FRPD | FRPD | Fondo Regional para la Productividad y el Desarrollo | Fondo financiado por el Royalty Minero para apoyar iniciativas de innovación, competitividad y fomento productivo. |
| GN-GLOS-FRIL | FRIL | Fondo Regional de Iniciativa Local | Fondo orientado a proyectos de infraestructura de menor escala, ejecutados principalmente por municipalidades. |
| GN-GLOS-ISAR | ISAR | Inversiones Sectoriales de Asignación Regional | Recursos de ministerios cuyo destino territorial es decidido por el GORE según prioridades regionales. |
| GN-GLOS-ERD | ERD | Estrategia Regional de Desarrollo | Instrumento de planificación de largo plazo que define visión, ejes y objetivos estratégicos para la región. |
| GN-GLOS-PROT | PROT | Plan Regional de Ordenamiento Territorial | Instrumento vinculante que orienta el uso del territorio regional y la localización de inversiones. |
| GN-GLOS-ZUBC | ZUBC | Zonificación del Uso del Borde Costero | Instrumento que define usos y prioridades del borde costero regional. |
| GN-GLOS-PLADETUR | PLADETUR | Plan Regional de Desarrollo Turístico | Instrumento que orienta el desarrollo del turismo en la región. |
| GN-GLOS-IPR | IPR | Intervención Pública Regional | Concepto paraguas que agrupa iniciativas de inversión (IDI) y programas públicos regionales (PPR). |
| GN-GLOS-IDI | IDI | Iniciativa de Inversión | Proyecto de inversión financiado con gasto de capital para crear o mejorar activos físicos o capital humano durable. |
| GN-GLOS-PPR | PPR | Programa Público Regional | Programa financiado principalmente con gasto corriente o mixto para entregar servicios o beneficios a la población. |
| GN-GLOS-SISREC | SISREC | Sistema de Rendición Electrónica de Cuentas | Plataforma de la Contraloría General de la República para gestionar rendiciones de cuentas de transferencias. |
| GN-GLOS-SIGFE | SIGFE | Sistema de Información para la Gestión Financiera del Estado | Sistema contable-financiero oficial donde se registran los movimientos presupuestarios del GORE. |
| GN-GLOS-BIP | BIP | Banco Integrado de Proyectos | Sistema que registra y monitorea iniciativas de inversión pública, incluyendo proyectos financiados con FNDR. |
| GN-GLOS-SNI | SNI | Sistema Nacional de Inversiones | Marco y plataforma para la evaluación técnico-económica de proyectos de inversión pública. |
| GN-GLOS-DIPIR | DIPIR | División de Presupuesto e Inversión Regional | División del GORE encargada de elaborar, ejecutar y controlar el presupuesto de inversión regional. |
| GN-GLOS-DIPLADE | DIPLADE | División de Planificación y Desarrollo Regional | División responsable de formular instrumentos de planificación y coordinar la estrategia de desarrollo regional. |
| GN-GLOS-DAF | DAF | División de Administración y Finanzas | División encargada de la gestión administrativa interna, finanzas, recursos humanos y abastecimiento del GORE. |
| GN-GLOS-DIFOI | DIFOI | División de Fomento e Industria | División encargada de políticas y programas de fomento productivo, ciencia, tecnología e innovación. |
| GN-GLOS-DIT | DIT | División de Infraestructura y Transportes | División encargada de planificar, ejecutar y supervisar programas y proyectos de infraestructura y transporte. |
| GN-GLOS-DIDESOH | DIDESOH | División de Desarrollo Social y Humano | División encargada de programas e iniciativas orientadas a cohesión social, inclusión y acceso a servicios. |
| GN-GLOS-SINAPRED | SINAPRED | Sistema Nacional de Prevención y Respuesta ante Desastres | Sistema que organiza la gestión del riesgo de desastres en Chile, asignando roles específicos a los gobiernos regionales. |
| GN-GLOS-SGD | SGD | Secretaría de Gobierno Digital | Órgano rector de la Estrategia de Gobierno Digital y de las plataformas transversales de transformación digital del Estado. |
| GN-GLOS-TDE | TDE | Transformación Digital del Estado | Proceso de modernización del Estado basado en el uso estratégico de tecnologías digitales, datos e identidad digital. |

## Parte I Fundamentos y Contexto
### ID
GORE-NUBLE-GUIA-PARTE1-FUNDAMENTOS-01
### Titulo
Parte I: Fundamentos y Contexto de la Administración Regional en Ñuble
### Introduccion General
#### ID
GORE-NUBLE-GUIA-INTRO-GENERAL-01
#### Proposito Alcance Estructura
#### ID
GORE-NUBLE-GUIA-INTRO-PROPOSITO-01
#### Purp
Guía técnico-operativa integral para administración GORE Ñuble.
#### Obj
Asistir a funcionarios, autoridades y expertos en el desempeño de sus funciones.
#### Ctx
Integra marco normativo general con contexto institucional específico. Vigencia para el año presupuestario 2026 (Ley N°21.796).
#### Alcance
| Cpt |
| --- |
| Caracterización y contexto de la Región de Ñuble. |
| Marco constitucional y legal. |
| Estructura organizacional del GORE Ñuble. |
| Competencias del GORE. |
| Procesos de inversión y financiamiento. |
| Diagnóstico estratégico de la Región de Ñuble. |
#### Estructura
| Cpt |
| --- |
| Parte-I: Fundamentos y Contexto de la Administración Regional en Ñuble. |
| Parte-II: El Gobierno Regional de Ñuble: Estructura, Funciones y Competencias. |
| Parte-III: Gestión Financiera y de Inversiones. |
| Parte-IV: Diagnóstico Estratégico para la Región de Ñuble. |
#### Actualizaciones Normativas e Institucionales 2026
#### ID
GORE-NUBLE-GUIA-INTRO-ACTUALIZACIONES-01
#### Nuevas Leyes Organicas y Reformas Clave
#### ID
GORE-NUBLE-GUIA-INTRO-LEYES-CLAVE-01
#### Ley 21074 Fortalecimiento Regionalizacion
#### Cpt
Ley-21074 (Fortalecimiento de la Regionalización, 2018).
#### Ctx
Plenamente vigente.
#### Act
- Elección democrática y directa de Gobernadores Regionales.
- Nueva estructura de divisiones administrativas en el GORE.
- Ampliación y mecanismo de transferencia de atribuciones.
- Modifica Ley N°19.175 (LOC GORE).
#### Ley 21730 Ministerio Seguridad Publica
#### Cpt
Ley-21730 (Crea Ministerio de Seguridad Pública, 2023).
#### Act
- Separa funciones de seguridad ciudadana y orden público del Ministerio del Interior.
#### Ctx
Impacto-Regional significativo.
#### Ley 21719 Proteccion Datos Personales
#### Cpt
Ley-21719 (Protección de Datos Personales, 2023).
#### Act
- Moderniza marco regulatorio.
- Crea Agencia de Protección de Datos Personales.
#### Req
- Nuevas obligaciones para el GORE en tratamiento de datos personales.
#### Ley 21180 Transformacion Digital Estado
#### Cpt
Ley-21180 (Transformación Digital del Estado, 2019).
#### Ctx
Plazos de implementación progresivos.
#### Req
- GORE debe tramitar procedimientos administrativos por medios electrónicos.
#### Obj
- Eliminar uso de papel.
- Modernizar la gestión administrativa.
#### Creacion Ministerio Seguridad Publica Impacto Regional
#### ID
GORE-NUBLE-GUIA-INTRO-MINSEG-01
#### Src
Ley N°21.730 (2023).
#### Impactos Principales
-
  #### Res
  Nuevos SEREMI de Seguridad Pública en cada región.
-
  #### Res
  Fortalecimiento de Consejos Regionales de Seguridad Pública.
  #### Resp
  - Preside Delegado Presidencial Regional (DPR).
  - Secretaría Ejecutiva a cargo del SEREMI de Seguridad Pública.
-
  #### Res
  Dependencia administrativa de Carabineros y PDI del Ministerio de Seguridad Pública.
-
  #### Res
  Nueva coordinación GORE-Seguridad Pública.
  #### Ctx
  Rol del GORE más explícito en prevención del delito, en coordinación con el nuevo ministerio.
#### Avances Transformacion Digital y Proteccion Datos
#### ID
GORE-NUBLE-GUIA-INTRO-DIGITAL-DATOS-01
#### Transformacion Digital Ley 21180
#### Cpt
Transformación Digital (Ley N°21.180).
#### Ctx
Avance considerable a diciembre 2025.
#### Req
- Procedimientos administrativos en plataformas electrónicas.
- Uso generalizado de firma electrónica avanzada.
- Progresiva eliminación del papel.
#### Principios
| Cpt |
| --- |
| Principio de Interoperabilidad. |
| Principio de Neutralidad tecnológica. |
| Principio de adecuada conservación documental digital. |
#### Proteccion Datos Ley 21719
#### Cpt
Protección de Datos Personales (Ley N°21.719).
#### Req
- GORE sujeto a principios y obligaciones estrictas en tratamiento de datos (Licitud, finalidad, proporcionalidad, seguridad).
#### Resp
- GORE responde ante la nueva Agencia de Protección de Datos Personales.
- Posible designación de delegados de protección de datos en el GORE.
#### Descentralizacion Fiscal y Presupuestaria
#### ID
GORE-NUBLE-GUIA-INTRO-FISCAL-01
#### Ctx
Actualizaciones relevantes en Ley de Presupuestos 2026 (Ley N°21.796) y directrices DIPRES/SUBDERE.
#### Novedades
#### Programa Presupuestario Unico Regional
#### Cpt
Programa Presupuestario Único Integrado por Región.
#### Ctx
Implementado desde 2025; vigente y aplicable para el año presupuestario 2026.
#### Act
- Integra gastos de funcionamiento e inversión.
#### Obj
- Otorgar mayor flexibilidad en gestión presupuestaria.
#### Programa Especial Asociatividad Planes Especiales
#### Cpt
Programa Especial de Asociatividad y Planes Especiales.
#### Ctx
Programa presupuestario nacional.
#### Obj
- Financiar asociatividad interregional.
- Apoyar planes para territorios especiales.
#### Nueva Estructura Presupuestaria Fondos
#### Cpt
Nueva estructura presupuestaria y fondos específicos.
#### Fondos
-
  #### Cpt
  FNDR (Fondo Nacional de Desarrollo Regional).
  #### Ref
  GN-GLOS-FNDR
-
  #### Cpt
  FRPD (Fondo Regional de Productividad y Desarrollo).
  #### Ref
  GN-GLOS-FRPD
  #### Ctx
  Derivado del Royalty Minero, destinado a iniciativas de innovación, competitividad y fomento productivo.
-
  #### Cpt
  Subvenciones 8% FNDR.
  #### Ref
  GN-GLOS-FNDR
-
  #### Cpt
  FRIL (Fondo Regional de Iniciativa Local).
  #### Ref
  GN-GLOS-FRIL
#### Actualizacion Glosas Normas Ejecucion
#### Cpt
Actualización de glosas y normas de ejecución.
#### Req
- Observancia rigurosa por parte del GORE.
#### Lineamientos Tecnicos DIPRES SUBDERE
#### Cpt
Lineamientos técnicos de DIPRES y SUBDERE.
#### Ctx
Basados en manuales, guías e instrucciones específicas.
#### Nuevas Competencias y Transferencias
#### ID
GORE-NUBLE-GUIA-INTRO-COMPETENCIAS-NUEVAS-01
#### Ctx
Proceso de descentralización en avance.
#### Src
Ley N°21.074.
#### Mech
- Transferencia de competencias sectoriales (nivel central -> GORE).
#### Ex
- Materia de turismo regional (algunos GORE ya asumieron facultades de SERNATUR).
#### Implicancias para GORE
-
  #### Ctx
  Los GORE no solo administran fondos, asumen gestión directa de políticas públicas.
-
  #### Req
  Desarrollar capacidades técnicas específicas a nivel regional.
-
  #### Resp
  SUBDERE en coordinación y apoyo técnico en procesos de traspaso de competencias.
### Contexto Region de Nuble
#### ID
GORE-NUBLE-GUIA-CTX-01
#### Caracterizacion Geografica y Administrativa
#### ID
GORE-NUBLE-GUIA-CTX-GEO-01
#### Creacion Region de Nuble
#### ID
GORE-NUBLE-GUIA-CTX-GEO-01-01
#### Fnd
Ley 21.033
#### Fechas Clave
| Ctx | Def |
| --- | --- |
| Fecha promulgación. | 2017-09-05. |
| Fecha vigencia. | 2018-09-06. |
#### Origen Territorial
#### Cpt
Origen territorial.
#### Def
Escisión de la Provincia de Ñuble desde la Región del Biobío.
#### Ubicacion y Geografia
#### ID
GORE-NUBLE-GUIA-CTX-GEO-01-02
#### Ubicacion
#### Cpt
Ubicación.
#### Def
Zona centro-sur, Chile.
#### Limites
#### Norte
Región del Maule.
#### Este
República Argentina.
#### Sur
Región del Biobío.
#### Oeste
Océano Pacífico.
#### Superficie
#### Cpt
Superficie.
#### Def
13,178.5 km².
#### Atributo
#### Cpt
Atributo superficie.
#### Def
Región más pequeña de Chile continental.
#### Componentes Geograficos
#### Cpt
Componentes geográficos.
#### Def
Cordillera de los Andes, Depresión Intermedia, Cordillera de la Costa, Litoral.
#### Capital Regional
#### Cpt
Capital regional.
#### Def
Chillán.
#### Division Politico Administrativa
#### ID
GORE-NUBLE-GUIA-CTX-GEO-01-03
#### Def
3 provincias, 21 comunas.
#### Provincias
| Nombre | Capital | Comunas |
| --- | --- | --- |
| Diguillín | {'Ctx': 'Capital.', 'Def': 'Bulnes.'} | {'Ctx': 'Comunas.', 'Def': 'Bulnes, Chillán, Chillán Viejo, El Carmen, Pemuco, Pinto, Quillón, San Ignacio, Yungay.'} |
| Itata | {'Ctx': 'Capital.', 'Def': 'Quirihue.'} | {'Ctx': 'Comunas.', 'Def': 'Cobquecura, Coelemu, Ninhue, Portezuelo, Quirihue, Ránquil, Treguaco.'} |
| Punilla | {'Ctx': 'Capital.', 'Def': 'San Carlos.'} | {'Ctx': 'Comunas.', 'Def': 'Coihueco, Ñiquén, San Carlos, San Fabián, San Nicolás.'} |
#### Autoridades Regional y Comunales
#### ID
GORE-NUBLE-GUIA-CTX-AUTORIDADES-01
#### Autoridades Nacionales Con Representacion Regional
#### ID
GORE-NUBLE-GUIA-CTX-AUTORIDADES-NACIONAL-01
#### Tabla Autoridades Nacionales
-
  #### Cargo
  Senadores
  #### Nombres
  - Gustavo Sanhueza Dueñas
  - Loreto Carvajal Ambiado
-
  #### Cargo
  Diputados (Distrito 19)
  #### Nombres
  - Cristóbal Martínez Ramírez
  - Felipe Camaño Cárdenas
  - Frank Sauerbaum Muñoz
  - Marta Bravo Salinas
  - Sara Concha Smith
-
  #### Cargo
  Delegado Presidencial
  #### Nombre
  Rodrigo García Hurtado
  #### Ctx
  Rol definido en el marco institucional del Gobierno Interior (Delegado Presidencial Regional).
#### Autoridades Region y Comunas Detalle
#### ID
GORE-NUBLE-GUIA-CTX-AUTORIDADES-REG-COM-01
#### Gobernador Regional
#### ID
GORE-NUBLE-GUIA-CTX-AUTORIDADES-GORE-01
#### Tabla
| Cargo | Nombre |
| --- | --- |
| Gobernador Regional | Óscar Crisóstomo Llanos |
#### Jefaturas Divisiones y Departamentos
#### ID
GORE-NUBLE-GUIA-CTX-AUTORIDADES-JEFATURAS-01
#### Tabla Jefaturas
| Division | Directivo |
| --- | --- |
| Administración Regional | Alejandro Aguilera Zambrano |
| Administración y Finanzas | Alicia Contreras Vielma |
| Presupuesto e Inversión Regional | Juan Parada González |
| Planificación y Desarrollo | Erick Solo de Zaldivar |
| Desarrollo Social y Humano | Tamara Valenzuela Fuentealba |
| Fomento e Industria | Raúl Súnico Galdames |
| Infraestructura y Transportes | Cristián Quiroz Reyes |
| Gabinete | nombre pendiente |
| Comunicaciones | Antonieta Soto Trombert |
| CIES | Álvaro Rivas Rivera |
#### Consejo Regional de Nuble
#### ID
GORE-NUBLE-GUIA-CTX-AUTORIDADES-CORE-01
#### Ctx
Rol definido en la estructura institucional del Gobierno Regional (Consejo Regional).
#### Alcaldes Region de Nuble
#### ID
GORE-NUBLE-GUIA-CTX-AUTORIDADES-ALCALDES-01
#### Ctx
Rol definido en la normativa de administración comunal y municipal.
#### Perfil Socioeconomico y Cuantitativo
#### ID
GORE-NUBLE-GUIA-CTX-SOCIOECONOMICO-01
#### Purp
Proveer síntesis cuantitativa de Ñuble (indicadores clave) vs. contexto nacional para identificar brechas estructurales y oportunidades de intervención.
#### Demografia y Territorio
#### Poblacion Total y Envejecimiento
#### Cpt
Población Total y Envejecimiento.
#### Def
La región posee 512,289 habitantes (población censada), con una edad promedio de 40.0 años (vs. 38.4 nacional). Presenta un proceso de envejecimiento acelerado, con un índice de 97.6 (vs. 79.0 nacional), lo que implica una mayor carga sobre sistemas de salud y pensiones.
#### Distribucion por Edad y Sexo
#### Cpt
Distribución por Edad y Sexo (Pirámide Poblacional).
#### Def
La estructura etaria muestra una base estrecha (población joven) y un ensanchamiento en grupos mayores, con un índice de masculinidad de 94.0 (vs. 96.3 nacional).
#### Tabla Distribucion Etaria
#### Encabezados
- Rango Etario
- Hombres (N°)
- Mujeres (N°)
- Total (N°)
- % Regional
- % Nacional (comparativo)
#### Filas
| Rango_Etario | Hombres | Mujeres | Total | Porcentaje_Regional | Porcentaje_Nacional |
| --- | --- | --- | --- | --- | --- |
| 0-14 años | 44219 | 42347 | 86566 | 16.9% | 18.2% |
| 15-29 años | 53642 | 52178 | 105820 | 20.7% | 22.5% |
| 30-44 años | 53189 | 54732 | 107921 | 21.1% | 23.4% |
| 45-59 años | 51734 | 54219 | 105953 | 20.7% | 19.8% |
| 60+ años | 52178 | 53851 | 106029 | 20.7% | 16.1% |
#### Ctx
La proporción de población mayor de 60 años (20.7%) supera el promedio nacional (16.1%), demandando políticas focalizadas en envejecimiento activo y soporte geriátrico.
#### Composicion Etnica y Migratoria
#### Cpt
Composición Étnica y Migratoria.
#### Indicadores
| Def |
| --- |
| Población inmigrante internacional: 2.1% (10,934 personas) vs. 8.8% nacional. Edad promedio: 33.6 años (vs. 33.5 nacional). Distribución por período de llegada: 36.5% entre 2017-2019 (vs. 33.5% nacional en períodos recientes), con un pico en migrantes de 25-29 años (18.4%). |
| Población indígena: 3.9% (20,145 personas) vs. 11.5% nacional. Predominio Mapuche (92.7%). Índice de envejecimiento indígena: 84.1 (vs. 53.9 nacional), destacando vulnerabilidad en grupos etarios mayores. |
| Población afrodescendiente: 0.5% (2,453 personas) vs. 0.9% nacional. |
#### Estructura Urbano Rural
#### Cpt
Estructura Urbano-Rural.
#### Def
Ruralidad marcada (28.7% vs. 11.3% nacional). Comunas extremas: Cobquecura (71.5%), Ninhue (71.2%).
#### Condiciones Sociales y Desarrollo Humano
#### Educacion
#### Cpt
Educación.
#### Def
Escolaridad promedio (18+ años): 11.0 años vs. 12.1 nacional. Tasa de alfabetismo (15+ años): 95.6% vs. 97.8% nacional. Distribución por nivel educativo: 36.2% con educación media completa (vs. 41.5% nacional); solo 4.7% con educación superior (vs. 18.4% nacional).
#### Discapacidad
#### Cpt
Discapacidad.
#### Def
Prevalencia: 15.3% (74,711 personas) vs. 11.1% nacional. Edad promedio: 58.2 años (vs. 56.4 nacional). Escolaridad promedio: 7.9 años vs. 8.9 nacional. Principales dificultades: caminar (7.6% vs. 5.6% nacional), ver (5.6% vs. 4.3% nacional).
#### Ctx
Mayor prevalencia regional exige intervenciones en accesibilidad y educación inclusiva.
#### Pobreza y Desigualdad
#### Cpt
Pobreza y Desigualdad.
#### Def
Pobreza por ingresos: 12.1% vs. 6.5% nacional. Pobreza multidimensional: 15.5% vs. 16.9% nacional. Focos críticos: Cobquecura (19.1%), Pemuco (19.0%).
#### Indice Desarrollo Humano
#### Cpt
Índice de Desarrollo Humano (IDH).
#### Def
Existen disparidades internas. Chillán presenta IDH 'medio-alto', mientras que la mayoría de las comunas se ubican en categorías 'medio-bajo' o 'bajo'. Ejemplos: Portezuelo (0.444), San Ignacio (0.437).
#### Salud
#### Cpt
Salud.
#### Def
Infraestructura: 7 hospitales, 29 CESFAM, más de 438,000 inscritos en atención primaria. Tasa de mortalidad general: 8.7 por 1,000 hab. vs. 6.9 nacional.
#### Economia Empleo y Conectividad
#### Estructura Productiva
#### Cpt
Estructura Productiva.
#### Def
Base en sector primario. Rubro 'Agricultura, ganadería, silvicultura y pesca' (2023): 7,217 empresas, 35,480 empleos dependientes.
#### Mercado Laboral
#### Cpt
Mercado Laboral.
#### Def
Desafíos estructurales. Tasa de desocupación: 9.6%. Tasa de ocupación informal: 33.0%. Brecha de género en desocupación: femenina 11.0% vs. masculina 8.6%.
#### Vivienda y Servicios Basicos
#### Cpt
Vivienda y Servicios Básicos.
#### Def
Viviendas particulares ocupadas: 187,513 (vs. 6,408,172 nacional). Hacinamiento: 4.5% vs. ~6.1% nacional. Distribución por tipo: 95.8% casas (vs. 74.1% nacional). Acceso a servicios: agua potable (81.5% vs. 92.3% nacional), electricidad (99.4% vs. 99.6% nacional).
#### Ctx
La brecha en agua potable (10.8% inferior a la media nacional) representa un riesgo sanitario y requiere inversión en infraestructura rural.
#### Conectividad Digital
#### Cpt
Conectividad Digital.
#### Def
Acceso a internet en hogares: 87.3% vs. 93.2% nacional. Dependencia de conexiones móviles: 49.7% (una de las más altas del país), limitando productividad y acceso a servicios digitales.
#### Seguridad y Riesgos
#### Seguridad Ciudadana
#### Cpt
Seguridad Ciudadana.
#### Def
Tasa de victimización: 15.4% vs. 21.7% nacional. Percepción de aumento de la delincuencia: 91.9%. Delitos clave: robo en lugar habitado (629.3 vs. 464.2 nacional), abigeato (39.3 vs. 14.8 nacional).
#### Riesgos Naturales y Antropicos
#### Cpt
Riesgos Naturales y Antrópicos.
#### Def
Exposición crítica a incendios forestales y déficit hídrico. Riesgo comunal: erupciones volcánicas (Pinto, Coihueco, San Fabián); tsunamis (Cobquecura, Trehuaco, Coelemu). Destaca Cobquecura con segundo ICFSR más alto de Chile.
### Marco Constitucional Legal e Institucional
#### ID
GN-P1-MARCO-CONSTITUCIONAL
#### Bases Constitucionales
#### ID
GN-MARCO-BASES-CONSTITUCION
#### Src
Constitución Política de la República de Chile.
#### Principios
| Cpt |
| --- |
| Principio de Estado unitario. |
| Principio de administración del Estado funcional y territorialmente descentralizada y desconcentrada. |
#### Proceso Descentralizacion
#### Cpt
Proceso de descentralización.
#### Obj
- Promover desarrollo integral y equitativo.
- Fortalecer participación ciudadana.
- Mejorar eficiencia y eficacia de la gestión pública.
- Adecuar políticas públicas a particularidades territoriales.
#### Dualidad Institucional
#### Cpt
Dualidad institucional entre Gobierno Interior y Administración Regional.
#### Gobierno Interior
#### Def
Representación del poder central para orden público y seguridad.
#### Nat
Función desconcentrada.
#### Administracion Regional
#### Def
Gestión del desarrollo económico, social y cultural de la región, a cargo del Gobierno Regional (GORE).
#### Nat
Función descentralizada y autónoma con autoridades electas.
#### Leyes Organicas y Normativa Fundamental
#### ID
GN-MARCO-LEYES-ORGANICAS
#### Ley 19175 LOC GORE
#### ID
GN-LEY-19175-LOC-GORE
#### Alias
LOC GORE
#### Texto Refundido
DFL N°1-19.175/2005.
#### Nat
Marco legal primordial que regula organización, atribuciones y funcionamiento de los Gobiernos Regionales (GORE).
#### Estructura GORE
#### Descripcion
Define al GORE como organismo con dos órganos clave.
#### Organos Clave
| Cpt | Def |
| --- | --- |
| Gobernador/a Regional. | Órgano ejecutivo del GORE. |
| Consejo Regional (CORE). | Órgano colegiado con facultades normativas, resolutivas y fiscalizadoras. |
#### Rol Global
#### Resp
El GORE actúa como administración superior de la región, enfocado en desarrollo social, cultural y económico.
#### Modificaciones Importantes LOC GORE
#### Descripcion
Reformas legales que impactan la LOC GORE y la institucionalidad regional.
#### Cambios
| Cpt | Detalle |
| --- | --- |
| Leyes 20.990 (2017) y 21.073 (2018). | Establecen e implementan la elección democrática y directa de los Gobernadores Regionales por sufragio universal. |
| Ley 21.074 (2018, Fortalecimiento de la Regionalización). | Modifica sustancialmente la LOC GORE, crea la figura del Administrador Regional, rediseña la estructura de divisiones y establece el mecanismo formal para la transferencia de competencias desde el nivel central a los GORE. |
| Ley 21.730 (2023, Ministerio de Seguridad Pública). | Permite la creación de una División de Prevención del Delito en los GORE, en coordinación con la nueva institucionalidad de seguridad pública. |
#### Ley 21074 Fortalecimiento Regionalizacion
#### ID
GN-LEY-21074
#### Nat
Hito fundamental en la descentralización de Chile; modifica en profundidad la Ley N°19.175.
#### Aportes Clave
| Cpt | Def |
| --- | --- |
| Elección Democrática de Gobernadores Regionales. | Institucionaliza la elección directa, dotando de legitimidad democrática a la máxima autoridad regional. |
| Nueva Estructura Administrativa de los GORE. | Establece divisiones obligatorias (Planificación, Presupuesto, Administración, etc.) para profesionalizar la gestión. |
| Transferencia de Competencias. | Crea un mecanismo formal para transferir funciones y facultades desde ministerios a los GORE, permitiendo una descentralización efectiva y gradual. |
| Fortalecimiento de la Planificación Regional. | Refuerza el rol de instrumentos como la Estrategia Regional de Desarrollo (ERD) y el Plan Regional de Ordenamiento Territorial (PROT). |
| Creación del Administrador Regional. | Incorpora una figura tipo 'gerente' del GORE, de confianza del Gobernador, para liderar la gestión administrativa interna. |
#### Componentes Administracion Publica Regional
#### ID
GN-MARCO-COMPONENTES-ADMIN
#### Ctx
Coexistencia de distintas formas de administración del Estado en la región, cuya interacción es clave para la gobernanza territorial.
#### Gobierno Interior
#### ID
GN-MARCO-GOB-INTERIOR
#### Def
Representación del poder ejecutivo central en el territorio, a cargo de funciones no descentralizadas (orden público, seguridad, coordinación de servicios nacionales).
#### Delegado Presidencial Regional
#### ID
GN-MARCO-DPR
#### Fundamento Juridico
Ley 19.175, Art. 1 y normas relacionadas.
#### Proc
Designado por el Presidente de la República como su representante natural e inmediato en la región, en tanto cuente con su confianza.
#### Resp
- Ejerce el gobierno interior de la región.
#### Advertencias
- No está subordinado al Gobierno Regional; es una autoridad paralela con ámbito de competencia distinto.
#### Atribuciones Orden y Seguridad
- Velar por la tranquilidad y el orden público (DFL 1-19.175/2005).
- Requerir auxilio de la fuerza pública (DFL 1-19.175/2005).
- Deducir querellas por temas de seguridad (DFL 7.912/1927, Ley 18.314/1984).
- Ejecutar la política nacional de seguridad pública (Ley 20.502/2011).
- Presidir el Consejo Regional de Seguridad Pública (Ley 20.502/2011).
- Requerir atención inmediata en emergencias (DFL 22/1959).
- Administrar complejos fronterizos y aplicar normativa de extranjería (DFL 1-19.175/2005).
- Autorizar o suspender recintos deportivos y determinar medidas de seguridad (Ley 19.327/1994).
#### Atribuciones Administracion Regional
- Representar extrajudicialmente al Estado en la región (DFL 1-19.175/2005).
- Coordinar y supervisar servicios públicos nacionales en la región (DFL 1-19.175/2005).
- Proponer terna para SEREMIs (DFL 1-19.175/2005).
- Proponer remoción de SEREMIs y jefes regionales de organismos no dependientes del GORE (DFL 1-19.175/2005).
- Delegar atribuciones en Delegados Presidenciales Provinciales (DFL 1-19.175/2005).
- Informar al Presidente sobre gobierno interior y desempeño de autoridades (DFL 1-19.175/2005).
- Distribuir recursos y subsidios entre comunas (Ley 18.778/1989).
- Convocar comités o consejos vinculados a educación pública y otros ámbitos sectoriales (Ley 21.040/2017, entre otras).
#### Ctx
Su rol se coordina con el GORE, que es una entidad autónoma; suele ser invitado a sesiones del CORE con derecho a voz.
#### Delegados Presidenciales Provinciales
#### ID
GN-MARCO-DPP
#### Fundamento Juridico
Ley 19.175, Art. 3 y normas complementarias.
#### Proc
Designados por el Presidente; representan al poder ejecutivo a nivel provincial bajo instrucciones del DPR.
#### Resp
- Supervigilar servicios públicos en la provincia.
#### Atribuciones Orden y Seguridad
- Mantener el orden público provincial (DFL 1-19.175/2005).
- Requerir fuerza pública (DFL 1-19.175/2005).
- Autorizar reuniones públicas (DFL 1-19.175/2005).
- Enfrentar emergencias (DFL 1-19.175/2005).
- Aplicar normativa de extranjería (DFL 1-19.175/2005, DL 1094/1975).
- Iniciar investigaciones y aplicar multas por infracciones específicas.
- Vigilar bienes del Estado e impedir ocupaciones ilegales (DFL 1-19.175/2005).
#### Atribuciones Administracion Provincial
- Supervisar programas y proyectos de desarrollo provincial no dependientes del GORE (DFL 1-19.175/2005).
- Informar necesidades al Delegado Presidencial Regional o SEREMIs (DFL 1-19.175/2005).
- Autorizar catas y excavaciones mineras en predios fiscales (Ley 18.248/1983).
- Definir número de patentes de alcoholes en comunas (Ley 19.925/2004).
#### Coordinacion Seguridad Publica
#### ID
GN-MARCO-COORD-SEGURIDAD
#### Ctx
Escenario posterior a la creación del Ministerio de Seguridad Pública (Ley 21.730).
#### Elementos Clave
| Cpt | Def |
| --- | --- |
| Coordinación DPR-SEREMI de Seguridad Pública. | Aunque el DPR depende del Ministerio del Interior, coordina estrechamente con el SEREMI de Seguridad Pública en materias de orden y seguridad. |
| Rol del SEREMI de Seguridad Pública. | Representante del Ministerio de Seguridad Pública en la región; implementa políticas de seguridad y prevención. |
#### Ambitos No Descentralizables
#### ID
GN-MARCO-NO-DESCENTRALIZABLE
#### Ctx
Materias de competencia exclusiva del gobierno central, no transferibles a los GORE.
#### Ambitos
- Relaciones exteriores.
- Defensa nacional.
- Administración de justicia.
- Mantenimiento del orden público y seguridad interior.
- Regulación de derechos fundamentales y sistema electoral.
#### Fundamento
Constitución Política y Ley 19.175.
#### Marco Juridico Transversal
#### ID
GN-MARCO-LEYES-TRANSVERSALES
#### Ctx
Leyes transversales de la Administración del Estado que definen el 'cómo' opera el GORE en la práctica.
#### Leyes
| ID | Numero | Nombre | Purp | Act |
| --- | --- | --- | --- | --- |
| GN-LEY-18575 | 18.575 | Ley de Bases Generales de la Administración del Estado. | Funciona como la 'Constitución' del aparato público. | Fija principios de legalidad, eficiencia, probidad y transparencia que obligan al GORE. Define acto administrativo y base de responsabilidad funcionaria. |
| GN-LEY-19880 | 19.880 | Ley de Bases de los Procedimientos Administrativos. | Regula el 'paso a paso' de las decisiones administrativas del GORE. | Establece derechos, plazos, notificaciones y recursos de impugnación; garantiza debido proceso administrativo. Con Ley 21.180, exige procedimientos electrónicos. |
| GN-LEY-19886 | 19.886 | Ley de Compras Públicas. | Norma el gasto público en adquisición de bienes y servicios. | Establece la licitación pública como regla general y regula compras vía Mercado Público para garantizar competencia y transparencia. |
| GN-LEY-20285 | 20.285 | Ley de Transparencia y Acceso a la Información Pública. | Materializa el principio de transparencia en la gestión del GORE. | Obliga a Transparencia Activa (publicación proactiva) y Pasiva (respuesta a solicitudes), con el Consejo para la Transparencia como fiscalizador. |
| GN-LEY-10336 | 10.336 | Ley Orgánica de la Contraloría General de la República. | Establece el rol del máximo órgano de control del Estado. | Define facultades de la CGR para fiscalizar legalidad (Toma de Razón), controlar finanzas, auditar gestión, emitir dictámenes obligatorios y determinar responsabilidades. |
| GN-RES-30-2015-CGR | Resolución N° 30/2015 CGR | Norma sobre rendición de cuentas. | Regula en detalle el procedimiento de rendición de cuentas. | Opera como manual operativo que rige cómo el GORE y los receptores de fondos justifican su uso; su incumplimiento es fuente principal de responsabilidad administrativa. |
| GN-LEY-21364 | 21.364 | Ley de Sistema Nacional de Prevención y Respuesta ante Desastres (SINAPRED). | Regula la gestión de riesgos de desastres en Chile. | Establece estructura, organización y funciones del SINAPRED, otorgando roles y responsabilidades específicas a los GORE en prevención, mitigación, preparación y respuesta ante emergencias. |
| GN-LEY-21663 | 21.663 | Ley Marco de Ciberseguridad e Infraestructura Crítica de la Información. | Establece el marco general para la ciberseguridad en Chile. | Crea la Agencia Nacional de Ciberseguridad y define obligaciones para organismos públicos y privados en prevención, reporte y gestión de incidentes de ciberseguridad. |

## Parte II Estructura Funciones y Competencias
### ID
GN-P2-ESTRUCTURA-COMPETENCIAS
### Estructura y Organizacion GORE
#### ID
GN-ESTRUCTURA-GORE
#### Fnd
Diseño institucional que combina legitimidad democrática con capacidad de gestión.
#### Src
Ley N°21.073, Ley N°21.074 y Ley N°19.175.
#### Nat
Entidad autónoma, personalidad jurídica de derecho público, patrimonio propio.
#### Resp
Administración superior de la región.
#### Obj
Cumplir responsabilidades en desarrollo social, cultural y económico de la región.
### Autoridades Electas
#### ID
GN-ESTRUCTURA-AUTORIDADES-ELECTAS
#### Descripcion
El GORE se compone políticamente de un Gobernador Regional y un Consejo Regional (CORE).
#### Gobernador Regional
#### ID
GN-ESTRUCTURA-GOBERNADOR
#### Resp
Máxima autoridad ejecutiva del Gobierno Regional; ejerce la administración superior de la región.
#### Fundamento Juridico
- Constitución Política, normas sobre gobiernos regionales.
- Ley N°19.175 (Orgánica Constitucional sobre Gobierno y Administración Regional).
- Leyes N°21.073 y N°21.074 (reformas de elección y fortalecimiento regional).
#### Eleccion Mandato y Requisitos
#### Proc Eleccion
- Elección por sufragio universal directo en la región.
- Segunda vuelta si ningún candidato obtiene al menos 40% de los votos.
#### Mandato
- Duración de 4 años.
- Posible reelección inmediata por una sola vez.
#### Requisitos
- Ser ciudadano con derecho a sufragio.
- Tener al menos 25 años de edad.
- Enseñanza media o equivalente cursada.
- Residencia en la región de al menos 2 años previos a la elección.
#### Cese y Subrogacion
- Causales de cese: renuncia, incapacidad, remoción, condena, entre otras definidas en la Constitución y leyes especiales.
- El Administrador Regional actúa como subrogante legal por un período máximo de 45 días, tras lo cual debe definirse reemplazo definitivo.
#### Competencias y Atribuciones
#### Planificacion y Estrategia
- Formular las políticas de desarrollo de la región.
- Someter al CORE las políticas, estrategias y proyectos de planes regionales.
- Proponer al CORE la suscripción de convenios de programación con ministerios u otros órganos.
- Proponer al CORE la declaración de territorios como zonas rezagadas.
#### Gestion Presupuestaria y Inversion
- Someter al CORE el proyecto de presupuesto del GORE.
- Proponer al CORE la distribución de sus recursos de inversión (FNDR, ISAR, otros fondos).
- Proponer al CORE el Anteproyecto Regional de Inversiones (ARI).
#### Administracion y Ejecucion
- Proveer a la ejecución de los planes, políticas y proyectos aprobados por el CORE.
- Nombrar y remover a funcionarios de su exclusiva confianza (Administrador Regional, Jefes de División).
- Administrar los bienes y recursos propios del GORE.
- Coordinar y supervigilar a los servicios públicos que dependan o se relacionen con el GORE.
- Dictar resoluciones e instrucciones necesarias para el ejercicio de sus atribuciones.
#### Relacion con CORE
- Presidir el Consejo Regional, con derecho a voto y voto dirimente en caso de empate.
- Convocar y elaborar la tabla de las sesiones del CORE.
- Responder por escrito, dentro de plazos legales, a los oficios fiscalizadores del CORE.
#### Probidad y Control
- Velar por el cumplimiento de normas de probidad administrativa dentro del GORE.
- Aplicar medidas disciplinarias al personal del Gobierno Regional.
#### Consejo Regional CORE
#### ID
GN-ESTRUCTURA-CORE
#### Resp
Órgano colegiado del GORE con facultades normativas, resolutivas y fiscalizadoras.
#### Rol
- Representar la participación ciudadana en la toma de decisiones regionales.
- Actuar como contrapeso y complemento del Gobernador Regional.
#### Composicion y Mandato
#### Composicion General
- Número de consejeros varía según población regional (mínimo 14, máximo 34).
#### Composicion Nuble
- El CORE de Ñuble está compuesto por 16 consejeros/as.
#### Eleccion
- Elección por sufragio universal directo, por circunscripciones provinciales.
#### Mandato
- Duración de 4 años, con posibilidad de reelección sucesiva hasta por dos períodos.
#### Facultades Principales
#### Resolutivas
- Aprobar, modificar o sustituir la Estrategia Regional de Desarrollo (ERD).
- Aprobar el presupuesto regional y la distribución de recursos de inversión (FNDR, ISAR, otros).
- Aprobar convenios de programación.
- Autorizar enajenación o gravamen de bienes raíces del GORE.
- Aprobar planes reguladores y otros instrumentos de ordenamiento territorial.
#### Normativas
- Aprobar reglamentos regionales que regulen materias de competencia del GORE.
- Aprobar el reglamento interno de funcionamiento del CORE.
#### Fiscalizadoras
- Fiscalizar actos del GORE y desempeño del Gobernador.
- Solicitar información a autoridades regionales o provinciales.
- Disponer auditorías externas a la ejecución presupuestaria del GORE.
- Encargar auditorías internas específicas a la Unidad de Control.
#### Presidencia y Secretaria
#### Presidencia
- El Gobernador Regional preside el CORE, con voz y voto dirimente en caso de empate.
#### Secretaria Ejecutiva
- Presta asesoría técnica y administrativa al CORE y actúa como ministro de fe.
- Designación mediante mayoría absoluta del CORE a partir de terna propuesta, y nombramiento formal por el Gobernador.
#### Estatuto del Consejero
#### Nat
Los consejeros no son funcionarios públicos, pero están sujetos a probidad y responsabilidad.
#### Derechos y Beneficios
- Dieta mensual asociada a asistencia efectiva a sesiones.
- Permisos laborales para asistir a sesiones y cometidos oficiales.
- Derecho a pasajes o reembolsos de traslados cuando corresponda.
- Acceso a capacitación financiada con presupuesto del GORE.
#### Obligaciones y Restricciones
- Sujeción a normas de probidad y conflicto de interés.
- Prohibición de votar en asuntos donde tengan interés personal o familiar.
#### Causales de Cese
- Incapacidad sobreviniente.
- Inasistencia injustificada reiterada a sesiones.
- Pérdida de requisitos o inhabilidades establecidas en la ley.
### Gestion Administrativa y Servicio Administrativo
#### ID
GN-ESTRUCTURA-GESTION-ADMIN
#### Resp
Gestión administrativa del GORE dirigida por el Gobernador Regional.
#### Regimen del Personal
#### ID
GN-ESTRUCTURA-GESTION-REGIMEN-PERSONAL
#### Fnd
- Ley N°19.175 (Orgánica Constitucional sobre Gobierno y Administración Regional).
- Ley N°19.379 (Plantas de Personal).
- Ley N°18.575 (Bases Generales de la Administración del Estado).
- DFL N°29/2004 (Estatuto Administrativo).
- Ley N°19.880 (Bases de los Procedimientos Administrativos).
- Ley N°20.880 (Probidad en la Función Pública y Prevención de Conflictos de Interés).
- Ley N°20.730 (Lobby y Gestión de Intereses).
- Ley N°20.285 (Transparencia y Acceso a la Información Pública).
#### Administrador Regional
#### ID
GN-ESTRUCTURA-ADM-REGIONAL
#### Fnd
Creado por Ley N°21.074.
#### Nat
Funcionario de exclusiva confianza del Gobernador Regional.
#### Resp
- Colaborador directo del Gobernador en la gestión administrativa (rol de 'gerente' operacional del GORE).
#### Funciones Clave
- Gestionar administrativamente el GORE.
- Coordinar el trabajo de los jefes de división.
- Velar por la ejecución de políticas, planes y programas regionales.
- Proponer y aplicar sistemas de gestión y control interno.
#### Ctx
- Es subrogante legal del Gobernador Regional hasta por 45 días, en caso de vacancia o ausencia.
#### Req
- Título profesional de al menos 8 semestres.
- Experiencia profesional mínima de 5 años.
#### Unidad de Control Interno
#### ID
GN-ESTRUCTURA-CONTROL-INTERNO
#### Fnd
Ley N°19.175, Art. 68 quinquies y siguientes.
#### Ctx
- También denominada Unidad de Auditoría Interna.
- Depende jerárquicamente del Gobernador Regional, pero con funciones técnicas de control.
#### Jefatura Unidad
#### Proc
- Nombramiento por el Gobernador Regional con acuerdo de 4/7 de los integrantes del CORE.
#### Req
- Profesional del área de auditoría, con título de al menos 8 semestres.
- Experiencia profesional mínima de 5 años.
#### Funciones Principales
- Fiscalizar la legalidad de los actos administrativos del GORE.
- Controlar la ejecución financiera y presupuestaria del Gobierno Regional.
- Realizar auditorías operativas internas a programas y proyectos.
- Emitir informes periódicos al CORE sobre avance presupuestario y hallazgos relevantes.
- Asistir técnicamente al CORE en el ejercicio de su función fiscalizadora.
- Representar por escrito (observar) actos ilegales al Gobernador Regional.
- Informar a la Contraloría General de la República cuando ilegalidades no se subsanan.
#### Estructura de Divisiones GORE
#### ID
GN-ESTRUCTURA-DIVISIONES
#### Fnd
Ley N°19.175, Art. 68 (modificada por Ley N°21.074).
#### Req Jefes Division
- Son cargos de exclusiva confianza del Gobernador Regional.
- Requieren título profesional de al menos 8 semestres y 5 años de experiencia.
#### Division Administracion y Finanzas DAF
#### ID
GN-ESTRUCTURA-DIVISION-DAF
#### Ref
GN-GLOS-DAF
#### Resp
- Liderar la gestión administrativa interna y los servicios generales del GORE.
#### Funciones Clave
- Gestionar personas y recursos humanos (RRHH).
- Administrar los sistemas de información internos.
- Gestionar la ejecución financiera, contable y presupuestaria de gastos de funcionamiento.
- Administrar pagos y registrar operaciones en los sistemas financieros.
- Gestionar adquisiciones y abastecimiento.
- Emitir certificados de disponibilidad presupuestaria.
#### Division Planificacion y Desarrollo Regional DIPLADE
#### ID
GN-ESTRUCTURA-DIVISION-DIPLADE
#### Ref
GN-GLOS-DIPLADE
#### Resp
- Elaborar y proponer estrategias, políticas, planes, programas y proyectos de desarrollo regional.
#### Funciones Clave
- Formular instrumentos de planificación (ERD, PROT, ZUBC, PLADETUR).
- Coordinar la elaboración del Anteproyecto Regional de Inversiones (ARI).
- Monitorear la implementación de planes e instrumentos de desarrollo regional.
- Prestar asistencia técnica a municipalidades en planificación y proyectos.
- Realizar seguimiento del Programa Público de Inversiones Regionales (PROPIR).
#### Division Presupuesto e Inversion Regional DIPIR
#### ID
GN-ESTRUCTURA-DIVISION-DIPIR
#### Ref
GN-GLOS-DIPIR
#### Resp
- Elaborar, proponer, ejecutar y controlar el presupuesto de inversión del GORE.
#### Funciones Clave
- Apoyar en la formulación de convenios de programación con ministerios y otros órganos.
- Asesorar en la admisibilidad técnica y económica de iniciativas de inversión (IDI).
- Administrar el FNDR y otros fondos de inversión regional.
- Realizar seguimiento y control de la cartera de inversiones.
- Coordinar con DIPRES y otros organismos la evaluación ex ante de proyectos cuando corresponda.
#### Division Fomento e Industria DIFOI
#### ID
GN-ESTRUCTURA-DIVISION-DIFOI
#### Ref
GN-GLOS-DIFOI
#### Resp
- Proponer, promover y ejecutar planes de desarrollo productivo, científico, tecnológico e innovación.
#### Funciones Clave
- Fomentar ciencia, tecnología e innovación a nivel regional.
- Coordinar la acción de servicios públicos del ámbito económico y productivo.
- Implementar la Estrategia Regional de Ciencia, Tecnología e Innovación.
- Diseñar y ejecutar proyectos y programas de fomento productivo.
#### Division Infraestructura y Transportes DIT
#### ID
GN-ESTRUCTURA-DIVISION-DIT
#### Ref
GN-GLOS-DIT
#### Resp
- Planificar, proponer, ejecutar y supervisar programas y proyectos de infraestructura y transporte regional.
#### Funciones Clave
- Actuar como unidad técnica y, cuando corresponda, ejecutora de obras regionales.
- Ser contraparte técnica de ministerios como MOP, MINVU y Ministerio de Transportes.
- Fomentar el desarrollo del transporte intercomunal, interprovincial e internacional.
- Ejecutar la política y el plan regional de transporte.
#### Division Desarrollo Social y Humano DIDESOH
#### ID
GN-ESTRUCTURA-DIVISION-DIDESOH
#### Ref
GN-GLOS-DIDESOH
#### Resp
- Proponer, promover y ejecutar planes orientados a igualdad, cohesión social y acceso a servicios.
#### Funciones Clave
- Ejecutar programas sociales en apoyo a personas y grupos vulnerables.
- Desarrollar programas de apoyo al deporte, educación, salud y cultura.
- Coordinar la acción de servicios públicos del ámbito social.
- Actuar como contraparte técnica de proyectos e iniciativas sociales.
#### Division Prevencion del Delito
#### ID
GN-ESTRUCTURA-DIVISION-PREV-DELITO
#### Nat
División opcional, orientada a seguridad pública con foco preventivo.
#### Resp
- Apoyar al Gobernador en la planificación y gestión de funciones del GORE en seguridad pública.
#### Ctx
- Especial foco en prevención social, situacional y comunitaria del delito, y atención a víctimas.
- Fundamento en normas que asignan competencias al GORE en prevención del delito (Ley N°19.175, Ley N°21.074 y Ley N°21.730).
#### Funciones Potenciales
- Coordinar y gestionar políticas regionales de prevención del delito.
- Gestionar proyectos de seguridad ciudadana financiados con recursos regionales.
- Servir de enlace técnico con la institucionalidad de seguridad pública.
#### Warn
- Rol de articulación, coordinación y gestión; no ejecuta funciones policiales.
### Identidad Institucional GORE
#### ID
GN-IDENTIDAD-INSTITUCIONAL
#### Mision
#### ID
GN-IDENTIDAD-MISION
#### Mssn
Liderar e impulsar el desarrollo sustentable de la Región de Ñuble.
#### Medios
- Gestión eficiente de la inversión pública.
- Responsabilidad presupuestaria.
- Coordinación público-privada y con la sociedad civil.
#### Obj
- Contribuir al desarrollo territorial armónico de la región.
#### Vision
#### ID
GN-IDENTIDAD-VISION
#### Def
Ser una institución que inspira, lidera e impulsa la integración territorial en Ñuble.
#### Medios
- Gestión responsable de los recursos públicos.
- Contribución al bienestar de la población.
- Apoyo a la cultura, el desarrollo y el patrimonio regional.
#### Objetivos Estrategicos Institucionales
#### ID
GN-IDENTIDAD-OEI
#### Periodo
2025-2026
#### OEI
| ID | Tipo | Descripcion | Enfoque_Genero | Enfoque_Cambio_Climatico |
| --- | --- | --- | --- | --- |
| OEI-1 | Estratégico | Desarrollar estrategias, políticas e instrumentos para planificación regional, gestión de información territorial y articulación de actores, contribuyendo al desarrollo participativo e integrado. | true | true |
| OEI-2 | Estratégico | Financiar cartera anual de iniciativas de inversión pública (incluido fomento productivo e innovación) en conjunto con actores público-privados para mejorar condiciones económicas y sociales. | true | true |
| OEI-3 | Estratégico | Implementar instancias de participación, fortalecimiento de capacidades y articulación de actores para la formulación, evaluación y ejecución eficaz, eficiente y oportuna de iniciativas financiadas con FNDR. | true | false |
#### Principios Orientadores
#### ID
GN-IDENTIDAD-PRINCIPIOS
#### Principios
| Cpt | Def |
| --- | --- |
| Compromiso | Compromiso con la comunidad y la función pública. |
| Eficiencia | Mejorar la calidad de vida con uso eficiente de recursos públicos. |
| Profesionalismo | Carrera funcionaria basada en capacidad, desempeño y apego irrestricto a la normativa. |
| Transparencia | Garantizar acceso a la información sobre actuaciones y decisiones para el control ciudadano. |
| Probidad | Preeminencia del interés general sobre el particular, con conducta honesta e íntegra. |
| Respeto | Cordialidad, igualdad, libertades y dignidad en el ambiente laboral y de atención. |
| Inclusión | No discriminación arbitraria, igualdad de derechos y oportunidades. |
| Sostenibilidad | Integrar la dimensión ambiental y la adaptación al cambio climático en políticas y proyectos. |
| Coordinación | Actuar en armonía con políticas nacionales y en coordinación con otros órganos del Estado y gobiernos locales para optimizar recursos y potenciar el impacto de la acción pública. |
### Organos Auxiliares y de Participacion
#### ID
GN-ESTRUCTURA-ORGANOS-AUXILIARES
#### Consejo de la Sociedad Civil COSOC
#### ID
GN-ESTRUCTURA-COSOC
#### Nat
Órgano consultivo del Gobierno Regional.
#### Ctx
- Su conformación es obligatoria de acuerdo con la Ley N°20.500 y la Ley N°21.074.
#### Caracteristicas
- Composición diversa, representativa y pluralista.
- Integrado por organizaciones de la sociedad civil sin fines de lucro.
#### Proc
- Un reglamento aprobado por el CORE define número de integrantes, mecanismos de selección y funcionamiento.
#### Materias de Consulta
- Instrumentos de planificación regional (ERD, PROT).
- Políticas regionales relevantes.
- Presupuesto regional y prioridades de inversión.
#### Comite de Alcaldes de Area Metropolitana
#### ID
GN-ESTRUCTURA-COMITE-ALCALDES
#### Ctx
- Opera en regiones donde existan Áreas Metropolitanas definidas.
#### Composicion
- Integrado por alcaldes de las comunas que conforman el Área Metropolitana.
#### Presidencia
- Presidido por el Gobernador Regional.
#### Secretaria Ejecutiva
- A cargo del Departamento de Áreas Metropolitanas, normalmente inserto en DIPLADE.
#### Funciones
- Formular propuestas sobre desarrollo metropolitano.
- Conocer la gestión del Área Metropolitana.
- Pronunciarse sobre planes metropolitanos y proyectos de alto impacto urbano.
#### Comite Regional de Ciencia Tecnologia e Innovacion CCTID
#### ID
GN-ESTRUCTURA-CCTID
#### Nat
Órgano asesor del GORE en materias de ciencia, tecnología e innovación para el desarrollo.
#### Proc
- Colabora con el Gobernador Regional a través de DIPLADE y/o la División de Fomento e Industria.
#### Funciones
- Identificar y formular políticas y lineamientos de ciencia, tecnología e innovación (CTCI).
- Elaborar o asesorar la Estrategia Regional de CTCI.
#### Corporaciones Regional de Desarrollo y Turismo
#### ID
GN-ESTRUCTURA-CORPORACIONES
#### Nat
Entidades de derecho privado sin fines de lucro en las que el GORE puede participar.
#### Proc
- El GORE está facultado para constituir o participar en corporaciones de desarrollo y/o de turismo.
#### Funciones Tipicas
- Realizar estudios y análisis para el desarrollo regional.
- Atraer inversión y fortalecer la asociatividad entre actores públicos y privados.
- Promover la innovación, el emprendimiento y el turismo.
#### Regla Presupuestaria y Financiamiento
#### Cond
- El aporte del GORE a corporaciones no puede exceder el 5% del presupuesto de inversión regional.
- Los proyectos ejecutados con fondos del GORE requieren cofinanciamiento de otras fuentes; el GORE financia como máximo el 50% del costo del proyecto.
#### Representacion y Gobernanza
#### Cpt
- El directorio debe incluir al menos un tercio de sus miembros designados por el CORE a propuesta del Gobernador Regional.
#### Prohib
- Consejeros regionales y sus parientes directos no pueden ser directores ni recibir remuneraciones de estas corporaciones.
### Competencias y Funciones del GORE
#### ID
GN-COMPETENCIAS-GORE
#### Src
Ley N°19.175 (modificada por reformas posteriores).
#### Def
Marco de acción del Gobierno Regional, con foco en planificación y gestión del desarrollo territorial, coordinación y financiamiento más que ejecución directa de políticas sectoriales.
#### Principios Rectores
#### ID
GN-COMPETENCIAS-PRINCIPIOS
#### Principios Ley 19175
- Equidad.
- Eficacia.
- Eficiencia.
- Participación efectiva.
- Preservación y mejora del medio ambiente.
#### Principios Bases Administracion Estado
- Responsabilidad.
- Coordinación.
- Control.
- Probidad.
- Impugnabilidad.
- Impulsión de oficio.
- Transparencia y publicidad.
- Respeto a la autonomía de los grupos intermedios.
- Compromiso.
- Profesionalismo.
- Respeto.
- Inclusión.
- Sostenibilidad.
#### Funciones Generales
#### ID
GN-COMPETENCIAS-GENERALES
#### Ctx
Macro-funciones que definen el quehacer del Gobierno Regional (Art. 16, Ley N°19.175).
#### Funciones
| Cpt | Def |
| --- | --- |
| Planificacion_Estrategica | Diseñar, elaborar, aprobar y aplicar las políticas, planes, programas y proyectos de desarrollo para la región, coherentes con la estrategia regional y los planes comunales. |
| Ordenamiento_Territorial | Orientar el desarrollo territorial de la región en coordinación con servicios públicos y municipalidades. |
| Elaboracion_Presupuestaria | Elaborar y aprobar el proyecto de presupuesto del GORE, ajustado a la normativa nacional. |
| Decision_sobre_Inversion_Publica | Resolver la inversión de los recursos del FNDR y otros fondos asignados al GORE. |
| Asignacion_de_Inversion_Sectorial | Decidir el destino de los recursos de inversión sectorial de asignación regional (ISAR). |
| Potestad_Normativa | Dictar normas generales (reglamentos regionales) para regular materias de competencia del GORE, publicadas en el Diario Oficial. |
| Prevencion_del_Delito | Diseñar y ejecutar políticas y programas regionales de prevención del delito y asistencia a víctimas, en coordinación con la institucionalidad de seguridad pública. |
| Asesoria_a_Municipios | Prestar asesoría técnica a municipalidades, especialmente en la formulación de planes y proyectos. |
| Gestion_de_Emergencias | Adoptar medidas frente a emergencias y catástrofes y desarrollar programas de prevención en el marco del sistema nacional de gestión de riesgos y desastres. |
| Transferencia_de_Competencias | Ejercer las nuevas competencias que le sean transferidas desde ministerios y servicios públicos. |
| Coordinacion_Interinstitucional | Mantener relación permanente con el gobierno nacional y sus organismos para armonizar el ejercicio de funciones. |
#### Funciones Especificas por Ambito
#### ID
GN-COMPETENCIAS-ESPECIFICAS
#### Ctx
Detalle de funciones específicas del GORE por áreas de desarrollo (Arts. 17, 18 y 19, Ley N°19.175).
#### Ordenamiento Territorial
#### Funciones
- Elaborar y aprobar el Plan Regional de Ordenamiento Territorial (PROT) como instrumento vinculante que orienta el uso del suelo a nivel regional.
- Elaborar y proponer la Zonificación del Uso del Borde Costero (ZUBC).
- Fomentar el desarrollo de áreas rurales y localidades aisladas.
- Participar en la dotación de infraestructura y equipamiento regional.
- Fomentar y velar por la protección del medio ambiente regional.
- Proponer la declaración de zonas rezagadas para focalizar la inversión.
#### Fomento Actividades Productivas
#### Funciones
- Formular políticas regionales para el fomento productivo, el emprendimiento y la innovación.
- Elaborar y aprobar la Política Regional de Ciencia, Tecnología e Innovación.
- Aprobar el Plan Regional de Desarrollo Turístico (PLADETUR).
- Promover la investigación científica y tecnológica y el desarrollo de la educación superior en la región.
- Apoyar la creación de oficinas de fomento productivo en los municipios.
#### Desarrollo Social y Cultural
#### Funciones
- Establecer prioridades regionales para la erradicación de la pobreza.
- Participar en acciones que faciliten el acceso de la población a salud, educación, vivienda, cultura y deporte.
- Fomentar expresiones culturales, cautelar el patrimonio histórico y velar por el desarrollo de las etnias originarias.
- Distribuir entre las municipalidades los recursos para programas sociales que ellas administren.
#### Gestion de Emergencias y Desastres
#### ID
GN-COMPETENCIAS-EMERGENCIAS
#### Fnd
Ley que crea el Sistema Nacional de Prevención y Respuesta ante Desastres (SINAPRED).
#### Ref
GN-GLOS-SINAPRED
#### Funciones
- Adoptar medidas para enfrentar emergencias y catástrofes en coordinación con autoridades competentes.
- Desarrollar programas de prevención y reducción de riesgos de desastres.
- Participar en órganos de coordinación (ej. comités regionales de gestión de riesgos) y financiar acciones de reconstrucción.
#### Nuevas Competencias en Seguridad Publica
#### ID
GN-COMPETENCIAS-SEGURIDAD
#### Src
Ley N°21.074 y Ley N°21.730.
#### Ctx
Competencias con foco preventivo, no policial.
#### Resp
- Diseñar y ejecutar políticas, planes y programas regionales de prevención del delito.
- Desarrollar iniciativas de atención y asistencia a víctimas.
- Asesorar técnicamente a municipios en materias de seguridad pública.
#### Warn
- Las funciones del GORE en seguridad pública son de apoyo, coordinación y financiamiento; no sustituyen las funciones de las policías.
#### Mecanismos de Transferencia de Competencias Sectoriales
#### ID
GN-COMPETENCIAS-TRANSFERENCIA
#### Src
Ley N°21.074 y normas constitucionales sobre gobiernos regionales.
#### Mech
- Proceso formal para transferir competencias desde ministerios a gobiernos regionales mediante decreto presidencial fundado.
#### Ctx
- La SUBDERE coordina y apoya técnica y administrativamente los procesos de traspaso.
- Ejemplos iniciales incluyen materias como turismo regional.
#### Modalidades de Ejecucion de Funciones y Programas Regional
#### ID
GN-COMPETENCIAS-MODALIDADES-EJECUCION
#### Cpt
- Modalidad 1: Ejecución directa por el GORE para programas de tipo 'blando' (capacitación, fomento, cultura), con divisiones sectoriales como unidades ejecutoras.
- Modalidad 2: Ejecución mediante convenios con servicios públicos o municipalidades, en que el GORE actúa como unidad financiera y el servicio o municipio como unidad técnica.
- Modalidad 3: Participación de corporaciones de desarrollo u otras entidades (universidades, ONG), donde el GORE financia una parte del proyecto sujeto a límites legales de aporte y cofinanciamiento.

## Parte III Gestion Financiera Inversion y Control
### ID
GN-P3-FINANZAS-INVERSION-CONTROL
### Purp
Describir el marco operativo para planificación, ejecución y control de recursos financieros e intervenciones públicas regionales (IPR) del GORE.
### Ctx
Integra gestión presupuestaria, ciclo de vida de IPR y flujos de aprobación y rendición de cuentas.
### Sistema Presupuestario Regional
#### ID
GN-P3-SISTEMA-PRESUPUESTARIO
#### Def
Proceso de planificación, administración, ejecución y control de recursos financieros del GORE.
#### Ctx
- El GORE tiene autonomía en la distribución de fondos dentro de un marco legal estricto.
- Está sujeto a supervisión de la Dirección de Presupuestos (DIPRES) y la Contraloría General de la República (CGR).
### Fuentes y Mecanismos de Financiamiento
#### ID
GN-P3-FINANCIAMIENTO-FUENTES
#### Ctx
El GORE canaliza recursos vía fondos (qué) y mecanismos (cómo); elegir la vía correcta es un paso crítico.
#### Fondos de Inversion Regional
| Cpt | Def |
| --- | --- |
| FNDR (Fondo Nacional de Desarrollo Regional) | Principal fondo para financiar proyectos de inversión y programas de desarrollo en la región. |
| FRPD (Fondo Regional para la Productividad y el Desarrollo) | Derivado del Royalty Minero; financia iniciativas de innovación, competitividad y fomento productivo. |
| ISAR (Inversiones Sectoriales de Asignación Regional) | Recursos sectoriales cuya distribución territorial decide el GORE para atender prioridades regionales. |
#### Mecanismos de Financiamiento
| Nombre | Purp |
| --- | --- |
| Sistema Nacional de Inversiones (SNI) general | Vía para proyectos de inversión que requieren evaluación técnica y económica completa para obtener recomendación satisfactoria. |
| FRIL (Fondo Regional de Iniciativa Local) | Vía simplificada para proyectos de infraestructura de menor escala ejecutados por municipalidades, exentos de evaluación RS. |
| Programas de Ejecucion Directa (Glosa 06, Partida 31, Ley N°21.796, 2026) | Para programas ejecutados por el propio GORE; requieren evaluación de diseño de DIPRES/SES para recomendación favorable. |
| Transferencias para Programas a Entidades Publicas | Programas ejecutados por otros organismos públicos; exentos de evaluación DIPRES/SES pero sujetos a evaluación interna rigurosa. |
| Subvenciones 8% FNDR (Glosa 07, Partida 31, Ley N°21.796, 2026) | Financiar actividades comunitarias de corta duración (cultura, deporte, social) vía concursos, principalmente a organizaciones privadas sin fines de lucro. |
| Otros Mecanismos Especiales | Procedimientos específicos (ej. Circular 33) para adquisiciones de activos o conservaciones que requieren visación de DIPRES (Ley de Presupuestos 2026, Ley N°21.796). |
### Ciclo Presupuestario Anual
#### ID
GN-P3-CICLO-PRESUPUESTARIO
#### Ctx
Ciclo anual del presupuesto regional con fases definidas; la interacción con el CORE y los órganos de control es fundamental.
#### Fases
-
  #### Nombre
  Formulacion
  #### Act
  - La División de Presupuesto e Inversión Regional (DIPIR) lidera la formulación del presupuesto de inversión (ARI).
  - La División de Administración y Finanzas (DAF) lidera el presupuesto de funcionamiento.
-
  #### Nombre
  Aprobacion_y_Distribucion
  #### Act
  - El Gobernador propone la distribución del presupuesto al CORE para su aprobación.
  #### Ctx
  - El acto administrativo de aprobación debe ser visado por DIPRES y tomado de razón por la CGR para adquirir vigencia.
-
  #### Nombre
  Ejecucion
  #### Act
  - DAF gestiona el registro financiero en SIGFE.
  - DIPIR monitorea el avance físico a través de sistemas como BIP.
  - Los pagos se ejecutan diariamente, sujetos a disponibilidad de caja.
  #### Sistemas Clave
  | Cpt | Ref |
  | --- | --- |
  | Sistema financiero SIGFE. | GN-GLOS-SIGFE |
  | Sistema de seguimiento de inversión BIP. | GN-GLOS-BIP |
-
  #### Nombre
  Modificaciones
  #### Act
  - Las reasignaciones de recursos de inversión, por regla general, requieren aprobación del CORE.
  #### Ctx
  - Todas las modificaciones relevantes deben ser visadas por DIPRES y CGR, aun cuando no requieran aprobación del CORE.
-
  #### Nombre
  Cierre_y_Evaluacion
  #### Act
  - DAF calcula la deuda flotante y el saldo final.
  - DIPIR evalúa el cumplimiento de metas físicas.
  - Los resultados alimentan la formulación del ciclo siguiente.
### Ejecucion Presupuestaria Historica 2020 2024
#### ID
GN-P3-EJECUCION-HISTORICA
#### Src
Serie de ejecución presupuestaria 2020-2024.
#### Purp
Mostrar la evolución de la ejecución presupuestaria del GORE Ñuble y su desempeño relativo.
#### Datos
| Anio | Presupuesto_Ejecutado_MMiles | Marco_Presupuestario_Final_MMiles | Porcentaje_Ejecucion |
| --- | --- | --- | --- |
| 2020 | 38293.595 | 39289.915 | 97.46 |
| 2021 | 39793.664 | 45112.559 | 88.21 |
| 2022 | 47372.679 | 51509.438 | 99.79 |
| 2023 | 59441.127 | 60015.566 | 99.04 |
| 2024 | 63330.546 | 69956.822 | 90.53 |
### Gestion Ciclo de Vida Intervenciones Publicas Regional
#### ID
GN-P3-GESTION-IPR-CICLOVIDA
#### Purp
Sistematizar la gestión de intervenciones públicas regionales (IPR) en un flujo estandarizado desde la postulación hasta el cierre.
#### Distincion Proyectos vs Programas
#### ID
GN-P3-GESTION-IPR-DISTINCION
#### IPR
#### Def
Término paraguas que agrupa iniciativas de inversión (IDI) y programas públicos regionales (PPR).
#### IDI
#### Nat
Gasto de capital (Subtítulos 31/33) para crear o mejorar activos físicos o capital humano durable.
#### Ref
GN-GLOS-SNI
#### Proc
- Calidad técnica evaluada por el Sistema Nacional de Inversiones (MDSF) para obtener recomendación satisfactoria (RS) o admisibilidad (AD).
#### PPR
#### Nat
Gasto corriente o mixto (Subtítulo 24) para entregar servicios, beneficios o cambiar conductas.
#### Proc
- Diseño evaluado por DIPRES/SES si ejecuta el GORE, o por el propio GORE si ejecuta una entidad pública tercera.
- Se busca recomendación favorable (RF) o informe técnico favorable (ITF).
#### Fases Ciclo Vida IPR
#### ID
GN-P3-IPR-CICLOVIDA-FASES
#### Fases
| Orden | Nombre | Obj |
| --- | --- | --- |
| 1 | Ingreso_Pertinencia_Admisibilidad | Recepcionar postulaciones y filtrar para alinear con estrategia regional y requisitos formales. |
| 2 | Evaluacion_Tecnica_y_Economica | Analizar el fondo de la IPR para determinar calidad y viabilidad, obteniendo aprobación técnica (RS, RF, AD, ITF). |
| 3 | Priorizacion_y_Financiamiento | El Gobernador prioriza IPR técnicamente aprobadas y propone financiamiento al CORE para su decisión. |
| 4 | Formalizacion_y_Gestion_Presupuestaria | Tramitar el acto administrativo (resolución o decreto) y, cuando corresponda, el convenio de transferencia con obligaciones de las partes. |
| 5 | Ejecucion_y_Seguimiento | La entidad ejecutora implementa la IPR mientras el GORE realiza seguimiento técnico y financiero. |
| 6 | Gestion_de_Modificaciones | Gestionar formalmente cambios relevantes (costo, alcance, plazos), que pueden requerir nueva evaluación técnica y aprobación presupuestaria. |
| 7 | Cierre_y_Evaluacion_ExPost | Formalizar la finalización de la IPR, aprobar la rendición final y, opcionalmente, realizar evaluación ex post para medir impacto y extraer lecciones. |
### Rendicion de Cuentas y Gobernanza del Control
#### ID
GN-P3-RENDICIONES-CONTROL
#### Purp
Describir el sistema de control que rige la gestión del GORE, asegurando probidad, transparencia y uso correcto de fondos públicos.
#### Concepto Rendicion de Cuentas
#### ID
GN-P3-RENDICION-DEF
#### Def
Procedimiento administrativo y de control para justificar el uso correcto de fondos públicos según fines y normativa.
#### Mssn
Comprobar ingreso, egreso o traspaso de recursos públicos, informando y respondiendo por la gestión y sus resultados.
#### Principios Rectores
#### ID
GN-P3-RENDICION-PRINCIPIOS
#### Principios
| Cpt | Def |
| --- | --- |
| Legalidad | Todo gasto debe estar amparado en la ley y en el convenio correspondiente. |
| Veracidad | La documentación debe ser auténtica, íntegra y fidedigna. |
| Acreditacion | Todo movimiento de fondos debe estar respaldado documentalmente. |
| Oportunidad | Las rendiciones deben presentarse dentro de los plazos establecidos. |
#### Norma Clave
#### ID
GN-P3-RENDICION-NORMA-CLAVE
#### Fnd
Resolución N°30 de 2015 de la Contraloría General de la República (CGR).
#### Ref
GN-RES-30-2015-CGR
#### Nat
Norma de procedimiento obligatoria para el GORE y los receptores de sus fondos; define expediente, plazos y restricciones (ej. no entregar nuevos fondos con rendiciones pendientes).
#### Gobernanza del Control
#### ID
GN-P3-RENDICION-GOBERNANZA
#### Ctx
La gestión del GORE está sujeta a un sistema de control dual (interno/externo) con múltiples filtros y vetos.
#### Control Interno
#### Actores
- Gobernador Regional (ejecutivo).
- Consejo Regional (político-fiscalizador).
- Administrador Regional (administrativo).
- Divisiones técnicas y financieras del GORE.
- Unidad de Control Interno (legalidad).
#### Control Externo
#### Actores
- Contraloría General de la República (CGR): control preventivo de legalidad, auditorías y dictámenes obligatorios.
- Dirección de Presupuestos (DIPRES): control de salud financiera y visación de modificaciones presupuestarias, evaluación de programas.
- Ministerio de Desarrollo Social y Familia (MDSF): control de la calidad técnica de la inversión pública (RS de proyectos).
#### Proceso de Rendicion de Cuentas
#### ID
GN-P3-RENDICION-PROCESO
#### Fnd
Resolución N°30 de 2015 de la CGR.
#### Def
Procedimiento para demostrar y justificar el uso correcto de fondos, acreditando ajuste a la ley y al convenio.
#### Resp
- El GORE es responsable final del correcto uso de los fondos, debiendo suspender transferencias y perseguir responsabilidades si el ejecutor no rinde adecuadamente.
#### Mech
- La rendición se gestiona obligatoriamente a través de la plataforma SISREC de la CGR.
- La DAF del GORE revisa y aprueba rendiciones, y contabiliza gastos en SIGFE.
#### Actores y Responsabilidades Clave
#### ID
GN-P3-RENDICION-ACTORES
#### Entidad Ejecutora
#### ID
GN-P3-RENDICION-ACTOR-EJECUTOR
#### Resp
- Usar los fondos según el convenio.
- Llevar registros contables y administrativos adecuados.
- Presentar rendiciones en forma y plazo.
- Reintegrar fondos no utilizados o mal rendidos.
#### Gobierno Regional
#### ID
GN-P3-RENDICION-ACTOR-GORE
#### Componentes
| Cpt | Resp |
| --- | --- |
| Referente Técnico-Financiero (RTF) | Primera línea de revisión técnica y financiera de la rendición. |
| DAF del GORE | Unidad central que revisa legalidad y finanzas, gestiona SISREC y contabiliza en SIGFE. |
| Gobernador Regional | Responsable político final de la correcta inversión de los fondos. |
#### Contraloria General de la Republica
#### ID
GN-P3-RENDICION-ACTOR-CGR
#### Resp
- Principal órgano de control externo: administra SISREC, examina y juzga cuentas e inicia juicios de cuentas ante perjuicio fiscal.
#### Proceso Operativo SISREC
#### ID
GN-P3-RENDICION-PROCESO-SISREC
#### Fnd
Resolución Exenta N°1.858 de 2023 de la CGR.
#### Ref
GN-GLOS-SISREC
#### Ctx
SISREC es la plataforma obligatoria para gestionar rendiciones de transferencias.
#### Flujo Simplificado
| Paso | Actor | Act |
| --- | --- | --- |
| 1 | Entidad ejecutora | ['Ingresa gastos en SISREC, adjunta respaldos digitalizados y envía la rendición al GORE con firma electrónica.'] |
| 2 | GORE-RTF | ['Revisa rendición en SISREC, aprueba o formula observaciones y, si corresponde, la deriva a DAF.'] |
| 3 | GORE-DAF | ['Firma el informe de aprobación total o parcial con firma electrónica avanzada y valida la rendición.'] |
| 4 | GORE-Contabilidad | ['Con el informe de aprobación, registra el gasto en SIGFE y archiva antecedentes.'] |
#### Gobernanza del Control y Consecuencias
#### ID
GN-P3-RENDICION-CONSECUENCIAS
#### Ctx
El sistema de control contempla consecuencias directas ante incumplimientos en rendiciones de cuentas.
#### Sistema de Control Multiples Filtros
#### ID
GN-P3-RENDICION-CONTROL-FILTROS
#### Componentes
- Control interno del GORE (divisiones técnicas, DAF, Unidad de Control Interno).
- Control externo de CGR, DIPRES y MDSF.
#### Consecuencias Del Incumplimiento
#### ID
GN-P3-RENDICION-CONSECUENCIAS-INCUMPLIMIENTO
#### Elementos
-
  #### Cpt
  Suspension_de_Nuevos_Fondos
  #### Prohib
  El GORE no debe entregar nuevos recursos a entidades con rendiciones pendientes y exigibles.
-
  #### Cpt
  Obligacion_de_Restituir
  #### Cause
  Rendiciones no presentadas, no aprobadas u observadas pueden generar obligación de reintegrar fondos.
-
  #### Cpt
  Responsabilidades
  #### Def
  Las irregularidades pueden derivar en responsabilidad administrativa (sumarios), civil (juicios de cuentas) y penal (fraude al fisco).

## Parte IV Diagnostico Estrategico Region Nuble
### ID
GN-P4-DIAGNOSTICO
### Desafios Regionales
#### ID
GN-P4-DESAFIOS
#### Desafios
-
  #### Nombre
  Pobreza_y_Desigualdad
  #### Obj
  Abordar brechas socioeconómicas estructurales.
  #### Ctx
  - Foco en zonas rurales y grupos vulnerables.
  - Tasa de pobreza por ingresos en Ñuble de alrededor de 12.1%, superior al promedio nacional.
  - Comunas críticas incluyen territorios como Cobquecura y Pemuco con niveles de pobreza cercanos al 19%.
-
  #### Nombre
  Diversificacion_Productiva
  #### Obj
  Superar dependencia del sector primario silvoagropecuario.
  #### Ctx
  - Base con más de siete mil empresas y decenas de miles de empleos ligados al agro.
  #### Req
  - Transición hacia agroindustria de mayor valor agregado, turismo y servicios.
-
  #### Nombre
  Seguridad_Hidrica_y_Cambio_Climatico
  #### Obj
  Gestionar los recursos hídricos de forma sostenible y adaptarse al cambio climático.
  #### Ctx
  - Región afectada por déficit hídrico permanente y alta exposición a incendios forestales.
-
  #### Nombre
  Conectividad
  #### Obj
  Cerrar brechas en caminos rurales, transporte público y acceso a internet de banda ancha fija.
  #### Ctx
  - Casi la mitad de los hogares depende exclusivamente de conexiones móviles, limitando el desarrollo.
-
  #### Nombre
  Capital_Humano
  #### Obj
  Elevar la calificación de la población y retener talentos.
  #### Ctx
  - Escolaridad promedio bajo la media nacional y numerosas comunas con IDH bajo o medio-bajo.
-
  #### Nombre
  Gobernanza
  #### Obj
  Fortalecer capacidades técnicas y de gestión del GORE.
  #### Req
  - Mejorar coordinación público-privada y profundizar la participación ciudadana.
-
  #### Nombre
  Equilibrio_Territorial
  #### Obj
  Reducir disparidades entre el polo urbano Chillán y comunas vulnerables.
  #### Ctx
  - Presencia de comunas con IDH significativamente inferior al promedio regional.
-
  #### Nombre
  Seguridad_Publica
  #### Obj
  Alinear gestión con alta percepción de inseguridad y delitos de alta connotación regional.
  #### Ctx
  - Percepción ciudadana de aumento de la delincuencia.
  #### Ex
  - Tasas elevadas de robo en lugar habitado y abigeato en comparación con el promedio nacional.
### Oportunidades Estrategicas
#### ID
GN-P4-OPORTUNIDADES
#### Oportunidades
| Nombre | Def |
| --- | --- |
| Logistica | Posición geográfica estratégica en la zona centro-sur como nexo entre norte y sur. |
| Agroalimentaria | Base productiva agrícola relevante y potencial para productos con denominación de origen. |
| Turismo | Potencial diversificado (rural, enoturismo, montaña, costa) con espacio para crecer. |
| Capital_Humano | Universidades y centros regionales como motor para formar talento y retener profesionales. |
| Identidad_y_Patrimonio | Rica herencia cultural y patrimonial como base para desarrollo social y oferta turística. |
| Gobernanza | Gobierno Regional joven y proactivo, con compromiso en procesos de descentralización. |
| Financiamiento | Disponibilidad de nuevas fuentes de financiamiento como el FRPD del Royalty Minero. |
| Transformacion_Digital | Uso de la transformación digital como eje habilitante para modernizar sectores y servicios. |
### Vision y Estrategia de Desarrollo Regional
#### ID
GN-P4-VISION-ESTRATEGIA
#### Purp
Sintetizar instrumentos y visiones que orientan el desarrollo de Ñuble (ERD, programa de gobierno, visión de futuro inteligente).
#### ERD Nuble 2024 2030
#### ID
GN-P4-VISION-ERD
#### Def
Principal instrumento de planificación regional de largo plazo, estructurado en ejes para abordar desafíos y oportunidades.
#### Lexico
- LE: Lineamiento Estratégico.
- OE: Objetivo Estratégico.
- AE: Actividad Estratégica.
#### Ejes
| Nombre | Lineamientos |
| --- | --- |
| Territorio_y_Medio_Ambiente | [{'LE': 'Desarrollo territorial planificado y resiliente.', 'OE_Resum': 'Planificar territorio, mejorar infraestructura y conectividad, fortalecer resiliencia y seguridad hídrica.'}, {'LE': 'Habitabilidad_y_Servicios', 'OE_Resum': 'Mejorar habitabilidad, acceso a servicios y gestión de residuos con enfoque de sostenibilidad.'}, {'LE': 'Valores_Ambientales', 'OE_Resum': 'Educar en valores ambientales y proteger ecosistemas, promoviendo turismo sostenible.'}] |
| Economia_Innovacion_y_Capital_Humano | [{'LE': 'Formacion_y_Retencion_de_Capital_Humano', 'OE_Resum': 'Promover innovación educativa y retener/atraer profesionales.'}, {'LE': 'Economia_Diversificada_con_Soporte', 'OE_Resum': 'Diversificar la matriz productiva, desarrollar CTI, fortalecer turismo y cadenas logísticas.'}] |
| Desarrollo_Social_Inclusivo | [{'LE': 'Bienestar_y_Seguridad', 'OE_Resum': 'Reducir pobreza, fortalecer salud, educación y disminuir violencia de género.'}, {'LE': 'Inclusion_Social', 'OE_Resum': 'Mejorar bienestar de personas mayores y garantizar igualdad para personas con discapacidad y neurodivergencias.'}] |
| Patrimonio_Cultura_e_Identidad | [{'LE': 'Desarrollo_Creativo_e_Identitario', 'OE_Resum': 'Fortalecer gestión cultural, economías creativas y visibilizar identidades locales y de pueblos originarios.'}, {'LE': 'Sustentabilidad_Patrimonial', 'OE_Resum': 'Investigar, valorizar y proteger el patrimonio cultural y arquitectónico.'}] |
| Institucionalidad_y_Gobernanza | [{'LE': 'Institucionalidad_Descentralizada_y_Transparente', 'OE_Resum': 'Consolidar institucionalidad regional, formar gestores públicos, incorporar innovación tecnológica y fortalecer mecanismos de control.'}, {'LE': 'Participacion_y_Equidad_Territorial', 'OE_Resum': 'Fortalecer mecanismos de participación y la gestión integrada subregional.'}] |
#### Programa de Gobierno Regional 2025 2029
#### ID
GN-P4-VISION-PROG-GOB
#### Def
Propuesta programática del Gobernador Regional que profundiza la ERD y organiza la acción de gobierno en ejes temáticos.
#### Ejes
- Infraestructura, conectividad y transformación digital.
- Economía, innovación y capital humano.
- Desarrollo social inclusivo.
- Medio ambiente y sostenibilidad.
- Institucionalidad y gobernanza regional.
- Gestión del riesgo de desastres y seguridad pública.
- Patrimonio, cultura e identidad.
#### Nuble Inteligente
#### ID
GN-P4-VISION-NUBLE-INTELIGENTE
#### Def
Visión para catalizar la transformación de Ñuble mediante tecnologías de la cuarta revolución industrial (IA, IoT, datos).
#### Pilares
| Nombre | Obj |
| --- | --- |
| Conectividad_Total_y_Habilitante | Establecer la conectividad digital como derecho habilitante para la Región Inteligente. |
| Potencia_Agroalimentaria_Inteligente_y_Sostenible | Transformar el sector agroalimentario con agricultura de precisión, gestión hídrica apoyada en datos e instrumentos de trazabilidad. |
| Ecosistema_de_Innovacion_y_Desarrollo_Tecnologico | Convertir a Ñuble en polo de desarrollo tecnológico, atrayendo talento en IA, software y biotecnología. |
| Industria_y_Servicios_4_0 | Modernizar y automatizar sectores clave como turismo, logística y manufactura para diversificar la economía. |
| Gobernanza_Inteligente_y_Bienestar_Humano | Usar tecnología para construir una gobernanza ágil, transparente y participativa que mejore los servicios públicos. |

## Parte V Transformacion Digital del Estado
### ID
GN-P5-TDE
### Ref
GN-GLOS-TDE
### Purp
Describir el marco estratégico, legal, técnico y de gobernanza de la Transformación Digital del Estado (TDE) y su impacto en la gestión del GORE.
### Fnd
Sintetiza lineamientos de la Estrategia de Gobierno Digital 2030, sus normas técnicas y guías de implementación.
### Ctx
- Destinado a funcionarios, directivos y equipos TIC del GORE que deben alinear su gestión con directrices nacionales de modernización.
### Fundamentos Estrategia Gobierno Digital
#### ID
GN-P5-TDE-FUNDAMENTOS
#### Purp
Establecer el porqué de la TDE, su visión de futuro y principios rectores.
#### Src
- Estrategia de Gobierno Digital 2030.
#### Vision 2030
#### Def
Chile consolida liderazgo digital con un Estado unificado, proactivo y confiable, basado en uso estratégico, ético y seguro de datos y un ecosistema de identidad digital al servicio de las personas.
#### Principios Rectores TDE
- Digital por diseño.
- Centrado en las personas.
- Gobierno integrado e interoperable (principio de 'una sola vez').
- Uso eficiente de recursos.
- Gobierno abierto, transparente y participativo.
- Innovación pública abierta y ecosistema GovTech.
- Entornos digitales seguros y confiables (protección de datos y ciberseguridad).
- Sistemas resilientes y sostenibles.
### Ejes Estrategicos y Desafios TDE
#### ID
GN-P5-TDE-EJES-DESAFIOS
#### Ejes Transformadores
- Servicios digitales centrados en las personas.
- Sector público eficiente mediante digitalización de procesos.
- Gestión inteligente basada en datos.
#### Ejes Habilitadores
- Gobernanza y rectoría digital.
- Competencias y talento digital.
- Identidad e infraestructura pública digital.
#### Desafios Estructurales
- Gobernanza fragmentada y marcos regulatorios débiles en datos e identidad.
- Baja confianza ciudadana en comparación internacional.
- Silos organizacionales y baja interoperabilidad de sistemas.
- Escasez de talento especializado y resistencia al cambio.
### Marco Institucional y Normativo TDE
#### ID
GN-P5-TDE-INST-NORMATIVO
#### Purp
Detallar institucionalidad que gobierna la TDE y normas que el GORE debe cumplir.
#### Institucionalidad Rectora
#### ID
GN-P5-TDE-INSTITUCIONALIDAD
#### Organo Rector
#### Nombre
Secretaría de Gobierno Digital (SGD)
#### Dep
Subsecretaría de Hacienda.
#### Mssn
Proponer y coordinar la Estrategia de Gobierno Digital y operar plataformas transversales del Estado.
#### Fnd
- Ley N°21.180 sobre Transformación Digital del Estado.
#### Req
- Todos los procedimientos administrativos deben realizarse por medios electrónicos.
- Plazo final de implementación plena aproximado a 2027 (cero papel).
#### Roles y Responsabilidades en el GORE
#### ID
GN-P5-TDE-ROLES-GORE
#### Purp
Describir roles que el GORE debe implementar para una gobernanza TIC adecuada.
#### Roles
| Nombre | Purp |
| --- | --- |
| Comite_de_Transformacion_Digital | Coordinar temas TIC estratégicos, liderar diagnóstico y plan de transformación digital. |
| Coordinador_de_Transformacion_Digital (CTD) | Enlace oficial del GORE con la SGD; lidera implementación del plan. |
| Oficial_de_Seguridad_de_la_Informacion (CISO) | Definir políticas de seguridad, gestionar riesgos y coordinar con la Agencia Nacional de Ciberseguridad. |
| Encargado_de_Proteccion_de_Datos (DPO) | Garantizar cumplimiento de la normativa de protección de datos personales. |
#### Normas Tecnicas Esenciales
#### ID
GN-P5-TDE-NORMAS-TECNICAS
#### Purp
Resumir normativas técnicas que operativizan la Ley 21.180.
#### Normas
-
  #### Nombre
  NT-Seguridad (DS N°7)
  #### Purp
  Establecer estándares de ciberseguridad basados en marcos como NIST.
  #### Req
  - Cada organismo debe contar con una Política de Seguridad de la Información.
-
  #### Nombre
  NT-Autenticacion (DS N°9)
  #### Purp
  Regular el uso de mecanismos oficiales de autenticación.
  #### Req
  - Uso de ClaveÚnica para personas y Clave Tributaria para empresas.
-
  #### Nombre
  NT-Interoperabilidad (DS N°12)
  #### Purp
  Regular el intercambio de datos a través de la Red de Interoperabilidad.
  #### Req
  - Uso de un Gestor de Acuerdos para formalizar intercambios y migrar desde plataformas heredadas.
-
  #### Nombre
  NT-Documentos_y_Expedientes (DS N°10)
  #### Purp
  Definir estructura y metadatos de documentos y expedientes electrónicos.
  #### Req
  - Contar con una Política de Gestión Documental.
-
  #### Nombre
  NT-Notificaciones (DS N°8)
  #### Purp
  Regular notificaciones vía Plataforma de Notificaciones y Domicilio Digital Único (DDU).
-
  #### Nombre
  NT-Calidad (DS N°11)
  #### Purp
  Asegurar calidad y continuidad de plataformas electrónicas.
  #### Req
  - Elaborar Catálogo de Plataformas y Plan de Mejora Continua.
### Pilares Habilitadores TDE para el GORE
#### ID
GN-P5-TDE-PILARES
#### Purp
Describir componentes técnicos y de gestión que el GORE debe adoptar como base para su transformación digital.
#### Gestion de Datos como Activo Estrategico
#### ID
GN-P5-TDE-PILARES-DATOS
#### Principio Rector
Los datos son un activo estratégico que debe ser gobernado.
#### Req
- Definir roles como Chief Data Officer y Data Stewards.
- Diseñar un plan de implementación y un modelo de gobernanza de datos.
#### Mech
- Aplicar el Marco de Referencia de Gestión de Datos del Estado (MGDE) para autoevaluar la madurez institucional.
#### Datos Abiertos
#### Req
- Publicar proactivamente datos de interés público en formatos abiertos (CSV, JSON) con metadatos estandarizados (ej. DCAT).
#### Purp
- Fomentar transparencia, investigación y creación de valor por parte de ciudadanía y sector privado.
#### Identidad Digital
#### ID
GN-P5-TDE-PILARES-IDENTIDAD
#### Modelo
#### Def
Modelo híbrido público-privado de identidad digital.
#### Corto Plazo
#### Act
- Consolidar ClaveÚnica como componente central de identidad.
- Implementar cédula de identidad digital.
- Implementar pasarelas de identidad que integren los mecanismos oficiales.
#### Rol GORE
#### Req
- Integrar sus sistemas con mecanismos oficiales de autenticación para garantizar seguridad y correcta identificación de usuarios.
#### Infraestructura y Plataformas Publicas
#### ID
GN-P5-TDE-PILARES-INFRA
#### Principio Adopcion
Cloud First (preferir servicios en la nube).
#### Req
- Priorizar uso de plataformas y servicios compartidos ofrecidos por la SGD para evitar duplicidad de esfuerzos y costos.
#### Plataformas Clave SGD
- FirmaGob (firma electrónica avanzada para funcionarios).
- DocDigital (comunicaciones oficiales entre organismos).
- SIMPLE (digitalización de procesos ciudadanos).
- Red de Interoperabilidad para intercambio de datos.
- Plataforma de Notificaciones asociada al Domicilio Digital Único.
### Gestion de Proyectos TIC y Capacidades Digitales
#### ID
GN-P5-TDE-PROYECTOS-CAPACIDADES
#### Purp
Establecer cómo el GORE debe gestionar iniciativas tecnológicas y desarrollar talento interno.
#### Ciclo de Vida de la Inversion TIC
#### ID
GN-P5-TDE-CICLO-INVERSION
#### Proceso EVALTIC
#### Purp
Proceso de DIPRES para aprobar técnica y presupuestariamente proyectos TIC antes de su inicio.
#### Req
- Formular proyectos TIC siguiendo criterios y plantillas EVALTIC.
#### Metodologia de Gestion de Proyectos
#### Rec
- Adoptar metodología de gestión de proyectos (tradicional, ágil o híbrida) para asegurar calidad y control.
#### Fnd
- La Guía Metodológica Unificada de la SGD define fases y plantillas mínimas (acta de constitución, cronograma, etc.).
#### Estrategia de Capacitacion y Talento Digital
#### ID
GN-P5-TDE-CAPACITACION
#### Desafio
Existe una brecha de competencias digitales en el Estado.
#### Estrategia Nacional
#### Obj
Fortalecer talento digital mediante trayectorias formativas por perfiles.
#### Rol GORE
#### Req
- Fomentar participación de funcionarios en capacitaciones de SGD y Servicio Civil.
- Identificar necesidades de capacitación para roles clave de la TDE (CTD, CISO, equipos TIC, etc.).
#### Perfiles Prioritarios
- Cargos directivos y jefaturas.
- Coordinador/a de Transformación Digital.
- Equipos de seguridad y ciberseguridad.
- Equipos TIC.
- Equipos de oficina de partes.
- Equipos de asuntos legales.
- Equipos de gestión documental.
