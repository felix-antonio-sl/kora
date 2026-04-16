# HODOM HSC
# Roadmap Ejecutable de Evolución

Versión: 1.4
Fecha: 2026-04-09
Estado: roadmap operativo inicial

Base:
- `opm-hodom-hsc-backlog-arquitectonico-v1.3.md`
- `opm-hodom-hsc-canonico-local-v1.0.md`
- `opm-hodom-hsc-gap-analysis-v1.2.md`

Objetivo: traducir el backlog arquitectónico a un plan ejecutable por fases, integrando:
- proceso,
- software,
- datos,
- gobernanza,
- gestión del cambio.

---

## 1. Principio rector

La evolución de HODOM HSC no debe perseguir solo “más digitalización”.

Debe perseguir tres resultados acoplados:
1. más coherencia clínica,
2. más control operacional,
3. más gobernabilidad directiva.

Por eso cada fase se diseña en 4 planos simultáneos:
- **proceso**,
- **datos**,
- **software**,
- **adopción/gobierno**.

---

## 2. Visión de resultado a 3 fases

### Fase I — Columna vertebral semántica
Resultado: el sistema gana estructura.

### Fase II — Gobierno en tiempo real
Resultado: el sistema gana visibilidad y capacidad de conducción.

### Fase III — Continuidad ampliada
Resultado: el sistema extiende mejor el cuidado hacia red, cuidador y post-egreso.

---

# 3. Fase I — Columna vertebral semántica

Horizonte sugerido: 4 a 8 semanas

## 3.1 Objetivos

1. Crear objeto fuerte **Plan de Atención**
2. Formalizar **máquina de estados del episodio**
3. Introducir **categoría de riesgo** explícita

---

## 3.2 Entregables por plano

### A. Proceso
- Definición canónica de Plan de Atención
- Definición de estados del episodio
- Definición operativa de riesgo clínico
- Reglas mínimas de transición entre estados

### B. Datos
- tabla o vista canónica de Plan de Atención
- catálogo de estados de episodio
- campo/objeto de riesgo clínico por episodio
- trazabilidad básica de versión del plan

### C. Software
- bloque “Plan actual” visible en ficha
- estado del episodio visible en ficha/censo/admisión/egreso
- riesgo visible en censo/ficha/agenda
- filtros básicos por estado y riesgo

### D. Adopción y gobierno
- mini-glosario operativo para equipo clínico y coordinación
- criterio único de uso de estados
- criterio único de asignación de riesgo
- validación con 3 a 5 casos reales

---

## 3.3 Historias de implementación sugeridas

### I-01 — Plan actual visible
Como equipo clínico y de coordinación,
quiero ver un bloque único de plan actual por episodio,
para no coordinarme por fragmentos dispersos.

### I-02 — Estado de episodio unificado
Como sistema HODOM,
quiero que cada episodio tenga un estado canónico visible,
para evitar ambigüedad entre postulaciones, ingresos, actividad y cierre.

### I-03 — Riesgo clínico operacionalizado
Como coordinación,
quiero ver la categoría de riesgo de cada episodio,
para priorizar mejor visitas, seguimiento y escalamiento.

---

## 3.4 Criterios de éxito de Fase I

- 90% de episodios activos con plan visible
- estado canónico del episodio presente en todas las superficies críticas
- categoría de riesgo visible al menos en censo y ficha
- reducción de ambigüedad en coordinación diaria

---

## 3.5 Riesgos

- querer hacer un plan demasiado sofisticado antes de estabilizar el objeto
- pelear por taxonomías excesivas de riesgo
- no validar con casos reales antes de desplegar

---

# 4. Fase II — Gobierno en tiempo real

Horizonte sugerido: 6 a 10 semanas posteriores o parcialmente solapadas con Fase I

## 4.1 Objetivos

1. Crear **cockpit directivo HODOM**
2. Unificar **Comunicación Clínica**
3. Formalizar **Capacidad Operativa Disponible**

---

## 4.2 Entregables por plano

### A. Proceso
- mapa único de decisión directiva
- definición de evento de comunicación clínica
- definición de capacidad operativa disponible
- reglas de escalamiento y excepción

### B. Datos
- objeto/evento canónico de comunicación
- vista consolidada de capacidad operativa
- vista directiva de excepción
- reglas de consistencia REM/cupos/alertas/llamadas

### C. Software
- dashboard directivo unificado
- bandeja o índice de comunicación clínica por episodio
- indicadores de continuidad, presión territorial y quiebre operativo
- alertas priorizadas para DT/coordinación

### D. Adopción y gobierno
- rutina de revisión diaria de cockpit
- rutina de revisión de llamadas críticas
- rutina de revisión de presión de cupos/carga territorial
- criterio único para resolver remoto / visita / derivación urgente

---

## 4.3 Historias de implementación sugeridas

### II-01 — Cockpit directivo único
Como Director Técnico o Coordinación,
quiero una sola vista con ocupación, riesgo, continuidad, llamadas críticas y consistencia,
para dirigir la unidad sin navegar por cinco módulos.

### II-02 — Evento de comunicación clínica
Como sistema,
quiero tratar llamadas, mensajes y comunicaciones relevantes como eventos estructurados,
para tener trazabilidad clínica real y no solo narrativa dispersa.

### II-03 — Capacidad operativa disponible
Como coordinación,
quiero ver la capacidad disponible real,
para decidir admisiones y cargas de agenda de forma segura.

---

## 4.4 Criterios de éxito de Fase II

- existencia de cockpit operativo usado diariamente
- llamadas críticas trazadas con resultado estructurado
- capacidad operativa disponible visible y accionable
- menos navegación fragmentada para decisiones de coordinación

---

## 4.5 Riesgos

- hacer dashboard lindo pero poco accionable
- no definir responsable claro de calidad de datos
- mezclar comunicación administrativa y clínica sin distinción útil

---

# 5. Fase III — Continuidad ampliada

Horizonte sugerido: 6 a 10 semanas posteriores

## 5.1 Objetivos

1. Hacer explícito el **seguimiento post-egreso**
2. Integrar mejor **portal paciente/cuidador** al canon principal
3. Incorporar **knowledge-in-the-loop**

---

## 5.2 Entregables por plano

### A. Proceso
- workflow post-egreso explícito
- integración del cuidador como nodo activo de continuidad
- puntos del proceso donde el conocimiento debe emerger contextualizado

### B. Datos
- objeto de seguimiento post-egreso
- objeto de mensaje/solicitud desde portal con vínculo a episodio
- eventos de continuidad APS/contrarreferencia
- registro de documento de emergencia y uso

### C. Software
- checklist post-egreso estructurado
- seguimiento programado
- integración portal ↔ comunicación clínica
- guías contextuales en llamadas, egreso, semáforo clínico, continuidad

### D. Adopción y gobierno
- protocolo de seguimiento temprano
- protocolo de contrarreferencia con APS
- protocolo de educación y uso del portal
- revisión de desenlaces tempranos post-egreso

---

## 5.3 Historias de implementación sugeridas

### III-01 — Seguimiento post-egreso estructurado
Como equipo HODOM,
quiero que cada egreso deje programado su seguimiento mínimo,
para no perder continuidad ni aprendizaje.

### III-02 — Cuidador como nodo activo
Como sistema,
quiero integrar mejor al cuidador mediante portal, indicaciones y comunicación estructurada,
para sostener el cuidado fuera de la visita.

### III-03 — Conocimiento contextual
Como profesional,
quiero que las guías aparezcan en el punto del proceso donde las necesito,
para reducir fricción y variabilidad.

---

## 5.4 Criterios de éxito de Fase III

- seguimiento post-egreso visible y trazado
- portal deja de ser satélite y se integra al flujo principal
- menor pérdida de continuidad informacional
- mejor soporte al cuidador y a decisiones frecuentes

---

## 5.5 Riesgos

- sobrecargar al cuidador con funciones sin soporte suficiente
- construir portal sin integrarlo al resto de la semántica del sistema
- convertir conocimiento en biblioteca estática en vez de ayuda contextual

---

# 6. Roadmap resumido por iniciativa

| Iniciativa | Fase | Resultado principal |
|------------|------|--------------------|
| Plan de Atención | I | columna vertebral clínica |
| Estados del episodio | I | consistencia end-to-end |
| Riesgo clínico | I | priorización operativa |
| Cockpit directivo | II | gobierno en tiempo real |
| Comunicación clínica unificada | II | continuidad y trazabilidad |
| Capacidad operativa disponible | II | decisiones de admisión y carga más seguras |
| Seguimiento post-egreso | III | continuidad ampliada |
| Integración portal | III | cuidador y paciente como nodos activos |
| Knowledge-in-the-loop | III | menos fricción y variabilidad |

---

# 7. Dependencias y orden lógico

## Dependencias duras blandas

- El cockpit no necesita esperar a que todo esté perfecto, pero mejora mucho con episodio/riesgo más firmes.
- La comunicación clínica unificada puede empezar por llamadas y luego absorber portal.
- El seguimiento post-egreso gana mucho si comunicación clínica ya está más ordenada.
- El portal debe integrarse después de clarificar mejor comunicación y continuidad.

## Orden lógico recomendado

1. Plan
2. Episodio
3. Riesgo
4. Cockpit
5. Comunicación
6. Capacidad
7. Post-egreso
8. Portal
9. Knowledge-in-the-loop

---

# 8. Gobierno del roadmap

## Comité mínimo sugerido

### Núcleo decisor
- Director Técnico
- Coordinación HODOM
- referente clínico operativo
- referente de producto/sistema

### Rol de este comité
- cerrar semántica antes de construir
- priorizar con criterio clínico-operacional
- revisar adopción, no solo entrega técnica
- proteger coherencia entre módulos

## Cadencia sugerida
- semanal: seguimiento táctico
- quincenal: validación de flujo con casos reales
- mensual: revisión de métricas de impacto

---

# 9. Métricas sugeridas por fase

## Fase I
- % episodios con plan visible
- % episodios con estado canónico correcto
- % episodios con riesgo visible

## Fase II
- tiempo de decisión directiva con cockpit
- % llamadas con resolución estructurada
- % días con capacidad operativa visible

## Fase III
- % egresos con seguimiento programado
- % mensajes portal vinculados a episodio correctamente
- tiempo de respuesta a consultas del cuidador

---

# 10. Veredicto operativo

Este roadmap no es un backlog de features.
Es una secuencia de maduración del sistema.

La apuesta correcta no es crecer caóticamente.
Es consolidar primero la estructura que permite que el crecimiento no rompa la unidad.

Si HODOM HSC hace bien estas tres fases, deja de tener solo una app operativa.
Pasa a tener un sistema clínico-operacional verdaderamente gobernable.
