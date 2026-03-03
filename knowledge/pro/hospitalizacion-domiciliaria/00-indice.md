---
_manifest:
  urn: "urn:pro:kb:hodom-indice"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-03"
    source: "Síntesis multi-fuente: MINSAL/DEIS Chile 2024-2026, DS 1/2022, DE 31/2024, NT 243/2025, Manual HaH (Johns Hopkins, CMS AHCAH, Cochrane)"
version: "1.1.0"
status: draft
tags: [hospitalizacion-domiciliaria, hah, chile, indice, normativa, operaciones, director-tecnico]
lang: es
---

# Hospitalización Domiciliaria — Índice General

## 1. Propósito y alcance

**Qué ES este corpus**: conocimiento operativo y normativo sobre Hospitalización Domiciliaria (HD / HaH) — modelo clínico, marco regulatorio chileno, gestión directiva, protocolos de seguridad y evidencia internacional.

**Qué NO es**: no es texto normativo vinculante, no reemplaza las normas técnicas MINSAL, no es protocolo clínico específico de un establecimiento.

**Audiencia primaria**:

| Rol | Uso esperado |
|-----|-------------|
| Director/a Técnico/a HD | Referencia normativa completa para el cargo |
| Coordinación de unidad HD | Gestión operacional, RRHH, protocolos |
| Alta dirección / Gestión | Diseño estratégico, financiamiento, benchmarking |
| Equipos clínicos HD | Protocolos, flujos, seguridad, registros |
| Agente `pro/medico-urgencias` | Referencia contexto HD para triage y derivación |

## 2. Mapa del corpus

| Archivo | URN | Contenido | Audiencia primaria |
|---------|-----|-----------|--------------------|
| `00-indice.md` | `urn:pro:kb:hodom-indice` | Índice, glosario, normativa | Todos |
| `01-situacion-chile.md` | `urn:pro:kb:hodom-situacion-chile` | Situación HD en Chile 2024-2026: epidemiología, normativa, producción, financiamiento, brechas | Gestión, política pública |
| `02-manual-hah.md` | `urn:pro:kb:hodom-manual-hah` | Modelo HaH internacional: evidencia, operaciones, tecnología, economía, barreras, futuro | Gestión, clínica, TI |
| `03-director-tecnico.md` | `urn:pro:kb:hodom-director-tecnico` | Manual DT: normativa cargo, RRHH, infraestructura, registros, protocolos, bioseguridad | Director Técnico, Coordinación |

## 3. Navegación

**Referencia cruzada inter-archivo**: `→ urn:pro:kb:hodom-director-tecnico §9.1` apunta al capítulo 9.1 de director-tecnico.

**Relación con corpus gestion-redes**: HD/HaH cubierta como unidad asistencial específica en `urn:pro:kb:gestion-redes-unidades` Cap. 17 — para modelo de gestión de redes y benchmarks comparados usar ese corpus.

**Precedencia normativa**: ante contradicción entre este corpus y la normativa MINSAL vigente, la normativa oficial prevalece.

## 4. Glosario HD

| Término / Acrónimo | Definición telegráfica |
|--------------------|------------------------|
| ACOs | Accountable Care Organizations — organizaciones atención responsable; modelo pago capitado valor |
| AHCAH | Acute Hospital Care at Home — programa CMS EE.UU.; exenciones reglamentarias HaH |
| ATB IV | Antibiótico intravenoso |
| Backfill margin | Efecto económico: camas liberadas por HD → admisión pacientes mayor agudeza → mayor margen institucional |
| CAEC | Cobertura Adicional Enfermedades Catastróficas — cobertura ISAPRE alto costo |
| CAUTI | Catheter-Associated Urinary Tract Infection — ITU asociada a catéter urinario |
| CLABSI | Central Line-Associated Bloodstream Infection — bacteriemia asociada a CVC |
| CUP | Catéter Urinario Permanente |
| CVC | Catéter Venoso Central |
| DE 31/2024 | Decreto Exento 31/2024 MINSAL — Norma Técnica HD vigente |
| DEIS | Departamento de Estadísticas e Información de Salud — MINSAL |
| DS 1/2022 | Decreto Supremo 1/2022 MINSAL — Reglamento establecimientos HD |
| DS 6/2009 | Decreto Supremo 6/2009 MINSAL — Reglamento manejo residuos establecimientos salud (REAS) |
| DS 41/2012 | Decreto Supremo 41/2012 MINSAL — Reglamento ficha clínica |
| DT | Director/a Técnico/a — cargo legal obligatorio en todo establecimiento HD |
| EPP | Elementos de Protección Personal |
| FMEA | Failure Mode and Effects Analysis — análisis modos de fallo para gestión de riesgos |
| FONASA | Fondo Nacional de Salud — seguro público de salud Chile |
| GES-4 | Garantía Explícita en Salud: Alivio del Dolor por Cáncer Avanzado y Cuidados Paliativos |
| GRD | Grupos Relacionados por el Diagnóstico — mecanismo pago hospitalario por casuística |
| HaH | Hospital at Home — hospitalización domiciliaria como alternativa a cama aguda |
| HD | Hospitalización Domiciliaria — término chileno equivalente a HaH |
| HL7 FHIR | Fast Healthcare Interoperability Resources — estándar interoperabilidad datos salud |
| IAAS | Infecciones Asociadas a la Atención de Salud — infecciones nosocomiales |
| IC | Insuficiencia Cardíaca |
| IoT | Internet of Things — dispositivos conectados para telemonitorización domiciliaria |
| ISAPRE | Institución de Salud Previsional — seguro privado de salud Chile |
| ITU | Infección del Tracto Urinario |
| Lock box | Caja de seguridad con llave para almacenamiento de sustancias controladas en domicilio |
| MAI | Modalidad de Atención Institucional — mecanismo financiamiento histórico FONASA |
| MCC | Modalidad de Cobertura Complementaria — NT 238 MINSAL; acceso FONASA a privados HD |
| MINSAL | Ministerio de Salud de Chile |
| NAC | Neumonía Adquirida en la Comunidad |
| NPS | Net Promoter Score — indicador satisfacción y recomendación |
| NT 243 | Norma Técnica 243 mayo 2025 MINSAL — taxonomía complejidad hospitalaria |
| OCDE | Organización para la Cooperación y el Desarrollo Económicos |
| EPOC | Enfermedad Pulmonar Obstructiva Crónica |
| PAC | Plan Anual de Capacitación |
| Picker Experience Score | Escala validada de experiencia del paciente |
| POCT | Point-of-Care Testing — diagnóstico en punto de atención (domicilio) |
| RCP | Reanimación Cardiopulmonar |
| RE 60/2022 | Resolución Exenta 60/2022 MINSAL — Norma Técnica Programa IAAS |
| REAS | Residuos de Establecimientos de Atención de Salud |
| RPM | Remote Patient Monitoring — monitorización remota de pacientes |
| SAMU | Servicio de Atención Médica de Urgencia — EMS público Chile |
| SBAR | Situation-Background-Assessment-Recommendation — metodología estructurada traspaso clínico |
| SCC | Score de Categorización de Complejidad — herramienta agudeza HD (Básico/Intermedio/Complejo) |
| SEC | Superintendencia de Electricidad y Combustibles — Chile |
| SENAMA | Servicio Nacional del Adulto Mayor — Chile |
| SEREMI | Secretaría Regional Ministerial de Salud — autoridad sanitaria regional Chile |
| SNF-at-Home | Skilled Nursing Facility at Home — equivalente domiciliario de centro de enfermería especializada |
| SSMOc | Servicio de Salud Metropolitano Occidente — datos referenciales HD 2024 |
| TET | Tubo Endotraqueal |
| TQT | Traqueostomía |
| Triple Aim | Marco IHI: experiencia paciente + salud poblacional + costo per cápita |
| VBC | Value-Based Care — atención basada en el valor |
| VVP | Vía Venosa Periférica |

## 5. Marco normativo de referencia

### 5.1 Normativa chilena HD

| Norma | Tipo | Alcance | Vigencia |
|-------|------|---------|----------|
| Código Sanitario DS 725/1968 | DFL | Habilitación prestadores | Vigente (mod. 2024) |
| Ley 20.584 (2012) | Ley | Derechos y deberes pacientes | Vigente |
| Ley 19.628 + 20.575 | Ley | Protección datos personales/sensibles | Vigente |
| DS 1/2022 MINSAL | Decreto Supremo | Reglamento establecimientos HD | Vigente |
| DS 41/2012 MINSAL | Decreto | Ficha clínica: contenido, formato, acceso | Vigente |
| DS 6/2009 MINSAL | Decreto | REAS: manejo, transporte, eliminación | Vigente |
| Decreto Exento 31/2024 MINSAL | Norma Técnica | Funcionamiento HD; manuales obligatorios; requisitos infraestructura/RRHH | Vigente |
| RE 60/2022 MINSAL | Resolución Exenta | Programa IAAS — prevención y control | Vigente |
| Norma Técnica 238 MINSAL | Norma Técnica | MCC: código 0201408 Día Cama HD Baja Complejidad | Vigente |
| Norma Técnica 243 MINSAL (mayo 2025) | Norma Técnica | Complejidad hospitalaria: rol transversal HD | Vigente |
| Ley 16.744 | Ley | Accidentes del trabajo y enfermedades profesionales | Vigente |
| Circular IF N° 7 (Superintendencia Salud) | Circular | CAEC ISAPRE: excepciones calificadas HD | Vigente |

### 5.2 Referentes internacionales HD

| Referente | Tipo | Alcance |
|-----------|------|---------|
| Johns Hopkins HaH Program (Leff et al.) | Programa fundacional | Criterios admisión, vías clínicas, outcomes — referente global |
| Cochrane Review: Shepperd et al. | Revisión sistemática | Efectividad HaH vs. hospitalización — evidencia de alta calidad |
| CMS AHCAH (Acute Hospital Care at Home) | Programa federal EE.UU. | Marco regulatorio, exenciones, paridad DRG hasta sept 2030 |
| IHI Triple Aim | Framework | Alineamiento estratégico experiencia/salud/costo |
| Joint Commission HaH Standards | Estándares acreditación | Seguridad, calidad, documentación HaH |
| FDA Digital Health Framework | Marco regulatorio | Dispositivos RPM aprobados; validación clínica |
| NICE Clinical Guidelines (UK) | Guías clínicas | Evidencia patologías elegibles HaH |

## 6. Control de versiones

| Versión | Fecha | Cambios | Autor |
|---------|-------|---------|-------|
| v1.0.0 | 2026-03-03 | Creación corpus desde fuentes primarias inbox/hodom (3 documentos, 2.655 líneas fuente). Koraficación KORA/MD: telegrafización, estructuración RAG, deduplicación SSOT, frontmatter, glosario centralizado | kora/curator |
| v1.1.0 | 2026-03-03 | S-REPAIR post-auditoría: eliminación invenciones (Ley 20.575, criterios exclusión espurios, sustancias controladas), reincorporación ~200 hechos perdidos (datos cuantitativos, articulado legal, anexos, perfiles RRHH). Corpus 673→1403 líneas | kora/curator |

### Política de actualización

| Aspecto | Regla |
|---------|-------|
| Frecuencia revisión | Ante cambio normativo MINSAL o nueva evidencia clínica relevante |
| Versionado | SemVer: MAJOR (reestructura), MINOR (sección nueva/reescrita), PATCH (correcciones puntuales) |
| Responsable | kora/curator + validación experto dominio (médico HD) |
| Sincronización | Tras modificar cualquier archivo → verificar coherencia con 00-indice.md |
| Normativa | Verificar vigencia anual; marcar derogaciones explícitamente |
