---
title: Docker Compose Templates
status: internal
lang: es
---

# Docker Compose Templates

## Template: OpenClaw Single Agent

```yaml
services:
  openclaw:
    image: openclaw/openclaw:latest
    restart: unless-stopped
    ports:
      - "127.0.0.1:3000:3000"
    volumes:
      - openclaw-data:/home/openclaw/.openclaw
      - ./workspace:/home/openclaw/.openclaw/workspace
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/healthz"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          memory: 2g
          cpus: "2.0"

volumes:
  openclaw-data:
```

## Template: OpenClaw Multi-Agent Conservador

```yaml
services:
  openclaw:
    image: openclaw/openclaw:latest
    restart: unless-stopped
    ports:
      - "127.0.0.1:3000:3000"
    volumes:
      - openclaw-data:/home/openclaw/.openclaw
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/healthz"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          memory: 4g
          cpus: "4.0"

volumes:
  openclaw-data:
```

## Notas
- Siempre bind a 127.0.0.1, nunca a 0.0.0.0
- No montar `docker.sock` en el template canonico. Si una excepcion operacional exige acceso al daemon, tratarla como decision de alto riesgo y documentarla fuera de este asset.
- Secrets via env vars, nunca hardcodeados en compose
- Healthcheck obligatorio para restart automatico
- Resource limits siempre explicitos
