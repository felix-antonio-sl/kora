# Arquitectura del Sistema Nacional de Servicios de Salud (SNSS)

**Fecha**: 2026-04-01 | **Estado**: Versión inicial | **Fuentes principales**: DFL 1/2005 (MINSAL); Ley 19.937 (2004); Ley 18.469 (1985); Ley 18.933 (1990)

---

## 1. Visión general

Chile tiene un sistema de salud mixto (público-privado) con cobertura universal obligatoria. Todo trabajador dependiente e independiente cotiza el 7% de su renta imponible para salud, eligiendo entre el asegurador público (FONASA) o uno privado (ISAPRE).

**Cobertura aproximada** [VERIFICAR]:
- FONASA: ~80% de la población (~15 millones)
- ISAPRE: ~15% (~3 millones)
- Fuerzas Armadas y de Orden: ~3%
- Sin seguro: ~2%

---

## 2. Estructura institucional

### 2.1 Ministerio de Salud (MINSAL)

Órgano rector del sector salud. Funciones: formulación de políticas, regulación, planificación estratégica, normas técnicas, vigilancia epidemiológica.

**Subsecretarías:**

#### Subsecretaría de Salud Pública
- Políticas de salud pública, promoción, prevención
- Vigilancia epidemiológica
- Determinantes sociales
- Divisiones: Prevención y Control de Enfermedades (DIPRECE), Políticas Públicas Saludables, Planificación Sanitaria
- Supervisión de las SEREMI de Salud

#### Subsecretaría de Redes Asistenciales
- Regulación y coordinación de la red asistencial pública
- Normas de organización y funcionamiento de los SS
- Gestión de recursos, inversión, RRHH
- Divisiones: Gestión de la Red Asistencial (DIGERA), Inversiones, Presupuesto, APS

### 2.2 Secretarías Regionales Ministeriales de Salud (SEREMI)

- 16 SEREMI (una por región, Ñuble separada de Biobío [VERIFICAR])
- Representan al MINSAL en el territorio
- Funciones: autoridad sanitaria regional, fiscalización, vigilancia epidemiológica local, permisos sanitarios, promoción de salud
- Dependen técnicamente de la Subsecretaría de Salud Pública
- Creadas por Ley 19.937 (separación de funciones asistenciales y de salud pública)

### 2.3 Servicios de Salud (SS)

- **29 Servicios de Salud** a nivel nacional [VERIFICAR: pueden haberse creado nuevos]
- Organismos descentralizados funcionalmente, con personalidad jurídica y patrimonio propio
- Cada SS tiene un Director elegido por Alta Dirección Pública
- Función: articular, gestionar y desarrollar la red asistencial en su territorio
- Administran hospitales y establecimientos de su dependencia
- Celebran convenios con la APS municipal

**Órganos de los SS:**
- Dirección del Servicio
- Consejo de Integración de la Red Asistencial (CIRA)
- Consejo Consultivo de Usuarios

### 2.4 Establecimientos asistenciales públicos

#### Hospitales
- Clasificación por complejidad: alta, mediana, baja
- **Establecimientos Autogestionados en Red (EAR)**: hospitales de alta complejidad con mayor autonomía de gestión (Ley 19.937)
- [VERIFICAR] ~60 hospitales EAR aproximadamente
- Hospitales no autogestionados: dependen directamente del SS

#### Atención Primaria de Salud (APS)
- Administrada mayoritariamente por municipios (Ley 19.378 — Estatuto APS)
- Algunos establecimientos bajo SS directamente
- Tipos de establecimientos:
  - **CESFAM** (Centro de Salud Familiar): principal dispositivo de APS urbana
  - **CECOSF** (Centro Comunitario de Salud Familiar): dispositivo comunitario
  - **Posta de Salud Rural**: APS en zonas rurales
  - **SAPU** (Servicio de Atención Primaria de Urgencia): urgencia de baja complejidad
  - **SAR** (Servicio de Alta Resolutividad): dispositivo de urgencia/resolutividad intermedia
  - **SUR** (Servicio de Urgencia Rural)

### 2.5 Fondo Nacional de Salud (FONASA)

- Asegurador público de salud
- Administra los recursos financieros del sector público de salud
- Funciones: financiar prestaciones (MAI y MLE), recaudar cotizaciones, clasificar beneficiarios
- **Tramos de beneficiarios:**
  - **Tramo A**: carentes de recursos / indigentes (gratuidad total en MAI)
  - **Tramo B**: ingreso imponible ≤ salario mínimo (gratuidad total en MAI)
  - **Tramo C**: ingreso entre 1 y 1.46 veces el salario mínimo (copago 10% en MAI)
  - **Tramo D**: ingreso > 1.46 veces el salario mínimo (copago 20% en MAI)
- **Modalidades:**
  - **MAI** (Modalidad de Atención Institucional): red pública
  - **MLE** (Modalidad de Libre Elección): prestadores privados con bonificación FONASA

### 2.6 Instituciones de Salud Previsional (ISAPRE)

- Aseguradoras privadas de salud
- Reguladas por la Superintendencia de Salud
- Contratos individuales con plan de salud, tabla de factores, deducible
- CAEC (Cobertura Adicional para Enfermedades Catastróficas)
- [VERIFICAR] ~7 ISAPRE abiertas operando; las cerradas/grupales tienen régimen distinto
- Sentencias Corte Suprema y TC sobre tabla de factores → Ley Corta ISAPRE

### 2.7 Superintendencia de Salud

- Organismo fiscalizador autónomo
- Funciones: supervisar FONASA, ISAPRE y prestadores; resolver conflictos; fiscalizar GES; acreditación de prestadores
- Divisiones: Fiscalización, Intendencia de Prestadores, Intendencia de Fondos y Seguros

### 2.8 Instituto de Salud Pública (ISP)

- Laboratorio nacional y de referencia
- Funciones: control de calidad de medicamentos, alimentos y productos de uso médico; laboratorio de referencia para vigilancia epidemiológica; registro sanitario de medicamentos; farmacovigilancia; salud ocupacional
- Dependiente del MINSAL

### 2.9 Central Nacional de Abastecimiento (CENABAST)

- Intermediación de compras de medicamentos e insumos para el sector público
- Economías de escala mediante licitaciones centralizadas
- Distribución a la red pública

### 2.10 Otras instituciones relevantes

- **COMPIN** (Comisión de Medicina Preventiva e Invalidez): certificación de discapacidad, licencias médicas
- **ACHS, IST, Mutual de Seguridad**: mutuales de accidentes del trabajo (Ley 16.744)
- **CONAC** / **Consejo Consultivo**: participación ciudadana

---

## 3. Flujos de financiamiento

```
Cotización 7% → FONASA o ISAPRE
                    │
            ┌───────┴───────┐
            ▼               ▼
         FONASA          ISAPRE
            │               │
    ┌───────┼───────┐       │
    ▼       ▼       ▼       ▼
  Per     PPV/    GES    Prestadores
 cápita   PPI   valorizado  privados
  APS    Hosp.
    │       │
    ▼       ▼
  Munic.  Servicios
  APS    de Salud
         Hospitales
```

**Aporte fiscal**: El Estado aporta recursos adicionales vía Ley de Presupuestos (aporte fiscal directo a SS, programas específicos).

**Per cápita APS**: asignación mensual por persona inscrita, con indexadores (ruralidad, pobreza, edad, etc.).

**PPV (Programa de Prestaciones Valoradas)**: pago por actividad a hospitales.

**PPI (Programa de Prestaciones Institucionales)**: transferencia global a hospitales.

**GES valorizado**: financiamiento específico para las garantías explícitas.

---

## 4. Separación de funciones (Ley 19.937)

La reforma de 2004 estableció la separación de funciones entre:

| Función | Institución |
|---|---|
| Rectoría y regulación | MINSAL (Subsecretarías) |
| Autoridad sanitaria | SEREMI de Salud |
| Aseguramiento | FONASA / ISAPRE |
| Prestación | SS / Hospitales / APS |
| Fiscalización | Superintendencia de Salud |

---

## 5. Fuentes

- Chile. DFL 1/2005 del Ministerio de Salud. Fija texto refundido, coordinado y sistematizado del DL 2763/1979 y leyes 18.933 y 18.469.
- Chile. Ley 19.937 (2004). Modifica el DL 2763 — Autoridad Sanitaria y Gestión.
- Chile. Ley 18.469 (1985). Regula el ejercicio del derecho constitucional a la protección de la salud.
- Chile. Ley 18.933 (1990). Crea la Superintendencia de ISAPRE.
- OPS/OMS. Perfil del Sistema de Salud: Chile. Monitoreo y Análisis de los Procesos de Cambio y Reforma.
- Becerril-Montekio V, Reyes JD, Manuel A. "Sistema de salud de Chile". Salud Pública Méx 2011;53(supl 2):s132-s143.
