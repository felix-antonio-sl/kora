---
_manifest:
  urn: "urn:gn:kb:modelos-actos-juridicos"
  provenance:
    created_by: "FS"
    created_at: "2026-01-29"
    source: "GORE Ñuble"
version: "2.0.0"
status: published
tags: [gore-nuble, gobierno-regional, actos-juridicos, modelos, normativa]
lang: es
---

# Modelos de Actos Jurídicos GORE Ñuble

## Propósito y Estructura de los Modelos
- **Objetivo**: Base de conocimiento para Agente IA "Generador de Documentación Administrativa" (ID: AGENT-GORE-DOCGEN-V1.0).
- **Misión**: Generación de actos administrativos formalmente correctos, legalmente válidos y coherentes.
- **Marco Legal General**: Ley N° 19.880.
- **Estructura Estándar (SFD/STS)**:
  - METADATA: Descripción y normativa.
  - HEADER: Identificación del acto (Tipo, Número, Lugar/Fecha).
  - VISTOS: Atribuciones de autoridad y antecedentes.
  - CONSIDERANDO: Motivación y fundamentos (Art. 11 y 41, Ley 19.880).
  - RESUELVO: Núcleo de la decisión y efectos.
  - CIERRE: Formalización y firmas.
- **Componentes de Campo**: Etiqueta, Tipo, Instrucción, Restricciones.

## Índice de Modelos de Actos Jurídicos
| ID Formulario | Descripción | Versión | Estado |
| :--- | :--- | :--- | :--- |
| `FORM-MODIF-CONV-01` | Resolución que Aprueba Modificación de Convenio | 1.0.0 | Completo |
| `FORM-RECTIF-ACTO-01` | Resolución que Rectifica Acto Administrativo | 1.0.0 | Completo |
| `FORM-RESCIL-CONV-01` | Resolución que Aprueba Resciliación de Convenio | 1.0.0 | Completo |
| `FORM-REVOCA-ACTO-01` | Resolución que Revoca un Acto Administrativo | 1.0.0 | Completo |
| `FORM-ESCRITO-INICIO-01` | Escrito de Inicio de Procedimiento | 1.0.0 | Completo |
| `FORM-ESCRITO-REPO-01` | Escrito de Recurso de Reposición | 1.0.0 | Completo |

## Modificación de Convenio (FORM-MODIF-CONV-01)
- **Descripción**: Resolución Exenta para formalizar alteraciones en cláusulas de convenios de colaboración o transferencia.
- **Normativa**: Ley N° 19.880; Ley N° 18.575 (LBGAE); Ley N° 19.175 (LOCGAR).
- **Secciones y Campos Críticos**:
  - **Header**: Tipo (Resolución Exenta), Número correlativo, Lugar/Fecha (Chillán).
  - **Vistos**: Atribuciones (Constitución, Ley 19.880, 18.575, 19.175, Res. 7/2019 CGR); Convenio Original (Individualización inequívoca); Solicitud de Modificación (Oficio o acuerdo).
  - **Considerando**: Contexto original; Fundamento de Modificación (Razones técnicas/operativas/fuerza mayor); Acuerdo de Partes.
  - **Resuelvo**:
    - Art. 1: Aprobación de modificación (referencia a Anexo N°1).
    - Art. 2: Aprobación de texto refundido (opcional/recomendado).
    - Art. 3: Vigencia de cláusulas no modificadas (Principio de Conservación).
  - **Cierre**: Anótese, comuníquese y archívese; Firma Gobernador Regional.

## Rectificación de Acto Administrativo (FORM-RECTIF-ACTO-01)
- **Descripción**: Corrección de errores de hecho, numéricos o de transcripción sin alterar la sustancia.
- **Normativa**: Artículo 62, Ley N° 19.880.
- **Configuración de Campos**:
  - **Vistos**: Atribuciones (Art. 62 Ley 19.880); Identificación de Acto Original.
  - **Considerando**:
    - Tipo de Error: Material, de hecho, transcripción o numérico.
    - Cláusula de Detección: Identificación del error en el acto original.
    - Detalle (Dice/Debe Decir): Especificidad concreta de la corrección.
  - **Resuelvo**:
    - Art. 1: Ejecución de rectificación (reemplazo de expresión).
    - Art. 2: Efecto retroactivo (*ex tunc*); la rectificación integra el acto original.
  - **Cierre**: Anótese, notifíquese y archívese.

## Resciliación de Convenio (FORM-RESCIL-CONV-01)
- **Descripción**: Terminación de convenio por mutuo disenso.
- **Normativa**: Arts. 1545 y 1567 Código Civil (supletorio); Ley N° 19.880; Ley N° 19.175.
- **Estructura del Acto**:
  - **Vistos**: Atribuciones; Convenio Original; Acuerdo de Resciliación previo.
  - **Considerando**: Existencia de relación contractual; Voluntad expresa de mutuo disenso; Estado de obligaciones (pendientes o inexistentes).
  - **Resuelvo**:
    - Art. 1: Aprobación de resciliación.
    - Art. 2: Efectos temporales (*ex nunc*); fecha efectiva de término.
    - Art. 3: Finiquito total (con o sin excepciones).
  - **Cierre**: Fórmulas estándar de tramitación.

## Revocación de Acto Administrativo (FORM-REVOCA-ACTO-01)
- **Descripción**: Retiro de acto VÁLIDO por razones de mérito, oportunidad o conveniencia. No aplica a actos ilegales.
- **Normativa**: Artículo 61, Ley N° 19.880.
- **Restricciones Legales**:
  - No puede lesionar derechos adquiridos (salvo consentimiento expreso).
  - Fundada en interés público sobreviniente.
- **Campos del Modelo**:
  - **Vistos**: Art. 61 Ley 19.880; Identificación de Acto a Revocar.
  - **Considerando**: Fundamento de mérito (descripción detallada); Declaración de no afectación de derechos adquiridos.
  - **Resuelvo**:
    - Art. 1: Revocación por razones expuestas.
    - Art. 2: Efectos hacia el futuro (*ex nunc*); resguardo de situaciones consolidadas.
  - **Cierre**: Anótese, notifíquese y archívese.

## Escrito de Inicio de Procedimiento (FORM-ESCRITO-INICIO-01)
- **Descripción**: Solicitud formal de particular ante GORE Ñuble.
- **Normativa**: Artículos 18, 21 y 30, Ley N° 19.880.
- **Secciones Obligatorias**:
  - **Sumilla**: En lo Principal (Solicitud); En el Otrosí (Documentos).
  - **Cuerpo**:
    - Identificación: Nombre, RUT, profesión, domicilio, correo electrónico (obligatorio para tramitación electrónica).
    - Representación (Opcional): Acreditación de poder (Art. 22 Ley 19.880).
    - Hechos: Exposición clara y circunstanciada.
    - Derecho (Opcional): Fundamento normativo.
    - Petición Concreta: Solicitud específica (Principio Conclusivo, Art. 8 Ley 19.880).
  - **Cierre**: Por tanto (Ruego a US); Otrosí (Acompaña documentos); Firma.

## Recurso de Reposición (FORM-ESCRITO-REPO-01)
- **Descripción**: Medio de impugnación contra actos del GORE para revisión por la misma autoridad.
- **Normativa**: Artículo 59, Ley N° 19.880.
- **Requisitos Críticos**:
  - **Plazo**: 5 días hábiles desde la notificación (fatal).
  - **Causa de Pedir**: Vicios de legalidad (incompetencia, vicios de forma, desviación de poder, falta de fundamentación).
- **Campos del Modelo**:
  - **Cuerpo**:
    - Identificación del Recurrente.
    - Identificación de Acto Impugnado: Número, fecha, fecha de notificación y resumen.
    - Fundamentos de Ilegalidad: Descripción de vicios y normas infringidas.
    - Petición Concreta: Dejar sin efecto, modificar o reemplazar el acto.
  - **Cierre**: Por tanto; Otrosí; Firma.
