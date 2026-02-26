---
_manifest:
  urn: "urn:korvo:agent-bootstrap:korax-user:2.0.0"
  type: "bootstrap_user"
---

## Perfil

- **Nombre:** Felix Sanhueza
- **Nombre operativo:** Korvo
- **Rol:** Funcionario GORE Ñuble / Hospital. Líder técnico, profesional multidisciplinario.
- **Ubicación:** Santiago timezone (America/Santiago, UTC-3/UTC-4)
- **Contexto organizacional:** Gobierno Regional, sector público, coordinación interinstitucional

## Contextos GTD

| Contexto | Descripción | Cuándo aplica |
| --- | --- | --- |
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
| relaciones | Contactos, networking, relaciones, fechas importantes | contacto, relación, reunión, networking |

## Rutinas

| Rutina | Horario | Frecuencia | Trigger |
| --- | --- | --- | --- |
| Triaje vespertino | 21:00 | Diario | Recordado por CM-CLOSE. Operador inicia con `/triaje`. |
| Planificación matutina | 08:00 | L-V | heartbeat_morning / `/plan` |
| Cierre nocturno | 21:00 | Diario | heartbeat_evening |
| Sincronización estratégica | Viernes 20:00 | Quincenal (semanas impares) | heartbeat_sync / `/sync` |
| Modo Caos | Libre | Mínimo 2h/semana (INV-11) | `/caos` |

## Umbrales de Salud del Sistema

| Métrica | Rango Saludable | Señal de Problema | Acción |
| --- | --- | --- | --- |
| Items en buffer | 0-30 | >30 | Sugerir triaje urgente o bancarrota |
| Waiting >5 días | 0-2 | ≥3 | Alertar en micro-check diario |
| Compromisos >14d sin actividad | 0-3 | ≥5 | Candidatos a bancarrota en /sync |
| Bloques DEEP/semana | ≥2 | 0-1 | Alertar déficit de tiempo profundo |
| Balance throughput (14d) | ≥0 | <0 por >4 semanas | Alertar acumulación de deuda |
| Días sin triaje | 0-2 | ≥3 | Activar protocolo de abandono |
| Señales de colapso | 0-1 | ≥3 | Activar modo emergencia |
| Horas Modo Caos/semana | ≥2 | 0 | Recordar protección de caos |
| Tiempo en sistema | <10% | >10% | Simplificar (P1) |

## Preferencias de Output

- **Formato:** Markdown con emojis funcionales (📥 captura, ✅ completado, ⚠️ alerta, 🛑 colapso, 🌀 caos)
- **Detalle:** Mínimo viable. Datos > prosa.
- **Confirmaciones:** Una línea. Sin elaboración.
- **Reportes:** Tablas y conteos. Sin narrativa.
- **Asesoría:** Perspectivas con curiosidad. Listas cortas y accionables.
