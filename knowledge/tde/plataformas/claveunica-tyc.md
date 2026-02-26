---
_manifest:
  urn: "urn:tde:kb:claveunica-tyc"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/terminos-y-condiciones/terminos-condiciones-claveunica"
version: 1.0.0
status: published
tags: [tde, plataforma, claveunica, términos-y-condiciones, normativa, identidad-digital, seguridad]
lang: es
---

# Términos y condiciones de ClaveÚnica

Aprobados por Resolución Exenta N° 733/2025 de la Subsecretaría de Hacienda.

## 1. Alcance y obligatoriedad

- Regulan uso del Sistema de ClaveÚnica por Entidades Usuarias.
- Obligatorios para todas las Entidades Usuarias sin necesidad de aprobación/aceptación (art. 2° transitorio, Ley N° 21.658).

## 2. Glosario

| Término | Definición |
|---------|-----------|
| Autenticación | Proceso electrónico que valida datos de identificación para acceso a plataforma electrónica |
| ClaveÚnica | Mecanismo oficial de autenticación operado por SGD. Uso exclusivo personas naturales (por sí o en representación). Basado en OpenID Connect. Factor primario: contraseña vinculada a RUN |
| Contraseña | Combinación de caracteres/números/símbolos confidencial para autenticarse vía ClaveÚnica |
| Entidad Usuaria | Entidad integrada a ClaveÚnica que lo usa como mecanismo de autenticación en sus plataformas |
| Integración | Proceso de conexión y habilitación al Sistema de ClaveÚnica |
| Mecanismo oficial de autenticación | ClaveÚnica, cédula de identidad digital y otros mecanismos validados por SGD que cumplen Norma Técnica de Autenticación |
| Ministerio | Ministerio de Hacienda |
| Subsecretaría | Subsecretaría de Hacienda |
| SGD | Secretaría de Gobierno Digital |
| Norma Técnica de Autenticación | DS N° 9, 17/08/2023, MinSegPres |
| Reglamento | DS N° 4, 2020, MinSegPres (Ley N° 21.180, TDE) |
| RUN | Rol Único Nacional (SRCeI) |
| Servicios SaaS | Software de entidades externas suministrado vía internet, accesible desde navegador web |
| Usuario/a | Persona natural con cuenta activa de ClaveÚnica que accede a servicios digitales integrados |

## 3. Criterios para ser Entidad Usuaria

Criterios mínimos evaluados por SGD:

1. Finalidad de promover bien común atendiendo necesidades públicas
2. Disposición legal/administrativa que permita u obligue uso de ClaveÚnica con casos de uso específicos y medidas de seguridad
3. Capacidad para garantizar seguridad, confiabilidad y responsabilidad + cumplimiento de estándares técnicos
4. Existencia de institución pública con competencias de supervisión/fiscalización del uso de ClaveÚnica

## 4. Habilitación e integración

- SGD proporciona lineamientos técnicos para integración, habilitación y operación
- Solicitud: trámite "Solicitud de Credenciales de Integración a ClaveÚnica" en [CeroFilas](https://gobdigital.cerofilas.gob.cl/)
- SGD acepta solo si se cumplen requisitos
- SGD PUEDE revocar autorización en cualquier etapa (incluso post-producción) si no hay habilitantes legales/administrativos. Sin responsabilidad por daños de la revocación
- Post-aceptación: ejecutar proceso según Guía Técnica Manual de Integración en [wikiguias.digital.gob.cl](https://wikiguias.digital.gob.cl/)
- Entidad es considerada "Entidad Usuaria" solo tras certificación + credenciales en producción
- Asistencia técnica: [Mesa de Servicios SGD](https://gobdigitalcl.freshdesk.com/support/tickets/new)

### Integración vía SaaS

Mismo proceso de habilitación. Verificación especial:
- Solicitud por persona de dotación del órgano público responsable
- URL institucional asociada al órgano

## 5. Contrapartes técnicas y comunicaciones

- Entidad Usuaria DEBE designar contraparte administrativa + contraparte técnica
- Informar a SGD según Manual de Integración
- Comunicaciones formales: vía [Mesa de Servicios SGD](https://gobdigitalcl.freshdesk.com/support/tickets/new)

## 6. Obligaciones de Entidades Usuarias

### 6.1 Cumplimiento normativo

1. Usar ClaveÚnica conforme a normativa y habilitantes legales/administrativos
2. Cumplir: Ley N° 19.880 (procedimientos administrativos), Ley N° 19.628 (protección vida privada), Ley N° 21.663 (ciberseguridad) + normas relacionadas
3. Cumplir normas técnicas mandatadas por art. 57 del Reglamento (especialmente NT Autenticación) y art. 47 DS N° 181/2020 MinEconomía (Ley N° 19.799, firma electrónica). Entidades no-AE: cumplir salvo incompatibilidad con naturaleza del negocio
4. Cumplir lineamientos, estándares, directrices y guías técnicas de SGD (Ley N° 21.658 y su reglamento)

### 6.2 Difusión y comunicación

1. Comunicar y difundir TyC y obligaciones derivadas en la organización
2. Si integración vía SaaS: difundir al proveedor. Incorporar en bases de licitación y contrato la obligación de cumplir TyC de ClaveÚnica + mecanismo de comunicación/difusión

### 6.3 Garantía de correcta integración

Conservar, actualizar, reparar y mantener infraestructura y sistemas operativos en condiciones óptimas para correcta integración y funcionamiento de ClaveÚnica.

### 6.4 Medidas de seguridad

1. **2FA**: habilitar segundo factor cuando trámite/servicio requiera nivel de seguridad superior al factor primario. SGD PUEDE exigir 2FA por razones de seguridad → plan de trabajo conjunto
2. Factores/mecanismos adicionales NO PUEDEN basarse en información accesible mediante ClaveÚnica o de fuentes de acceso público
3. **Incidentes**: aviso inmediato a SGD ante sospecha o identificación de incidentes (accesos no autorizados a contraseñas/credenciales, etc.)
4. **Auditorías**: cooperar con SGD proporcionando información para auditorías e identificación de brechas
5. **Actualizaciones**: realizar modificaciones en protocolos/estándares solicitadas por SGD por motivos de seguridad o continuidad

### 6.5 Prohibiciones

1. Solicitar, almacenar o registrar credenciales/contraseñas de usuarios de ClaveÚnica
2. Crear/habilitar/recomendar mecanismos de automatización de acceso
3. Acceder o intentar acceder sin autorización expresa de SGD
4. Manipular o intentar manipular el sistema para acceso no autorizado
5. Distribuir, sublicenciar o transferir ClaveÚnica a terceros
6. Compartir credenciales de integración con terceros no autorizados
7. Usar para fines maliciosos (extracción/divulgación datos sin autorización, actividades ilegales, dañar seguridad)
8. Ingeniería inversa, descompilar o desensamblar software/componentes

## 7. Disponibilidad y suspensión del servicio

### 7.1 Suspensiones programadas

- Mantenimiento preventivo o mejoramiento de infraestructura
- Aviso previo ≥ **48 horas** vía web ClaveÚnica con detalle de horas inicio/término

### 7.2 Suspensiones no programadas

| Causa | Descripción |
|-------|-------------|
| Emergencias | Fallas técnicas, cortes de energía, fuerza mayor |
| Acción de terceros | Fallas por ataques informáticos u otros |

- Comunicación vía web ClaveÚnica y/o contraparte técnica
- SGD NO puede asegurar porcentaje de disponibilidad. Realizará esfuerzos razonables para evitar contingencias

### 7.3 Otros ajustes

Cambios que afecten funcionamiento (ej: actualización de parámetros de seguridad del certificado) → comunicados a Entidad Usuaria.

## 8. Incumplimiento y suspensión

- SGD PUEDE suspender servicio sin previo aviso ante incumplimiento de TyC por Entidad Usuaria o proveedor SaaS
- Notificación por email a contraparte técnica con razones y causal
- Suspensión NO exime de demás obligaciones
- SGD determina condiciones de reanudación

## 9. Costos

- Todos los costos de integración, implementación y uso de ClaveÚnica son de cargo exclusivo de la Entidad Usuaria
- Incluye: administración, actualización, reparación, infraestructura, hardware/software, personal, seguridad, ciberseguridad, protección de vida privada

## 10. Uso de marca

- ClaveÚnica = marca registrada (N° 1062117, INAPI) a nombre de la Secretaría y Administración General del Ministerio de Hacienda
- Uso no autorizado infringe Ley N° 19.039 (Propiedad Industrial), art. 19 bis letra d)
- PROHIBIDO: reproducción, modificación o distribución no autorizada del software/componentes y uso no autorizado de marca/logos de [claveunica.gob.cl](https://claveunica.gob.cl)

## 11. Responsabilidad por daños

- Ministerio liberado de responsabilidad por daños directos/indirectos por mal uso del sistema o contravención de TyC
- No responsable por daños de suspensión por incumplimiento

## 12. Modificación de TyC

- Subsecretaría PUEDE modificar TyC sin expresión de causa en cualquier momento
- Aviso previo vía [claveunica.gob.cl](https://claveunica.gob.cl) (salvo fuerza mayor)
- Vigencia: **10 días hábiles** desde publicación en Diario Oficial

## 13. Adecuación de estándares

- Entidades integradas previamente: plazo de **60 días corridos** desde vigencia de TyC para adecuarse
- Plazo extensible por SGD ante dificultades/impedimentos operativos justificados → solicitar a [claveunica@digital.gob.cl](mailto:claveunica@digital.gob.cl) dentro del mismo plazo
- Incumplimiento → SGD facultada para suspender servicio
