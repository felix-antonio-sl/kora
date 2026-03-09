---
_manifest:
  urn: urn:gn:kb:gore-ideal
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/01_fundamentos/intro/kb_gn_900_gore_ideal_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- gobernanza
- descentralizacion
- gore-4-0
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/01_fundamentos/intro/kb_gn_900_gore_ideal_koda.yml
    source_hashes:
      domains/gn/01_fundamentos/intro/kb_gn_900_gore_ideal_koda.yml: 1d810f7b8ad238e32a65a326820389cc6b269929ceee4af04ece2b6c170d35a1
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.53
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 6
    meat_count: 256
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gobernanza__gore-ideal.md.json
---

# GORE Ñuble Ideal / GORE 4.0
## Source
### Ctx Required
- staging/gn/kb_gn_900_gore_ideal.md
- DFL N° 1-19.175 (LOC GORE)
### Ctx Optional
- knowledge/domains/gn/kb_gn_000_intro_gores_nuble_koda.yml

## Glosario Conceptos Clave
### Proposito
Definir conceptos estructurales recurrentes del Gobierno Regional y del modelo GORE 4.0.
### Terminos
| ID | Cpt | Def | Src |
| --- | --- | --- | --- |
| GN-GORE-IDEAL-GLOS-GORE | Gobierno Regional (GORE) | Institución descentralizada con personalidad jurídica de derecho público y patrimonio propio, encargada de la administración superior de la región y del desarrollo social, cultural y económico del territorio. | Ley N° 19.175, Art. 13. |
| ID | Cpt | Def | Src |
| --- | --- | --- | --- |
| GN-GORE-IDEAL-GLOS-GOBERNADOR | Gobernador Regional | Máxima autoridad ejecutiva del GORE, elegida por sufragio universal directo, responsable de conducir políticamente el gobierno regional. | Ley N° 19.175, Art. 23. |
| ID | Cpt | Def | Src |
| --- | --- | --- | --- |
| GN-GORE-IDEAL-GLOS-CORE | Consejo Regional (CORE) | Órgano colegiado del GORE que representa territorialmente a la comunidad regional y ejerce funciones normativas, resolutivas y fiscalizadoras. | Ley N° 19.175, Art. 28. |
| ID | Cpt | Def |
| --- | --- | --- |
| GN-GORE-IDEAL-GLOS-DPR | Delegado Presidencial Regional (DPR) | Representante natural e inmediato del Presidente en la región, a cargo del gobierno interior y de la coordinación de servicios públicos nacionales. |
| ID | Cpt | Def | Src |
| --- | --- | --- | --- |
| GN-GORE-IDEAL-GLOS-ERD | Estrategia Regional de Desarrollo (ERD) | Instrumento de planificación de largo plazo que define visión, ejes y objetivos estratégicos para el desarrollo regional. | Ley N° 19.175, Art. 16. |
| ID | Cpt | Def | Src |
| --- | --- | --- | --- |
| GN-GORE-IDEAL-GLOS-PROT | Plan Regional de Ordenamiento Territorial (PROT) | Instrumento vinculante que orienta el uso del territorio regional y la localización de inversiones. | Ley N° 19.175, Art. 17. |
| ID | Cpt | Def | Src |
| --- | --- | --- | --- |
| GN-GORE-IDEAL-GLOS-FONDO-FNDR | Fondo Nacional de Desarrollo Regional (FNDR) | Principal fondo de inversión regional, destinado a financiar proyectos y programas priorizados por el GORE. | Ley N° 19.175, Art. 74. |
| ID | Cpt | Def |
| --- | --- | --- |
| GN-GORE-IDEAL-GLOS-FONDO-FRPD | Fondo Regional para la Productividad y el Desarrollo (FRPD) | Fondo financiado por el Royalty Minero para apoyar iniciativas de innovación, competitividad y fomento productivo. |
| ID | Cpt | Def | Src |
| --- | --- | --- | --- |
| GN-GORE-IDEAL-GLOS-FONDO-ISAR | Inversiones Sectoriales de Asignación Regional (ISAR) | Recursos de ministerios sectoriales cuya destinación territorial final es decidida por el GORE según prioridades regionales. | Ley N° 19.175, Art. 80. |
| ID | Cpt | Def |
| --- | --- | --- |
| GN-GORE-IDEAL-GLOS-DIGITAL-TWIN | Gemelo Digital (Digital Twin) del territorio | Modelo virtual dinámico que integra datos territoriales, sociales, económicos y ambientales de la región para simular escenarios de política pública. |
| ID | Cpt | Def |
| --- | --- | --- |
| GN-GORE-IDEAL-GLOS-GORE-4-0 | GORE 4.0 | Modelo ideal de Gobierno Regional que integra tecnologías de la Cuarta Revolución Industrial (IA, IoT, ciencia de datos) con su mandato de desarrollo territorial y gobernanza participativa. |

## Actores Clave
### Proposito
Identificar actores institucionales clave que intervienen en el ciclo del GORE y en sus límites funcionales.
### Entidades
| ID | Cpt | Def |
| --- | --- | --- |
| GN-GORE-IDEAL-ACTOR-MDSF | Ministerio de Desarrollo Social y Familia (MDSF) | Órgano que emite la Recomendación Satisfactoria (RS) para proyectos de inversión pública registrados en el Sistema Nacional de Inversiones. |
| ID | Cpt | Def |
| --- | --- | --- |
| GN-GORE-IDEAL-ACTOR-DIPRES | Dirección de Presupuestos (DIPRES) | Órgano responsable de la arquitectura programática y del control macro presupuestario del Estado, incluyendo lineamientos y visación de modificaciones presupuestarias. |
| ID | Cpt | Def |
| --- | --- | --- |
| GN-GORE-IDEAL-ACTOR-CGR | Contraloría General de la República (CGR) | Órgano superior de control de legalidad de los actos de la Administración del Estado y del examen de cuentas. |
| ID | Cpt | Ref | Rol |
| --- | --- | --- | --- |
| GN-GORE-IDEAL-ACTOR-CORE | Consejo Regional (CORE) | GN-GORE-IDEAL-GLOS-CORE | Actor político clave en la aprobación del presupuesto regional y en el control político interno sobre el Gobernador Regional. |

## Parte I Identidad y Motor GORE
### Referencias
- GN-GORE-IDEAL-GLOS-GORE
- GN-GORE-IDEAL-GLOS-GOBERNADOR
- GN-GORE-IDEAL-GLOS-CORE
### Introduccion
#### Proposito
Introducir la anatomía conceptual, operativa y potencial del Gobierno Regional.
#### Definicion
Presenta al GORE como institución autónoma de nivel intermedio, nacida del proceso de descentralización, que opera tensionada entre su legitimidad democrática y un Estado históricamente centralizado.
#### Objetivos
- Ofrecer una comprensión multidimensional del GORE más allá de la mera lectura legal.
- Conectar diseño normativo, restricciones operativas y visión de máximo potencial institucional.
### Cinco Pilares Identidad GORE
#### Pilar 1 Definicion Esencial
#### Referencias
GN-GORE-IDEAL-GLOS-GORE
#### Definicion
El GORE es la administración superior de la región, concebida como territorio con características e intereses propios, que acerca decisiones de desarrollo al lugar donde se producen sus efectos.
#### Proposito
- Adaptar la acción pública a particularidades locales.
- Materializar el principio de descentralización del Estado.
#### Pilar 2 Naturaleza Juridica
#### Definicion
El GORE es una persona jurídica de derecho público, autónoma patrimonial y de gestión.
#### Fuentes
- Ley N° 19.175, Art. 13 y 69.
#### Componentes
| Cpt | Res |
| --- | --- |
| Personalidad jurídica de derecho público | Puede adquirir derechos, contraer obligaciones, poseer bienes y ser parte en juicios. |
| Cpt | Res |
| --- | --- |
| Autonomía patrimonial | Dispone de patrimonio propio, administra y enajena bienes con acuerdo del CORE, para cumplir sus fines. |
| Cpt | Res |
| --- | --- |
| Autonomía de gestión | Define su organización interna y la administración de sus recursos dentro del marco legal. |
| Cpt | Def |
| --- | --- |
| Descentralización vs. desconcentración | El GORE es un ente descentralizado con autoridades electas, mientras que el Delegado Presidencial Regional es un órgano desconcentrado que representa directamente al nivel central. |
#### Pilar 3 Mision Estrategica
#### Definicion
El propósito del GORE es el desarrollo social, cultural y económico integral de la región.
#### Caracteristicas
- Foco estratégico de largo plazo, no solo administración cotidiana.
- Uso de la planificación como herramienta central (ERD, PROT y otros instrumentos técnicos vinculantes).
- Orientación a armonizar decisiones públicas con una visión de 5–20 años para el territorio.
#### Pilar 4 Origen Poder Legitimidad
#### Definicion
El poder político del GORE emana del sufragio universal que elige al Gobernador Regional y a los Consejeros Regionales.
#### Fuentes
- Ley N° 19.175, Art. 23 y 29.
#### Resultados
- Otorga una legitimidad democrática única en el nivel intermedio del Estado.
- Permite al Gobernador hablar 'en nombre de la región' y defender una agenda propia frente al nivel central.
#### Pilar 5 Arquitectura Dual Poder
#### Definicion
El diseño interno del GORE equilibra eficiencia decisional y representación democrática mediante un sistema dual de poder.
#### Componentes
| Cpt | Ref | Res |
| --- | --- | --- |
| Gobernador Regional | GN-GORE-IDEAL-GLOS-GOBERNADOR | Máxima autoridad ejecutiva, motor de iniciativa política, responsable de proponer políticas, planes y presupuesto. |
| Cpt | Ref | Res |
| --- | --- | --- |
| Consejo Regional (CORE) | GN-GORE-IDEAL-GLOS-CORE | Órgano colegiado que delibera, aprueba, modifica o rechaza las principales decisiones, y fiscaliza la gestión del Gobernador. |
| Cpt | Def |
| --- | --- |
| Equilibrio Ejecutivo–Colegiado | Ninguna decisión estratégica relevante se toma de forma unilateral; requiere negociación constante entre el órgano ejecutivo regional y el CORE. |
#### Pilar 6 Rol Coordinador
#### Definicion
La función coordinadora es el eje distintivo del GORE en un ecosistema con múltiples actores y jerarquías.
#### Mecanismo
- Utiliza la planificación (ERD, PROT) para fijar un marco común de acción para el territorio.
- Usa el financiamiento (FNDR, FRPD, ISAR) como palanca para alinear servicios públicos y municipios.
- Compra coordinación a través de incentivos presupuestarios más que por mando jerárquico.
### Motor Cinco Funciones
#### Definicion
El GORE opera mediante un ciclo integrado de cinco funciones: planificar, financiar, ejecutar, coordinar y normar.
#### Referencias
- GN-GORE-IDEAL-GLOS-GORE
#### Funciones
| Cpt | Def | Ref |
| --- | --- | --- |
| Planificar | Traducir la misión estratégica en instrumentos técnicos y vinculantes como la ERD y el PROT, validados por el CORE. | ['GN-GORE-IDEAL-GLOS-ERD', 'GN-GORE-IDEAL-GLOS-PROT'] |
| Cpt | Def | Ref |
| --- | --- | --- |
| Financiar | Administrar y asignar recursos de fondos como FNDR, FRPD e ISAR de acuerdo con la estrategia regional y con criterios técnicos de elegibilidad. | ['GN-GORE-IDEAL-GLOS-FONDO-FNDR', 'GN-GORE-IDEAL-GLOS-FONDO-FRPD', 'GN-GORE-IDEAL-GLOS-FONDO-ISAR'] |
| Cpt | Def |
| --- | --- |
| Ejecutar | Implementar programas propios (principalmente 'blandos') y viabilizar proyectos de inversión a través de convenios donde el GORE actúa como unidad financiera y otra entidad como unidad técnica. |
| Cpt | Def |
| --- | --- |
| Coordinar | Alinear servicios sectoriales, municipios y nivel central en torno a la estrategia regional, usando información, convenios y recursos como palancas de coordinación. |
| Cpt | Def |
| --- | --- |
| Normar | Dictar normas generales dentro de su competencia para regular procedimientos e instrumentos regionales, siempre subordinadas a la ley y a decretos supremos, y sujetas a control de legalidad externo. |

## Parte II Limites y Restricciones Modelo
### Introduccion
#### Definicion
La autonomía del GORE está acotada por un entramado de leyes, jerarquías y contrapesos que condicionan significativamente cada una de sus cinco funciones motoras.
### Limites Funcion Planificar
#### Items
| Cpt | Def | Src |
| --- | --- | --- |
| Coherencia con políticas nacionales y presupuesto | La planificación regional (ERD, PROT y otros instrumentos) debe ser coherente con las políticas públicas nacionales y con el Presupuesto de la Nación. No puede contradecir lineamientos sectoriales ni planificar más allá de los marcos de financiamiento nacionales. | ['Ley N° 19.175, Art. 20 bis y 16 letra a).'] |
| Cpt | Def |
| --- | --- |
| Competencia material y ámbitos excluidos | El GORE solo puede planificar materias para las cuales tiene competencias legales en los Art. 16–19 de la LOC GORE. Ámbitos como relaciones exteriores, defensa nacional, administración de justicia y orden público interno son no descentralizables y permanecen en el nivel central. |
| Cpt | Def | Src |
| --- | --- | --- |
| Coordinación obligatoria con entes sectoriales y municipios | Incluso dentro de sus competencias, la planificación debe realizarse en coordinación con organismos sectoriales y municipalidades, por ejemplo en seguridad pública preventiva y desarrollo territorial. La planificación regional se transforma en un ejercicio de negociación y acuerdo, no de imposición unilateral. | ['Ley N° 19.175, Art. 16 letras i) y c).'] |
| Cpt | Def |
| --- | --- |
| Planificación anidada y jerarquía multiescalar | La ERD y otros instrumentos regionales deben articularse con políticas nacionales hacia arriba y con instrumentos comunales hacia abajo, actuando como una capa intermedia en un sistema de planificación anidado. |
### Limites Funcion Financiar
#### Items
| Cpt | Ref | Def | Src |
| --- | --- | --- | --- |
| Control técnico externo (MDSF) | ['GN-GORE-IDEAL-ACTOR-MDSF'] | Ningún proyecto de inversión puede ser financiado con fondos regionales sin contar con informe técnico-económico favorable (Recomendación Satisfactoria, RS) del Ministerio de Desarrollo Social y Familia. | ['Ley N° 19.175, Art. 75.'] |
| Cpt | Ref | Def |
| --- | --- | --- |
| Control presupuestario central (DIPRES) | ['GN-GORE-IDEAL-ACTOR-DIPRES'] | La Dirección de Presupuestos define la arquitectura de programas, revisa el diseño de programas no sujetos al SNI y visa modificaciones relevantes en la Ley de Presupuestos, limitando la discrecionalidad regional. |
| Cpt | Ref | Def |
| --- | --- | --- |
| Control de legalidad (Contraloría General) | ['GN-GORE-IDEAL-ACTOR-CGR'] | Los actos administrativos que aprueban gastos y transferencias deben someterse a la Toma de Razón de la Contraloría. Si ésta estima que el acto es ilegal, el gasto no puede ejecutarse. |
| Cpt | Ref | Def | Src |
| --- | --- | --- | --- |
| Control político interno (CORE y umbral 7.000 UTM) | ['GN-GORE-IDEAL-ACTOR-CORE'] | El Gobernador propone, pero el CORE aprueba la distribución del presupuesto de inversión. Los proyectos que superan un umbral de 7.000 UTM requieren aprobaciones específicas, reforzando el rol resolutivo del Consejo. | ['Ley N° 19.175, Art. 36 letras d) y e), Art. 78.'] |
| Cpt | Def | Src |
| --- | --- | --- |
| Topes numéricos a transferencias a corporaciones | Los aportes a corporaciones privadas sin fines de lucro están sujetos a límites porcentuales tanto sobre el presupuesto de inversión como sobre el costo total del proyecto, y se prohíbe que el GORE garantice deudas de estas entidades. | ['Ley N° 19.175, Art. 101.'] |
| Cpt | Def |
| --- | --- |
| Restricciones por elegibilidad y rendición de cuentas | Fondos como ISAR solo pueden destinarse a iniciativas que cumplan los criterios del ministerio de origen, y la normativa de rendiciones impide nuevas transferencias a entidades con rendiciones pendientes, operando como freno inmediato al financiamiento. |
### Limites Funcion Ejecutar
#### Items
| Cpt | Def | Src |
| --- | --- | --- |
| Rol predominante como unidad financiera, no técnica | En la mayoría de los proyectos de inversión, el GORE actúa como unidad financiera que transfiere recursos a otra entidad pública que ejerce el rol de unidad técnica responsable de diseñar, licitar, construir y recepcionar las obras. | ['Ley N° 19.175, Art. 81 ter.'] |
| Cpt | Def |
| --- | --- |
| Ejecución directa restringida a programas 'blandos' | La ejecución directa del GORE se concentra en programas sin infraestructura compleja (capacitaciones, estudios, fomento productivo, cultura), reflejando limitaciones estructurales para operar como 'constructora' de grandes obras. |
| Cpt | Def | Src |
| --- | --- | --- |
| Prohibición de usurpar funciones sectoriales | Las competencias del GORE no alteran las funciones de la Administración central del Estado. No puede asumir de facto roles propios de ministerios como MOP o MINSAL; su lugar es financiar y coordinar, no reemplazar a los servicios especializados. | ['Ley N° 19.175, Art. 106.'] |
| Cpt | Def |
| --- | --- |
| Limitaciones prácticas de capacidades técnicas internas | La dotación de personal y capacidades del GORE está diseñada para planificación, evaluación y supervisión, no para ejecución en terreno; carece de masa crítica de ingenieros, inspectores y equipos necesarios para obras de gran escala. |
### Limites Funcion Coordinar
#### Items
| Cpt | Def | Src |
| --- | --- | --- |
| Ausencia de mando directo sobre servicios públicos | Los SEREMI dependen jerárquicamente de sus ministerios y colaboran con el Delegado Presidencial, no del Gobernador. La coordinación del GORE se ejerce sin subordinación formal sobre la mayoría de los servicios regionales. | ['Ley N° 19.175, Art. 62 y 63.'] |
| Cpt | Def |
| --- | --- |
| Autoridad paralela del Delegado Presidencial | El Delegado Presidencial Regional tiene atribuciones explícitas de coordinación, fiscalización y supervigilancia de servicios públicos nacionales, generando un polo de poder paralelo con frecuencia más fuerte en la cadena jerárquica que el del Gobernador. |
| Cpt | Def |
| --- | --- |
| Vínculo condicionado a relaciones financieras o competenciales | El poder de coordinación del Gobernador es más robusto cuando existe una relación directa (por ejemplo, a través de convenios de financiamiento o competencias transferidas); en ausencia de estos vínculos, su influencia es principalmente política. |
| Cpt | Def |
| --- | --- |
| Poder blando: convocar e informar, no instruir | La ley habilita al GORE a convocar y requerir información a servicios y municipios, pero no a impartir instrucciones jerárquicas. La coordinación efectiva depende de la calidad de la negociación y del uso estratégico del presupuesto como incentivo. |
### Limites Funcion Normar
#### Items
| Cpt | Def | Src |
| --- | --- | --- |
| Subordinación jerárquica a la ley y a los decretos supremos | Las normas regionales deben dictarse con sujeción a las leyes y a los decretos supremos; un reglamento regional que los contradiga es ilegal. | ['Ley N° 19.175, Art. 16 letra h).'] |
| Cpt | Def |
| --- | --- |
| Competencia material acotada a funciones propias | La potestad reglamentaria del GORE se restringe a materias vinculadas a sus funciones legales; no puede regular ámbitos reservados a otros ministerios o niveles de gobierno. |
| Cpt | Def |
| --- | --- |
| Control externo de legalidad (Toma de Razón) | Toda norma regional está sujeta a control preventivo obligatorio de la Contraloría; actos que excedan competencias o vulneren jerarquía normativa pueden ser objetados. |
| Cpt | Def |
| --- | --- |
| Procedimiento interno con contrapesos | El Gobernador tiene iniciativa reglamentaria, pero el CORE debe aprobar los reglamentos de funcionamiento y otras normas internas, evitando que un solo órgano concentre el poder normativo. |
| Cpt | Def |
| --- | --- |
| Publicidad como condición de vigencia | Las normas regionales solo adquieren fuerza obligatoria una vez publicadas en el Diario Oficial, reforzando la transparencia y la publicidad de las reglas de juego. |

## Parte III Vision GORE Ideal 4 0
### Introduccion
#### Definicion
Describe el despliegue máximo del potencial del Gobierno Regional en un escenario de condiciones ideales: alta colaboración intergubernamental, capacidades tecnológicas avanzadas y participación ciudadana robusta.
#### Cpt
- El GORE deja de ser una entidad principalmente reactiva y se convierte en motor proactivo de desarrollo, innovación y gobernanza territorial.
- Se configura un modelo 'GORE 4.0' que fusiona mandato de desarrollo con tecnologías de la Cuarta Revolución Industrial.
### Funcion Planificar 4 0
#### Mision
Posicionar al GORE como arquitecto del territorio inteligente mediante planificación basada en datos y simulaciones.
#### Dimensiones
| Cpt | Ref | Def |
| --- | --- | --- |
| Gemelo Digital del territorio | GN-GORE-IDEAL-GLOS-DIGITAL-TWIN | La planificación se apoya en un modelo vivo que integra variables territoriales, sociales, económicas y ambientales y permite simular impactos de políticas y proyectos antes de implementarlos. |
| Cpt | Ref | Def |
| --- | --- | --- |
| ERD y PROT como capas lógicas vinculantes | ['GN-GORE-IDEAL-GLOS-ERD', 'GN-GORE-IDEAL-GLOS-PROT'] | La ERD opera como hoja de ruta dinámica y el PROT como 'constitución territorial', ambos programados en el Gemelo Digital de modo que cualquier proyecto pueda ser testeado respecto de su alineamiento y coherencia multiescalar. |
| Cpt | Def |
| --- | --- |
| Centro de inteligencia territorial | El GORE lidera un sistema de información territorial integrado, con datos en tiempo real y analítica avanzada, que permite pasar de una planificación reactiva a una planificación predictiva y prospectiva (clima, demografía, movilidad, riesgos, participación). |
| Cpt | Def |
| --- | --- |
| Convenios y ARI como herramientas de simulación y co-diseño | Los Convenios de Programación y el Anteproyecto Regional de Inversiones (ARI) se negocian utilizando simulaciones del Gemelo Digital, convirtiéndose en instrumentos de co-diseño con el nivel central basados en evidencia. |
| Cpt | Def |
| --- | --- |
| Participación ciudadana aumentada por IA | La 'efectiva participación de la comunidad' se amplifica mediante plataformas de deliberación masiva apoyadas por IA, que sintetizan miles de aportes ciudadanos en argumentos estructurados que alimentan la planificación. |
### Funcion Financiar 4 0
#### Mision
Transformar al GORE en una banca de desarrollo regional inteligente que maximiza el impacto de cada peso público.
#### Dimensiones
| Cpt | Def |
| --- | --- |
| Financiamiento estratégico y catalítico | Cada decisión de financiamiento se evalúa por su contribución a objetivos estratégicos de la ERD, utilizando un motor de recomendación algorítmico, supervisado por equipos humanos, para priorizar proyectos de mayor impacto social, territorial y productivo. |
| Cpt | Ref | Def |
| --- | --- | --- |
| Portafolio diversificado de instrumentos | ['GN-GORE-IDEAL-GLOS-FONDO-FNDR', 'GN-GORE-IDEAL-GLOS-FONDO-FRPD', 'GN-GORE-IDEAL-GLOS-FONDO-ISAR'] | El GORE gestiona activamente un portafolio de fondos (FNDR, FRPD, ISAR y otros), combinándolos de forma estratégica para cerrar brechas sociales, habilitar infraestructura y sofisticar la estructura productiva. |
| Cpt | Def |
| --- | --- |
| Smart contracts y trazabilidad total | La ejecución financiera se automatiza parcialmente mediante contratos inteligentes asociados a hitos verificables (sensores, BIM, reportes digitales), de modo que los desembolsos se liberan solo cuando se comprueba el cumplimiento de metas. La trazabilidad de los fondos es pública y auditable, potencialmente reforzada por tecnologías tipo blockchain. |
| Cpt | Def |
| --- | --- |
| Ventanilla única digital con asistencia de IA | Los proponentes acceden a una plataforma única donde la IA guía la formulación de iniciativas, reduce errores y agiliza la obtención de la RS y demás visaciones, simplificando el ciclo burocrático. |
### Funcion Ejecutar 4 0
#### Mision
Consolidar al GORE como orquestador de la ejecución 4.0, garantizando calidad y oportunidad más que hacer directamente las obras.
#### Dimensiones
| Cpt | Def |
| --- | --- |
| PMO Regional como 'torre de control' | Se crea una Oficina de Gestión de Proyectos (PMO) regional que opera como torre de control predictiva, monitoreando convenios y obras con datos en tiempo real (drones, sensores, sistemas de gestión) para anticipar retrasos, sobrecostos y riesgos. |
| Programas habilitantes para región inteligente | La limitada ejecución directa del GORE se concentra en programas habilitantes que fortalecen capacidades digitales y de gestión de municipios y servicios (plataformas de IA como servicio, capacitación, estándares de datos), creando las bases para la infraestructura inteligente. |
| Unidades de desbloqueo aumentadas por IA | Se implementa una unidad especializada en 'desbloquear' procesos burocráticos críticos (permisología, compras públicas, coordinación multi-actor), apoyada por IA para mapear cuellos de botella y rediseñar procesos de forma sistémica. |
### Funcion Coordinar 4 0
#### Mision
Convertir al GORE en plataforma de gobernanza como servicio (GaaP), habilitando colaboración descentralizada entre actores públicos y privados.
#### Dimensiones
| Cpt | Def |
| --- | --- |
| Co-diseño vertical con el nivel central | La relación con el gobierno nacional evoluciona hacia un co-diseño de políticas públicas, donde los datos y simulaciones del Gemelo Digital regional informan ajustes en políticas nacionales y convenios de inversión conjunta. |
| Sincronización horizontal del aparato público regional | El Gobernador lidera un 'gabinete regional de desarrollo' de facto en el que la interoperabilidad de sistemas y una 'fuente única de verdad' de datos permiten coordinar agendas y presupuestos entre servicios, GORE y municipios. |
| Empoderamiento territorial de los municipios | El GORE provee a los municipios servicios de alto valor (plataforma de datos, herramientas de IA, asistencia técnica avanzada), nivelando capacidades y reduciendo brechas institucionales entre comunas. |
| Articulación ampliada vía APIs y datos abiertos | La coordinación con privados, academia y sociedad civil se realiza mediante APIs y catálogos de datos abiertos que permiten construir servicios y soluciones sobre la infraestructura de información regional, con el GORE como broker de conocimiento. |
### Funcion Normar 4 0
#### Mision
Usar la potestad reglamentaria como palanca habilitante y basada en evidencia para acelerar el desarrollo territorial.
#### Dimensiones
| Cpt | Def |
| --- | --- |
| Regulación basada en misiones y estándares | El GORE dicta reglamentos que dan fuerza ejecutiva a sus planes y establecen estándares de calidad, sostenibilidad e interoperabilidad de datos que toda iniciativa financiada por recursos regionales debe cumplir. |
| Proceso normativo dinámico y co-diseñado | Las normas se elaboran mediante procesos abiertos con consultas públicas tempranas y análisis de impacto regulatorio, y se actualizan en ciclos cortos a partir de evidencia sobre su efectividad, en diálogo permanente con la Contraloría. |
| Simplificación y sandboxes regulatorios | La prioridad normativa es simplificar y unificar procedimientos críticos y, en paralelo, crear sandboxes regulatorios que permitan experimentar con nuevas tecnologías (IA, movilidad autónoma, energías distribuidas) en entornos controlados, posicionando a la región como laboratorio vivo de innovación pública. |
