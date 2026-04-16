# USER.md — Korvo (Félix)

*urn:korvo:agent-bootstrap:korax-user:2.0.0*

## Identidad

- **Nombre completo:** Félix Antonio Sanhueza Luna
- **Tratamiento interno:** Korvo
- **Nacimiento:** 1981
- **Ubicación:** Chillán, Región de Ñuble, Chile
- **Idioma:** Español nativo (es-CL)
- **Timezone:** Chile (UTC-3 / UTC-4 según horario)
- **Estado civil:** Casado con Claudia (Clau)

## Formación

| Programa | Institución | Año |
| --- | --- | --- |
| Médico Cirujano | Universidad de Concepción | 2006 |
| Formación Psiquiatría Infantil | UdeC (énfasis PTSD, salud mental comunitaria) | — |
| Especialidad Salud Pública | Superintendencia de Salud | 2023 |
| Magíster Gestión en Salud | Universidad del Desarrollo | 2023 |
| Diplomado Inteligencia Artificial | PUCV (93h) | 2024 |

## Roles profesionales

### GORE Ñuble — Departamento de Gestión Institucional
- Sistemas, modelamiento institucional, optimización e inteligización de procesos
- **Éxito:** mejora operativa medible, estandarización, trazabilidad, gobernanza + ejecución

### Hospital de San Carlos — Médico de Urgencias
- Atención de urgencias, síntesis clínica, documentación
- **Éxito:** decisiones clínicas seguras y documentadas

## Contextos GTD

| Contexto | Descripción | Cuándo aplica |
|---|---|---|
| @trabajo | Tareas del GORE Ñuble | Horario laboral, oficina |
| @hospital | Tareas relacionadas con hospital | Contexto hospitalario |
| @casa | Tareas domésticas y personales | Fuera de horario laboral |
| @digital | Tareas ejecutables desde cualquier dispositivo | Siempre disponible |
| @llamada | Tareas que requieren coordinación telefónica | Disponibilidad de interlocutor |
| @korax | Tareas de mantenimiento del sistema PCA | Sesión con el agente |

## Dominios de Vida

| Dominio | Alcance | Señales de entrada |
| --- | --- | --- |
| salud | Bienestar físico/mental, hábitos, rutinas, sueño, ejercicio | bienestar, dormir, ejercicio, médico, estrés, energía |
| finanzas | Presupuesto, gastos, ahorro, inversiones | dinero, ahorro, gasto, inversión, presupuesto |
| metas | OKRs personales, proyectos vitales, deadlines | meta, objetivo, proyecto, deadline |
| aprendizaje | Skills, cursos, libros, conocimiento | aprender, curso, libro, skill |
| relaciones | Contactos, networking, fechas importantes | contacto, relación, reunión, networking |

## Umbrales de Salud del Sistema

| Métrica | Rango Saludable | Señal de Problema | Acción |
|---|---|---|---|
| Items en buffer | 0-30 | >30 | Sugerir triaje urgente o bancarrota |
| Waiting >5 días | 0-2 | ≥3 | Alertar en micro-check diario |
| Compromisos >14d sin actividad | 0-3 | ≥5 | Candidatos a bancarrota en /sync |
| Bloques DEEP/semana | ≥2 | 0-1 | Alertar déficit de tiempo profundo |
| Balance throughput (14d) | ≥0 | <0 por >4 semanas | Alertar acumulación de deuda |
| Días sin triaje | 0-2 | ≥3 | Activar protocolo de abandono |
| Señales de colapso | 0-1 | ≥3 | Activar modo emergencia |
| Horas Modo Caos/semana | ≥2 | 0 | Recordar protección de caos |
| Tiempo en sistema | <10% | >10% | Simplificar (P1) |

## Rutina semanal

| Día | Patrón |
| --- | --- |
| Lun | GORE día completo |
| Mar | GORE día completo, trabajo nocturno hasta 02:00 |
| Mié | Turno hospital 08-20h |
| Jue | GORE media tarde, patrón similar martes |
| Vie | GORE día, turno 20-08h |
| Sáb | Sueño no reparatorio, visita padres o suegros |
| Dom | Actividad familiar mañana, tarde familia o amigas |

## Perfil cognitivo (FPM)

**Fortalezas:** Abstracción conceptual (S+), reconocimiento de patrones (S), pensamiento crítico (S), flexibilidad cognitiva (S), metacognición (S), sentido de agencia (S), persistencia (S)

**Limitaciones:**
- Memoria de trabajo (N-: 25/100) → Korax recuerda, rastrea, resume
- Meticulosidad (N-: 25/100) → Korax verifica detalles, checklists
- Tolerancia al error (B: 20/100) → Korax revisa antes de entregar
- Atención sostenida (N: 40/100) → ciclos todo-o-nada

**Intervenciones que funcionan:** checklist mínimo, división en microtareas, reencuadre por evidencia, pausa breve estructurada

**Intervenciones que fallan:** motivación abstracta, presión sin estructura, sobrecarga informativa

## Comunicación

- **Tono:** directo, serio, semiformal
- **Formatos preferidos:** listas, headings, Markdown, YAML/JSON, Mermaid
- **Evitar siempre:** relleno, adornos, condescendencia, placeholders, explicar basics sin que se pida
- **Challenge style:** preguntas críticas, contraargumentos, verificación — Korvo quiere ser desafiado
