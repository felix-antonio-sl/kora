---
_manifest:
  urn: urn:gn:kb:flujos-aprobacion-documentos
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: "GORE Ñuble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- gestion
- flujos-aprobacion
- inversion-publica
- gn
lang: es
---

# Flujos de Aprobación de Documentos — GORE Ñuble

## Glosario de Actores y Siglas

| Actor / Sigla | Nombre Completo | Rol Principal |
| :--- | :--- | :--- |
| GORE | Gobierno Regional | Administración superior regional; ejecuta inversión y programas. |
| CORE | Consejo Regional | Aprueba presupuesto, ERD y modificaciones; fiscaliza gestión. |
| Gobernador/a | Gobernador/a Regional | Firma ejecutiva final; representación legal del GORE. |
| Admin. Regional | Administrador/a Regional | Coordinación interna; V°B° pre-firma; subrogancia legal. |
| DAF | División de Administración y Finanzas | Gestión financiera, contable, convenios, pagos, SIGFE. |
| DIPIR | División de Presupuesto e Inversión Regional | Presupuesto inversión, evaluación IDI, seguimiento BIP. |
| DIPLADE | División de Planificación y Desarrollo Regional | ERD, ARI/PROPIR, presidencia CDR. |
| Asesoría Jurídica | — | Control legalidad interno; redacción y revisión de actos. |
| Unidad de Control | — | Control preventivo y posterior; dependencia técnica CGR. |
| Oficina de Partes | — | Ingreso formal; número SGDOC; derivación. |
| CDR | Comité Directivo Regional | Filtro estratégico-político pre-evaluación (Jefaturas + Admin.). |
| RTF | Referente Técnico-Financiero | Primera línea de revisión y seguimiento por proyecto. |
| SEREMI MDSF | Min. Desarrollo Social y Familia | Evaluación técnica IDI; otorga RS, AD o FI/OT. |
| DIPRES | Dirección de Presupuestos | Evaluación ex-ante Glosa 06; resol. presupuesto; visa Partida 31. |
| CGR | Contraloría General de la República | Toma de Razón preventiva; fiscalización a posteriori. |
| SIGFE | Sistema de Información Financiera del Estado | Registro contable-presupuestario oficial. |
| BIP | Banco Integrado de Proyectos | Registro y seguimiento de IDI en SNI. |
| FEA | Firma Electrónica Avanzada | Sustituye firma manuscrita; valida actos electrónicos. |
| SNI | Sistema Nacional de Inversiones | Marco de evaluación técnico-económica de proyectos. |
| IDI | Iniciativa de Inversión | IPR de capital (obras, activos); sujeta a evaluación SNI. |
| RS | Recomendación Satisfactoria | Resultado favorable evaluación MDSF para IDI. |
| RF | Recomendación Favorable | Resultado favorable evaluación DIPRES para programas Glosa 06. |
| AD | Admisible | Resultado favorable MDSF para proyectos de conservación. |
| ERD | Estrategia Regional de Desarrollo | Instrumento estratégico que orienta prioridades regionales. |

## Principios Jurídico-Procedimentales

| Principio | Definición Operacional |
| :--- | :--- |
| **Legalidad** | Actuación exclusiva dentro del ámbito de competencia; actos fuera de competencia son nulos. |
| **Escrituración Electrónica (Ley 21.180)** | Procedimientos 100% electrónicos; papel es excepción; registro en expediente electrónico único. |
| **Impugnabilidad** | Actos sujetos a recursos de reposición y jerárquico según ley. |
| **Probidad y Transparencia** | Conducta funcionaria intachable; primacía interés general; publicidad de fundamentos. |
| **Control Externo (CGR)** | Fiscalización de legalidad y fondos; incluye Toma de Razón preventiva. |

Instrumentos tecnológicos:
- **Expediente Electrónico:** Registro íntegro de actuaciones; garantiza trazabilidad y acceso a interesados (Ley 21.180).
- **FEA:** Sustituye firma manuscrita; otorga validez legal y ejecutoriedad a resoluciones y decretos.

## Flujo General: Resoluciones Exentas y Decretos sin Imputación Presupuestaria

Aplica a: nombramientos, comisiones, reglamentos internos, respuestas ciudadanas.

1. **Iniciación:** Unidad competente elabora borrador con fundamentos de hecho y derecho.
2. **Revisión Jurídica:** Asesoría Jurídica verifica ajuste a normativa y competencias.
3. **V°B° Control Interno:** Unidad de Control verifica conformidad con procedimientos internos.
4. **V°B° Jefatura/Administrador:** Jefatura de División origen visa; luego Administrador/a Regional.
5. **Firma con FEA:** Gobernador/a Regional firma mediante FEA.
6. **Notificación y Archivo:** Notificación a interesados; registro en expediente electrónico (Oficina de Partes).

Advertencia: Exentos de Toma de Razón previa (regla general); sujetos a control posterior CGR.

## Flujo SNI Estándar — IDI Nivel 2 y 3 (Requieren RS)

| Paso | Responsable | Actividades Clave | Resultado |
| :--- | :--- | :--- | :--- |
| 1 | Analista GORE (DIPIR) | Verificar RIS y metodologías SNI; elaborar Acta de Admisibilidad interna. | IDI admisible para envío a MDSF. |
| 2 | Jefatura DIPIR / Gobernador/a | Elaborar y visar oficio a SEREMI MDSF; cadena V°B° interna. | Oficio despachado. |
| 3 | Analista MDSF | Admisibilidad (5 días); Análisis Técnico-Económico/ATE (10 días). | RATE: RS / FI / OT. |
| 4 | Unidad Formuladora / Analista GORE | Si RS: avanza. Si FI/OT: subsanar (máx. 60 días hábiles). | Aprobado Técnicamente (RS). |
| 5 | Jefatura DIPIR | Monitorear BIP; comunicar cartera RS para priorización. | Cartera disponible para financiamiento. |

## Flujos Simplificados SNI

### Proyectos < 5.000 UTM (Exención RS)
- Aprobación técnica radica en GORE (no en MDSF).
- GORE envía "Carta de Responsabilidad" a MDSF declarando ausencia de impedimentos y no fraccionamiento.
- Restricciones: no aplica si hay EIA/CMN, problemas de terreno, fraccionamiento o exclusiones legales.
- Resultado interno: estado `Exento RS`.

### Proyectos de Conservación (Costo ≤ 30% valor reposición)
- MDSF solo verifica clasificación como "Conservación".
- Resultado: RATE `AD` (Admisible); no equivale a RS completo.

### Programas Glosa 06 — Proceso Bifásico DIPRES/SES
1. **Fase Perfil:** GORE envía Formulario de Perfil. DIPRES/SES evalúan pertinencia.
2. **Fase Diseño:** Si perfil aprueba, GORE elabora Formulario de Diseño (Marco Lógico). Revisión iterativa hasta calificación `RF` (Recomendación Favorable).
- RF es requisito obligatorio para financiamiento de programas Glosa 06.

## Flujo: Modificaciones Presupuestarias

### Restricciones Clave 2026 (Partida 31)

| Glosa | Contenido | Condición CORE |
| :--- | :--- | :--- |
| **Glosa 10 (Subt. 31)** | No requiere acuerdo CORE si variación ≤ 10% del costo total aprobado (reajustado). | Excepción |
| **Glosa 11 (Subt. 33)** | Mismo umbral del 10% para arrastres/creaciones. | Excepción |
| **Glosa 14 (Emergencias)** | Traspaso hasta 3% inversión a Subinterior; uso hasta 2% propio. Ejecución sin esperar tramitación total. Informes trimestrales a DIPRES y Comisión Mixta. | Sin CORE |

### Tipología de Modificaciones y Actos Requeridos

| Tipo de Modificación | Descripción | Impacta P31 | Acto Administrativo |
| :--- | :--- | :--- | :--- |
| Reasignación Interna | Movimiento entre subtítulos presupuesto GORE. | No | Resolución GORE |
| Creación IDI FRPD | Asignación desde provisión FRPD (Ítem 33.03) a proyectos. | No | Resolución GORE |
| Suplemento | Aumento presupuesto por mayor aporte fiscal. | Sí | D.S. DIPRES + Resolución GORE |
| Transferencia Externa | Reasignación FNDR a ministerios (consolidable). | Sí | D.S. DIPRES + Resolución GORE |
| Emergencias (3%) | Traspaso fondo emergencia a Subsecretaría Interior. | Sí | D.S. DIPRES + Resolución GORE |

### Instancias de Aprobación

- **CORE:** Regla general para toda alteración del presupuesto de inversión.
- **Excepciones CORE:** Gobernador puede modificar sin acuerdo previo en: aumentos ejecución hasta 10% (máx. 7.000 UTM), emergencias 3% (Glosa 14), reajustes legales, sentencias judiciales, variaciones tipo de cambio.
- Aunque no requieran CORE, siempre exigen:
  1. **Visación DIPRES:** Revisión normativa obligatoria.
  2. **Toma de Razón CGR:** Control preventivo de legalidad; requisito para vigencia y ajuste en SIGFE.

## Flujo: Convenios y Transferencias de Recursos

### Restricciones Normativas 2026

- **Glosa 03 (Inversión):** Prohibido financiar préstamos, gastos en personal, bienes/servicios de consumo, ni constituir/comprar sociedades con fondos de inversión.
- **Art. 07 (Subt. 24 y 33):** Desglose mensual previo a DIPRES como autorización máxima; informes de avance requeridos; no incluye gastos en personal o consumo salvo norma expresa.

### Proceso de Formalización de Convenios

1. **Elaboración:** División técnica redacta borrador (objeto, plazos, productos, cláusulas rendición/restitución).
2. **Revisión Jurídica:** Asesoría Jurídica valida legalidad (concursos, garantías en privados). DAF valida cláusulas financieras.
3. **Suscripción:** Firma de Gobernador/a y Representante Legal de entidad receptora.
4. **Aprobación y CGR:** Resolución aprobatoria; remisión obligatoria a CGR para Toma de Razón.

Advertencia: Prohibido realizar transferencias sin Toma de Razón previa de la resolución aprobatoria.

## Reglas de Devengo por Tipo de Transferencia

| Tipo Receptor | Subtítulo | Momento de Devengo |
| :--- | :--- | :--- |
| Sector Privado | S24-01 / S33-01 | Cuando obligación es exigible según convenio. |
| Municipios | S24-02 / S33-02 | Cuando obligación es exigible (acto/convenio tramitado). |
| Servicios Públicos (no consolidables) | S24-03 / S33-03 | Al aprobarse la rendición de cuentas. |
| Servicios Públicos (consolidables) | S24-03 / S33-03 | Cuando obligación es exigible conforme al convenio. |

## Conclusiones Estructurales

- **Proporcionalidad:** Rutas diferenciadas según riesgo, monto y naturaleza; controles exhaustivos reservados para mayor impacto fiscal.
- **Gobernanza de Control Dual:** Filtros internos (División/CORE/Gobernador) y externos (MDSF/DIPRES/CGR) actúan como compuertas obligatorias.
- **Hito Crítico:** Toma de Razón CGR es el principal garante del erario público previo al desembolso.
- **Trazabilidad:** Todo acto queda registrado en expediente electrónico único (Ley 21.180) con FEA del Gobernador/a.
