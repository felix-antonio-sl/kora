---
_manifest:
  urn: urn:gn:kb:bpmn-d07-rrhh
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: "GORE Ñuble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- rrhh
- bpmn
- gestion-personas
- gn
lang: es
---

# BPMN D07: Gestión de Personas (RRHH)

## Metadatos del Dominio

| Atributo | Valor |
| :--- | :--- |
| ID | DOM-RRHH |
| Criticidad | Alta |
| Dueño | Área de Gestión de Personas |
| Procesos | 7 (P1–P7) |
| Subprocesos | ~20 |

## Mapa General: Ciclo de Vida del Funcionario

P1 Ingreso y Contratación → P2 Inducción → P3 Remuneraciones (núcleo transversal) → P4 Tiempo y Ausentismo / P5 Desarrollo y Capacitación / P6 Bienestar → P7 Egreso.

## P1: Ingreso y Contratación

**Sistemas:** SIGPER, SIAPER.

### Tipos de Contrato

| Tipo | Descripción |
| :--- | :--- |
| Planta | Cargo titular, carrera funcionaria |
| Contrata | Transitorio, renovación anual |
| Honorarios | Servicios específicos, sin vínculo laboral |

### Flujo

**Reclutamiento:**
1. Identificar vacante → elaborar perfil de cargo
2. Publicar llamado en Empleo Público y web GORE
3. Recepción de postulaciones

**Selección:**
4. Filtro curricular → evaluación técnica/psicológica
5. Entrevista Comisión → propuesta de terna
6. Gobernador/a decide

**Contratación:**
7. Oferta formal → aceptación del candidato
8. Resolución de nombramiento → alta en SIGPER y SIAPER
9. Firma contrato/decreto

## P2: Inducción e Integración

**Fases:** 11.

1. Bienvenida institucional → entrega de credencial y accesos
2. Presentación en división/área → asignar mentor/agente inductor
3. Recorrido instalaciones
4. Capacitación: misión/visión, organigrama, sistemas, normativa
5. Entrega de documentos clave → configuración puesto de trabajo
6. Seguimiento 30-60-90 días → evaluación período de prueba

## P3: Remuneraciones y Compensaciones

**Sistemas:** SIGPER, PREVIRED, SIGFE.
**Base:** Escala Única de Sueldos (EUS).

### Componentes de la Remuneración

| Componente | Descripción |
| :--- | :--- |
| Sueldo base | Según grado EUS |
| Asignaciones | Zona, antigüedad, profesional |
| Bonos | PMG, productividad, otros |
| Horas extra | Según normativa |

### Flujo Mensual

1. Recopilar novedades: licencias, horas extra, descuentos
2. Calcular remuneración bruta
3. Aplicar descuentos: previsión, salud, impuestos, otros
4. Generar liquidación → revisión y validación → autorización de pago
5. Pagar PREVIRED (cotizaciones)
6. Transferir a cuentas de funcionarios
7. Contabilizar en SIGFE → archivar liquidaciones

## P4: Tiempo, Asistencia y Ausentismo

### Registro de Asistencia

1. Funcionario marca entrada/salida → sistema registra en reloj control
2. Generar reporte diario

### Permisos

1. Solicitar permiso (administrativo o particular)
2. Jefatura aprueba/rechaza → registrar en sistema

### Licencias Médicas

1. Funcionario presenta licencia médica → RRHH recepciona y valida
2. Enviar a Isapre/COMPIN → resolución (aprobada o rechazada)
3. Ajustar remuneración

### Feriados

1. Solicitar feriado legal/progresivo → verificar saldo disponible
2. Jefatura autoriza → descontar días

## P5: Desarrollo Organizacional y Capacitación

### Flujo

**Detección de Necesidades (DNC):**
1. Aplicar encuesta DNC → análisis de brechas → priorizar necesidades

**Plan de Capacitación (PAC anual):**
2. Elaborar PAC → Comité Bipartito aprueba → asignar presupuesto

**Ejecución:**
3. Convocar funcionarios → ejecutar capacitaciones → evaluar aprendizaje → certificar

**Seguimiento:**
4. Medir transferencia al puesto → evaluar impacto → retroalimentar próximo ciclo

### Calificaciones

**Período:** Septiembre–Agosto.

1. Precalificación por jefatura → notificación al funcionario
2. ¿Apelación?
   - No → Junta Calificadora define nota final
   - Sí → Junta resuelve apelación → define nota final
3. Listas: 1 (Distinción) / 2 (Buena) / 3 (Condicional) / 4 (Regular) / Eliminación
4. Registrar en hoja de vida

## P6: Bienestar y Calidad de Vida

### Afiliación

1. Funcionario ingresa → invitar al Servicio de Bienestar
2. Aceptar y afiliar → descuento mensual por planilla

### Prestaciones

1. Solicitar beneficio: médico, económico, préstamo, convenio
2. Unidad de Bienestar evalúa → Consejo Administrativo aprueba si requiere → otorgar beneficio

### Actividades

1. Planificar eventos: deportivos, recreativos, culturales
2. Ejecutar actividad → evaluar satisfacción

### Prevención de Riesgos

1. Identificar riesgos laborales → elaborar matriz de riesgos → medidas preventivas
2. CPHS monitorea → ¿Accidente?
   - Sí → DIAT/DIEP → Mutual investiga → medidas correctivas
   - No → continuar monitoreo

## P7: Egreso y Desvinculación

### Causales de Egreso

| Causal | Tipo |
| :--- | :--- |
| Renuncia voluntaria | Voluntario |
| Retiro por pensión | Jubilación |
| No renovación 31/12 | Término contrata |
| Eliminación por nota | Calificación lista 4 |
| Destitución | Disciplinario |
| Incompatibilidad de salud | Salud |

### Procedimiento de Cierre

1. Resolución de cese → entrega de cargo
2. Devolución: credencial, equipos, documentos
3. Cierre de accesos: TI, edificio
4. Certificado de servicios
5. Liquidación final: feriados pendientes, bonos proporcionales
6. Baja en SIGPER y SIAPER

## Sistemas Involucrados

| Sistema | Función |
| :--- | :--- |
| SYS-SIGPER | Gestión de personas, remuneraciones |
| SYS-SIAPER | Control personal del Estado |
| SYS-PREVIRED | Cotizaciones previsionales |
| SYS-SIGFE | Contabilización |

## Normativa Aplicable

| Norma | Alcance |
| :--- | :--- |
| Ley 18.834 | Estatuto Administrativo |
| Ley 18.575 | Bases Administración del Estado |
| Ley 20.880 | Probidad, declaraciones |
| Código del Trabajo | Honorarios |

## Referencias Cruzadas

| Dominio | Vínculo |
| :--- | :--- |
| D02 Ciclo Presupuestario | Subtítulo 21, Remuneraciones |
| D01 Actos Administrativos | Resoluciones de nombramiento |
