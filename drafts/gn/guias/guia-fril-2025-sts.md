---
_manifest:
  urn: urn:gn:kb:guia-fril-2025-sts
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/ipr/kb_gn_026_guia_fril_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- fril
- infraestructura
- inversion-publica
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_026_guia_fril_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_026_guia_fril_koda.yml: 3aca0ba1ca44ad48be392f8c310805f0410020dcd31808b08db83934122ed97e
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 2.38
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 4
    meat_count: 798
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/guias__guia-fril-2025-sts.md.json
---

# Instructivo FRIL 2025 – Región de Ñuble
## Source
### Contexto requerido
- Guía Operativa FRIL – Resolución Exenta N° 15.051/2023 SUBDERE
- Ley N° 21.796 – Ley de Presupuestos del Sector Público 2026 (Glosa 12, Programa 02, Subtítulo 33)
- DFL 1-19.175 – Ley Orgánica Constitucional de Gobierno y Administración Regional (LOC GORE)
- Ley N° 18.575 – Bases Generales de la Administración del Estado
- Ley N° 19.880 – Bases de los Procedimientos Administrativos
- Ley N° 21.074 – Fortalecimiento de la Regionalización
- Circular N° 11/2025 del Ministerio de Hacienda (Glosas GORE)
- Resolución N° 36/2024 de la Contraloría General de la República (Exención Toma de Razón)

## Glosario FRIL Conceptos Clave
### Proposito
Definir conceptos, siglas y actores clave utilizados en el instructivo FRIL 2025.
### Terminos
| ID | Sigla | Cpt | Def |
| --- | --- | --- | --- |
| GN-FRIL-GLOS-FNDR | FNDR | Fondo Nacional de Desarrollo Regional | Principal fuente de financiamiento de la inversión regional administrada por los Gobiernos Regionales. |
| GN-FRIL-GLOS-FRIL | FRIL | Fondo Regional de Iniciativa Local | Fondo FNDR destinado a proyectos de infraestructura comunal de menor escala, ejecutados principalmente por municipalidades. |
| GN-FRIL-GLOS-GORE | GORE | Gobierno Regional | Institución descentralizada, con personalidad jurídica y patrimonio propio, a cargo de la administración superior de la región. |
| GN-FRIL-GLOS-CORE | CORE | Consejo Regional | Órgano colegiado del GORE con facultades normativas, resolutivas y fiscalizadoras; aprueba instructivos y marcos de asignación FRIL. |
| GN-FRIL-GLOS-SUBDERE | SUBDERE | Subsecretaría de Desarrollo Regional y Administrativo | Organismo del Ministerio del Interior que emite la Guía Operativa FRIL y visa metodologías regionales de evaluación. |
| GN-FRIL-GLOS-MDSF | MDSF | Ministerio de Desarrollo Social y Familia | Responsable de la evaluación técnico-económica de iniciativas de inversión en el SNI. |
| GN-FRIL-GLOS-BIP | BIP | Banco Integrado de Proyectos | Plataforma del SNI para registro, evaluación y seguimiento de iniciativas de inversión, incluyendo proyectos FRIL. |
| GN-FRIL-GLOS-GESDOC | GESDOC | Sistema de Gestión Documental del GORE | Plataforma electrónica para el registro de oficios, resoluciones y anexos asociados a proyectos FRIL. |
| GN-FRIL-GLOS-RS | RS | Recomendado Satisfactoriamente | Resultado de evaluación técnica-económica que acredita que la iniciativa cumple requisitos normativos y de admisibilidad. |
| GN-FRIL-GLOS-IDI | IDI | Iniciativa de Inversión | Unidad de análisis del SNI que agrupa estudios, proyectos y programas de inversión pública. |
| GN-FRIL-GLOS-BNUP | BNUP | Bien Nacional de Uso Público | Terreno o espacio de dominio público destinado al uso de toda la comunidad (calles, plazas, áreas verdes, etc.). |
| GN-FRIL-GLOS-ITO | ITO | Inspector Técnico de Obra | Profesional responsable de supervisar técnicamente la ejecución de la obra financiada con FRIL. |

## Normativa FRIL Clave
### Proposito
Registrar las normas principales usadas como fundamento del instructivo FRIL 2025.
### Normas
| ID | Cpt | Def |
| --- | --- | --- |
| GN-FRIL-NORM-CPR-01 | Constitución Política de la República | Norma suprema del ordenamiento jurídico chileno; establece organización del Estado y principios de probidad, responsabilidad y control. |
| GN-FRIL-NORM-LOC-GORE-01 | Ley N° 19.175 (LOC GORE) | Ley Orgánica Constitucional sobre Gobierno y Administración Regional, texto refundido en DFL 1-19.175. |
| GN-FRIL-NORM-LEY-18575-01 | Ley N° 18.575 | Ley Orgánica Constitucional de Bases Generales de la Administración del Estado. |
| GN-FRIL-NORM-LEY-19880-01 | Ley N° 19.880 | Establece Bases de los Procedimientos Administrativos. |
| GN-FRIL-NORM-LEY-21796-01 | Ley N° 21.796 – Presupuesto 2026 | Ley de Presupuestos del Sector Público para el año 2026; incluye Glosa 12 de FNDR para FRIL. |
| GN-FRIL-NORM-LEY-21074-01 | Ley N° 21.074 | Ley de Fortalecimiento de la Regionalización del País. |
| GN-FRIL-NORM-DL575-01 | Decreto Ley N° 575 – Regionalización del País | Norma que establece principios y reglas de regionalización y FNDR. |
| GN-FRIL-NORM-RES36-CGR-2024-01 | Resolución N° 36/2024 CGR | Fija normas sobre exención del trámite de Toma de Razón para ciertos actos administrativos. |
| GN-FRIL-NORM-CIRC11-HACIENDA-2025-01 | Circular N° 11/2025 Ministerio de Hacienda | Imparte instrucciones sobre aplicación de glosas presupuestarias de Gobiernos Regionales. |
| GN-FRIL-NORM-RES15051-SUBDERE-2023-01 | Resolución Exenta N° 15.051/2023 SUBDERE | Fija Guía Operativa FRIL a nivel nacional. |

## Instructivo FRIL 2025
### Titulo
Instructivo FRIL 2025 – Región de Ñuble
### Proposito
Establecer reglas, requisitos, procesos y documentación para la formulación,
evaluación, adjudicación, ejecución y rendición de proyectos FRIL financiados
con recursos FNDR del GORE Ñuble durante el año presupuestario 2025.

### Destinatarios
- Municipalidades de la Región de Ñuble.
- Equipos técnicos de SECPLA y DOM comunales.
- Equipos de la División de Presupuesto e Inversión Regional (DIPIR).
- Equipos de la División de Desarrollo Social y Humano, Infraestructura y otras divisiones del GORE vinculadas a FRIL.
### Alcance
- Aplica a iniciativas FRIL 2025 financiadas con cargo a Subtítulo 33 FNDR.
- Complementa y particulariza la Guía Operativa FRIL emitida por SUBDERE.
- Vigente mientras no existan modificaciones relevantes en Ley de Presupuestos o normativa relacionada.
### Estructura Secciones
| ID | Cpt |
| --- | --- |
| GN-FRIL-SEC-1-RESOLUCION | Resolución Exenta que aprueba el instructivo FRIL 2025. |
| GN-FRIL-SEC-2-INTRO | Introducción, objetivos del programa y marco legal. |
| GN-FRIL-SEC-3-MONTO-MARCO | Montos máximos/mínimos, marco por comuna y prioridades. |
| GN-FRIL-SEC-4-LINEAMIENTOS | Lineamientos de postulación, categorías y reglas especiales. |
| GN-FRIL-SEC-5-PROHIBICIONES | Prohibiciones y restricciones a la postulación. |
| GN-FRIL-SEC-6-TERRENOS | Situaciones especiales de terrenos y documentación legal. |
| GN-FRIL-SEC-7-PLAZOS | Períodos y plazos de difusión, postulación, evaluación y asesoría. |
| GN-FRIL-SEC-8-PROCESO | Etapas y procesos: ingreso, admisibilidad, revisión y resultados. |
| GN-FRIL-SEC-9-DOC-POSTULACION | Documentación requerida para la postulación (checklist). |
| GN-FRIL-SEC-10-OTRAS-CONSID | Otras consideraciones de postulación y autorizaciones. |
| GN-FRIL-SEC-11-REEVALUACIONES | Reglas para reevaluaciones de proyectos FRIL. |
| GN-FRIL-SEC-12-TRANSFERENCIAS | Transferencia de recursos, convenios y flujos de pago. |
| GN-FRIL-SEC-13-EJECUCION | Ejecución, licitación, adjudicación, contratación y garantías. |
| GN-FRIL-SEC-14-RENDICIONES-INFORMES | Rendiciones, informes y proyectos sin adjudicación. |
| GN-FRIL-SEC-15-MODIFICACIONES-TERMINO | Modificaciones de contrato, término de proyecto y vigencia del instructivo. |
| GN-FRIL-SEC-16-ANEXOS | Anexos operativos: checklist, planillas tipo y certificados. |
### Sec 1 Resolucion Exenta
#### Encabezado
#### Cpt
Resolución Exenta que aprueba instructivo FRIL 2025.
#### Numero
4A/00894/16.05.2025
#### Proposito
Aprobar instructivo para formulación y evaluación de iniciativas FRIL, año presupuestario 2025.
#### Vistos
#### Cpt
Marco normativo que sustenta la resolución.
#### Fundamento
| Ref |
| --- |
| GN-FRIL-NORM-CPR-01 |
| GN-FRIL-NORM-LOC-GORE-01 |
| GN-FRIL-NORM-LEY-21074-01 |
| GN-FRIL-NORM-LEY-18575-01 |
| GN-FRIL-NORM-LEY-21796-01 |
| GN-FRIL-NORM-LEY-19880-01 |
| GN-FRIL-NORM-DL575-01 |
| GN-FRIL-NORM-RES36-CGR-2024-01 |
| GN-FRIL-NORM-CIRC11-HACIENDA-2025-01 |
| GN-FRIL-NORM-RES15051-SUBDERE-2023-01 |
|  |
|  |
#### Considerandos
#### Cpt
Razones que justifican la emisión del instructivo FRIL 2025.
#### Just
- El presupuesto de Inversión Regional es instrumento fundamental para el desarrollo social, cultural y económico regional.
- Acuerdo del CORE para aprobar el Instructivo del Fondo Regional de Iniciativa Local (FRIL) 2025 (Sesión N°158, 09/04/2025, Certificado N°1177/2025).
- Visación de la metodología de evaluación FRIL por parte de SUBDERE (Oficio N°1667/2025).
- Acuerdo del CORE para modificar el plazo de postulación de proyectos FRIL 2025 (Sesión N°86, 14/05/2025, Certificado N°1198/2025).
- Necesidad de orientaciones técnicas y administrativas para optimizar el trabajo con eficiencia y eficacia.
- Necesidad de unificar normas vigentes para el buen uso de los recursos públicos.
#### Vigencia Instructivo
#### Nat
Indefinida hasta modificación por nueva resolución exenta.
#### Resuelvo
#### Acciones
- Aprobar el texto del Instructivo Concurso Postulación FRIL 2025 para financiamiento FNDR.
- Adjuntar certificados del CORE y oficio de visación de SUBDERE como parte integrante de la resolución.
- Ordenar la publicación de la resolución e instructivo en el sitio web del GORE Ñuble y en el portal de transparencia activa.
### Sec 2 Introduccion y Marco Programa
#### Introduccion Programa FRIL
#### Cpt
Programa FRIL.
#### Definicion
Mecanismo de financiamiento para proyectos de inversión en infraestructura comunal de menor escala.
#### Objetivos
- Elevar la calidad de vida de los habitantes de las comunas de la Región de Ñuble (urbano y rural).
#### Mecanismo
- Transferencia de recursos FNDR a municipalidades para ejecución de proyectos.
#### Fundamento
| Ref | Ctx |
| --- | --- |
| GN-FRIL-NORM-LEY-21796-01 | Asignación presupuestaria anual en Ley de Presupuestos. |
#### Proceso
| Act |
| --- |
| Municipios formulan y presentan iniciativas. |
| GORE evalúa iniciativas según Guía Operativa SUBDERE y lineamientos del instructivo regional. |
|  |
#### Objetivo Fondo FRIL
#### Objetivos
Financiar proyectos de infraestructura comunal de menor tamaño que mejoren la calidad de vida de la población, tanto en zonas urbanas
como rurales, priorizando iniciativas con alto impacto social y territorial.

#### Acciones Financiables
- Ejecución de infraestructura pública.
- Mantenimiento de infraestructura pública.
- Conservación de infraestructura pública.
| Ctx |
| --- |
| Incluye infraestructura social y deportiva. |
#### Fundamento
| Ref | Ctx |
| --- | --- |
| GN-FRIL-NORM-LEY-21796-01 | Glosa 12, Subtítulo 33, Programa 02. |
#### Marco Legal Programa
#### Cpt
Normativa que rige el programa FRIL 2025.
#### Fundamento
| Ref |
| --- |
| GN-FRIL-NORM-LOC-GORE-01 |
| GN-FRIL-NORM-LEY-18575-01 |
| GN-FRIL-NORM-LEY-21796-01 |
| GN-FRIL-NORM-RES15051-SUBDERE-2023-01 |
| GN-FRIL-NORM-CIRC11-HACIENDA-2025-01 |
### Sec 3 Monto y Marco a Postular
#### Monto Maximo Proyecto
#### Requisitos
- Monto máximo por proyecto: igual o inferior a 4.545 UTM (valorizada al 01.01.2025).
- Equivalente aproximado: $306.464.805 CLP.
#### Just
- Se descuenta un 10% del máximo normativo de 5.000 UTM para cubrir posibles aumentos de obra.
#### Monto Minimo Proyecto
#### Requisitos
- Monto mínimo por proyecto: $100.000.000 CLP.
#### Marco Por Comuna
#### Requisitos
- Postulación habilitada para las 21 comunas de la Región de Ñuble.
- Cada comuna puede postular hasta 5 iniciativas en el período regular.
- Monto total máximo a postular por comuna en período regular: M$1.000.000.
#### Llamados Extraordinarios
#### Condiciones
- El GORE podrá desarrollar llamados extraordinarios por áreas temáticas o por emergencias.
#### Mecanismo
- Los llamados se informan a las municipalidades por oficio.
- Requieren resolución exenta previa que defina marco, montos, justificación y plazos.
#### Prioridades GORE
#### Rec
- Priorizar proyectos con alto impacto social y territorial.
- Priorizar proyectos integrados con otras soluciones presentes en el territorio.
### Sec 4 Lineamientos de Postulacion
#### Acciones Financiables
#### Cpt
Obras civiles FRIL.
#### Acciones
- Construcción.
- Reposición.
- Mejoramiento.
- Habilitación.
- Normalización.
- Ampliación.
#### Categorias Proyecto
#### Requisitos
- Cada proyecto debe definirse en una sola categoría (la más relevante).
- Cada comuna debe presentar al menos un proyecto asociado a los ejes regionales de Salud, Seguridad o Reactivación Económica.
#### Tabla Categorias
#### Contexto
Resumen estructurado de categorías y subcategorías del instructivo.
#### Grupos
| Cpt |
| --- |
| A - Desarrollo Territorial |
| B - Servicios |
| C - Desarrollo Social y Económico |
| D - Medio Ambiente |
#### Reglas Especiales Postulacion
#### Excepcion Conteo Proyectos
#### Cpt
Excepción al máximo de 5 iniciativas por comuna.
#### Condiciones
- Proyectos en categorías A2 (Acceso al Agua) y A3 (Vial) no se contabilizan dentro del máximo de 5 proyectos.
#### Just
- El acceso al agua y el mejoramiento de caminos son fundamentales para el desarrollo regional.
#### Dep
- Aplicación sujeta a disponibilidad de revisión por parte de la unidad revisora FRIL del GORE.
#### Proyectos Multiubicacion
#### Condiciones
- Un proyecto puede considerar múltiples ubicaciones dentro de la comuna.
#### Requisitos
- Las ubicaciones deben compartir naturaleza, alcance y objetivo.
- Debe existir un solo presupuesto y una sola licitación para el conjunto.
### Sec 5 Prohibiciones Postulacion
#### Prohibiciones Generales
#### Prohibiciones
- Financiar gastos en personal, bienes y servicios de consumo de municipalidades.
- Adquirir o reponer activos no financieros que no formen parte de un proyecto de obras civiles.
- Financiar proyectos de servicios básicos que incluyan instalaciones domiciliarias privadas.
- Financiar proyectos con fines de lucro.
- Financiar proyectos por etapas (fraccionamiento de obras).
- Financiar dos o más proyectos en un mismo terreno o mismo tramo de BNUP en el mismo año presupuestario.
- Financiar dos o más proyectos para la misma actividad/uso en un mismo terreno en años distintos, si el primero no está ejecutado totalmente.
#### Criterios Terreno y Tramo
#### Cpt
Definición administrativa de terreno y tramo.
#### Contexto
- El terreno se identifica por el mismo rol de avalúo.
- El tramo vial se verifica con coordenadas y archivos KMZ, a criterio del GORE.
#### Vinculo ERD
#### Prohibiciones
- Postular proyectos que no indiquen su relación con la Estrategia Regional de Desarrollo de Ñuble 2020–2028 en el oficio conductor.
### Sec 6 Situaciones Especiales de Terrenos
#### Proyectos en Terrenos Privados
#### Condiciones
- Se permiten proyectos en terrenos privados bajo condiciones específicas que resguarden el uso público y la vida útil de las obras.
#### Proyectos Ley Indigena
#### Condiciones
- Proyectos de infraestructura social o deportiva en inmuebles que son bienes comunes de comunidades conformadas según Ley N° 19.253.
#### Requisitos
- Certificación de tenencia/posesión emitida por el Alcalde.
- Certificado de CONADI que acredite la condición de comunidad indígena.
#### Personas Juridicas Sin Fines de Lucro
#### Requisitos
- Acreditar calidad de persona jurídica sin fines de lucro, con documento municipal que indique directiva vigente.
- Acreditar que el privado otorga a la municipalidad el uso y goce de la propiedad por un período no inferior a la vida útil de las obras (usufructo o comodato).
- Presentar escritura pública inscrita en el Conservador de Bienes Raíces, incorporando la prohibición de enajenar por al menos 20 años.
- Adjuntar certificado simple de la unidad jurídica municipal que respalde la información legal de la propiedad.
#### Control GORE
#### Cpt
Control jurídico adicional del GORE.
#### Mecanismo
- El departamento jurídico del GORE podrá realizar análisis adicionales y solicitar más antecedentes si existen dudas.
### Sec 7 Periodos y Plazos
#### Difusion
#### Dln
- Desde la aprobación del marco presupuestario y durante todo el año 2025.
#### Postulacion
#### Llamados
| Cpt | Dln |
| --- | --- |
| 1er Llamado | Desde la aprobación administrativa del instructivo hasta 30 días corridos posteriores. |
| 2do Llamado | Desde el 01 de septiembre al 30 de septiembre de 2025. |
#### Evaluacion
#### Dln
- Desde el 01 de marzo de 2025 al 12 de diciembre de 2025.
#### Advertencias
- Iniciativas sin aprobación técnica a esa fecha serán calificadas como NO VIGENTE.
#### Asesoria Tecnica
#### Mecanismo
- Acompañamiento metodológico durante todo el año por parte de profesionales del Depto. de Análisis y Evaluación.
- Para colaboración adicional, los municipios deben enviar correo al coordinador del Depto. (dato de contacto en instructivo).
#### Otras Convocatorias
#### Condiciones
- Pueden desarrollarse convocatorias adicionales asociadas a Provisiones FNDR u otras materias específicas.
#### Mecanismo
- Se elaborará resolución exenta del Gobernador Regional con lineamientos, montos y plazos específicos.
### Sec 8 Etapas y Procesos FRIL
#### Ingreso Iniciativas
#### Mecanismo
- Ingreso de iniciativas vía banner 'FRIL' en la página web del GORE Ñuble, utilizando las credenciales de GESDOC.
#### Requisitos
- Usuarios deben estar habilitados con clave única y autorizados por su institución ante el administrador de GESDOC.
- Al presentar oficio y ficha IDI, todos los archivos requeridos para admisibilidad deben estar cargados en el BIP.
#### Resultados
- El incumplimiento de estos requisitos implica INADMISIBLE.
#### Admisibilidad
#### Definicion
Revisión formal de completitud de antecedentes y cumplimiento de requisitos mínimos del instructivo y la Guía Operativa.
#### Condiciones
- Serán inadmisibles las postulaciones fuera de plazo o que incluyan prohibiciones expresas del instructivo FRIL.
#### Etapa Revision y RATE
#### Dln
- El GORE dispondrá de un máximo de 60 días hábiles para emitir el primer Resultado de Análisis Técnico-Económico (RATE) desde el ingreso de antecedentes completos.
#### Resultados
- El análisis genera un acta de evaluación con resultados posibles: Recomendado (RS) o No Recomendado (FI, OT, NV, IN).
#### Resultado RS
#### Definicion
Recomendado Satisfactoriamente.
#### Condiciones
- Se otorga cuando la iniciativa cumple con todos los antecedentes administrativos, técnicos y normativa vigente.
#### Resultados
- Emisión de certificado RS, acta de evaluación, presupuesto final y ficha IDI aprobada.
- Habilita la iniciativa para ser presentada a aprobación de financiamiento, sujeta a disponibilidad presupuestaria.
#### Vigencia RS
#### Dln
- Vigente para el año en que se obtiene.
- El municipio dispone de 90 días desde la firma del convenio para presentar licitación; de lo contrario, se pierde vigencia de la aprobación técnica.
#### Resultado No Recomendado
#### Tipos
| Cpt | Cond |
| --- | --- |
| FI (Falta Información) | Faltan antecedentes, existen errores de cálculo o se requieren ajustes subsanables. |
| OT (Objetado Técnicamente) | Iniciativa mal formulada o con problemas técnicos/normativos insubsanables. |
| NV (No Vigente) | No se cumplen plazos de subsanación., El municipio informa que el proyecto ya no es de interés o se financió por otra vía. |
| IN (Incumplimiento de Normativa) | Se asignan recursos, adjudica, ejecuta gasto o se modifican archivos en BIP después de la aprobación técnica sin informe favorable del GORE. |
#### Dln
- Plazo para subsanar observaciones FI/OT: máximo 30 días hábiles, prorrogables a criterio del analista.
### Sec 9 Documentacion para Postulacion
#### Ref Checklist
#### Fuentes
DOC-GORE-NUBLE-FRIL-2025-ANEXO-01-CHECKLIST
#### Contexto
El instructivo detalla un checklist exhaustivo de documentos obligatorios. Este artefacto sintetiza sus requisitos clave.
#### Oficio Conductor
#### Requisitos
- Oficio del Alcalde(sa) al Gobernador Regional, firmado y registrado en GESDOC y BIP.
- Incluir nombre del proyecto concordante con ficha IDI y código BIP.
- Indicar relación con Estrategia Regional de Desarrollo (Ejes, Lineamientos).
- Indicar relación con PLADECO Comunal (Eje, Lineamiento, Acción).
- Especificar tipología (FRIL) y año presupuestario.
#### Ficha IDI
#### Requisitos
- Ficha IDI descargada desde BIP del año presupuestario en ejercicio (2025).
- Indicar Subtítulo 33 e inversión menor a 5.000 UTM.
- Toda la información debe ser coherente con el proyecto postulado.
#### Fotografias y Localizacion
#### Requisitos
- Mínimo 4 fotografías de la situación actual y su entorno, con descripción y antigüedad menor a 6 meses.
- Para proyectos viales, al menos 3 fotos de tramos representativos.
- Incluir localización con coordenadas UTM (Huso 18 Sur, Datum WGS84).
- Adjuntar archivo digital de ubicación en formato KML o KMZ.
#### Especificaciones Tecnicas
#### Requisitos
- Especificaciones detalladas (materialidad, dimensiones, métodos de ejecución).
- Itemizado de partidas coherente con presupuesto.
- Firmadas por profesional competente y Director(a) SECPLA.
#### Presupuesto Obras
#### Requisitos
- Presupuesto ingresado en BIP y GESDOC en formato PDF y Excel.
- Desglose por partidas (cantidad, precio unitario), gastos generales, utilidades e IVA.
- Planilla de cubicaciones por partida.
- Firmado por profesional competente y Alcalde(sa).
- El analista del GORE puede solicitar análisis de precio unitario (APU) cuando corresponda.
#### Certificacion Propiedad
#### Casuistica
| Cpt | Req |
| --- | --- |
| Caso A – Terreno Municipal | Escritura de la propiedad., Certificado de Dominio Vigente con Hipotecas y Gravámenes (vigencia máxima 60 días). |
| Caso B – BNUP administrado por municipio | Certificado DOM que acredite condición de BNUP (parques, plazas, calles). |
| Caso C – BNUP no administrado por municipio | Concesión, autorización de uso o proyecto aprobado por la entidad responsable del BNUP. |
| Caso D – Caminos Vecinales | Documentos que acrediten cumplimiento del Decreto 293/2008 del MOP. |
| Caso E – Terreno Privado (Comodato/Usufructo) | Escritura de usufructo o contrato de comodato inscrito en CBR, con prohibición de enajenar por período no inferior a vida útil de obras. |
#### Otros Documentos Claves
#### Incluye
- Certificado Compromiso Operación y Mantención (con costos mensuales/anuales y vida útil).
- Certificados de Factibilidad Eléctrica/Sanitaria.
- Permiso o Anteproyecto de Edificación o Informe Técnico OGUC, según corresponda.
- Títulos profesionales o patentes de responsables técnicos.
- Render o imágenes objetivo de obras.
- Planimetría completa (ubicación, emplazamiento, arquitectura, especialidades, topografía).
- Proyecto de Ingeniería si normativa lo exige.
- Certificados de Participación Ciudadana.
- Certificados de Pertinencia Técnica según tipo de proyecto.
#### Tabla Pertinencia Tecnica
#### Proposito
Tabla referencial de qué servicio o municipalidad emite el certificado de pertinencia técnica según tipo de proyecto.
#### Fuentes
- kb_gn_026_guia_fril_sts.md – Sección 2.10.15.
#### Filas
| Tipo_Proyecto | Servicio_Responsable | Tipo_Pertinencia |
| --- | --- | --- |
| Proyectos deportivos de uso formativo o competitivo | Instituto Nacional de Deportes | Pertinencia Servicio |
| Proyectos deportivos de uso recreativo | Municipalidad | Pertinencia Municipal |
| Obras de infraestructura educacional | SEREMI de Educación | Pertinencia Servicio |
| Obras de infraestructura de salud | SEREMI de Salud | Pertinencia Servicio |
| Proyectos de construcción o extensión de redes de alcantarillado y/o agua potable área urbana o rural | Dirección de Obras Hidráulicas | Pertinencia Servicio |
| Proyectos de construcción o extensión de redes de alcantarillado y/o agua potable área urbana o rural | Empresa sanitaria | Pertinencia Servicio |
| Proyectos de obras viales urbanos | Servicio de Vivienda y Urbanismo | Pertinencia Servicio |
| Proyectos de obras viales rurales | Dirección de Vialidad | Pertinencia Servicio |
| Obras en cauces de ríos | Dirección de Obras Hidráulicas | Pertinencia Servicio |
| Obras en cauces de ríos | Asociación de Canalistas | Pertinencia de institución |
| Proyectos de señalética vial en área urbana | SEREMI de Transporte y Telecomunicaciones | Pertinencia Servicio |
| Proyectos de señalética turística vial área urbana y rural | SERNATUR | Pertinencia Servicio |
| Proyectos de alumbrado público | Seremi de Energía | Pertinencia Servicio |
| Áreas verdes municipales | Municipalidad | Pertinencia Municipal |
#### Tabla Visacion Servicios
#### Proposito
Tabla referencial de qué servicio debe visar qué tipo de obra FRIL.
#### Fuentes
- kb_gn_026_guia_fril_sts.md – Sección 2.10.16.
#### Filas
| Tipo_Proyecto | Servicio_Responsable | Proyectos_Que_Contemplan_Visacion |
| --- | --- | --- |
| Proyectos deportivos de uso formativo o competitivo | Instituto Nacional de Deportes | Construcción o reposición de: Gimnasios, Multicanchas, Piscinas, Estadios, Canchas de tenis, Camarines, Graderías, Techos, Multicanchas, Medialunas, Entre otros. |
| Obras de infraestructura educacional | SEREMI de Educación | Construcción, reposición: Salas de clases, Laboratorios, Entre otros. |
| Obras de infraestructura de salud | Servicio de Salud de Ñuble | Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Establecimientos de salud, Entre otros. |
| Obras de infraestructura de salud | SEREMI de Salud | Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Alcantarillado, Agua potable área urbana, Agua potable área rural, Entre otros. |
| Proyectos de construcción o extensión de redes de alcantarillado y/o agua potable área urbana o rural | Dirección de Obras Hidráulicas | Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Agua potable área rural, Entre otros. |
| Proyectos de construcción o extensión de redes de alcantarillado y/o agua potable área urbana o rural | Empresa sanitaria | Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Agua potable área urbana, Entre otros. |
| Proyectos de obras viales urbanos | Servicio de Vivienda y Urbanismo | Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Pavimentos, Aceras, Evacuación de aguas lluvias, Aceras, Muros de contención, Puentes, etc. |
| Proyectos de obras viales rurales | Dirección de Vialidad | Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Pavimentos, Evacuación de aguas lluvias, Aceras, Muros de contención, Puentes, Refugios peatonales, etc. |
| Pronunciamiento sobre instalaciones u obras cuyo emplazamiento requiera ocupar los terrenos de faja vial de un camino público rural | Dirección de Vialidad (paralelismos) | Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Alumbrado público. |
| Obras en cauces de ríos | Dirección General de Aguas | Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Obras de cauces de ríos, Entre otros. |
| Obras en cauces de ríos | Dirección de Obras Hidráulicas | Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Obras de cauces de ríos, Entre otros. |
| Obras en cauces de ríos | Asociación de Canalistas | Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Obras de cauces de ríos, Entre otros. |
| Proyectos de señalética vial en área urbana | SEREMI de Transporte y Telecomunicaciones | Construcción, reposición, mejoramiento, habilitación, normalización, ampliación (siempre que exista modificación de lo señalado en Manual de Señalética Vial): Semáforos, Demarcaciones viales, Señalética, Entre otros. |
| Proyectos de señalética vial en área urbana | Dirección de Tránsito Municipal | Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Semáforos, Demarcaciones viales, Señalética, Entre otros. |
| Proyectos de alumbrado público (cuando corresponda) | Seremi de Energía | Reposición, mejoramiento, habilitación, normalización, ampliación (masivo): Alumbrado público (calles urbanas, rutas de vialidad, etc.), Alumbrado en plazas y áreas verdes. |
| Proyectos que requieran declaraciones o estudios de impacto ambiental | Servicio de Evaluación Ambiental | Consulta de Pertinencia, considerando lo indicado en artículo 26 del D.S. 40 de 2012 del Ministerio del Medio Ambiente (Reglamento del SEIA). |
### Sec 10 Otras Consideraciones
#### Activos No Financieros
#### Condiciones
- Se puede financiar mobiliario, equipamiento y equipos informáticos como parte de un proyecto de infraestructura FRIL.
#### Requisitos
- Solo unidades necesarias para la puesta en funcionamiento del recinto.
- Costo acumulado no debe superar el 10% del costo total del proyecto (salvo casos especiales de alumbrado público o infraestructura deportiva, evaluados caso a caso).
- Costo se imputa a obras civiles y se incluye como partida en presupuesto.
- Detalle de activos con al menos tres cotizaciones formales y cuadro comparativo técnico.
#### Prohibiciones
- No se pueden adquirir activos no financieros que no sean parte del proyecto de obras civiles.
#### Tramitacion Autorizaciones
#### Responsables
- Municipio es responsable de tramitar todas las autorizaciones de servicios competentes.
#### Requisitos
- Autorizaciones deben presentarse junto con el expediente para obtener recomendación técnica.
- Proyectos APR deben incluir memoria de cálculo de agua potable y torre de agua.
- Proyectos de ampliación/remodelación requieren que edificación existente cuente con permiso de edificación y recepción final.
- Todos los proyectos deben incorporar Accesibilidad Universal conforme OGUC y DS50.
#### De la Revision
#### Proposito
Precisar facultades de revisión del analista del GORE durante todo el proceso y el uso de visitas a terreno como parte del análisis.
#### Mecanismo
- El profesional analista del GORE puede formular nuevas observaciones durante todo el proceso de revisión, incluso después de subsanaciones anteriores.
#### Requisitos
- El analista debe, cuando la disponibilidad presupuestaria y de recursos lo permita, realizar visitas a terreno para revisar la integralidad del proyecto.
#### Responsables
- La División de Desarrollo Regional, a través de sus analistas, entregará asesoría técnica permanente a las municipalidades en la etapa de revisión.
### Sec 11 Reevaluaciones
#### Solicitud Reevaluacion
#### Dln
- Puede solicitarse desde 60 días después de la aprobación técnica y hasta 30 días corridos antes del término del plazo contractual de ejecución.
#### Requisitos
- Solicitud dirigida al GORE con resumen ejecutivo, informe ITO GORE (si obra en ejecución) y respaldos (presupuestos, cotizaciones, Carta Gantt).
#### Responsables
- Unidad responsable depende de la etapa: Depto. de Presupuesto (desde creación presupuestaria hasta adjudicación) y Depto. de Inversiones (desde adjudicación hasta recepción definitiva).
#### Dln Subsanar
- Plazo para subsanar observaciones de reevaluación: máximo 30 días corridos.
#### Casos No Acepta Reevaluacion
#### Prohibiciones
- Modificaciones menores que pueden registrarse en libro de obras.
- Cambios significativos del objetivo del proyecto (alcances, finalidad).
- Cambios de materialidad no justificados por habitabilidad o correcta ejecución.
- Aumento de obras sobre el 10% del monto original o sobre 5.000 UTM.
- Cambios de ubicación que impliquen cambio de rol, salvo que mantengan objetivo y se presenten todos los antecedentes del nuevo emplazamiento para nueva recomendación técnica.
#### Evaluacion Segun Instructivo Vigente
#### Mecanismo
- Las reevaluaciones se analizan respecto al instructivo vigente.
- Si un punto no está en instructivo vigente, se aplica el del año en que se aprobó la iniciativa.
### Sec 12 Transferencia de Recursos
#### Solicitud Financiamiento
#### Proceso
- Una vez que la iniciativa cuenta con RS, se elabora resolución que incorpora el proyecto al marco presupuestario.
- El Gobernador Regional aprueba el financiamiento e instruye a DIPIR a continuar con el proceso.
#### Convenio Transferencia
#### Responsables
- Depto. de Presupuestos gestiona la creación presupuestaria y suscripción del convenio GORE-Municipio.
#### Contenido Minimo
- Detalle de ítems de gasto.
- Modalidad de ejecución.
- Requisitos para modificaciones y transferencias de recursos.
- Derechos y obligaciones de las partes.
- Reglas de administración financiera y restricciones.
- Forma y oportunidad de rendiciones.
- Reglas de devolución de recursos.
- Especificaciones para señaléticas y placas.
- Proceso de cierre administrativo.
- Anexo con presupuesto detallado aprobado.
#### Transferencia a Municipios
#### Mecanismo
- Transferencia se realiza según programación financiera presentada por el municipio y avance efectivo de obras, avalado por ITO GORE.
#### Requisitos
- Recursos se depositan en cuenta corriente exclusiva para fondos FNDR.
- Primera transferencia se efectúa tras la entrega de antecedentes establecidos en el convenio.
- Transferencias posteriores se condicionan a rendiciones mensuales y avance de obra.
### Sec 13 Ejecucion Proyecto FRIL
#### Modelos Ejecucion
#### Cpt
La ejecución se rige por normativa de Municipalidades y Ley de Compras Públicas.
#### Mdl
- Ejecución Directa: la municipalidad ejecuta con sus propios procedimientos.
- Administración Delegada: la municipalidad supervisa técnica, administrativa y financieramente todo el proyecto ejecutado por terceros.
- Licitación Pública: modalidad principal para ejecución de obras FRIL.
#### Licitacion Publica
#### Dln
- Municipio debe llamar a propuesta en un plazo máximo de 45 días corridos desde la resolución que aprueba el convenio.
#### Advertencias
- El incumplimiento puede significar la reasignación de fondos.
- Si a los 90 días corridos desde el convenio no se ha licitado, la iniciativa pierde su recomendación técnica.
#### Requisitos
- Municipio debe nombrar Inspector Técnico de Obra (ITO) competente (ingeniero civil, ingeniero constructor, constructor civil, arquitecto).
#### Adjudicacion
#### Condiciones
- Municipio puede adjudicar si la oferta no supera el monto aprobado por el GORE.
#### Proceso
- Si la mejor oferta supera el monto aprobado, tras al menos 3 llamados a licitación, el municipio puede solicitar aumento de presupuesto al GORE.
#### Cond Adicional
- Aumento debe estar dentro del 10% del monto original y ajustarse a reglas de reevaluación FRIL.
#### Contratacion
#### Dln
- La contratación debe decretarse en un máximo de 20 días desde el acto que aprueba la adjudicación.
#### Advertencias
- El incumplimiento faculta al GORE para reasignar los fondos.
#### Requisitos
- Contratación bajo modalidad de suma alzada, sin reajustes ni intereses.
- Municipio debe remitir al GORE todos los antecedentes de adjudicación en un plazo no mayor a 15 días desde la entrega de terreno.
#### Garantias
#### Mecanismo
- Municipio puede exigir garantías por seriedad de la oferta, fiel cumplimiento de contrato y correcta ejecución.
#### Mdl
- Boletas de garantía bancaria, vale vista u otras modalidades permitidas por ley.
#### Requisitos
- Garantía de fiel cumplimiento: mínimo 10% del monto del contrato, con vigencia plazo contractual + 90 días.
- Garantía de correcta ejecución: mínimo 5%, con vigencia de 365 días desde la recepción provisoria sin observaciones.
#### Responsables
- Es responsabilidad exclusiva de la Municipalidad mantener vigentes las garantías.
### Sec 14 Rendiciones e Informes
#### Rendiciones
#### Cpt
Rendición de recursos FRIL transferidos a municipalidades.
#### Requisitos
- Los recursos FRIL no se incorporan al presupuesto municipal; se rinden a CGR y al GORE.
- Rendición conforme Resolución N° 30/2015 de CGR y normativa complementaria.
- Municipios deben enviar al GORE comprobante de ingreso, decretos de pago e informes mensuales de inversión.
#### Prohibiciones
- Los recursos solo pueden utilizarse para ejecución del mismo proyecto FRIL.
#### Informes
#### Requisitos
- Informe mensual debe remitirse dentro de los primeros 15 días hábiles administrativos del mes siguiente.
- Incluso sin movimiento, debe enviarse informe declarando 'sin movimiento'.
#### Proyectos sin Adjudicacion
#### Condiciones
- Obras no adjudicadas 90 días corridos después de la tramitación total del convenio podrán ser reevaluadas.
#### Requisitos
- Para solicitar la reevaluación por no adjudicación se debe haber cumplido con el número de llamados a licitación establecidos en la Ley N° 19.886 de Compras Públicas.
#### Contexto
- El instructivo establece consecuencias y tratamiento de proyectos sin adjudicación; se recomienda coordinar con DIPIR y DAF para ajustes presupuestarios y eventuales reasignaciones.
### Sec 15 Modificaciones y Termino
#### Modificaciones Contrato
#### Requisitos
- Toda modificación de contrato (salvo aquellas que solo ajustan plazo) debe ser autorizada por el GORE antes de su ejecución y a costo cero.
- ITO debe informar obligatoriamente al GORE sobre eventos relevantes (ejecución deficiente, incumplimientos, hechos sobrevinientes).
- Municipio debe informar por oficio al GORE modificaciones de plazos y/o paralizaciones.
- Cambios cualitativos y cuantitativos significativos requieren solicitar reevaluación al GORE.
- Solicitudes de modificación deben presentarse con al menos 30 días antes del término del plazo contractual.
#### Advertencias
- Solicitudes fuera de plazo pueden ser rechazadas.
#### Termino Proyecto
#### Requisitos
- Al finalizar la obra, la Unidad Técnica municipal debe remitir recepción provisoria y ficha de cierre al GORE.
- DOM fiscaliza cumplimiento de Ley General de Urbanismo y Construcciones hasta la recepción.
- Acta de recepción debe consignar fecha de entrega de terreno y eventuales atrasos imputables al contratista.
#### Proceso
- La recepción definitiva se realiza según plazos de bases de licitación y precede a la liquidación del contrato.
#### Vigencia Instructivo
#### Cpt
Vigencia y aplicabilidad territorial.
#### Contexto
- Aplica a comunas de la Región de Ñuble.
#### Dln
- Entra en vigencia a contar de la total tramitación del acto administrativo que lo aprueba.
- Permanece vigente mientras no existan cambios relevantes en Ley de Presupuestos y normas relacionadas.
#### Operatividad GESDOC
#### Conting
- Si el sistema GESDOC no está completamente operativo, la División de Planificación y Desarrollo Regional adoptará medidas para asegurar la postulación y resguardo de la información.
#### Acciones
- Dichas medidas deberán ser informadas oportunamente a cada municipalidad.
### Sec 16 Firmas y Anexos
#### Firmas y Distribucion
#### Acciones
- Se adjuntan certificados de acuerdo del CORE y oficio de visación de SUBDERE como anexos de la resolución.
- La resolución es firmada por el Gobernador Regional de Ñuble.
#### Dest
- Administración Regional – GORE Ñuble.
- División de Presupuesto e Inversión Regional – GORE Ñuble.
- División de Planificación y Desarrollo Regional – GORE Ñuble.
- División de Desarrollo Social y Humano – GORE Ñuble.
- División de Infraestructura y Transporte – GORE Ñuble.
- División de Fomento e Industria – GORE Ñuble.
- Departamento de Análisis y Evaluación DIPIR – GORE Ñuble.
- Departamento de Presupuesto de Inversión Regional – GORE Ñuble.
- Oficina de Partes.
#### Anexos Operativos
#### Proposito
Resumir anexos críticos (checklist, planillas y certificados) y remitir a plantillas detalladas en documentos fuente.
#### Anexo 1 Checklist Postulacion
#### Proposito
Listar la totalidad de archivos requeridos para la evaluación de una iniciativa FRIL 2025.
#### Requisitos
- Oficio conductor firmado e ingresado en GESDOC y BIP.
- Ficha IDI 2025.
- Fotografías y localización (coordenadas + KML/KMZ).
- Especificaciones técnicas y presupuesto por partida.
- Certificación de propiedad según tipología de terreno.
- Certificados de operación y mantención, factibilidad, permisos, participación ciudadana, pertinencia técnica y otros según tipo de proyecto.
#### Advertencias
- Al momento de la presentación del oficio, todos los archivos del checklist deben estar cargados en BIP y GESDOC.
#### Anexo 2 Especificaciones Tecnicas
#### Proposito
Establecer el formato y contenido mandatorio para el documento de Especificaciones Técnicas (EE.TT.) de proyectos FRIL.
#### Bloque Identificacion Proyecto
#### Cpt
Ficha de identificación.
#### Requisitos
- Codigo BIP.
- Ubicación.
- Superficie (m², ml, unidades, etc.).
- Arquitecto.
- Unidad Técnica (municipalidad).
- Mandante (municipalidad).
- Unidad Financiera: Gobierno Regional de Ñuble.
#### Generalidades
#### Requisitos
- Las obras deben ejecutarse considerando planos, EE.TT., reglamentos, normas y legislación vigente.
#### Concordancias
#### Cpt
Relación entre planos y EE.TT.
#### Definicion
Los planos y las EE.TT. son complementarios.
#### Responsables
Contratista.
#### Acciones
- Conocer y compatibilizar todos los documentos del proyecto.
- Informar diferencias antes de iniciar la construcción.
#### Orden Prelacion Documentos
#### Cpt
Orden de prelación en caso de divergencias.
#### Orden
- Consultas y aclaraciones en portal Mercado Público.
- Instrucciones y criterios de la Inspección Técnica de Obra (ITO).
- Planos de detalles (escalas mayores sobre generales).
- Especificaciones Técnicas Generales y de especialidad.
- Proyecto de Arquitectura y Detalles.
- Especificaciones Técnicas.
- Planos de Estructuras.
#### Condiciones
- Ante divergencias entre profesionales, prevalece el arquitecto autor del proyecto.
#### Administracion y Control Obra
#### Calidad Materiales
#### Requisitos
- Todos los materiales deben ser de primera calidad dentro de su especie.
#### Auth
- La ITO rechazará materiales que no cumplan lo especificado.
- La ITO puede solicitar ensayos o certificaciones técnicas en cualquier etapa.
#### Condiciones
- Si se especifica una marca, es referencial; se pueden proponer alternativas de calidad igual o superior, sujetas a aprobación de la ITO.
#### Archivos Obra
#### Requisitos
- Mantener en obra un juego completo de planos actualizados y ordenados.
- Solo tendrán validez planos firmados y timbrados en original.
#### Permisos
#### Responsables
- El Contratista es responsable de cancelar todos los permisos y derechos asociados a la construcción (rotura de vías, empalmes, etc.).
#### Inspeccion Tecnica Obra
#### Responsables
- El control de la obra estará a cargo de la ITO, nombrada por el mandante.
#### Requisitos
- El contratista debe cumplir estrictamente todas las instrucciones de la ITO, registradas en el Libro de Obra.
#### Prohibiciones
- La ITO no puede efectuar cambios al proyecto sin V°B° del arquitecto proyectista y del Mandante.
#### Libro Obras
#### Requisitos
- Mantener un Libro de Obra tipo MANIFOLD triplicado en obra.
- Registrar entrega de terreno, control de trabajos, aclaraciones, marcha de faenas, recepción de materiales, atrasos, observaciones y recepción de obras.
#### Normas Seguridad
#### Responsables
- El contratista asume responsabilidad completa por daños a personas o propiedad.
#### Requisitos
- Tomar todas las medidas de seguridad para evitar accidentes.
- Asegurar uso de Elementos de Protección Personal (EPP) adecuados por parte de todo el personal.
#### Obras Civiles y Provisionales
#### Gastos Adicionales
#### Cpt
Certificados de ensayos de materiales.
#### Responsables
- El contratista debe realizar y costear ensayos en laboratorios autorizados.
#### Requisitos
- Entregar informe de ensayo a la ITO y registrarlo en Libro de Obra.
#### Limpieza y Cuidado
#### Responsables
- El contratista debe mantener la obra aseada, ordenada y con vigilancia hasta la recepción final.
#### Obras Provisionales
#### Instalaciones Provisorias
#### Requisitos
- Ejecutar empalmes provisorios a redes de electricidad, agua potable y alcantarillado.
- Dar de baja todas las conexiones provisorias al finalizar la obra.
- Instalar señalética preventiva y protecciones.
#### Construcciones Provisorias
#### Requisitos
- Construir bodega de herramientas y materiales, con recintos separados para materiales delicados.
- Construir o habilitar oficina para ITO y Profesional Residente (con equipamiento básico).
- Construir servicios higiénicos para el personal (WC, lavamanos, urinario, ducha).
- Desarmar y retirar todas las construcciones provisorias al finalizar la obra.
#### Trabajos Previos
#### Requisitos
- Despeje de terreno según descripción del proyecto.
- Escarpe y nivelación de terreno según especificaciones.
- Escarpe, relleno y compactación con espesores y materiales definidos.
- Trazado, niveles y replanteo conforme a dimensiones y métodos establecidos.
#### Letrero y Placa
#### Letrero Obras
#### Requisitos
- Construir letrero de obras según Normas Gráficas del GORE Ñuble.
#### Spec
- Tamaño tipo 00: 5,00 m (ancho) x 2,00 m (alto).
- Impresión en vinilo PVC o autoadhesivo de alta calidad, resistente al agua, con tintas con filtro UV (garantía 3 años).
- Tipografía obligatoria: Museo Sans.
#### Prohibiciones
- No se puede añadir logotipo de la constructora; solo su nombre en sección 'Contratista'.
#### Contenido
- Nombre del proyecto (según Ficha IDI).
- Financia: Gobierno Regional de Ñuble.
- Inversión: monto total en M$.
- Fecha de inicio (según acta entrega de terreno).
- Plazo de ejecución (según oferta adjudicada).
- Unidad técnica.
- Contratista.
#### Estructura Valla
#### Spec
- Pilares: 3 unidades, perfil rectangular 100x100x3 mm.
- Vientos: diagonales, perfil 50x50x3 mm.
- Fundación: hormigón, profundidad mínima 0,75 m.
- Marco: perfil 20x20x2 mm, 5,0x2,0 m.
- Soporte gráfica: plancha de zinc 0,5 mm.
#### Advertencias
- Especificaciones estructurales son mínimas y deben corroborarse con memoria de cálculo.
#### Placa Informativa
#### Requisitos
- Instalar al menos una placa informativa.
#### Spec
- Material: acero fotograbado bajo relieve.
- Medidas mínimas: 80 cm (ancho) x 60 cm (alto).
- Debe usar marco oficial del GORE descargable desde sitio web.
#### Contenido
- Nombre del proyecto y logos (GORE y organización) del mismo tamaño.
- Frase: 'Iniciativa realizada con apoyo del Gobierno Regional de Ñuble, siendo Gobernador (nombre del Gobernador Regional)'.
#### Obra Gruesa y Firmas
#### Obra Gruesa
#### Requisitos
- Describir todas las partidas de la obra en concordancia con el presupuesto oficial.
#### Ex
- Fundaciones: hormigón premezclado con parámetros de dosificación, docilidad y control de calidad.
#### Auth
- Se debe solicitar autorización a la ITO antes de llenar fundaciones.
#### Advertencias
- La ITO puede ordenar demolición de estructuras con segregaciones o desniveles.
#### Prohibiciones
- No se aceptan demoliciones posteriores para pasar instalaciones; deben dejarse espacios previstos.
#### Firmas
#### Requisitos
- El documento debe ser firmado por Profesional Responsable y Director(a) de SECPLA, indicando nombre, RUT y profesión.
#### Anexo 3 Presupuesto Oficial
#### Proposito
Definir la estructura y desglose de partidas mandatorio para el presupuesto de proyectos FRIL.
#### Formato
#### Frmt
- Presupuesto en formatos Excel y PDF, según secciones de documentación del instructivo.
#### Encabezado
#### Requisitos
- Nombre del Proyecto (según Ficha IDI).
- Código BIP.
- Comuna.
- Mandante.
- Fecha.
#### Columnas Obligatorias
#### Requisitos
- ITEM
- DESCRIPCION
- UNIDAD
- CANTIDAD
- PRECIO UNITARIO
- PRECIO TOTAL
#### Estructura Partidas
#### Cpt
Estructura jerárquica de ítems y sub-ítems del presupuesto.
#### Tabla Resumen
#### Contexto
- La planilla debe contemplar, al menos, los siguientes grupos de partidas, siguiendo el detalle del instructivo:
#### Grupos
- 1 GASTOS GENERALES (letrero de obra, ensayos de laboratorio, fletes, permisos y derechos, utilidades).
- 2 OBRAS PROVISIONALES (instalaciones y construcciones provisorias).
- 3 TRABAJOS PREVIOS (limpieza, escarpe, nivelación, demoliciones).
- 4 OBRA GRUESA (excavaciones, hormigones, moldajes, enfierraduras, estructuras, albañilería, tabiquería, techumbre).
- 5 TERMINACIONES (revestimientos, puertas, ventanas, pinturas).
- 6 INSTALACIONES (alcantarillado, agua potable, electricidad, gas, climatización).
- 7 OBRAS EXTERIORES (cierros, pavimentos exteriores, áreas verdes, iluminación exterior).
- 8 EQUIPAMIENTO Y EQUIPOS.
- 9 OTROS (ítems específicos adicionales).
#### Resumen Costos
#### Requisitos
- Presentar COSTO NETO como suma de todos los precios totales.
- Calcular IVA 19% sobre costo neto.
- Calcular COSTO TOTAL PROYECTO como suma de costo neto + IVA.
#### Firmas
#### Requisitos
- Presupuesto debe ser firmado por Profesional Responsable (nombre, RUT, firma).
- Presupuesto debe ser firmado por Alcalde(sa) (nombre, RUT, firma).
#### Anexo 4 Certificado Costos Operacion Mantencion
#### Proposito
Definir el formato y contenido mandatorio del certificado que garantiza financiamiento de costos de operación y mantención del proyecto.
#### Entidad Emisora
#### Cpt
Quién puede emitir el certificado.
#### Requisitos
- Honorable Concejo Municipal de la municipalidad correspondiente.
- Organización usuaria del proyecto (indicando su RUT).
#### Contenido Mandatorio
#### Requisitos
- Identificación de la aprobación (tipo de sesión, número y fecha del acuerdo).
- Identificación del proyecto (nombre completo y código BIP).
- Declaración expresa de compromiso de financiar costos de operación y mantención.
- Periodo del compromiso (toda la vida útil estimada del proyecto, en años).
- Desglose de costos de operación y mantención (montos mensuales y anuales por separado).
- Cláusula de cierre que indique que el certificado se extiende para ser presentado al GORE Ñuble.
#### Mdl
- Texto tipo incluye fórmulas del estilo: 'en sesión N°..., de fecha ...', 'respecto al proyecto denominado...', 'durante toda su vida útil, estimada en ... años', y detalle de costos mensuales/anuales de operación y mantención.
#### Firmas Requeridas
#### Requisitos
- Firma 1: Alcalde(sa) o Presidente(a) de la organización (nombre, cargo, firma).
- Firma 2: Secretario(a) Municipal o Secretario(a) de la organización (nombre, cargo, firma).
#### Anexo 5 Permiso Anteproyecto o Informe Tecnico
#### Proposito
Definir documentación obligatoria para acreditar aprobación normativa de las obras a ejecutar según su tipología.
#### Requisitos
- Se debe adjuntar uno de los tres documentos siguientes, según características del proyecto.
#### Opcion 1 Permiso Edificacion
#### Condiciones
- Obligatorio para proyectos que contemplen construcción de obras nuevas, ampliaciones o reposiciones que legalmente requieran permiso.
#### Opcion 2 Anteproyecto Edificacion
#### Condiciones
- Puede presentarse cuando el proyecto requiere Permiso de Edificación pero este aún no está disponible al momento de postular.
#### Requisitos
- Debe ser emitido por la Dirección de Obras Municipales (DOM) correspondiente.
#### Opcion 3 Informe Tecnico Profesional
#### Contexto
- Aplicable a proyectos que no requieren Permiso de Edificación (por ejemplo, mejoramiento, habilitación, normalización).
#### Requisitos
- Indicar explícitamente el cumplimiento del proyecto con la Ordenanza General de Urbanismo y Construcción (OGUC).
- Estar firmado por profesional competente y por Director(a) SECPLA o Director(a) de Obras Municipales.
#### Anexo 6 Certificado Pertinencia Tecnica
#### Proposito
Establecer documentación obligatoria para certificar pertinencia técnica de la iniciativa y ausencia de duplicidad de financiamiento.
#### Requisitos
- Se debe presentar uno de los dos tipos de certificados, según la naturaleza del proyecto.
#### Opcion 1 Certificado Alcalde
#### Contexto
- Formato definido en Anexo 6 para proyectos donde el municipio tiene competencia técnica principal (ej. proyectos deportivos recreativos, áreas verdes municipales).
#### Requisitos
- Declarar que el terreno no se encuentra asociado a otra iniciativa de inversión con ninguna otra fuente de financiamiento.
- Declarar que la iniciativa postulada no se encuentra asociada a otra fuente de financiamiento (sectoriales, fondos propios, etc.).
#### Opcion 2 Certificado Servicio Competente
#### Condiciones
- Aplicable a proyectos que por su naturaleza involucran la competencia de otros servicios del Estado.
#### Requisitos
- Certificado emitido por el servicio al cual le compete la visación de la iniciativa (ej. SEREMI de Educación para infraestructura educacional, SERVIU para obras viales urbanas, SEREMI de Energía para alumbrado público).
#### Fuentes
- kb_gn_026_guia_fril_sts.md – Sección 4.2 a 4.6 (Anexos 2–6).
