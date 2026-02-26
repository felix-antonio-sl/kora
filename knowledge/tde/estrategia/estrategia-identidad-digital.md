---
_manifest:
  urn: "urn:tde:kb:estrategia-identidad-digital"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/Estrategias/identidad-digital"
version: 1.0.0
status: published
tags: [estrategia, identidad-digital, claveunica, tde, ciberseguridad, firma-electronica]
lang: es
---

# Estrategia de Identidad Digital

Marco estratégico para nuevo sistema de identidad digital de personas naturales (por sí o en representación). Extensible a objetos y sistemas. Plan de acción actualizable cada 6 meses por SGD.

## Alcance

- Personas naturales actuando por sí
- Eventualmente: personas en representación de otra persona natural/jurídica
- Potencial extensión gradual: objetos y sistemas

## Relevancia

### Derechos

- Identidad = derecho humano (Convención Derechos del Nino, UNICEF 1989)
- ODS 16: identidad jurídica para todos al 2030
- Inclusión digital: acceso servicios básicos, salud, beneficios sociales, capital financiero, voto, cruce fronteras, propiedad bienes

### Impacto económico

| Fuente | Dato |
|--------|------|
| UE (2021) | Billeteras identidad digital: 1.268 M EUR valor anadido en 10 anos |
| Reino Unido (2022) | Nuevo sistema identidad digital: ~800 M GBP beneficios anuales esperados |
| Estonia (2019) | Sistema identidad/firma digital: ahorro hasta 2% PIB anual |
| McKinsey (2019) | Economías ingreso medio-alto: identidad digital aporta 3-13% PIB al 2030 |
| McKinsey (2022) | Inversión global tecnologías privacidad/autenticidad: ~47.000 M USD/ano |
| Banco Mundial (2024) | Reducción costos gestión/verificación identidad hasta 50% |
| WEF (2022) | Pagos digitales = principal método compra LAC, +18% comercio electrónico (2020) |

## Estado actual Chile

### Activos existentes

1. **Registro Civil**: registro poblacional centralizado + RUN (identificador único universal)
2. **SII (1995)**: digitalización tributaria pionera + Clave Tributaria (RUT-clave)
3. **Ley 19.799 (2002)**: equivalencia funcional documentos físicos/electrónicos + marco confianza firma electrónica avanzada (Entidad Acreditadora MINECON + prestadoras + usuarios)
4. **ClaveUnica (2010+)**: plataforma SGD, >15M usuarios, ~1.800 trámites. Origen: Clave Internet Registro Civil (2010), ampliada a OAE (2011+). Marco jurídico actual: solo Administración Pública + AFP + prestadoras certificación
5. **Compromisos internacionales**: DEPA (interoperabilidad identidades digitales), Acuerdo Marco UE (cooperación identidad digital), Recomendación OCDE Gobernanza Identidad Digital (38 países, G20, G7)

### Desafios

1. **Fraude creciente**:
   - 50% chilenos ha sufrido intento fraude pagos electrónicos (UGM/B&W, 2023)
   - 29% adultos mayores víctima fraude digital hasta jul-2024 (ClaroVTR/Criteria)
   - 21.000 casos troyanos bancarios Chile 2023 (Kaspersky)
   - Phishing = amenaza consolidada
   - Suplantación identidad: +30-45% (PDI, 2022)
   - 58% estafas reportadas vía Internet (PDI, 2022)

2. **Marco regulatorio débil**:
   - Regulación fraccionada e insuficiente
   - Solo regulada: firma electrónica avanzada (ley) + ClaveUnica en OAE/AFP (admin)
   - Sin habilitantes legales expansión ClaveUnica a sector privado general
   - No existe identidad digital "jurídica/oficial" equivalente a cédula física

3. **Gobernanza fragmentada**:
   - Registro Civil: identidad civil + documentos oficiales
   - SGD: ClaveUnica + CasillaUnica + FirmaGob
   - MINECON: acreditación/regulación firma electrónica avanzada
   - SII: Clave Tributaria
   - Sectoriales: CMF, Superintendencia Pensiones, Subprev, Poder Judicial
   - Sin institución responsable coordinación general
   - Modelo indefinido: centralizado vs descentralizado vs federado

## Vision 2030

Chile con ecosistema identidad digital al servicio de las personas, alianza público-privada, líder regional economía digital y nuevo líder mundial identidad digital.

## Objetivo

Implementar nuevo sistema identidad digital inclusivo, seguro, confiable. Personas naturales acceden simple y amigablemente a productos/servicios digitales públicos/privados, nacionales/internacionales.

## Nuevo sistema público-privado

### Modelo

- **Identidad fundacional**: modelo centralizado (Registro Civil + RUN) -- se mantiene
- **Operación**: parcialmente descentralizado -- integración (canal distribución privado) + provisión servicios confianza (público + privado)
- Colaboración público-privada obligatoria para adopción, escalabilidad, seguridad, interoperabilidad, resiliencia

### Implementación corto plazo (2025-2026)

**Gobernanza**: Comité Ejecutivo Identidad Digital:
- Registro Civil (identidad original + cédula digital)
- SGD (líder/coordinador TD + ClaveUnica)
- ANCI (auditor seguridad)
- Entidad Acreditadora MINECON (regulador firma electrónica)

**Tecnología**: broker/pasarela identidad digital sobre infraestructura ClaveUnica:
- Factor primario: ClaveUnica
- Factor mayor seguridad: Cédula Identidad Digital (Registro Civil)
- Uso: OAE (Norma Técnica Autenticación) + otras entidades según Comité

**Financiamiento**: modelo costo distribuido (pago por transacción) vía Registro Civil para entidades privadas. Sector público: presupuesto SGD.

### Implementación mediano plazo (2027-2030)

**Gobernanza**: autoridad pública única claramente establecida por ley. Entidades acreditadas (públicas/privadas) prestan servicios confianza independientes. Extensible a objetos/sistemas y otras entidades (Subtel).

**Tecnología**: broker ampliado con servicios confianza acreditados (públicos/privados). Estándares para nuevas oportunidades negocio.

**Financiamiento**: sector privado = costo distribuido (pago por transacción). Sector público: evaluar transición desde costo centralizado a distribuido proporcional a volumen transacciones.

## Tabla responsabilidades

| Actividad | Corto plazo | Mediano plazo |
|-----------|-------------|---------------|
| Identidad original | Registro Civil | Registro Civil |
| Decretos/reglamentos/leyes | MinHacienda + MinJusticia | MinHacienda + MinJusticia |
| Liderazgo/coordinación sistema | Comité Ejecutivo (SGD, ANCI, RC, MINECON) | Autoridad pública única (ley) |
| Estándares funcionales/tecnológicos | Comité Ejecutivo | Autoridad pública única |
| Fiscalización | ANCI + Registro Civil | Autoridad pública única |
| Servicios confianza | SGD + Registro Civil | Entidades acreditadas + SGD + RC |
| Nuevos servicios al broker | SGD | SGD |
| Integración entidades | SGD + privados | SGD + privados |
| Cobro entidades privadas | Registro Civil | Autoridad pública única |
| Claves con estándares | SGD | SGD |

## Plan de acción

### Corto plazo (2025-2026)

| Acción | Responsable | Plazo | Verificación |
|--------|-------------|-------|-------------|
| Cédula identidad digital | Registro Civil | Q4-2024 | Hito lanzamiento |
| Constituir Consejo Identidad Digital | MinHacienda | Q1-2025 | Acta primera sesión |
| Indicadores impacto/resultado | Consejo ID | Q2-2025 | Informe técnico |
| Primera versión broker identidad | MinHacienda | Q2-2025 | Cédula digital en ClaveUnica |
| Reforma Norma Técnica Autenticación | MinHacienda | Q2-2025 | Decreto publicado |
| Estándares seguridad autenticación | MinHacienda + ANCI | Q2-2025 | Norma publicada |
| Piloto broker sector público | MinHacienda | Q3-2025 | Broker v1 en producción |
| Proponer entidad rectora | MinHacienda | Q4-2025 | Informe técnico |
| Modelo financiamiento servicios privados | MinHacienda | Q4-2025 | Informe técnico |
| Piloto broker entidades privadas | MinHacienda | Q1-2026 | Broker v1 producción privados |
| Financiamiento ClaveUnica privados | Registro Civil | Q1-2026 | Convenios tramitados |
| FirmaGob en lista confianza MINECON | MinHacienda | Q4-2026 | FirmaGob en trust list |

### Mediano plazo (2027-2030)

| Acción | Responsable | Plazo | Verificación |
|--------|-------------|-------|-------------|
| Autoridad rectora por ley | MinHacienda | Q1-2027 | Ley publicada |
| Modelo financiamiento servicios privados confianza | Autoridad rectora | Q2-2027 | Segun corresponda |
| Nuevos prestadores servicios confianza | Autoridad rectora | Q3-2027 | Piloto concluido |
| Evaluación intermedia | MinHacienda | Q2-2028 | Informe independiente |
| Evaluación final | MinHacienda | Q4-2030 | Informe independiente |
