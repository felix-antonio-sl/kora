---
_manifest:
  urn: urn:agengai:kb:00-fundamentos-previos
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '00'
- fundamentos
- previos
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:00-fundamentos-previos
---

# Capítulo 0 — Fundamentos Previos

> **Propósito:** Si vas a leer un manual sobre agentes IA autónomos, necesitas tener claros los conceptos que el manual asume que ya sabes. Este capítulo es el "curso de nivelación" — los fundamentos de arquitectura de software, IA, y operaciones que hacen el resto del manual absorbible.

- ---

## 0.1 Modelos de Lenguaje (LLMs): La Pieza Central

### Qué es un LLM

- Un Large Language Model es una red neuronal entrenada para predecir la siguiente secuencia de tokens dado un contexto.
- En la práctica:

```
[Instrucciones del sistema + historial de conversación + tu mensaje]
 │
 ▼
 LLM API
 │
 ▼
 [Respuesta generada]
```

- No "piensa" como un humano.
- No "sabe" cosas.
- Genera texto estadísticamente coherente basado en patrones aprendidos durante el entrenamiento.
- Pero lo hace tan bien que puede razonar, planificar, escribir código, y usar herramientas.

### Lo que importa para agentes

| Concepto | Qué es | Por qué importa |
|----------|--------|-----------------|
| **Context window** | Cantidad máxima de tokens que el modelo puede "ver" simultáneamente | Limita cuánta conversación + instrucciones caben en un turno |
| **Tokens** | Unidades de texto (~4 chars en inglés, ~3 en español). No son palabras ni caracteres | Todo se mide en tokens: costo, límites, velocidad |
| **System prompt** | Instrucciones que van al principio del contexto, antes de cualquier mensaje | Define quién es el agente, cómo se comporta, qué puede hacer |
| **Temperature** | Control de aleatoriedad (0 = determinístico, 1 = creativo) | Agentes usan temp baja para consistencia |
| **Streaming** | Enviar tokens uno a uno conforme se generan | UX: el usuario ve la respuesta en tiempo real, no espera al final |
| **Tool use / Function calling** | El modelo puede pedir ejecutar funciones (leer archivos, correr comandos, buscar web) | **Esto es lo que convierte un chatbot en un agente** |

### Proveedores y modelos

```
Provider = la empresa/API que hospeda el modelo
Model = el modelo específico

Ejemplos:
 anthropic/claude-sonnet-4-6 ← Provider: Anthropic, Model: Claude Sonnet 4.6
 openai-codex/gpt-5.2 ← Provider: OpenAI Codex, Model: GPT 5.2
 moonshot/kimi-k2.5 ← Provider: Moonshot, Model: Kimi K2.5
```

- Un agente puede usar diferentes modelos para diferentes tareas (barato para checks, caro para análisis profundo).

### Prompt caching

- Los providers modernos cachean el prompt si no cambia entre llamadas:

```
Turn 1: [System prompt + msg 1] → cache MISS ($$$)
Turn 2: [System prompt + msg 1 + msg 2] → cache HIT para el prefix ($$)
Turn 3: [System prompt + msg 1 + msg 2 + 3] → cache HIT para más prefix ($)
```

- **Implicación:** Mantener el system prompt estable entre turns reduce costos.
- Si cambias algo al principio, invalidas todo el cache.

- ---

## 0.2 Tool Use: De Chatbot a Agente

### La diferencia fundamental

```
CHATBOT:
 Usuario: "¿Qué hora es?"
 Bot: "No tengo acceso a la hora actual."

AGENTE:
 Usuario: "¿Qué hora es?"
 Agente: [tool_call: exec("date")] → "Thu Feb 20 22:30:00 UTC 2026"
 Agente: "Son las 22:30 UTC."
```

- El modelo no ejecuta nada. **Pide** al runtime que ejecute.
- El runtime (gateway, en OpenClaw) ejecuta y devuelve el resultado.
- El modelo ve el resultado y decide qué hacer después.

### El loop agente

```
 ┌──────────────────────┐
 │ │
 ▼ │
User message → Model inference → ¿Tool call?
 │ │
 │ SÍ → Execute tool
 │ │ │
 │ │ ▼
 │ │ Tool result
 │ │ │
 │ └─────┘
 │
 NO → Respuesta final al usuario
```

- Este loop puede iterar muchas veces: el modelo puede hacer 5, 10, 20 tool calls antes de dar una respuesta.
- Cada iteración consume tokens.

### Tipos de tools comunes

| Tool | Qué hace | Riesgo |
|------|---------|--------|
| `read` | Lee archivos | Bajo (solo lectura) |
| `write` | Escribe archivos | Medio (puede sobreescribir) |
| `exec` | Ejecuta comandos shell | **Alto** (puede hacer cualquier cosa) |
| `browser` | Navega la web con un browser real | Alto (sesiones logueadas) |
| `web_search` | Busca en la web | Bajo |
| `message` | Envía mensajes a canales | Medio (acción externa) |

- **El poder del agente viene de los tools.
- El riesgo también.**

- ---

## 0.3 Arquitectura Cliente-Servidor y APIs

### El patrón básico

```
Cliente ──── request ────► Servidor ──── request ────► Servicio externo
 ◄─── response ─── ◄─── response ───
```

- En OpenClaw:

- **Cliente:** Tu teléfono (Telegram), tu laptop (CLI, browser), un script
- **Servidor:** El gateway OpenClaw
- **Servicios externos:** APIs de LLM (Anthropic, OpenAI), servicios web, bases de datos

### HTTP y REST

```
POST /hooks/agent HTTP/1.1 ← Método + Path
Host: localhost:18789 ← Dónde
Authorization: Bearer SECRET ← Quién eres
Content-Type: application/json ← Formato del body

{"message": "Analiza esto"} ← Payload
```

- Los webhooks de OpenClaw son HTTP POST.
- Si entiendes "hago un POST con un JSON a una URL y me devuelve una respuesta", entiendes webhooks.

### WebSocket

- HTTP es request-response.
- WebSocket es una **conexión persistente bidireccional**:

```
HTTP: Cliente → request → Server → response (cierra)
WebSocket: Cliente ←→ Server (abierto permanentemente, ambos envían cuando quieren)
```

- OpenClaw usa WebSocket para la comunicación en tiempo real: streaming de tokens, typing indicators, eventos de sesión.
- Los canales de mensajería (Telegram, WhatsApp) usan sus propios protocolos pero el gateway los normaliza.

### Autenticación

```
Token = string secreto que prueba tu identidad

"Bearer sk-ant-abc123..." ← Token en un header HTTP
```

- Si alguien tiene tu token, puede hacer lo mismo que tú.
- Por eso:

- Tokens largos (>32 chars) y aleatorios
- Nunca en URLs (se cachean/loguean)
- Diferentes tokens para diferentes propósitos (gateway ≠ webhooks ≠ API keys)

- ---

## 0.4 Containers y Docker

### El problema

```
"En mi máquina funciona" → "En el servidor no"
```

- Diferentes versiones de librerías, paths, configuraciones, permisos.
- Un programa que funciona en tu laptop puede fallar en un servidor.

### La solución: containers

- Un container es un **paquete que incluye todo lo que necesita para correr**: código, runtime, librerías, config.
- Siempre corre igual, en cualquier host que tenga Docker.

```
┌─────────────────────────────────────────┐
│ HOST (tu servidor) │
│ │
│ ┌────────────┐ ┌────────────┐ │
│ │ Container A │ │ Container B │ │
│ │ │ │ │ │
│ │ Node.js │ │ Python │ │
│ │ OpenClaw │ │ Flask │ │
│ │ Puerto 18789│ │ Puerto 5000 │ │
│ └────────────┘ └────────────┘ │
│ │
│ Docker Engine │
│ Linux Kernel │
└─────────────────────────────────────────┘
```

### Conceptos clave de Docker

| Concepto | Qué es | Analogía |
|----------|--------|---------|
| **Image** | Template read-only para crear containers | Molde de galleta |
| **Container** | Instancia running de una image | La galleta |
| **Volume** | Disco persistente que sobrevive al container | USB que puedes conectar/desconectar |
| **Network** | Red virtual entre containers | LAN privada |
| **Bind mount** | Carpeta del host montada dentro del container | "Esta carpeta de afuera es visible adentro" |
| **Docker Compose** | Archivo YAML que define múltiples containers + networks + volumes | "El plano de toda la infraestructura" |

### Docker Compose básico

```yaml
version: "3.8"
services:
 mi-app:
 image: node:22
 ports:
 - "8080:8080" # host:container
 volumes:
 - ./data:/app/data # bind mount
 - app-storage:/app/db # named volume
 environment:
 - API_KEY=${API_KEY} # variable de entorno
 networks:
 - mi-red

networks:
 mi-red:
 driver: bridge

volumes:
 app-storage:
```

```bash
docker compose up -d # levantar todo en background
docker compose logs -f # ver logs en vivo
docker compose stop # parar todo
docker compose down # parar + eliminar containers (volumes persisten)
```

### Para OpenClaw

- OpenClaw puede correr:

1. **Nativo** (Node.js directo en el host) — más simple, acceso total al sistema
2. **En Docker** (gateway en container) — aislamiento, portabilidad
3. **Nativo + Docker sandbox** (gateway en host, tools en containers) — el patrón más común

- ---

## 0.5 Networking Básico

### Puertos

```
IP:Puerto = dirección completa de un servicio

127.0.0.1:18789 → localhost, puerto 18789 (solo accesible desde la misma máquina)
0.0.0.0:18789 → todas las interfaces (accesible desde la red)
```

- Un programa "escucha" en un puerto.
- Si dos programas intentan usar el mismo puerto → conflicto.

### Loopback (127.0.0.1) vs LAN vs Internet

```
127.0.0.1 (loopback) → Solo yo puedo acceder
10.x.x.x / 192.168.x → Mi red local puede acceder
0.0.0.0 (todas) → Cualquiera que pueda llegar a mi IP
```

- **Seguridad:** Si un servicio no necesita ser accesible desde fuera, debe escuchar en loopback.
- Siempre.

### VPN y Tailscale

```
Internet público: cualquiera puede ver tu IP + puerto
VPN (Tailscale): red privada virtual, solo miembros de tu tailnet
```

- Tailscale crea una red mesh privada.
- Tu servidor y tu laptop se ven entre sí con IPs privadas (100.x.x.x) sin exponer puertos a internet.

- **Tailscale Serve:** Expone un servicio de tu máquina a otros dispositivos de tu tailnet. **Tailscale Funnel:** Expone un servicio a internet público via un dominio Tailscale (decisión deliberada).

### DNS y resolución de nombres

```
korax-gateway → 172.18.0.2 (dentro de Docker network)
google.com → 142.250.x.x (DNS público)
```

- Dentro de una red Docker, los containers se resuelven por nombre de servicio.
- No necesitas IPs.

- ---
