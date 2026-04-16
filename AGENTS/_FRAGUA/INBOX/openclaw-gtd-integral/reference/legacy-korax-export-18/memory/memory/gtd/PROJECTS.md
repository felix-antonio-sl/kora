# Projects

Proyectos activos (>1 acción para completar).

---

## Trabajo (GORE Ñuble)

### Transformación Digital / GoreOS
- **Estado:** En progreso
- **Next:** Definir 3 historias de usuario prioritarias para GoreOS (derivar de ERD 2024-2030)
- **Bloqueo:** Falta priorización clara desde ERD 2024-2030

#### Ontología y modelo de datos
- [ ] Roadmap de madurez del modelo ontológico GoreOS (ontología básica → extendida → GORE → modelo datos → contra realidad → formalización categorial → implementación)
- [ ] Iterar ontología v3 hacia formalización BFO (Basic Formal Ontology)
- [ ] Exportar la ontología GoreOS a formato interoperable (OWL? YAML?)
- [ ] Refactorizar y conciliar dominios: plantillas deben albergar dominio conceptual y modelo categorial (incl. Región en D-TERR)
- [ ] Unificar dominio de gestión org con los demás dominios GoreOS

#### User stories y entidades
- [ ] Revisar con detención las historias de usuario — todo parte de ahí
- [ ] Sanear US, sanear procesos, entidades involucradas → mejorar para migración
- [ ] Mejorar entity en su relación agente, competencia, proceso
- [ ] Que cada US genere una spec ejecutable (Historias → Capacidades = specs finales con documentación semántica)
- [ ] Historias de usuario para inventario de sistemas y listado total de funcionarios
- [ ] En GoreOS, un usuario es la combinación de un agente (humano o máquina) con un rol — modelar
- [ ] Auditar relación entre user stories y entidades del modelo

#### IPR (Inversión Pública Regional)
- [ ] Modelamiento y modelo de datos de IPR
- [ ] Reconstruir entidad IPR
- [ ] Auditar entidades artificiales agregadas al modelo IPR que no tienen sustancia real
- [ ] Verificar si IniciativaInversion o ConvenioTransferencia ya existen en el modelo
- [ ] Revisar métricas de inversión regional: https://x.com/clawdbot/status/2015265005210353824 (rate IDI y PPR)

#### SIGFE y finanzas GORE
- [ ] Continuar modelamiento SIGFE desde diagramas Mermaid existentes (revisar mermaid → solventar → expandir → BFO)
- [ ] Las rendiciones de convenios son solo datos extra sobre la entidad principal — modelar correctamente
- [ ] Gestión financiera convenios GORE (8% administración) — convenios a fin de año + devengo
- [ ] Implementar Slim Para Titi (D-FIN): paridad funcional + OCR resoluciones

#### Infraestructura y migración
- [ ] Generar base de datos (Drizzle/PostGIS) e infraestructura Hetzner en servidor dedicado
- [ ] Migración de datos legacy: funcionarios, inventario de sistemas
- [ ] Auditoría y gestión de actores: identificar usuarios, roles y actores externos. Definir dominio Admin

#### Estrategia y gestión
- [ ] Revisión general del estado del proyecto GoreOS
- [ ] Alinear GoreOS con Ley de Transformación Digital del Estado (adecuación normativa)
- [ ] DGI — coordinar reunión con Alejandro
- [ ] Stack metodológico para DGI: Wisluth, arquitectura organizacional, lean six sigma y AI con humano en centro
- [ ] ¿Existe un modelo de arquitectura organizacional sin formalizar? verificar
- [ ] Estrategia de change management para GoreOS (habilitación y adopción)
- [ ] ¿Cuándo parten los concursos? (¿públicos GORE? ¿ADP?) — aclarar contexto
- [ ] Buscar dictámenes CGR sobre Ñuble, ref 250, persona: María Antonieta

### Skill GoreOS para Korax
- **Estado:** Nuevo — capturado 2026-02-03
- **Next:** Definir alcance y funcionalidades de la skill
- **Objetivo:** Skill custom que encapsule conocimiento GoreOS para consultar/modificar

### Resolución 30 + Manuales (Nicolás)
- **Estado:** En progreso — capturado 2026-02-28
- [ ] Terminar avances resolución 30 y manuales
- [ ] Actualizar todo lo de Nicolás: añadir lo que falta + rendición 30 + revisar manuales
- [ ] Coordinar con Nicolás Lara sobre 10 monitores

---

## Personal

### Sistema Korvo-Korax
- **Estado:** En progreso — gran avance 2026-02-22
- **Logros:** Nodo "air" (Mac) paired+connected via launchd ✅, DAU/SIAU + SGH mapeados y con escritura ✅, dual systemd corregido ✅
- **Next:** Estabilizar reconexión TLS intermitente en "air"; evolucionar capacidades (gmail, calendar)

#### Memoria y contexto
- [ ] Mejorar estrategia de memoria entre Korax (OpenClaw) y Claude Code
- [ ] Memoria vectorial — ¿mejorar embeddings, cambiar provider, tuning?
- [ ] Migrar conocimiento acumulado en ChatGPT, Gemini y notas al workspace

#### Integraciones pendientes
- [ ] Conectar OpenClaw a WhatsApp como canal
- [ ] Integrar TickTick (tareas) con Korax
- [ ] Configurar forwarding de correos a koraxfx@gmail.com
- [ ] Diagnosticar bounces de correo enviado por Korax

#### Tools y skills
- [ ] Definir qué funcionalidades van como tools vs skills en OpenClaw
- [ ] Pipeline de evaluación de skills disponibles (probar, poblar, seleccionar → desarrollar)
- [ ] Auditar skills necesarios vs disponibles
- [ ] Habilitar canvas para dashboards y skill de coding
- [ ] Aprender y usar el sistema de hooks de OpenClaw
- [ ] Que Korax elija modelo según tarea/costo automáticamente (autogestión de modelos)
- [ ] Inventariar qué puede hacer OpenClaw out-of-the-box

#### Agentes y arquitectura
- [ ] Crear agente tipo "visionario" + habilitar Molt (¿otro bot?) — clarificar contexto
- [ ] Darle acceso web a agente Molt
- [ ] Escribir historias de usuario para capacidades de Korax
- [ ] Documentar qué corre sandboxed, qué en Docker, y definir estructura ideal del workspace
- [ ] Configurar múltiples canales Telegram. "V de V" — clarificar concepto

#### Dev environment (Mac)
- [ ] Configurar iTerm para Claude Code
- [ ] Configurar Claude Code para que no pida tanto permiso (--dangerously-skip-permissions o CLAUDE.md con allowlist)
- [ ] Revisar cuándo se generan /init y claude.md automáticamente
- [ ] Instalar plugins Claude Code
- [ ] Crear alias shell para lanzar Claude Code
- [ ] Darle acceso al CLI a Korax (invocar CLIs vía exec)
- [ ] Crear cuenta GitHub para el agente Korax

### Korax Autoconocimiento
- **Estado:** Nuevo — nucleo del sistema reflexivo
- **Next:** Implementar lectura automática de ESTADO-SISTEMA.md al iniciar sesión
- **Objetivo:** Capacidad reflexiva completa (saber quién soy, qué puedo hacer, cómo estoy compuesto)

### Grupo de estudio/trabajo con Calderón
- **Estado:** Nuevo — capturado 2026-02-10
- **Next:** Enviar mensaje a Calderón para definir objetivo + formato (estudio/trabajo) + frecuencia
- **Bloqueo:** Falta clarificar alcance/compromiso

---

## Negocio / Sanixai

### Sanixai — plataforma
- **Estado:** En incubación
- [ ] Revisar Stripe en detalle — configurar pagos Sanixai
- [ ] Desplegar app en Dokploy: https://dokploy.sanixai.com/
- [ ] Funcionalidad de documentos compartidos
