# Fallback Chain Test Plan — 2026-02-21

**Objetivo:** Validar que cada modelo en la cadena de fallback puede actuar como Korax.

**Criterios de validación:**
| Criterio | Qué valida |
|----------|------------|
| Respuesta coherente | No errores, no respuestas vacías |
| Sin leak de reasoning | Thinking interno no visible como texto |
| Tool calls funcionales | Puede usar exec, memory_search, etc. |
| System prompt largo | Aguenta ~20K tokens de contexto |

---

## Modelos a testear

| # | Alias | Modelo | Notas |
|---|-------|--------|-------|
| 1 | minimax | minimax-portal/MiniMax-M2.5 | reasoning: true, API anthropic-messages |
| 2 | kimi | moonshot/kimi-k2.5 | 256K ctx, gratis |
| 3 | glm-flash | zai/glm-4.7-flash | Gratis, rápido |
| 5 | glm5 | zai/glm-5 | reasoning: true, 744B MoE |

**No requieren prueba:**
- `sonnet` — primary, ya validado
- `opus` — Anthropic native, mismo proveedor que sonnet

---

## Protocolo de pruebas

### Paso 1 — Respuesta básica

```
/model <alias>
Responde en una frase: ¿quién eres y cuál es tu función?
```

| Alias | ¿Respuesta en español? | ¿Sin artefactos? | ¿Sin <thinking> visible? | ✅/❌ |
|-------|------------------------|------------------|--------------------------|------|
| minimax | | | | |
| kimi | | | | |
| glm-flash | | | | |
| glm5 | | | | |

---

### Paso 2 — Tool call simple

```
/model <alias>
¿Qué hora es en Chile ahora mismo?
```

**Debe llamar:** `session_status` o tool similar

| Alias | ¿Tool call ejecutado? | ¿Respuesta con dato real? | ✅/❌ |
|-------|----------------------|---------------------------|------|
| minimax | | | |
| kimi | | | |
| glm-flash | | | |
| glm5 | | | |

---

### Paso 3 — Tool call con exec

```
/model <alias>
¿Cuánto espacio libre hay en disco?
```

**Debe llamar:** `exec` con `df -h` o similar

| Alias | ¿Tool call ejecutado? | ¿Resultado correcto? | ¿No alucinado? | ✅/❌ |
|-------|----------------------|---------------------|----------------|------|
| minimax | | | | |
| kimi | | | | |
| glm-flash | | | | |
| glm5 | | | | |

---

### Paso 4 — Contexto largo (memory)

```
/model <alias>
¿Quién es Korvo? Resume en 3 bullets desde lo que sabes.
```

**Valida:** Procesa system prompt (~20K tokens) correctamente

| Alias | ¿Responde con info de USER.md/MEMORY.md? | ¿3 bullets coherentes? | ✅/❌ |
|-------|------------------------------------------|------------------------|------|
| minimax | | | |
| kimi | | | |
| glm-flash | | | |
| glm5 | | | |

---

### Paso 5 — Reasoning leak (solo minimax y glm5)

```
/model <alias>
Explica brevemente por qué es importante validar modelos antes de usarlos en producción.
```

**Criterio:** NO debe mostrar bloques de razonamiento interno como texto visible

| Alias | ¿Thinking visible en output? | ✅/❌ |
|-------|------------------------------|------|
| minimax | | |
| glm5 | | |

---

## Resumen de resultados

| Alias | P1 | P2 | P3 | P4 | P5 | Total | Estado |
|-------|----|----|----|----|----|-------|--------|
| minimax | | | | | | /5 | |
| kimi | | | | | — | /4 | |
| glm-flash | | | | | — | /4 | |
| glm5 | | | | | | /5 | |

**Criterio de aprobación:** ✅ en todos los pasos aplicables

---

## Cadena propuesta post-validación

Si todos pasan:
```
```

Si alguno falla, se reordena o remueve según severidad.

---

## Ejecución

1. Korvo ejecuta cada prueba en sesión nueva con `/model <alias>`
2. Korax registra resultados en este archivo
3. Al completar, se decide la cadena final
4. Se aplica en `~/.openclaw/openclaw.json`
5. Restart gateway: `sudo systemctl restart openclaw-gateway`

---

*Test plan preparado 2026-02-21*
