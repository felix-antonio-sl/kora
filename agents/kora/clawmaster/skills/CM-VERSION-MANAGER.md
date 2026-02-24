---
_manifest:
  urn: "urn:kora:skill:clawmaster-version-manager:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-VERSION-MANAGER

## Proposito
Gestiona el ciclo de vida de versiones OpenClaw: identificar version actual, evaluar upgrades disponibles, planificar migracion, ejecutar upgrade, verificar, y rollback si necesario.

## Procedimiento

### Paso 1: Estado Actual
- `openclaw --version` — version instalada
- `openclaw status` — estado general
- Identificar metodo de instalacion (npm global, Docker, source, nix)
- Verificar si hay config custom o patches aplicados

### Paso 2: Evaluar Upgrade Disponible

| Canal | Comando/Metodo | Frecuencia | Riesgo |
|-------|---------------|------------|--------|
| **Stable** | npm: `npm view openclaw version`, Docker: check latest tag | Mensual (calver vYYYY.M.D) | Bajo |
| **Beta** | npm: `openclaw@beta`, Docker: beta tag | Semanal | Medio |
| **Dev** | From source: git pull main | Diario | Alto |

### Paso 3: Analisis Pre-Upgrade
1. Leer CHANGELOG entre version actual y target
2. Identificar breaking changes
3. Evaluar impacto en config actual:
   - Campos deprecados o renombrados
   - Nuevos campos requeridos
   - Cambios en comportamiento por defecto
   - Migraciones automaticas vs manuales
4. Verificar compatibilidad de plugins/skills custom

### Paso 4: Plan de Migracion
- Backup config: `cp openclaw.json openclaw.json.bak`
- Backup workspace: `cp -r workspace/ workspace.bak/`
- Para Docker: tag imagen actual antes de pull
- Documentar pasos de rollback

### Paso 5: Ejecutar Upgrade

| Metodo | Procedimiento |
|--------|--------------|
| npm global | `npm update -g openclaw` |
| Docker | `docker pull openclaw/openclaw:latest && docker compose up -d` |
| Source | `git pull && pnpm install && pnpm build` |
| Nix | `nix flake update` |

### Paso 6: Post-Upgrade Verification
```
openclaw --version       # version correcta
openclaw doctor          # sin issues
openclaw doctor --fix    # aplicar migraciones automaticas
openclaw status --all    # servicios ok
openclaw security audit  # sin regresiones
```
- Test message en cada canal activo

### Paso 7: Rollback (si necesario)
1. Restaurar config backup
2. Reinstalar version anterior: `npm install -g openclaw@{version_anterior}`
3. Para Docker: revertir a imagen anterior
4. Verificar rollback: `openclaw doctor`

## Output
Upgrade completado. Reporte: {version_anterior, version_nueva, breaking_changes[], migraciones_aplicadas[], verificacion, rollback_disponible: bool}.
