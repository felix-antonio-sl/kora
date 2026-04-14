---
name: docker-development
description: Optimize Dockerfiles, generate docker-compose configurations, and audit container security. Use when optimizing image size or build speed, creating or improving docker-compose setups, implementing multi-stage builds, hardening container security, or applying container best practices for any language or framework.
license: MIT
metadata: {"version":"1.0.0","author":"Alireza Rezvani","category":"engineering","updated":"2026-03-16"}
---

# Docker Development

Smaller images. Faster builds. Secure containers.

## Slash Commands

| Command | Purpose |
|---------|---------|
| `/docker:optimize` | Analyze and rewrite a Dockerfile for size, speed, and layer caching |
| `/docker:compose` | Generate or improve a docker-compose.yml |
| `/docker:security` | Audit a Dockerfile or running container for security issues |

## Workflow

### `/docker:optimize`

1. Read the Dockerfile; identify base image, layer count, and anti-patterns.
2. Apply the optimization checklist from `{baseDir}/references/dockerfile-best-practices.md`.
3. Run static analysis:
   ```bash
   python {baseDir}/scripts/dockerfile_analyzer.py Dockerfile
   python {baseDir}/scripts/dockerfile_analyzer.py Dockerfile --security
   ```
4. Emit the optimized Dockerfile with inline comments explaining each decision.
5. Load the multi-stage pattern from `{baseDir}/references/dockerfile-best-practices.md` if the image exceeds 200MB or uses a compiled language.

### `/docker:compose`

1. Identify services: app, database, cache, queue, proxy.
2. Apply compose best practices from `{baseDir}/references/compose-patterns.md`.
3. Validate the generated file:
   ```bash
   python {baseDir}/scripts/compose_validator.py docker-compose.yml
   python {baseDir}/scripts/compose_validator.py docker-compose.yml --strict
   ```
4. Emit `docker-compose.yml` + `.env.example` with all required variables documented.

### `/docker:security`

1. Audit Dockerfile with `{baseDir}/scripts/dockerfile_analyzer.py Dockerfile --security`.
2. Check runtime config (compose or run flags) against the security checklist in `{baseDir}/references/dockerfile-best-practices.md`.
3. Emit a severity-graded report: CRITICAL / HIGH / MEDIUM / LOW with fix per finding.

## Output Contract

- One optimized artifact per response (Dockerfile or compose file).
- Inline comments only for non-obvious decisions.
- Security report: one finding per line with severity and fix.
- Declare estimated size reduction when optimizing images.

## Proactive Triggers

Flag these without being asked:

- `:latest` tag → pin to a specific version
- No `.dockerignore` → create one (`.git`, `node_modules`, `__pycache__`, `.env`)
- `COPY . .` before dependency install → reorder to preserve cache
- Running as root → add `USER` instruction
- Secrets in `ENV` or `ARG` → use BuildKit secret mounts
- Image >1GB → multi-stage build required
- No `HEALTHCHECK` → add one

## Guardrails

- Never bake secrets into image layers.
- Never recommend `--privileged` without explicit user justification.
- Multi-stage builds are the default for compiled languages and Node.js — not optional.
- Do not generate Kubernetes manifests; stay within Docker and Compose scope.
