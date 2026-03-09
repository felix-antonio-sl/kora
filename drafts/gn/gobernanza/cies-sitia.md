---
_manifest:
  urn: urn:gn:kb:cies-sitia
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/04_habilitadores/arquitectura/kb_gn_080_cies_sitia_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- seguridad-publica
- emergencias
- sitia
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/04_habilitadores/arquitectura/kb_gn_080_cies_sitia_koda.yml
    source_hashes:
      domains/gn/04_habilitadores/arquitectura/kb_gn_080_cies_sitia_koda.yml: 2e65308d557054d6aaac05e2bc0f238dc5cd5c29391108605cf5827bd3ed8796
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.93
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 7
    meat_count: 202
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gobernanza__cies-sitia.md.json
---

# Centro Integrado de Emergencia y Seguridad (CIES) - SITIA Ñuble
## Source
### Ctx Required
- staging/gn/kb_gn_080_cies_sitia.md
- CIES SITIA.md
- Ley N° 19.628 sobre Protección de la Vida Privada
### Ctx Optional
- knowledge/domains/gn/kb_gn_200_marco_legal_gores_koda.yml

## Glosario Conceptos Clave
### Proposito
Definir y referenciar conceptos estructurales del CIES y de la integración SITIA.
### Terminos
| ID | Ref | Cpt |
| --- | --- | --- |
| CIES-SITIA-GLOS-CIES | CIES-SITIA-DESC-CIES-NUBLE-01 | CIES-NUBLE |
| ID | Ref | Cpt |
| --- | --- | --- |
| CIES-SITIA-GLOS-SITIA-PATENTES | CIES-SITIA-CAP-SITIA-PATENTES-01 | SITIA-Patentes |
| ID | Ref | Cpt |
| --- | --- | --- |
| CIES-SITIA-GLOS-SITIA-EVIDENCIA | CIES-SITIA-CAP-SITIA-EVIDENCIA-01 | SITIA-Evidencia |
| ID | Ref | Cpt |
| --- | --- | --- |
| CIES-SITIA-GLOS-SITIA-ARMAS | CIES-SITIA-CAP-SITIA-ARMAS-01 | SITIA-Armas |
| ID | Ref | Cpt |
| --- | --- | --- |
| CIES-SITIA-GLOS-SITIA-UNIF-VID | CIES-SITIA-CAP-SITIA-UNIF-VID-01 | SITIA-Unificacion-Videos |
| ID | Ref | Cpt |
| --- | --- | --- |
| CIES-SITIA-GLOS-GOB-DATOS | CIES-SITIA-DESC-GOB-DATOS-01 | Gobernanza-Datos |
| ID | Cpt | Src |
| --- | --- | --- |
| CIES-SITIA-GLOS-SPD | Subsecretaría de Prevención del Delito (SPD) | ['KB-GN-200-MARCO-LEGAL-GORES-KODA / LMSP-SPD-01'] |
| ID | Ref | Cpt |
| --- | --- | --- |
| CIES-SITIA-GLOS-CADENA-CUSTODIA | CIES-SITIA-PROC-CADENA-CUST-01 | Cadena-Custodia-Digital |

## Descripcion General
### Conceptos
| ID | Cpt | Def | Nat | Purp | Ctx |
| --- | --- | --- | --- | --- | --- |
| CIES-SITIA-DESC-CIES-NUBLE-01 | CIES-NUBLE | Centro Integrado de Emergencia y Seguridad de Ñuble. | Iniciativa estratégica del Gobierno Regional. | Fortalecer la seguridad pública y la gestión integral de riesgos. | Aplicado a las 21 comunas de la región de Ñuble. |
| ID | Cpt | Nat | Mech |
| --- | --- | --- | --- |
| CIES-SITIA-DESC-FUNC-PRINC-01 | Funcionalidad-Principal | Núcleo para vigilancia, coordinación y respuesta ante emergencias y delitos. | Utiliza tecnología de punta y colaboración interinstitucional. |
| ID | Cpt | Def | Resp | Ref | Purp | Mech |
| --- | --- | --- | --- | --- | --- | --- |
| CIES-SITIA-DESC-ALIANZA-01 | Alianza-Estrategica | Colaboración con el Sistema Integrado de Teleprotección con Inteligencia Artificial (SITIA). | Subsecretaría de Prevención del Delito. | CIES-SITIA-GLOS-SPD | Potenciar capacidades del CIES. | Integrar capacidades locales del CIES con plataformas de analítica avanzada a nivel nacional. |
| ID | Cpt | Obj |
| --- | --- | --- |
| CIES-SITIA-DESC-CAP-POT-01 | Capacidades-Potenciadas | ['Reforzar la detección de prófugos.', 'Reforzar la búsqueda de personas desaparecidas.', 'Reforzar la localización de vehículos con encargo de búsqueda.'] |
| ID | Cpt | Req | Fnd |
| --- | --- | --- | --- |
| CIES-SITIA-DESC-GOB-DATOS-01 | Gobernanza-Datos | Gobernanza de datos transparente. | Pleno respeto de la Ley N° 19.628. |

## Objetivos
### Objetivos
| Obj |
| --- |
| Mejorar capacidad de prevención y respuesta ante emergencias y delitos en la región. |
| Obj |
| --- |
| Fortalecer coordinación interinstitucional para gestión efectiva de seguridad pública. |
| Obj | Purp |
| --- | --- |
| Potenciar análisis de video con herramientas de IA de nivel nacional. | ['Anticipar riesgos.', 'Optimizar gestión de emergencias.'] |
| Obj | Mech |
| --- | --- |
| Facilitar intercambio de evidencia digital con Ministerio Público y policías. | A través de plataformas unificadas. |
| Obj | Mech |
| --- | --- |
| Contribuir al desarrollo social, económico y territorial de Ñuble. | Mediante la reducción de riesgos y amenazas. |

## Componentes Clave
### Infraestructura Tecnologica y Fisica
#### Sala Monitoreo Central
#### Contexto
Ubicada en GORE Ñuble.
#### Caracteristicas
| Cpt | Def | Fnd | Ctx | Purp |
| --- | --- | --- | --- | --- |
| Diseño-Ergonomia | Sala de 77,03 m². | Diseñada según norma ISO 11064. | Incluye zonas operativas, técnicas, de supervisión y de descanso. | Garantizar rendimiento óptimo y bienestar del personal. |
| Cpt | Def | Ctx | Mech | Purp |
| --- | --- | --- | --- | --- |
| Visualizacion-Centralizada | Video Wall de 6x2 metros. | Pantallas LED modulares 4K. | Capaz de mostrar hasta 16 vistas simultáneas. | Permitir monitoreo global y detallado de puntos críticos. |
| Cpt | Def | Ctx | Purp |
| --- | --- | --- | --- |
| Estaciones-Trabajo | 7 estaciones de trabajo (6 operadores, 1 supervisor). | ['3 estaciones adicionales para Unidad Operativa de Control de Tránsito (UOCT).', 'Cada estación equipada con monitor Full HD 32", teclado ergonómico, joystick.'] | Control preciso de cámaras PTZ. |
| Cpt | Def | Ctx | Purp |
| --- | --- | --- | --- |
| Centro-Datos | Infraestructura robusta. | ['Racks APC NetShelter SX.', 'Servidores redundantes Dell PowerEdge R740.', 'Sistemas de Alimentación Ininterrumpida (UPS).'] | Garantizar operación continua 24/7. |
#### Sistema Integrado Camaras y Red
#### Elementos
| Cpt | Def | Ctx |
| --- | --- | --- |
| Cobertura-Regional | 209 puntos de vigilancia en 21 comunas. | 140 cámaras PTZ 4K y 69 cámaras multisensor/panorámicas. |
| Cpt | Def | Ctx |
| --- | --- | --- |
| Conectividad | Red híbrida de alta velocidad con 316 nodos. | 80% fibra óptica (100Mbps) y 20% enlaces inalámbricos (50Mbps). |
| Cpt | Def | Res |
| --- | --- | --- |
| Arquitectura-Federacion | Modelo federado para gestión centralizada con autonomía local. | Garantiza resiliencia, robustez y escalabilidad. |
| Cpt | Def | Mech | Ctx |
| --- | --- | --- | --- |
| Software-Gestion-VMS | Plataforma HikCentral. | Permite gestión centralizada, acceso a video grabado, notificaciones. | Compatibilidad con estándar ONVIF. |
| Cpt | Def | Mech |
| --- | --- | --- |
| Almacenamiento-Seguro | Capacidad para 60 días de grabaciones a máxima resolución. | Redundancia (RAID, ANR) y cifrado para proteger integridad de datos. |
#### Capacidades Analitica Avanzada CIES SITIA
#### Fundamento
El sistema CIES cuenta con analítica de video (VCA) para funciones base (detección de movimiento, seguimiento, conteo, intrusión).
#### Cpt
La capacidad es potenciada por la integración con plataformas especializadas de SITIA.
#### Capacidades
| ID | Cpt | Purp | Mech | Res |
| --- | --- | --- | --- | --- |
| CIES-SITIA-CAP-SITIA-PATENTES-01 | SITIA-Patentes | Complementar la lectura de placas local con una red integrada nacional (pórticos públicos y privados). | Datos contrastados en tiempo real con registro oficial de vehículos con encargo de búsqueda. | Genera dashboards dinámicos sobre zonas críticas de robo y rutas probables. |
| ID | Cpt | Def | Fnd | Purp | Dest | Res |
| --- | --- | --- | --- | --- | --- | --- |
| CIES-SITIA-CAP-SITIA-EVIDENCIA-01 | SITIA-Evidencia | Plataforma digital para la gestión de evidencias. | Basada en Genetec Clearance. | Facilitar solicitud, almacenamiento y compartición segura de pruebas audiovisuales. | ['Municipios.', 'Policías.', 'Fiscalía.'] | Asegura cadena de custodia digital y reduce tiempos de investigación. |
| ID | Cpt | Mech | Purp | Res |
| --- | --- | --- | --- | --- |
| CIES-SITIA-CAP-SITIA-ARMAS-01 | SITIA-Armas | Implementa modelos de IA (basados en YOLOv11) en la red de cámaras. | Generar alertas automáticas en tiempo real al detectar un arma de fuego en la vía pública. | Apoya labores de fiscalización y control. |
| ID | Cpt | Purp | Mech | Res |
| --- | --- | --- | --- | --- |
| CIES-SITIA-CAP-SITIA-UNIF-VID-01 | SITIA-Unificacion-Videos | Centralizar las señales de las cámaras del CIES en una interfaz única a nivel nacional. | Permite acceso a Carabineros de Chile. | Refuerza la coordinación y la capacidad de respuesta ante emergencias. |
### Personal y Estructura Operativa
#### Componentes
| Cpt | Def | Ctx |
| --- | --- | --- |
| Equipo-Humano | 3 operadores y 1 supervisor por turno en la sala. | Se integra personal de la UOCT. |
| Cpt | Def | Ctx | Obj |
| --- | --- | --- | --- |
| Turnos-Operacion | Cobertura inicial de 16 horas diarias (08:00 a 00:00). | Dos turnos rotativos. | Proyección de extenderse a 24/7. |
| Cpt | Fnd | Subroles |
| --- | --- | --- |
| Roles-Capacitacion | Personal capacitado conforme al Manual de Operaciones. | [{'Cpt': 'Operadores', 'Resp': 'Detección temprana, clasificación de incidentes, seguimiento en tiempo real.'}, {'Cpt': 'Supervisores', 'Resp': 'Gestión de incidentes críticos, articulación de recursos, enlace interinstitucional.'}, {'Cpt': 'Soporte-Tecnico', 'Resp': 'Mantenimiento preventivo y correctivo de la plataforma.'}] |
| Cpt | Def | Dest |
| --- | --- | --- |
| Enlaces-Interinstitucionales | Personal que actúa como facilitador de comunicación directa. | ['Carabineros.', 'PDI.', 'Bomberos.', 'SAMU.', '21 municipios.'] |
### Procesos y Protocolos Marco Operativo Legal
#### Fundamento
Todas las actuaciones se rigen por un estricto Manual de Operaciones.
#### Requisitos
Garantizar el cumplimiento de la Ley N° 19.628 sobre Protección de la Vida Privada.
#### Procesos
| Cpt | Def | Ctx |
| --- | --- | --- |
| Protocolos-Vigilancia-Respuesta | Procedimientos estandarizados para monitoreo, detección, clasificación y escalamiento de incidentes. | Clasificación por prioridad (alta, media, baja). |
| ID | Cpt | Def | Proc | Req |
| --- | --- | --- | --- | --- |
| CIES-SITIA-PROC-CADENA-CUST-01 | Cadena-Custodia-Digital | Las grabaciones son consideradas evidencia legal. | Su entrega se realiza únicamente bajo requerimiento formal (orden judicial o del Ministerio Público). | Utilizar medios seguros y controlados para garantizar validez. |
| Cpt | Proc | Act | Mech | Cond |
| --- | --- | --- | --- | --- |
| Gestion-Privacidad | Grabaciones se almacenan por un máximo de 30 días. | Eliminación segura e irreversible posterior al plazo. | Ciudadanos pueden solicitar cautela de una grabación por hasta 6 meses. | Si son víctimas o testigos de un delito. |
| Cpt | Def | Purp | Res |
| --- | --- | --- | --- |
| Plan-Contingencia | Análisis de riesgos y plan de acción. | Enfrentar fallos técnicos, cortes de energía o desastres naturales. | Asegurar la continuidad operativa. |
| Cpt | Def | Ctx |
| --- | --- | --- |
| Coordinacion-Interinstitucional | Canales de comunicación directos y protocolos de acción conjunta. | Con todas las entidades de seguridad y emergencia. |

## Sostenibilidad y Modelo Gestion
### Componentes
| Cpt | Mech | Purp |
| --- | --- | --- |
| Financiamiento-Operativo | Continuidad garantizada a través de presupuesto anual. | Cubrir gastos recurrentes (RR.HH., mantenimiento, servicios). |
| Cpt | Def | Ctx |
| --- | --- | --- |
| Mantenimiento-Garantia | Garantía técnica de 22 meses. | Incluye mantenimiento preventivo trimestral. |
| Cpt | Mech | Resp | Ref | Purp |
| --- | --- | --- | --- | --- |
| Convenio-Colaboracion | La relación con SITIA se formaliza a través de un convenio marco de colaboración. | Subsecretaría de Prevención del Delito y Gobierno Regional. | CIES-SITIA-GLOS-SPD | Establecer los ejes de cooperación en integración tecnológica, intercambio de datos y capacitación. |

## Beneficios Para Region
### Resultados
- Mayor seguridad y protección (disuasión y respuesta rápida).
- Mejora en los tiempos de respuesta ante emergencias, minimizando daños.
- Fortalecimiento de la coordinación interinstitucional, optimizando uso de recursos.
- Generación de evidencia de alta calidad y estandarizada para apoyar procesos judiciales.
- Acceso a una red de inteligencia nacional, mejorando capacidad de análisis y prevención.
- Creación de un entorno más seguro para la inversión y la vida en comunidad en Ñuble.
