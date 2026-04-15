---
_manifest:
  urn: urn:tde:kb:estrategia-identidad-digital
  provenance: https://wikiguias.digital.gob.cl/Estrategias/identidad-digital
version: 1.0.0
status: published
tags:
- tde
- estrategia
- identidad digital
- ClaveÚnica
- cédula digital
- autenticación
- gobernanza digital
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:tde:kb:estrategia-identidad-digital
---

# Estrategia de Identidad Digital

---

## La identidad digital en Chile: estado actual

- **Registro Civil e Identificación (SRCeI):** establece la identidad civil; infraestructura basada en el Rol Único Nacional (RUN), identificador único asignado al nacer, que garantiza unicidad y universalidad de la identidad.
- **SII (desde 1995):** lideró digitalización de trámites tributarios; desarrolló la Clave Tributaria (par RUT-clave) para acceso a servicios tributarios en línea.
- **Ley N° 19.799 (2002):** establece equivalencia funcional de documentos físicos y electrónicos; regula servicios de certificación de firma electrónica avanzada; crea marco de confianza compuesto por la Entidad Acreditadora (Ministerio de Economía), entidades acreditadas (prestadoras de certificación) y usuarios.
- **ClaveÚnica:** plataforma desarrollada y operada por la SGD. Nació en 2010 como Clave Internet para trámites del Registro Civil; desde 2011 se amplió a otros órganos de la Administración. Tiene más de 15 millones de usuarios/as (SGD, 2024) y facilita acceso a aproximadamente 1.800 trámites. El marco jurídico actual solo permite su uso a la Administración Pública y algunas entidades privadas (AFP y prestadoras de certificación).
- **Compromisos internacionales:** Chile es parte del Acuerdo de Asociación de Economía Digital (DEPA); suscribió un Acuerdo Marco Avanzado con la UE; ha adoptado la Recomendación del Consejo de la OCDE sobre Gobernanza de la Identidad Digital (estándar respaldado por 38 países, reconocido por G20 y G7).

---

## Desafíos

**1. Aumento del fraude digital:**
- La mitad de los chilenos ha sufrido algún intento de fraude con pagos electrónicos (UGM & Black & White, 2023).
- El 29% de los adultos mayores afirmó haber sido víctima de fraude digital en lo que iba de 2024 (ClaroVTR & Criteria, 2024).
- En 2023 se reportaron 21.000 casos de troyanos bancarios en Chile (Kaspersky, 2023).
- El delito de suplantación de identidad ha aumentado entre un 30% y 45% (PDI, 2022).
- En 2022, el 58% de las estafas reportadas se cometieron a través de Internet (PDI, 2022).

**2. Marco regulatorio débil y fraccionado:**
- Solo se ha regulado la prestación de servicios de certificación de firma electrónica avanzada a nivel de ley.
- A nivel administrativo, solo se ha regulado el uso de ClaveÚnica en organismos del Estado, el Poder Judicial y las AFP y AFC III.
- No existen habilitantes legales para expandir de manera general el uso de ClaveÚnica en el sector privado.
- Ausencia de una identidad digital "jurídica" u "oficial" equivalente a la cédula de identidad física.

**3. Gobernanza fragmentada:**
- SRCeI: establece y registra identidad civil; gestiona documentos oficiales.
- SGD: desarrolla y opera ClaveÚnica, CasillaÚnica y FirmaGob.
- Ministerio de Economía: acredita, inspecciona y regula el mercado de firma electrónica avanzada.
- SII: opera la Clave Tributaria.
- Órganos sectoriales (CMF, Superintendencia de Pensiones, Subsecretaría de Previsión Social, Poder Judicial): han dictado normas sobre autenticación.
- No existe una institución claramente responsable de liderar y coordinar el sistema; no está claro si el modelo actual es descentralizado, centralizado o federado.

---

## Visión

Para el año 2030, Chile contará con un ecosistema de identidad digital al servicio de las personas, construido sobre una sólida alianza público-privada, consolidándose como líder regional en economía digital y uno de los nuevos líderes mundiales en identidad digital.

---

## Objetivo

Implementar un nuevo sistema de identidad digital inclusivo, seguro y confiable que permita a las personas naturales (por sí o en representación de otra persona natural o jurídica) acceder de manera simple y amigable a toda clase de productos y servicios digitales públicos y privados, nacionales e internacionales.

---

## Nuevo sistema público-privado de identidad digital

### Modelo propuesto

La estrategia propone construir un marco de confianza de identidad digital basado en el **modelo centralizado para el otorgamiento de la identidad fundacional**, aprovechando la robustez del sistema actual (ClaveÚnica está construida sobre el RUN del Registro Civil). El sistema será **necesariamente implementado mediante colaboración público-privada** para:
1. Asegurar adopción y escalabilidad en el sector privado: entidades privadas actuarán como canal de distribución y como identificadoras de necesidades sectoriales.
2. Garantizar seguridad, interoperabilidad y resiliencia: asesoría técnica y servicios de confianza de entidades privadas, sobre la infraestructura pública digital de la SGD, bajo un modelo de marco de confianza.

El sistema será en parte descentralizado tanto en la integración (canal de distribución) como en la operación (provisión de servicios de confianza).

---

### Implementación: dos etapas

#### Corto plazo — hacia 2026

**Gobernanza:** Comité Ejecutivo de Identidad Digital integrado por:
- Registro Civil: responsable del establecimiento de la identidad original y proveedor de la cédula de identidad digital.
- SGD: líder y coordinador del uso de tecnologías digitales y proveedor de ClaveÚnica.
- ANCI (Agencia Nacional de Ciberseguridad): auditor de la seguridad del modelo.
- Entidad Acreditadora del Ministerio de Economía: regulador e inspector de la firma electrónica.

**Tecnología:** implementar un *broker* o pasarela de identidad digital sobre la infraestructura de ClaveÚnica, ofreciendo servicios de autenticación. El primer servicio: Cédula de Identidad Digital del Registro Civil. El *broker* podrá ser utilizado por órganos de la Administración (según la Norma Técnica de Autenticación de la Ley de TD) y por entidades públicas y privadas según criterios, forma, alcance y gradualidad que determine el Comité Ejecutivo.

**Financiamiento:** modelo de "costo distribuido" basado en volumen de transacciones, actualmente utilizado por el Registro Civil para ClaveÚnica con entidades privadas. El sector público continúa financiado por el presupuesto corriente de la SGD. Los servicios públicos de identidad digital serán gratuitos y accesibles para toda la población.

#### Mediano plazo — hacia 2030

**Gobernanza:** rectoría asumida por una única autoridad pública establecida por ley. Cualquier entidad debidamente acreditada (pública o privada) podrá prestar servicios de confianza de manera independiente y sumarse al *broker* tecnológico. El establecimiento de la identidad fundacional seguirá siendo responsabilidad del Registro Civil. Eventualmente podrían sumarse objetos y sistemas y otras entidades (ej. Subsecretaría de Telecomunicaciones).

**Tecnología:** al *broker* de identidad podrán sumarse mecanismos administrados por entidades públicas y privadas que cumplan requisitos. Se fomentará el desarrollo de otros servicios de confianza mediante estándares que generen nuevas oportunidades de negocio.

**Financiamiento:** el sector privado seguirá con modelo de cobro distribuido (pago por transacción). El sector público deberá evaluar si adopta también un modelo de costo distribuido en proporción al volumen de transacciones de sus usuarios.

---

### Tabla resumen: responsables por actividad

| Actividad | Responsable(s) — Corto plazo | Responsable(s) — Mediano plazo |
|-----------|------------------------------|-------------------------------|
| Establecer o verificar la identidad original | Registro Civil | Registro Civil |
| Elaborar decretos, reglamentos y leyes | Ministerio de Hacienda; Ministerio de Justicia y DDHH | Ministerio de Hacienda; Ministerio de Justicia y DDHH |
| Liderar y coordinar el sistema | Comité Ejecutivo (SGD, ANCI, Registro Civil, Entidad Acreditadora MINECON) | Autoridad pública claramente definida |
| Establecer estándares funcionales, tecnológicos, de confianza y de seguridad | Comité Ejecutivo | Autoridad pública claramente definida |
| Acreditar cumplimiento de estándares | Comité Ejecutivo | Autoridad pública claramente definida |
| Fiscalizar el cumplimiento de estándares | ANCI; Registro Civil | Autoridad pública claramente definida |
| Prestar servicios de confianza | SGD; Registro Civil | Entidades acreditadas; SGD; Registro Civil |
| Sumar servicios de confianza al *broker* de identidad digital | SGD | SGD |
| Integrar servicios de confianza en entidades públicas y privadas | SGD; Entidades privadas | SGD; Entidades privadas |
| Cobrar a entidades privadas que utilicen servicios de confianza públicos | Registro Civil | Autoridad pública claramente definida |
| Proveer el servicio de claves que cumplan estándares | SGD | SGD |

El plan de acción de la estrategia será revisado y actualizado cada seis meses por la SGD.

---

## Anexo: Plan de Acción

| Alcance | Acción | Descripción | Responsable | Plazo | Medio de verificación |
|---------|--------|-------------|-------------|-------|-----------------------|
| Corto plazo 2025-2026 | Implementar cédula de identidad digital | Nueva cédula con 32 medidas de seguridad y versión digital opcional en app móvil | Registro Civil | Q4-2024 | Hito de lanzamiento realizado |
| Corto plazo 2025-2026 | Constituir Consejo de Identidad Digital | Inicio de funciones del Consejo (SGD, Registro Civil y ANCI) | Ministerio de Hacienda | Q1-2025 | Acta de la primera sesión firmada |
| Corto plazo 2025-2026 | Definir indicadores de impacto y resultado del nuevo sistema | Definir línea de base, metas e indicadores para evaluaciones intermedias y final | Consejo de Identidad Digital | Q2-2025 | Informe técnico publicado |
| Corto plazo 2025-2026 | Desarrollar primera versión del *broker* de identidad digital | Servicio de autenticación sobre ClaveÚnica transformándola en pasarela de identidad | Ministerio de Hacienda | Q2-2025 | Cédula de identidad digital disponible en el servicio de autenticación de ClaveÚnica |
| Corto plazo 2025-2026 | Reformar la Norma Técnica de Autenticación | Actualizar Decreto N° 9, de 2023, del Ministerio SEGPRES sobre Norma Técnica de Autenticación | Ministerio de Hacienda | Q2-2025 | Decreto supremo publicado |
| Corto plazo 2025-2026 | Establecer estándares y niveles de seguridad para servicios de autenticación | Norma conjunta de ciberseguridad y seguridad de la información para quienes operen y/o desarrollen servicios de autenticación | Ministerio de Hacienda & ANCI | Q2-2025 | Norma publicada |
| Corto plazo 2025-2026 | Iniciar piloto del *broker* de identidad digital en el sector público | Habilitar el uso del *broker* para órganos públicos | Ministerio de Hacienda | Q3-2025 | *Broker* en producción usado por instituciones públicas |
| Corto plazo 2025-2026 | Proponer entidad rectora | Recomendación técnica sobre cuál debería ser la entidad rectora, su alcance y competencias | Ministerio de Hacienda | Q4-2025 | Informe técnico publicado |
| Corto plazo 2025-2026 | Proponer modelo de financiamiento para servicios privados de confianza | Definir modelo que operará cuando se sumen proveedores privados de autenticación al *broker* | Ministerio de Hacienda | Q4-2025 | Informe técnico publicado |
| Corto plazo 2025-2026 | Iniciar piloto del *broker* en entidades privadas determinadas | Habilitar el uso del *broker* por entidades privadas seleccionadas | Ministerio de Hacienda | Q1-2026 | *Broker* en producción usado por instituciones privadas |
| Corto plazo 2025-2026 | Implementar modelo de financiamiento para uso de ClaveÚnica por entidades privadas | Entidades privadas firman convenio con Registro Civil para pago por volumen de transacciones (costo distribuido) | Registro Civil | Q1-2026 | Convenios totalmente tramitados |
| Corto plazo 2025-2026 | Ingresar FirmaGob a la lista de confianza de la Entidad Acreditadora | Cumplir todos los requisitos para ser agregados a la *trust service list* de MINECON | Ministerio de Hacienda | Q4-2026 | FirmaGob agregado a la lista de confianza |
| Mediano plazo 2027-2030 | Contar con una única autoridad rectora | Establecer por ley la entidad que ejercerá la rectoría del sistema | Ministerio de Hacienda | Q1-2027 | Ley publicada |
| Mediano plazo 2027-2030 | Administrar modelo de financiamiento para servicios privados de confianza | Definir modelo que operará cuando se sumen proveedores privados al sistema | Autoridad rectora | Q2-2027 | Según corresponda |
| Mediano plazo 2027-2030 | Incluir nuevos prestadores de servicios de confianza | Expandir solución para integrar nuevos servicios de autenticación e identidad de prestadores acreditados (público y privado) | Autoridad rectora | Q3-2027 | Piloto con nuevos prestadores concluido |
| Mediano plazo 2027-2030 | Realizar evaluación intermedia del sistema | Evaluar primeros años de operación del sistema y sus pilotos | Ministerio de Hacienda | Q2-2028 | Informe de entidad independiente publicado |
| Mediano plazo 2027-2030 | Realizar evaluación final del sistema | Evaluar primeros años de la operación del sistema y sus pilotos | Ministerio de Hacienda | Q4-2030 | Informe de entidad independiente publicado |
