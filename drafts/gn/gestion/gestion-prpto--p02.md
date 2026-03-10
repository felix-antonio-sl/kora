---
_manifest:
  urn: urn:gn:kb:gestion-prpto-p02
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-10'
    source: domains/gn/03_operacion/presupuesto/kb_gn_018_gestion_prpto_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- presupuesto
- finanzas-publicas
- gestion-regional
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/presupuesto/kb_gn_018_gestion_prpto_koda.yml
    source_hashes:
      domains/gn/03_operacion/presupuesto/kb_gn_018_gestion_prpto_koda.yml: 84d61c7a2af70675d2abcefaa4477ec3fbeb37cd83d79ac824e554660ec67819
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.91
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 12
    meat_count: 838
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gestion__gestion-prpto.md.json
  kora:
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:gn:kb:gestion-prpto
---

# Gestión Financiera y Operativa del Presupuesto Regional (GORE) - Parte 02

## Cierre Presupuestario
### Compromisos y Cortes
- **Acciones:** Definir fechas de corte para nuevos compromisos (usualmente diciembre) y comunicarlas.
- **Responsables:** DAF comunica fechas límite., DIPIR verifica registro adecuado de compromisos.
### Deuda Flotante
- **Definicion:** Obligaciones devengadas en el año pero pendientes de pago al 31 de diciembre.
- **Responsables:** DAF calcula, registra y tramita su incorporación en el presupuesto del año siguiente mediante creación del ítem 34.07 Deuda Flotante.
- **Fundamento:** Art. 34 Ley 21.796 permite exceder las sumas fijadas para este ítem.
- **Cpt:** Si el Saldo Inicial de Caja (SIC) supera la deuda flotante, se financia 100% con SIC (solo Resolución GORE)., Si SIC es insuficiente, se usa todo el SIC y la diferencia con mayor aporte fiscal (Resolución GORE + Decreto DIPRES).
- **Advertencias:** Priorizar pago de deuda flotante al inicio del nuevo ejercicio.
### Evaluacion y Cierre Sistemas
- **Acciones:** DAF realiza ajustes contables, prepara Informe de Ejecución Anual y genera nuevo SIC., DIPIR evalúa ejecución física de proyectos, identifica logros, retrasos y cuellos de botella, retroalimentando la siguiente formulación.
### ID Cierre Sistemas
- **Acciones:** DAF realiza cierre en SIGFE y DIPIR actualiza estado final en BIP.

## Gestion Subtitulos Presupuestarios
- **Referencias:** GN-PPTO-GLOS-FNDR, GN-PPTO-GLOS-FRIL, GN-PPTO-GLOS-FRPD
- **Proposito:** Describir subtítulos clave, su contenido y consideraciones operativas para la gestión regional.
- **Fuentes:** Chileindica y Ley de Presupuestos 2026.
- **Contexto:** Subtítulos clave: 21, 22, 23, 24, 26, 29, 31, 33, 34.
### Subtitulo 21 Gastos en Personal
- **Cpt:** Remuneraciones y obligaciones del empleador del personal del GORE.
- **Responsables:** DAF.
- **Acciones:** Asegurar que pagos respeten dotaciones, topes de glosas y normativa.
- **Ctx Flexibilidad 2026:** Glosa 01 Partida 31: sin límite de antigüedad para contratas; contratas pueden ejercer funciones directivas (hasta 20%); honorarios pueden actuar como agente público., Art. 05 Ley 21.796: suspensión de compatibilidad de cargo de planta con contrata.
#### Items Relevantes
- **Asunto:** Ítems del Subtítulo 21 relevantes para inversión regional.
- **Fuentes:** Documentos curados presupuesto/Chileindica.
- **Cpt:** Ítem 03 Otras Remuneraciones / Asignación 001 Honorarios a Suma Alzada: permite contratar profesionales para asesoría o ejecución en programas de inversión, clave para programas directos (Glosa 06).
### Subtitulo 22 Bienes y Servicios
- **Cpt:** Gastos operativos (insumos, servicios básicos, arriendos, pasajes).
- **Responsables:** DAF.
- **Acciones:** Gestionar adquisiciones vía Ley de Compras y buscar eficiencia.
- **Prohibiciones:** Prohibido reasignar recursos de inversión hacia Subtítulo 22 (Glosa 04 Partida 31).
- **Fundamento:** Incremento de Subtítulo 22 solo con ingresos propios o SIC.
- **Contexto:** DIPIR interviene solo cuando programas directos (Glosa 06) destinan parte de su 5% a este subtítulo.
#### Items Relevantes
- **Asunto:** Ítems del Subtítulo 22 relevantes para la inversión regional.
- **Cpt:** Ítem 08 Servicios Generales / Asignación 007 Pasajes, Fletes y Bodegajes: algunos gastos de consumo se informan como inversión pública regional en Chileindica.
### Subtitulo 23 Prestaciones Seguridad Social
- **Cpt:** Gastos por prestaciones previsionales y de asistencia social; uso en GORE generalmente bajo.
- **Responsables:** DAF.
### Subtitulo 24 Transferencias Corrientes
- **Cpt:** Recursos transferidos sin contraprestación directa para gastos corrientes de otras instituciones (funcionamiento e inversión asociados).
- **Nat:** Doble componente (funcionamiento e inversión).
- **Fundamento:** Transferencias a privados deben ser por concurso público y convenio (Art. 23-27 Ley 21.796).
#### Reglas Transferencias Privados 2026
- **Fundamento:** Art. 23-27 Ley 21.796.
- **Req General:** Transferencias corrientes y de capital a instituciones privadas deben ser resultado de concurso público abierto y transparente y materializarse mediante convenio., La asignación directa sin concurso procede sólo de forma excepcional y debe acreditarse mediante resolución fundada.
- **Causales Asignacion Directa Sin Concurso:** En concursos respectivos no se presentaron interesados., Sólo existe una persona jurídica como posible beneficiario o ejecutor., Emergencia, urgencia o imprevisto debidamente calificados.
- **Convenios Obligaciones y Prohibiciones:** El convenio debe indicar objeto social/fines del receptor y acreditar su pertinencia previamente a la suscripción., El convenio debe indicar actividades específicas y/o conceptos de gasto a financiar., No puede establecer compromisos financieros que excedan el ejercicio presupuestario sin autorización previa DIPRES., Debe condicionar la suscripción al cumplimiento íntegro de la Ley N°19.862., Rendiciones de cuentas deben realizarse vía Sistema de Rendición Electrónica de Cuentas (SISREC) CGR, según instrucciones CGR., Salvo plazo distinto en convenio, el organismo público tiene plazo máximo de 3 meses para pronunciarse fundadamente sobre la rendición., Debe exigir restitución si recursos se destinan a finalidad distinta, no se utilizan, no se rinden o son observados.
- **Reglas Ejecutoras Politica Publica:** Para instituciones privadas ejecutoras de políticas públicas: exigir al menos 2 años de antigüedad y experiencia acreditada., Exigir garantías cuando el total de recursos a transferir supere 1.000 UTM; garantía equivalente al 5% del monto total.
- **Inhabilidades Concursos y Convenios:** No podrán intervenir en procesos concursal/adjudicación/suscripción quienes tengan parentesco (hasta 4° consanguinidad/3° afinidad) con directivos o ejecutivos de institución participante., No podrán intervenir quienes hayan trabajado o desempeñado labores directivas en institución participante en los 2 años anteriores al cargo público., Debe dejarse constancia en actas de la nómina de funcionarias/os y personal a honorarios que intervino en el proceso.
- **Restituciones y Reintegros:** Los organismos públicos receptores que deban reintegrar recursos a rentas generales deben hacerlo a más tardar dentro del mes siguiente al cierre de la rendición., El proceso de rendición no podrá extenderse por más de 6 meses desde la finalización de la ejecución del convenio.
#### Items
- **Cpt:** Ítem 01 Al Sector Privado., Ítem 03 A Otras Entidades Públicas., Ítem 04 A Empresas Públicas no Financieras., Ítem 05 A Empresas Públicas Financieras., Ítem 08 A Instituciones Privadas Ejecutoras de Políticas Públicas., Ítem 09 A Unidades o Programas del Servicio.
#### Transferencias Item09 Unidades Programas Servicio 2026
- **Fundamento:** Art. 07 Ley 21.796.
- **Condiciones:** Transferencias corrientes a Unidades o Programas del Servicio, ejecutados total o parcialmente por éste.
- **Requisitos:** Desglose previo a la ejecución presupuestaria en conceptos de gasto, según visación DIPRES., Reporte mensual a DIPRES: avance de actividades e información de ejecución presupuestaria.
- **Resultados:** El desglose constituye autorización máxima de gasto por concepto; modificaciones por igual procedimiento., Personal contratado con cargo a dichos recursos no forma parte de la dotación del Servicio.
- **Prohibiciones:** No incluir recursos para gastos en personal ni bienes y servicios de consumo, salvo autorización por norma expresa en el respectivo presupuesto.
#### Concurso 8pct FNDR
- **Asunto:** Concurso de Vinculación con la Comunidad 8% FNDR.
- **Fuentes:** Glosa 07 Partida 31 Ley 21.796.
- **Condiciones:** Límite hasta 8% del total del presupuesto de inversión regional; mínimo 1% a cultura y patrimonio., Concursos exentos de evaluación ex-ante Glosa 06., Se podrá asignar hasta un 10% de los recursos del Concurso 8% para asignaciones directas asociadas con casos emblemáticos, excepcionales y emergentes, previo acuerdo del CORE y sujeto a la Resolución N°72 de 08.01.2025 DIPRES y sus modificaciones.
- **Contexto:** Actividades financiables: deportivas y del programa Elige Vivir Sano., Actividades financiables: seguridad ciudadana., Actividades financiables: participación de niños, niñas, adolescentes y jóvenes (Ley N°21.302, art. 6 letra p))., Actividades financiables: carácter social (discapacidad con dependencia severa, prevención y rehabilitación de drogas)., Actividades financiables: atención de adultos mayores e integración y promoción del envejecimiento activo., Actividades financiables: protección del medioambiente y educación ambiental., Actividades financiables: adopción, rescate, atención y tratamiento veterinario, y gestión de residuos de animales., Actividades financiables: funcionamiento de establecimientos de larga estadía para adultos mayores, residencias familiares para niños/niñas/adolescentes/jóvenes, y dispositivos del Servicio de Reinserción Social Juvenil., Actividades financiables: funcionamiento de teatros municipales o regionales y/o monumentos históricos con atención a público., Actividades financiables: culturales y patrimoniales., Ejecutores: municipalidades, otras entidades públicas, instituciones privadas sin fines de lucro, organizaciones de la sociedad civil y organizaciones comunitarias sin fines de lucro.
- **Proceso:** DIPIR elabora bases (aprueba CORE)., Comisiones evalúan., CORE aprueba adjudicados., DAF formaliza y fiscaliza transferencias.
#### Programas y Transferencias Publicas
- **Asunto:** Transferencias corrientes a entidades públicas y ejecución directa de programas.
- **Fundamento:** Glosa 06 Partida 31 Ley 21.796.
- **Condiciones:** Programas nuevos de ejecución directa requieren evaluación ex-ante DIPRES/MDSF., Prohibido usar inversión para financiar gastos permanentes de otros servicios (Glosa 03)., Receptor público puede usar hasta 5% para honorarios de gestión., Glosa 06 habilita financiar áreas fuera de competencias LOC GORE en casos específicos.
- **Referencias:** GN-PPTO-GLOS-FNDR, GN-PPTO-GLOS-FRIL, GN-PPTO-GLOS-DIPRES, GN-PPTO-GLOS-MDSF
#### Reglas Oferta Programatica Glosa06 2026
- **Fundamento:** Glosa 06 Partida 31 (GN-LEY-PPTO-2026-P31-GLO-06).
- **Excepciones Evaluacion ExAnte:** Programas que hayan iniciado su ejecución en años anteriores., Subvenciones asociadas al Concurso de Vinculación con la Comunidad 8%., Transferencias a universidades, municipalidades, otras entidades públicas y gobierno central e instituciones privadas beneficiarias sin fines de lucro., Ayudas tempranas e iniciativas de fomento productivo vinculadas a emergencias y desastres naturales, en coordinación con el Ministerio del Interior.
- **Principios:** Coherencia con políticas públicas nacionales, coordinación, unidad de acción, eficiencia y eficacia., Evitar duplicidad o interferencia de funciones con otros órganos de la Administración del Estado.
- **Regla 5pct Administracion GORE:** Se podrá destinar hasta un 5% del monto total de la transferencia a gastos de administración en el GORE (personal, bienes y servicios de consumo y adquisición de activos no financieros) asociados a la ejecución del programa., El personal contratado a honorarios con cargo al 5% tendrá la calidad de agente público.
- **Regla 5pct Honorarios Receptor Publico:** En la entidad pública receptora se podrá contratar personal a honorarios con cargo a la transferencia; vínculo cesará de pleno derecho al finalizar el convenio., No podrá ser superior al 5% del total de la transferencia recibida.
- **Ambitos Adicionales Permitidos:** Emergencia: prevención/mitigación incendios forestales; labores preventivas por eventos climatológicos; gestión del riesgo de desastres (Ley N°21.364) y continuidad de servicios APR; sanitización y calefacción ante catástrofes; ayudas tempranas y reconstrucción (coordinación Subsecretaría del Interior); demolición de infraestructura en mal estado (certificada por municipalidad)., Seguridad Pública: iniciativas de prevención y seguridad ciudadana., Salud: planes de resolución de lista de espera (coordinación MINSAL); cuidados de discapacidad en centros regionales de rehabilitación (instituciones privadas ejecutoras)., Cuidados: adultos mayores (SENAMA), condominios tutelados, ELEAM, auxilio extraordinario a personas en situación de calle (MDSF), distribución medicamentos a domicilio (Servicio de Salud)., Cambio Climático y Gestión de Residuos: protección ambiental/educación ambiental; mantención de parques/áreas verdes/jardines botánicos; operación tratamiento residuos/reciclaje/valorización; subsidios a municipalidades para disposición final residuos; gestión de residuos de animales., Energía, Transporte y Telecomunicaciones: autogeneración de energía; conectividad internet y radiocomunicaciones; subsidios Ley N°20.378; transporte escolar rural., Gestión Hídrica: funcionamiento/mantención/reparación sistemas APR y sanitarios rurales y/o desalinización; operación alcantarillado., Asistencia Técnica: asistencia técnica a municipalidades para fortalecer cartera de proyectos.
### Subtitulo 26 Otros Gastos Corrientes
- **Cpt:** Devoluciones y compensaciones por daños a terceros (uso bajo pero posible).
- **Items:** Ítem 01 Devoluciones., Ítem 02 Compensaciones por Daños.
- **Responsables:** DAF.
### Subtitulo 29 Activos No Financieros
- **Cpt:** Adquisición de bienes de capital del GORE (equipos, vehículos, terrenos).
- **Proposito:** Financiar reposición de activos para otras instituciones públicas (Glosa 09 Partida 31).
- **Condiciones:** Activos nuevos requieren certificado de disponibilidad presupuestaria para los gastos recurrentes que generen dichos activos., El certificado debe ser emitido por el Ministerio o la Subsecretaría respectiva., Para Fuerzas de Orden y Seguridad Pública: certificado de pertinencia emitido por el Ministerio de Seguridad Pública., Para Cuerpos de Bomberos: certificado de pertinencia técnica emitido por la Junta Nacional de Bomberos de Chile., Compra de terrenos: coordinar con SERVIU de la región respectiva, cuando corresponda.
- **Responsables:** DIPIR identifica necesidades; DAF ejecuta adquisición.
#### Items
- **Cpt:** Ítem 01 Terrenos., Ítem 02 Edificios., Ítem 03 Vehículos., Ítem 04 Mobiliario y Otros., Ítem 05 Máquinas y Equipos., Ítem 06 Equipos Informáticos., Ítem 07 Programas Informáticos., Ítem 99 Otros Activos no Financieros.
### Subtitulo 31 Iniciativas Inversion Directa
- **Cpt:** Inversión real ejecutada directamente por el GORE (unidad mandante).
- **Fundamento:** Glosa 10 Partida 31.
- **Requisitos:** Respetar competencias GORE y someterse al SNI., Licitación pública obligatoria si proyectos/programas de inversión superan 1.000 UTM (Art. 06 Ley 21.796)., Licitación pública obligatoria si estudios básicos superan 500 UTM (Art. 06 Ley 21.796)., Identificaciones presupuestarias de iniciativas contratadas en años anteriores en ejecución y aquellas creadas en el mismo año no requerirán nueva aprobación del CORE si los montos totales o resultantes son iguales o menores al 10% de los costos totales ya aprobados por el Consejo Regional, reajustados a la moneda del año en curso.
- **Proceso:** GORE actúa como unidad mandante; DAF gestiona licitación y contratación.
#### Alcances Glosa10 2026
- **Fundamento:** Glosa 10 Partida 31 (GN-LEY-PPTO-2026-P31-GLO-10).
- **Cpt:** Iniciativas adicionales permitidas: infraestructura pública (construcción, conservación y mejoramiento) en coordinación con ministerio sectorial., Iniciativas adicionales permitidas: transporte (coordinación MTT) en marco Ley N°20.378., Iniciativas adicionales permitidas: electrificación, gas, energía, conectividad digital, telefonía celular y comunicaciones (incluye conexiones domiciliarias)., Iniciativas adicionales permitidas: agua potable y alcantarillado; proyectos sanitarios en áreas de concesión de empresas del sector público; APR y mitigación/reparación por cambio climático (pequeños productores y habitantes rurales)., Regla especial 2026: saneamiento rural o proyectos en territorios insulares (SSR) pueden definir como Unidad Técnica a empresa pública o privada que opere en la región, mediante resolución fundada., DOH y Subdirección de Servicios Sanitarios Rurales informan a Gobiernos Regionales y Contraloría Regional regiones sin especialistas (20 enero y 30 junio)., Huellas y caminos vecinales privados de uso público: administración directa/contrato/compra servicio; requiere compromiso formal de transferencia de faja y visto bueno Dirección Regional de Vialidad., Personal a honorarios para ejecución de proyectos tendrá calidad de agente público.
#### Items
- **Cpt:** Ítem 01 Estudios Básicos., Ítem 02 Proyectos (estudios preinversionales y ejecución)., Ítem 03 Programas de Inversión.
### Subtitulo 33 Transferencias Capital
- **Cpt:** Transferencia de recursos a terceros para ejecutar proyectos de inversión; subtítulo de mayor peso.
- **Responsables:** Municipalidades, servicios públicos, corporaciones, etc.
- **Fundamento:** Glosa 11 Partida 31 y normativa complementaria.
- **Requisitos:** Cada transferencia debe formalizarse en un convenio con definición de objeto, monto, plazos, obligaciones, seguimiento y garantías.
- **Referencias:** GN-PPTO-GLOS-FNDR, GN-PPTO-GLOS-FRIL, GN-PPTO-GLOS-FRPD
#### Alcances Glosa11 2026
- **Fundamento:** Glosa 11 Partida 31 (GN-LEY-PPTO-2026-P31-GLO-11).
- **Cpt:** Iniciativas adicionales permitidas: PMU/PMB en coordinación con SUBDERE., Iniciativas adicionales permitidas: infraestructura social/deportiva en inmuebles con calidades jurídicas específicas y en inmuebles fiscales en tuición de organizaciones privadas sin fines de lucro con fines sociales., Iniciativas adicionales permitidas: caminos comunitarios en territorios Ley N°19.253 o de comunidades agrícolas., Iniciativas adicionales permitidas: fachadas de inmuebles privados con protección patrimonial., Iniciativas adicionales permitidas: protección/puesta en valor de Monumentos Nacionales, Inmuebles de Conservación Histórica, zonas de conservación, UNESCO y Lista Tentativa (incluye ejecución con sector privado)., Iniciativas adicionales permitidas: subsidios a empresas (públicas o privadas) para inversión social (electrificación, gas, energía, telefonía/comunicaciones), evaluadas como iniciativa de inversión por MDSF., APR/sanitarios rurales/desalinización: transferencia por resolución fundada del Gobernador Regional con efectos sin esperar total tramitación; requiere pronunciamiento técnico favorable Subdirección SSR., Transferencias a municipalidades y empresas sanitarias para monitoreo, mantenciones, diseño de soluciones y trabajos preventivos ante filtraciones de redes agua potable/alcantarillado; incluye pavimentación post recambio de redes; previa visación del órgano competente regional., Para proyectos de Construcción de Infraestructura Sanitaria financiados por GORE, rige límite de costo del art. 8° DS N°829/1998 del Ministerio del Interior y sus modificaciones.
#### Items
- **Cpt:** Ítem 01 Al Sector Privado., Ítem 03 A Otras Entidades Públicas (ítem principal de inversión GORE)., Ítem 04 A Empresas Públicas no Financieras., Ítem 05 A Empresas Públicas Financieras., Ítem 06 A Gobiernos Extranjeros., Ítem 07 A Organismos Internacionales.
#### Casos Especiales
- **Cpt:** FRIL: fondo para proyectos municipales de menor escala; seguir Guía Operativa FRIL SUBDERE (Resolución Exenta N°15.051 de 29 de diciembre de 2023)., FRIL: proyectos municipales con costo total por proyecto inferior a 5.000 UTM (valorizadas al 1 de enero del ejercicio presupuestario vigente) no requieren informe favorable MDSF; se debe ingresar al SNI la información necesaria según Oficio Ordinario N°2 de 26 de enero de 2024 e instructivo asociado., FRIL: GORE puede aprobar por resolución instructivos o bases (metodología distribución entre comunas, procedimientos de ejecución, entrega de recursos, rendición y otros)., FRIL: una vez aprobados los montos por municipio, el compromiso de financiamiento debe informarse mediante oficio dirigido al municipio respectivo., Emergencia hídrica: permite transferir a municipios y sanitarias para reparar redes de agua con visación de órgano técnico competente.
#### Roles
- **Responsables:** DIPIR articula cartera de proyectos, coordina RS, prioriza y coordina convenios y seguimiento técnico., DAF elabora aspectos financieros de convenios, ejecuta transferencias y revisa rendiciones.
### Subtitulo 34 Servicio de Deuda
- **Cpt:** Pagos asociados principalmente a la Deuda Flotante del año anterior.
- **Prohibiciones:** GORE no puede endeudarse sin ley especial.
- **Proposito:** Registrar y pagar la Deuda Flotante; uso de Ítem 34.07.
- **Advertencias:** Alto nivel de deuda flotante recurrente indica gestión deficiente.

## Glosas Relevantes y Fondos
- **Referencias:** GN-PPTO-GLOS-FNDR, GN-PPTO-GLOS-FRPD
### FNDR
- **Asunto:** Fondo Nacional de Desarrollo Regional.
- **Definicion:** Principal fuente de financiamiento de inversión regional.
- **Contexto:** Distribución (referencial): 90% asignado por ley, 10% gestionado por SUBDERE/DIPRES., DIPIR programa cartera para ejecutar 90%; DAF vigila uso autorizado de giros.
- **Requisitos:** Glosa 16 Partida 31 exige reporte trimestral de destino de fondos y publicación de proyectos.
### FRPD
- **Asunto:** Fondo Regional para la Productividad y el Desarrollo (FRPD).
- **Definicion:** Fondo que reemplaza al FIC, orientado a innovación, competitividad, ciencia y tecnología.
- **Fundamento:** Glosa 13 Partida 31 Ley 21.796., Art. 13 Ley 21.591 (Royalty Minero) y reglamento específico., Glosa 13 Partida 31 (GN-LEY-PPTO-2026-P31-GLO-13): Decreto N°1699 de 6 de diciembre de 2025 MH; Resolución Exenta N°33/2024 MinCiencia; Resolución Exenta N°08/2025 Subsecretaría de Economía y sus modificaciones.
- **Proceso:** Crear provisión FRPD en Ítem 33.03 del presupuesto inicial., Reasignar durante el año a iniciativas específicas vía modificaciones presupuestarias.
- **Cpt:** Evita doble concursabilidad., Tipología Innovación y Competitividad (Res. Ex. N°33 Subdere 2024) exenta de evaluación ex-ante Glosa 06; otras tipologías se rigen por normativa general., Se podrán transferir directamente recursos a iniciativas seleccionadas mediante concurso convocado por CORFO o ANID, cuyas instituciones ejecutoras estén incluidas en Resolución Exenta N°33/2024 MinCiencia y sus modificaciones., Se podrán efectuar creaciones y modificaciones de asignaciones para el pago de compromisos de arrastre de iniciativas ejecutadas por instituciones elegibles del Fondo de Innovación y Competitividad., Se podrá participar del financiamiento de iniciativas de Programas de Desarrollo Productivo Sostenible (Ministerio de Economía) y del Programa de Financiamiento Estructural I+D+i Universitario (Ministerio de Ciencia)., DIPIR gestiona fondo; DAF maneja provisión y control financiero.
### Equidad y Territorios Rezagados
- **Asunto:** Fondos para corregir desigualdades territoriales.
- **Cpt:** Fondo de Equidad Interregional, integrado al programa de inversión., Planes de Zonas Extremas y Territorios Rezagados, financiados con programa especial de Asociatividad y Planes Especiales.
### Subvenciones 8pct
- **Asunto:** Subvenciones concursables 8% FNDR.
- **Fundamento:** Glosa 07 Partida 31 Ley 21.796; vinculado a GORE-FIN-SUB-24-CONCURSO-8FNDR-01.
- **Requisitos:** Proceso de asignación transparente mediante concursos., Rendición de cuentas vía SISREC CGR (Art. 24 Ley 21.796).
### Asociatividad Regional
- **Asunto:** Asociatividad regional y participación en personas jurídicas.
- **Mecanismo:** GORE puede participar en corporaciones y fundaciones.
- **Fundamento:** Art. 101 LOC GORE; programa especial de asociatividad; Glosa 08 Partida 31 Ley 21.796.
- **Condiciones:** Aporte máximo GORE: 5% del presupuesto de inversión., Aportes para funcionamiento son anuales; no proceden convenios plurianuales., Cofinanciamiento máximo 50% con recursos GORE., Aportes privados pueden ser no pecuniarios, valorizados en convenio.
- **Requisitos:** Informar y publicar periódicamente sobre corporaciones financiadas., Al término del primer trimestre: informar a DIPRES y publicar en webs del GORE y corporación: razón social; misión/objetivos/productos; directorio; organigrama; instituciones que financian; vínculo con objetivos del GORE; planificación anual con resultados esperados., Trimestralmente (dentro de 30 días): número de profesionales, remuneración y perfil; concursos de contratación; recursos transferidos/ejecutados (período y acumulado); indicadores de gestión (avance físico y financiero de iniciativas)., Dar cuenta pública anual; mantener estados financieros publicados; regirse por Ley N°20.285 en lo aplicable.
### Universidades Regionales
- **Asunto:** Transferencias a universidades regionales.
- **Fundamento:** Glosa 05 Partida 31 Ley 21.796.
- **Cpt:** Habilita transferencias a universidades del DFL N°4 de 1981 con casa central en la región., Fines deben estar dentro de competencia universitaria y sujetarse a reglas de concursabilidad cuando aplique., Ejecución y uso: sólo para fines dentro del ámbito de competencia del establecimiento adjudicatario., Ejecución preferente por universidades con sede en la región respectiva., Ejecución íntegra por la propia universidad., Estas transferencias se podrán exceptuar del mecanismo de concursabilidad establecido en el articulado de la ley.
### Region Nuble Programa 19 2026
- **Fundamento:** Glosas específicas Gobierno Regional Región de Ñuble (Programa 19) Partida 31 Ley 21.796: GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19.
#### Funcionamiento Regional
- **Fundamento:** GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19.
- **Cpt:** Dotación máxima de vehículos: 5 (GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-01)., Gastos en personal: 4.222.003 miles (GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-02)., Incluye dotación máxima de personal 101, horas extraordinarias (Miles de $9.928), viáticos territorio nacional (Miles de $19.802) y exterior (Miles de $17.100), convenios con personas naturales (N°3; Miles de $115.294), funciones críticas (N°2; Miles de $23.242) (GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-03)., Monto máximo para gastos en el ítem de publicidad: 84.272 miles (GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-05).
#### Informes Especificos 2026
- **Cpt:** Informar trimestralmente a la Comisión Especial Mixta de Presupuestos sobre convenios y montos para compra y distribución de agua vía camiones aljibe u otros medios, comunas, población beneficiada y acciones para incentivar competencia (GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-06)., Informar trimestralmente a Comisiones de Economía del Senado y de la Cámara sobre proyectos de inversión a implementarse en Ñuble y efecto en generación de empleo regional (GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-07).

## Control Externo y Documentacion
### Toma de Razon y Control CGR
- **Asunto:** Toma de Razón y control de legalidad por CGR.
- **Cpt Hitos:** Resolución de presupuesto inicial., Resoluciones de modificaciones presupuestarias (previa visación DIPRES)., Decretos Supremos., Convenios relevantes.
- **Rec:** Planificar tiempos, asegurar calidad documental y archivar actos tramitados para futuras revisiones.
- **Referencias:** GN-PPTO-GLOS-CGR
### Documentacion DIPRES
- **Asunto:** Preparación de antecedentes para DIPRES.
- **Cpt Reportes:** Programa de ejecución y caja mensual., Ejecución presupuestaria mensual., Reporte trimestral de transferencias., Ejecución de inversión Subt. 31 por código BIP., Informe mensual de dotación de personal.
- **Rec:** Ante dudas, solicitar dictamen a DIPRES o CGR antes de ejecutar.
- **Referencias:** GN-PPTO-GLOS-DIPRES, GN-PPTO-GLOS-CGR
### Formatos y Anexos DIPRES
- **Asunto:** Formatos y anexos requeridos por DIPRES.
- **Fuentes:** Oficio Circular N°11 DIPRES 2025 (última versión disponible en corpus).
- **Proposito:** Estandarizar información remitida.
- **Cpt Anexos:** Anexo 1: Certificado de Acuerdo CORE., Anexo 2: Reporte Mensual de Ejecución., Anexo 3: Reporte Trimestral de Transferencias.

## Instrumentos de Ejecucion
### Convenios y Transferencias
- **Cpt:** El convenio de transferencia es la herramienta jurídica central para materializar transferencias Subt. 24 y 33.
- **Proposito:** Formalizar relaciones entre GORE y receptor, definir obligaciones y asegurar rendición.
- **Fundamento:** Art. 23-27 Ley 21.796 para transferencias a privados y normativa complementaria para entidades públicas.
- **Req Contenido Minimo:** Partes, objeto, monto, plazos y productos., Obligaciones de ejecución y seguimiento., Reglas de rendición de cuentas, reintegro de saldos y garantías.
- **Referencias:** GN-PPTO-GLOS-CGR, GN-PPTO-GLOS-DIPRES, GN-PPTO-GLOS-SIGFE, GN-PPTO-GLOS-SISREC
#### Proceso
- **Secuencia:** Elaboración de borrador., Suscripción por las partes., Entrega de garantías cuando corresponda., Toma de Razón si aplica., Ejecución (pago y monitoreo)., Rendición (SISREC)., Cierre (aprobación rendición y reintegro de saldos).
### Programas Directos GORE
#### Marco
- **Asunto:** Programas ejecutados directamente por el GORE (oferta programática adicional).
- **Fundamento:** Art. 20 letra k) LOC GORE; Glosa 06 Partida 31 Ley 21.796.
- **Mecanismo:** GORE desarrolla programas con cargo a presupuesto de inversión, ejecutados directamente o vía privados a través de concursos.
#### Evaluacion ExAnte
- **Requisitos:** Programas nuevos ejecutados directamente por GORE deben someterse a evaluación ex-ante de diseño por MDSF/DIPRES (Glosa 06).
- **Fuentes:** Oficio Circular N°22 DIPRES.
- **Proceso:** GORE nomina contraparte., Presenta perfil de programa., Completa Formulario de Diseño Ex-Ante., SES/DIPRES revisan y emiten certificado.
- **Resultados:** Recomendado Favorablemente (RF) es requisito para financiar el programa.
- **Cond Excepciones:** Continuidad de programas existentes., Concursos 8% FNDR., Transferencias a entidades públicas., Emergencias., Programas con RF previo o FRPD según Res. 33/2024.
#### Gastos Administracion Programas
- **Cpt Regla Clave:** GORE puede destinar hasta 5% del monto de cada programa a gastos de administración propios., Receptor público puede usar hasta 5% para contratar honorarios de gestión.

## Cumplimiento Hitos y KPIs
### Sistema Seguimiento Hitos
- **Proposito:** Instaurar sistema interno de seguimiento de hitos de ejecución física y financiera.
- **Proceso:** Planificación anual: DIPIR y DAF definen hitos y cronograma maestro., Monitoreo periódico: reuniones técnicas mensuales y directivas trimestrales., Coordinación interinstitucional con unidades técnicas., Alertas tempranas para detectar problemas y reaccionar oportunamente.
- **Referencias:** GN-PPTO-GLOS-DIPIR, GN-PPTO-GLOS-DAF
### Indicadores Desempeno
- **Asunto:** Indicadores clave para monitoreo de desempeño.
- **Fuentes:** Indicadores GORE Ñuble en Ley de Presupuestos (vigente).
- **Contexto:** La Ley fija indicadores de eficacia, eficiencia, calidad y economía para cada GORE.
- **Ejemplos Nuble:** % de proyectos Subt. 31 y 33 (incluyendo FRIL) con visita en terreno., % de iniciativas FNDR del PROPIR georreferenciadas y pertinentes., % de iniciativas de fomento productivo que benefician a mujeres.
- **Objetivos:** Lograr gestión por resultados evitando ejecución apresurada de fin de año ('dicembreo').
- **Referencias:** GN-PPTO-GLOS-FNDR, GN-PPTO-GLOS-FRIL, GN-PPTO-GLOS-PROPIR

## Herramientas de Soporte
### SIGFE
- **Definicion:** Sistema de Información para la Gestión Financiera del Estado, contable-presupuestario y transaccional.
- **Responsables:** DAF.
- **Proposito:** Control presupuestario en línea., Generación de reportes para DIPRES., Gestión de pagos y registro de todas las etapas del gasto.
- **Rec:** DIPIR debiera contar con usuarios de consulta para seguimiento de ejecución por iniciativa.
- **Referencias:** GN-PPTO-GLOS-SIGFE
### BIP
- **Definicion:** Banco Integrado de Proyectos, plataforma del SNI para registro y seguimiento de iniciativas de inversión.
- **Nat:** Registro único nacional de proyectos con código BIP.
- **Responsables:** DIPIR.
- **Proposito:** Evaluación ex-ante y obtención de RS/AD., Seguimiento físico y planificación multianual (ARI).
- **Advertencias:** Interoperabilidad limitada con SIGFE; requiere conciliaciones manuales.
- **Referencias:** GN-PPTO-GLOS-BIP, GN-PPTO-GLOS-SNI
### Chileindica
- **Asunto:** Plataforma Chileindica.
- **Fuentes:** Guías Chileindica e instructivo de coordinación ARI-PROPIR.
- **Definicion:** Plataforma para coordinación y seguimiento de inversión pública regional (ARI y PROPIR).
- **Contexto:** URL: https://www.chileindica.cl.
- **Proposito:** Formulación y aprobación de ARI y PROPIR., Seguimiento de ejecución del PROPIR.
- **Responsables:** SEREMI y servicios públicos regionales, en coordinación con GORE.
- **Referencias:** GN-PPTO-GLOS-ARI, GN-PPTO-GLOS-PROPIR, GN-PPTO-GLOS-GORE

## Conclusion General
### Sintesis
- **Cpt:** La gestión presupuestaria GORE es un proceso complejo que exige trabajo colaborativo entre DAF y DIPIR., DAF aporta rigor financiero, cumplimiento normativo y control de fondos., DIPIR aporta visión de desarrollo, priorización de inversiones y seguimiento de resultados., Objetivo cuantitativo: ejecutar 100% del presupuesto., Objetivo cualitativo: ejecutar con eficiencia, legalidad y pertinencia territorial., Claves del éxito: dominar el ciclo presupuestario, aplicar correctamente clasificador y glosas, documentar actos y someterse a controles, usando esta guía como referencia.
- **Resultados:** Una gestión presupuestaria sólida y confiable respalda los objetivos de desarrollo regional y la legitimidad del GORE frente a la ciudadanía y los órganos de control.
- **Referencias:** GN-PPTO-GLOS-GORE, GN-PPTO-GLOS-DAF, GN-PPTO-GLOS-DIPIR
