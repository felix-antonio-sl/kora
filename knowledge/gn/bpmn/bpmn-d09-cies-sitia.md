---
_manifest:
  urn: urn:gn:kb:bpmn-d09-cies-sitia
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: "GORE Ñuble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- seguridad-publica
- cies
- sitia
- bpmn
- gn
lang: es
---

# BPMN D09: Gestión Operativa CIES/SITIA (Seguridad Pública)

## Metadatos del Dominio

| Atributo | Valor |
| :--- | :--- |
| ID | DOM-CIES |
| Criticidad | Alta |
| Dueño | Supervisor CIES |
| Procesos | 3 (Monitoreo, Coordinación, Evidencias) |
| Subprocesos | ~8 |

## Contexto Operativo

| Aspecto | Detalle |
| :--- | :--- |
| Cobertura | 16 horas (08:00–00:00); proyección a 24/7 |
| Ubicación | Sala de monitoreo GORE Ñuble |
| Coordinación | Policías, emergencias, 21 municipios |
| Marco legal | Ley 21.427, Ley 20.965, Ley 20.502 |

## Capacidades SITIA

| Módulo | Función |
| :--- | :--- |
| SITIA-Patentes | Lectura automática de placas, contraste en tiempo real con encargos de búsqueda, alerta a CIES y policías |
| SITIA-Armas | Detección IA (YOLOv11) sobre cámaras CIES; alerta automática verificada por operador |
| SITIA-Evidencia | Gestión evidencias digitales (Genetec Clearance) |
| SITIA-Unificación | Integración nacional con plataforma SPD |

## P1: Monitoreo, Detección y Escalamiento

**Sistema:** HikCentral VMS.

### Flujo

1. Operador CIES monitorea cámaras (continuo)
2. SITIA detecta automáticamente: patentes alertadas, armas visibles
3. Identificar evento/incidente → clasificar prioridad
4. Según prioridad:
   - Alta: alarma inmediata → Supervisor CIES evalúa → activar protocolo → coordinar con Carabineros/PDI/Bomberos/SAMU
   - Media: registro y seguimiento → Supervisor evalúa
   - Baja: solo registro

### Clasificación de Incidentes

| Prioridad | Tipo | Acción |
| :--- | :--- | :--- |
| Alta | Delito en curso, emergencia vital | Activación inmediata |
| Media | Sospecha, situación anómala | Seguimiento y evaluación |
| Baja | Evento menor | Solo documentar |

## P2: Coordinación Interinstitucional

**Entidades:** Carabineros, PDI, Bomberos, SAMU, Municipios.

### Flujo

1. Incidente clasificado → Enlace CIES activa canal
2. Según tipo de emergencia:
   - Seguridad → Carabineros (133)
   - Investigación → PDI (134)
   - Incendio → Bomberos (132)
   - Salud → SAMU (131)
3. Confirmar recepción y unidades → seguimiento en tiempo real
4. Registro de respuesta → cierre de incidente

### Protocolos de Comunicación

| Canal | Uso |
| :--- | :--- |
| Radio VHF | Comunicación directa con policías |
| Líneas directas | Centrales de emergencia |
| WhatsApp institucional | Coordinación municipal |
| Plataforma SITIA | Integración nacional |

## P3: Gestión de Evidencias Digitales

**Plataforma:** SITIA-Evidencia (Genetec Clearance).

### Flujo

**Solicitud:**
1. Fiscalía/Tribunal solicita evidencia → recepción oficio en GORE
2. Verificar: orden judicial o requerimiento MP

**Extracción:**
3. Supervisor CIES autoriza
4. Localizar grabación en HikCentral → exportar clip seguro
5. Subir a SITIA-Evidencia

**Entrega:**
6. Generar cadena de custodia
7. Entrega por medio controlado → acta de entrega → registro para trazabilidad

### Cadena de Custodia Digital

| Elemento | Verificación |
| :--- | :--- |
| Hash de archivo | Integridad |
| Metadatos | Fecha/hora/cámara |
| Log de accesos | Quién manipuló |
| Firma digital | Autenticidad |

## Gestión de Privacidad y Retención

### Política de Retención

| Aspecto | Regla |
| :--- | :--- |
| Retención normal | 30 días |
| Eliminación | Segura e irreversible |
| Cautela ciudadana | Hasta 6 meses (víctima/testigo) |

### Flujo de Retención

1. Grabación generada → almacenar 30 días
2. ¿Solicitud de cautela?
   - Sí → extender retención hasta 6 meses → revisar al vencimiento → eliminar
   - No → eliminar automáticamente al vencimiento

Ley 19.628: tratamiento de datos personales debe respetar licitud, finalidad y proporcionalidad.

## Sostenibilidad Operativa

### Modelo de Financiamiento

| Componente | Fuente |
| :--- | :--- |
| Personal CIES | Presupuesto anual GORE |
| Mantención equipos | Garantía 22 meses + presupuesto |
| Servicios SITIA | Convenio marco con SPD |

### Mantención (Trimestral)

Revisión equipos → actualizaciones software → reporte de estado.

## Sistemas Involucrados

| Sistema | Función |
| :--- | :--- |
| SYS-HIKCENTRAL | VMS gestión cámaras |
| SYS-SITIA | Plataforma nacional |
| SYS-SITIA-EVIDENCIA | Gestión evidencias |
| SYS-SITIA-PATENTES | Lectura placas |
| SYS-SITIA-ARMAS | Detección IA |

## Normativa Aplicable

| Norma | Alcance |
| :--- | :--- |
| Ley 21.427 | Sistema Nacional de Seguridad Pública |
| Ley 20.965 | Cámaras de vigilancia |
| Ley 20.502 | ONEMI/funcionamiento emergencias |
| Ley 19.628 | Protección de vida privada |
| Ley 21.719 | Datos personales |

## Referencias Cruzadas

| Dominio | Vínculo |
| :--- | :--- |
| D01 Actos Administrativos | Convenios con entidades coordinadas |
