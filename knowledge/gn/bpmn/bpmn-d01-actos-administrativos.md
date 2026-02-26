---
_manifest:
  urn: urn:gn:kb:bpmn-d01-actos-administrativos
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
- actos-administrativos
- ley-19880
- ley-21180
- gn
lang: es
---

# BPMN D01: Tramitación de Actos Administrativos

## Metadatos del Dominio

| Atributo | Valor |
| :--- | :--- |
| ID | DOM-ACTOS-ADMIN |
| Criticidad | Alta |
| Dueño | Unidad Jurídica |
| Procesos | 2 (Resoluciones Exentas, Convenios y Transferencias) |
| Subprocesos | ~14 fases |
| SLA | 15 días hábiles |

## Mapa General

Dos procesos principales con elementos transversales compartidos:

| Proceso | Elementos transversales |
| :--- | :--- |
| P1: Resoluciones Exentas | Expediente Electrónico, Firma Electrónica Avanzada |
| P2: Convenios y Transferencias | Expediente Electrónico, FEA, Toma de Razón (cuando aplica) |

## P1: Resoluciones Exentas

### Fases y Responsables

| Fase | Responsable | Acción principal |
| :--- | :--- | :--- |
| 1. Iniciación | Área Requirente | Elaborar borrador, adjuntar antecedentes, ingresar al SGD |
| 2. Revisión Jurídica | Unidad Jurídica | Verificar legalidad y forma; V°B° o devolver con observaciones |
| 3. Gestión | Centro de Gestión | Asignar N° resolución, completar formalidades |
| 4. Control | Unidad de Control | Verificar procedencia; V°B° o reparar |
| 5. V°B° Administrador/a | Administrador/a Regional | Revisar y visar |
| 6. Firma | Gobernador/a Regional | Firmar con FEA |
| 7. Notificación y Archivo | Oficina de Partes | Numerar, fechar, notificar, publicar si corresponde, archivar |

### Bifurcaciones

- Fase 2: si Jurídica observa → devuelve a Área Requirente (reinicia fase 1)
- Fase 4: si Control repara → devuelve a Área Requirente (reinicia fase 1)

## P2: Convenios y Transferencias

### Flujo

1. Área requirente propone convenio
2. Elaborar borrador
3. Revisión Jurídica → si requiere ajustes, vuelve al paso 2
4. Resolución que aprueba convenio
5. Toma de Razón si corresponde
6. Firma de partes
7. Ejecución y seguimiento

### Contenido Mínimo del Convenio

| Elemento | Descripción |
| :--- | :--- |
| Partes | GORE + Entidad receptora |
| Objeto | Descripción del programa/proyecto |
| Monto | Valor total y calendario |
| Plazos | Duración y fechas clave |
| Obligaciones | Deberes de cada parte |
| Rendición | Modalidad, plazos, SISREC |
| Restitución | Condiciones de devolución |
| Probidad | Cláusulas anticorrupción |

### Criterios Toma de Razón (CGR)

| Condición | Resultado |
| :--- | :--- |
| Monto supera umbral CGR | Requiere Toma de Razón |
| Bajo umbral | Exento |
| Normativa específica | Consultar Resolución CGR |

## Expediente Electrónico (Ley 21.180)

### Estructura

| Componente | Contenido |
| :--- | :--- |
| Metadatos | ID único, fecha creación, tipo de acto |
| Documentos | Borrador, antecedentes, visaciones |
| Firmas | FEA funcionarios, FEA autoridad |
| Trazabilidad | Log de acciones con fecha/hora |

### Principios TDE

| Principio | Aplicación |
| :--- | :--- |
| Equivalencia funcional | Documento digital = papel |
| Neutralidad tecnológica | Sin dependencia de proveedor |
| Interoperabilidad | Comunicación entre sistemas |
| Seguridad | Integridad, autenticidad, no repudio |

## Sistemas Involucrados

| Sistema | Función |
| :--- | :--- |
| SYS-DOCDIGITAL | Gestión documental, expediente electrónico |
| SYS-FIRMAGOB | Firma Electrónica Avanzada |
| SYS-SIGFE | Registro de compromisos |
| SYS-TRANSPARENCIA | Publicación |

## Normativa Aplicable

| Norma | Alcance |
| :--- | :--- |
| Ley 19.880 LBPA | Procedimiento administrativo |
| Ley 21.180 TDE | Expediente electrónico |
| Ley 19.799 | Firma electrónica |
| Resolución 30/2015 CGR | Rendiciones |
| Ley 19.886 | Contratación pública |

## Referencias Cruzadas

| Dominio | Vínculo |
| :--- | :--- |
| D03 Gestión IPR | Fase 4 Formalización |
| D02 Ciclo Presupuestario | Modificaciones, resoluciones |
| D08 Rendiciones | Convenios de transferencia |
