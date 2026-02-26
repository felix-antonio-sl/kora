---
_manifest:
  urn: urn:gn:kb:bpmn-d08-rendiciones
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: "GORE Ñuble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- bpmn
- rendiciones
- finanzas
- gn
lang: es
---

# BPMN D08: Gestión de Rendiciones de Cuentas

## Metadatos del Dominio

| Atributo | Valor |
| :--- | :--- |
| ID | DOM-RENDICIONES |
| Criticidad | Crítica |
| Dueño | UCR/DAF |
| Procesos | 3 (Tradicional, SISREC, Tipología) |
| Subprocesos | ~10 |

## Mapa General

P3 Tipología de Fondos determina la ruta: P1 Rendición Tradicional o P2 Rendición vía SISREC. Ambos procesos se apoyan en marco normativo, expediente/documentación y control/transparencia.

## P1: Rendición Tradicional (sin SISREC)

**SLA:** 18 días hábiles GORE + 15 días EE.
**Estado:** En transición a SISREC.

### Plazos por Etapa

| Etapa | Plazo | Responsable |
| :--- | :--- | :--- |
| Presentación por EE | 15 días hábiles mes siguiente | Entidad Ejecutora |
| Recepción y registro | 2 días hábiles | Oficina de Partes |
| Asignación a revisor | 2 días hábiles | UCR/DAF |
| Revisión técnico-financiera | 7 días hábiles | RTF |
| Control final | 4 días hábiles | UCR/DAF |
| Contabilización | 2 días hábiles | UCR/DAF |
| Archivo | 1 día hábil | UCR/DAF |

### Flujo

1. Entidad Ejecutora prepara rendición (papel/digital)
2. Oficina de Partes recepciona (2 días)
3. UCR registra y asigna (2 días)
4. RTF revisión técnico-financiera (7 días) → ¿OK?
   - Sí → Certificado de aprobación
   - No → observar → devuelve a EE para corrección
5. UCR control final (4 días)
6. Contabilizar SIGFE (2 días)
7. Archivar (1 día)

## P2: Rendición vía SISREC

**Plataforma:** SISREC CGR.
**Obligatorio:** Sí (Resolución 1858/2023 CGR).

### Tipos de Informe

| Tipo | Uso |
| :--- | :--- |
| Mensual | Rendición regular con transacciones |
| Regularización | Corrección de observaciones |
| Sin Movimiento | Período sin gastos |

### Flujo Entidad Otorgante (GORE/RTF)

1. Crear Programa en SISREC
2. Registrar y enviar transferencia
3. Recibir informe de rendición → revisar transacciones → ¿Correcto?
   - Sí → aprobar
   - No → observar
4. Enviar a Jefe DAF → ¿Conforme?
   - Sí → firmar con FEA
   - No → devolver (1 día)
5. UCR descargar informe de aprobación → contabilizar SIGFE (2 días) → archivar (2 días)

### Flujo Entidad Ejecutora

1. Recibir transferencia en SISREC → aceptar transferencia
2. Crear informe de rendición (mensual/regularización/sin movimiento)
3. Ingresar transacciones → adjuntar respaldos digitalizados
4. Enviar a Ministro de Fe → ¿Auténtico?
   - No → devolver para corrección
   - Sí → certificar
5. Encargado ejecutor revisa → ¿Conforme?
   - Sí → firmar FEA y enviar a GORE
   - No → devolver para corrección

## P3: Rendición por Tipología de Fondos

### Requisitos por Tipología

| Fondo | Vía | Requisitos especiales |
| :--- | :--- | :--- |
| FNDR Subt. 31 | BIP + SIGFE | Actualizar avance físico-financiero |
| FNDR Subt. 33 | SISREC | RTF revisa coherencia técnica |
| FRIL | SISREC | Considerar informe ITO, SNI |
| FRPD | SISREC | Seguimiento metas por división |
| 8% FNDR | SISREC | Medios verificación, gastos prohibidos |
| Programas Subt. 24 | SISREC | Tope 5% gastos administración |
| Circular 33 | BIP + SISREC | RATE conservación |

## Procedimientos Contables SIGFE

### F07: Transferencias a Sector Privado

| Fase | Acción contable |
| :--- | :--- |
| 1. Entrega fondos | Devengo obligación y pago |
| 2. Aprobación rendición | Reconocimiento del gasto |
| 3. Reintegro | Devengo cobro y recepción |

### F08: Transferencias a Sector Público

Mismas fases que F07. Para servicios públicos no consolidables: el devengo del gasto ocurre al aprobar la rendición.

## Marco Normativo

| Norma | Alcance |
| :--- | :--- |
| Resolución 30/2015 CGR | Procedimiento general |
| Resolución 1858/2023 CGR | Uso obligatorio SISREC |
| Ley 19.862 | Registro Colaboradores Estado |
| Ley 21.719 | Protección Datos Personales |

### Artículos Clave Resolución 30/2015

| Artículo | Contenido |
| :--- | :--- |
| Art. 2 | Constitución expediente |
| Art. 4-5 | Documentación auténtica |
| Art. 10 | Expediente de rendición |
| Art. 13 | Gastos post-tramitación |
| Art. 18 | Prohíbe nuevos fondos si hay rendiciones pendientes |
| Art. 31 | Obligación de restituir fondos |

## Expediente de Rendición

### Componentes

| Componente | Descripción |
| :--- | :--- |
| Informe de Rendición | Documento formal del ejecutor |
| Comprobantes de Ingreso | Recepción de fondos |
| Comprobantes de Egreso | Facturas, boletas, contratos |
| Comprobantes de Traspaso | Operaciones sin efectivo |
| Registro Ley 19.862 | Si aplica (privados) |
| Medios de Verificación | Fotos, listas, informes |

### Documentación Auténtica

| Soporte | Requisito |
| :--- | :--- |
| Papel | Original o copia autentificada |
| Electrónico | Firma electrónica según Ley 19.799 |
| Digitalizado | Autentificado por Ministro de Fe |

## Responsabilidades y Sanciones

| Tipo | Consecuencia |
| :--- | :--- |
| Administrativa | Sumario → Censura/Multa/Destitución |
| Civil | Juicio de Cuentas CGR → Restituir |
| Penal | Malversación/Fraude → Prisión |

Consecuencias directas: obligación de restituir fondos + suspensión de nuevas transferencias.

## Control y Transparencia

### Control Interno

| Mecanismo | Responsable |
| :--- | :--- |
| Auditorías selectivas | Unidad de Control |
| Listas de chequeo | UCR/RTF |
| Seguimiento físico-financiero | RTF |

### Fiscalización Externa

| Organismo | Función |
| :--- | :--- |
| CGR | Juzgamiento cuentas, auditorías, SISREC |
| DIPRES | Monitoreo ejecución vía SIGFE |

### Transparencia

| Obligación | Detalle |
| :--- | :--- |
| Glosa 08 | Info corporaciones/fundaciones |
| Glosa 16 | Cartera proyectos, acuerdos CORE |

## Sistemas Involucrados

| Sistema | Función |
| :--- | :--- |
| SYS-SISREC | Rendición electrónica CGR |
| SYS-SIGFE | Contabilización |
| SYS-BIP-SNI | Avance físico-financiero |
| SYS-FIRMAGOB | Firma Electrónica Avanzada |

## Referencias Cruzadas

| Dominio | Vínculo |
| :--- | :--- |
| D03 Gestión IPR | Cierre financiero Fase 7 |
| D02 Ciclo Presupuestario | Contabilización, devengo |
