---
_manifest:
  urn: urn:salud:kb:resolucion-aprueba-instructivo-seguridad-ciberseguridad-p04
  provenance:
    created_by: Codex
    created_at: '2026-06-05'
    source: Resolucion Exenta RES_853, MINSAL, 23 JUL 2025
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- resolucion
- acto-administrativo
lang: es
extensions:
  kora:
    family: note
    shard_index: 4
    shard_count: 4
    shard_root_urn: urn:salud:kb:resolucion-aprueba-instructivo-seguridad-ciberseguridad
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Resolucion Exenta RES_853 - Aprueba Instructivo de Seguridad de la Informacion y Ciberseguridad para el Sector Salud ITS-NC-007-V.2.0, Abril 2025 - Parte 04

## Estandares Internacionales y Normativa Nacional de Referencia

| Estandar | Descripcion |
| --- | --- |
| ISO 27001:2022 | SGSI: establecer, implantar, mantener y mejorar |
| ISO 27002:2022 | Controles y mejores practicas para SGSI |
| NIST SP 800-53 | Catalogo de controles de privacidad y seguridad para sistemas de informacion |
| ISO/IEC 27799:2016 | Aplica ISO 27002 al ambito de la salud |
| ISO 31000 | Gestion de riesgos |
| ISO 22301 | Sistema de gestion de continuidad del negocio |
| HIPAA (EE.UU.) | Proteccion de datos y privacidad de informacion de salud |
| GDPR (UE 2016/679) | Proteccion de datos personales en la UE |
| EU Electronic Health Record Exchange Format | Intercambio de registros electronicos de salud con interoperabilidad y seguridad |
| European Data Governance Act (DGA) | Intercambio seguro de datos en la UE, incluidos datos de salud |
| NIST Cybersecurity Framework | Marco con 5 funciones: Identificar, Proteger, Detectar, Responder, Recuperar |
| CIS Controls v8 | Controles priorizados para defensa contra amenazas ciberneticas |
| ISO/IEC 27035 | Gestion de incidentes de seguridad de la informacion |
| Directiva NIS 2 (UE 2022/2555) | Requisitos de ciberseguridad para sectores criticos, incluyendo salud |
| ENISA | Buenas practicas, marcos y herramientas para ciberseguridad a nivel europeo |
| ISO/IEC 27033 | Seguridad de redes: diseno, gestion y proteccion de infraestructura de red |
| EU AI Act | Marco legal para regular desarrollo y uso de IA |
| Recomendaciones CPLT sobre Transparencia Algoritmica | RE N°372/2025 y Guia del CPLT para adopcion de transparencia algoritmica |

### Matriz de Riesgos de Seguridad de la Informacion (ejemplo)

| Amenaza | Vulnerabilidad | Impacto | Control Preventivo | Control Correctivo |
| --- | --- | --- | --- | --- |
| Ransomware | Sistemas desactualizados, falta de parches | Inaccesibilidad a datos clinicos criticos, interrupcion servicios | Actualizacion periodica, EDR/antivirus NG, segmentacion de redes criticas | IRP, restauracion desde respaldos verificados |
| Perdida/robo de dispositivos moviles | Falta de cifrado, ausencia de MDM | Fuga de datos sensibles de pacientes | Cifrado completo, MFA, MDM | Borrado remoto, investigacion de incidente, notificacion a autoridad |
| Acceso no autorizado a sistemas clinicos | Politicas de acceso debiles, cuentas compartidas | Modificacion/exfiltracion de datos de pacientes, dano reputacional | RBAC, MFA, contrasenas robustas, revisiones periodicas de permisos | Bloqueo inmediato de cuentas, analisis forense, remediacion de brechas |
| Phishing dirigido a personal | Falta de capacitacion, filtros de correo inadecuados | Compromiso de credenciales, infeccion de malware | Programas de concientizacion, filtros avanzados antiphishing/antispam | Restablecimiento inmediato de credenciales, analisis de contencion |
| Fallas en sistemas criticos (HIS, PACS, LIS) | Ausencia de alta disponibilidad y respaldo | Interrupcion de diagnosticos y tratamientos | Arquitecturas de alta disponibilidad, sistemas de respaldo en caliente, pruebas de restauracion | Activacion de procedimientos de contingencia, recuperacion desde entornos redundantes |

### Estructura de Politicas y Procedimientos (ejemplo)

| Categoria ISO/IEC 27001:2022 | Politica / Procedimiento |
| --- | --- |
| Politicas de Seguridad | Politica General de Seguridad de la Informacion. Procedimiento de revision/aprobacion de politicas. Procedimiento de difusion. |
| Organizacion de la Seguridad de la Informacion | Politica de Control de Accesos. Procedimiento de gestion de cuentas de usuario. Procedimiento de revision periodica de accesos. |
| Seguridad de los Recursos Humanos | Politica de Uso Aceptable de Recursos Institucionales. Procedimiento de monitoreo de uso de recursos. Procedimiento de sancion. |
| Gestion de Activos | Politica de Gestion de Activos. Procedimiento de inventario. Procedimiento de clasificacion y etiquetado. |
| Control de Acceso | Politica de Clasificacion y Manejo de la Informacion. Procedimiento de clasificacion. Procedimiento de destruccion segura. |
| Criptografia | Politica de Uso de Criptografia. Procedimiento de cifrado. Gestion de llaves. |
| Seguridad Fisica y del Entorno | Politica de Seguridad Fisica y Ambiental. Procedimiento de control fisico. Procedimiento de contingencias ambientales. |
| Seguridad en las Operaciones | Politica de Respaldo y Recuperacion. Procedimiento de respaldos. Procedimiento de prueba de restauracion. |
| Seguridad en las Comunicaciones | Politica de Correos Electronicos. Prevencion de phishing. Cifrado de correos. |
| Adquisicion, Desarrollo y Mantenimiento de Sistemas | Politica de Seguridad en el Ciclo de Vida de los Sistemas. Procedimiento de desarrollo seguro. Pruebas de aceptacion. |
| Relacion con Proveedores | Politica de Relacion con Proveedores. Evaluacion de proveedores. Acuerdos de confidencialidad. |
| Gestion de Incidentes | Politica de Gestion de Incidentes. IRP. Procedimiento de notificacion. Analisis post-incidente. |
| Continuidad del Negocio | Politica de Continuidad Operacional y DRP. Procedimiento de activacion del plan. Procedimiento de pruebas de continuidad. |
| Cumplimiento | Politica de Proteccion de Datos Personales. Procedimiento de gestion de consentimientos. Procedimiento de anonimizacion. |

### Indicadores Clave de Desempeno e Indicadores Clave de Riesgo (ejemplo)

| Area | Indicador | Objetivo | Frecuencia | Meta | Umbral de Alerta |
| --- | --- | --- | --- | --- | --- |
| Capa Fisica | % de areas criticas con cumplimiento de acceso fisico | Evaluar cumplimiento de politicas | Mensual | 100% | <95% |
| Seguridad Fisica | N° de eventos registrados (robos, vandalismo) | Detectar accesos no autorizados | Mensual | 0 | >0 |
| Red/Firewall Perimetral | Tasa de bloqueo de intentos de intrusion | Medir eficacia de barreras | Semanal | 99.9% | <99.5% |
| IDS/IPS | N° de alertas criticas del SOC | Supervisar anomalias y amenazas | Diario | 0 | >0 |
| Capa de Red | % de segmentos de red conformes a arquitectura | Evaluar cumplimiento de segmentacion | Mensual | 100% | <95% |
| Endpoints | % de endpoints con antivirus/EDR actualizado | Verificar cobertura | Semanal | >98% | <95% |
| Endpoints | N° de detecciones de malware en equipos de usuario | Monitorear infecciones | Semanal | <5 | >10 |
| Aplicacion | N° de vulnerabilidades graves sin corregir (>30 dias) | Identificar riesgos no mitigados | Mensual | 0 | >0 |
| Aplicacion | % de aplicaciones/APIs criticas con SAST/DAST aplicadas | Verificar cobertura de pruebas | Mensual | >90% | <80% |
| Datos | % de datos sensibles cifrados en reposo | Asegurar confidencialidad | Mensual | 100% | <95% |
| Datos | N° de incidentes de fuga de datos validados | Detectar brechas | Anual | 0 | >0 |
| Capacitacion | % de personal capacitado en ciberseguridad | Asegurar conocimiento basico | Anual | >95% | <90% |
| Normativo | N° de incumplimientos documentados | Detectar violaciones a politicas | Mensual | 0 | >0 |
| Identidades | % de cuentas inactivas deshabilitadas | Prevenir accesos indebidos | Mensual | >95% | <90% |
| Vulnerabilidades | Tasa de vulnerabilidades criticas sin mitigar (>30 dias) | Reducir exposicion prolongada | Mensual | <5% | >10% |
| Respuesta | Tiempo medio de respuesta ante incidentes | Mejorar eficiencia | Mensual | <8h | >12h |
| Deteccion (SOC/SIEM) | Tiempo medio desde ocurrencia hasta deteccion | Reducir latencia | Mensual | <1h | >4h |
| Cumplimiento Normativo | % de controles requeridos implementados | Asegurar alineacion con leyes y estandares | Anual | 100% | <95% |

Consideraciones: adaptar indicadores a cada institucion. Asegurar que sean cuantificables. Resultados deben permitir toma de decisiones informada. Revisar y ajustar periodicamente.
