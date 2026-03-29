# Deploy — steipete en el gateway de clawforge

## Que es

`steipete` es un agente de ingenieria de software agentico que se agrega como segundo agente al gateway OpenClaw donde ya corre `clawforge`. Comparten el mismo Gateway daemon pero tienen workspaces, sesiones y canales completamente aislados.

## Pre-requisitos

- Gateway de clawforge corriendo y saludable (`openclaw health` OK)
- Node.js 24+ (o 22.14+ minimo)
- Bot de Telegram independiente para steipete (crear en @BotFather)

## Estructura de este paquete

```
steipete-host-native/
├── DEPLOY.md              ← esta guia
├── config/
│   └── openclaw-delta.json  ← patch a aplicar sobre openclaw.json existente
└── workspace/
    ├── IDENTITY.md
    ├── SOUL.md
    ├── AGENTS.md
    ├── TOOLS.md
    └── skills/
        ├── blast-radius-estimator/SKILL.md
        ├── loop-closer/SKILL.md
        ├── repo-architect/SKILL.md
        ├── context-hygiene/SKILL.md
        └── tooling-craftsman/SKILL.md
```

## Deploy en el servidor

### 1. Copiar workspace

```bash
cp -a workspace/ ~/.openclaw/workspace-steipete/
```

### 2. Agregar credenciales del bot

```bash
# Agregar al ~/.openclaw/.env existente:
echo "TELEGRAM_BOT_TOKEN_STEIPETE=<token-del-bot-steipete>" >> ~/.openclaw/.env
```

### 3. Registrar el agente

```bash
openclaw agents add steipete --workspace ~/.openclaw/workspace-steipete
```

### 4. Parchear openclaw.json

El archivo `config/openclaw-delta.json` contiene el delta a aplicar. Editar `~/.openclaw/openclaw.json` manualmente o con el comando config:

**Opcion A — edicion manual (recomendada para la primera vez):**

```bash
# Ver config actual
openclaw config file

# Abrir y agregar:
# - en agents.list: el entry de steipete (ver openclaw-delta.json)
# - en channels.telegram.accounts: la cuenta steipete (ver openclaw-delta.json)
```

**Opcion B — via CLI:**

```bash
# Registrar bot de steipete (si openclaw soporta multi-account telegram)
openclaw channels add telegram --agent steipete --token "$TELEGRAM_BOT_TOKEN_STEIPETE"
```

Reemplazar placeholders en la config:

| Placeholder | Valor |
|---|---|
| `__REPLACE_TELEGRAM_BOT_TOKEN_STEIPETE__` | Token del bot de steipete (@BotFather) |
| `__TELEGRAM_USER_ID__` | Mismo ID numerico del operador (igual que en clawforge) |

### 5. Validar config

```bash
openclaw config validate
```

### 6. Reiniciar gateway

```bash
openclaw gateway restart
```

### 7. Verificar

```bash
openclaw doctor
openclaw agents list
openclaw skills list --agent steipete
openclaw channels list
```

Resultado esperado:
- `openclaw agents list` muestra `clawforge` (default) y `steipete`
- `openclaw skills list --agent steipete` muestra 5 skills
- Canal telegram de steipete aparece conectado

### 8. Prueba de humo

Enviar mensaje al bot de steipete en Telegram. El agente debe responder con su persona `steipete` (directo, anti-bullshit, orientado a ingenieria).

## Notas de routing

El gateway rutea mensajes al agente correcto por `accountId` en `channels.telegram`:
- Mensajes al bot de **clawforge** → agente `clawforge`
- Mensajes al bot de **steipete** → agente `steipete`

El routing es determinista. Los dos agentes no interfieren entre si.

## Verificacion de fidelidad

| Prompt de prueba | Respuesta esperada de steipete |
|---|---|
| "Tengo una idea para una feature" | Pide claridad minima, estima blast radius, ejecuta |
| "Organiza este repo" | Audita estructura, propone cambios de menor a mayor blast radius |
| "Deberia usar X o Y para este CLI?" | Respuesta directa con criterio tecnico, sin fence-sitting |
| "Hacer PR, tests, worktrees para cada cambio" | Evalua si el contexto justifica esa ceremonia; rechaza si es solo-dev |

## Upgrade

```bash
# steipete hereda el upgrade del gateway compartido
npm update -g openclaw
openclaw gateway restart
openclaw doctor
```

## Agregar USER.md (opcional pero recomendado)

```bash
cat > ~/.openclaw/workspace-steipete/USER.md << 'EOF'
## Perfil del operador

- Rol: ingenieria / producto
- Experiencia con agentes: alta
- Preferencia de idioma: es-CL
- Foco actual: [describir proyecto o contexto actual]
EOF
```
