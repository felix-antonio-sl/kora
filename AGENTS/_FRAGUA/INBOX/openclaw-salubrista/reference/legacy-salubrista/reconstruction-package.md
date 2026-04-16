# Paquete de Reconstrucción — Salubrista-HaH v1.0.0

**Fecha:** 2026-04-05
**Agente:** salubrista-hah (kora/salubrista-hah)
**Runtime:** OpenClaw sobre Docker, red kora-federation

---

## 1. Identidad del Agente

| Campo | Valor |
|-------|-------|
| ID | `salubrista-hah` |
| Namespace | `salud/salubrista-hah` |
| Emoji | 🏥 |
| Modelo por defecto | `zai/glm-5.1` |
| Canal | Telegram |
| Timezone | America/Santiago |
| Puerto gateway | 18830 |

---

## 2. Archivos Core del Workspace

Todos estos archivos van en la raíz del workspace (`~/.openclaw/workspace/`):

| Archivo | Rol | Descripción |
|---------|-----|-------------|
| `AGENTS.md` | FSM + reglas | Máquina de estados finitos completa (11 estados, transiciones priorizadas), 17 reglas duras, checklist de co-inducción de 17 ítems, protocolo de corrección, contexto multi-turno, wiring de herencia |
| `SOUL.md` | Identidad + paradigma | Persona que integra: salubrista, epidemiólogo aplicado, gestor hospitalario, diseñador de sistemas, especialista en continuidad, especialista HD. 4 paradigmas cognitivos, 4 ejes transversales, 5 tensiones estructurales, tono |
| `TOOLS.md` | Herramientas + KB routing | `kb_route` (routing map hospitalización + HD + salud pública), `knowledge_retrieval` (URN → ruta archivo), `web_search` (guías de uso), federación kora (directorio + hook URLs) |
| `USER.md` | Perfil de usuario | 7 perfiles objetivo, rutinas esperadas, preferencias de output (idioma, formato, escala, KPIs, rol copiloto) |
| `IDENTITY.md` | Marcador de identidad | Nombre + emoji |
| `HEARTBEAT.md` | Instrucciones de heartbeat | Verificar hallazgos pendientes, check-in si >24h sin interacción |
| `BOOTSTRAP.md` | Bootstrap y recovery | Pre-requisitos, inicialización post-deploy, post-recovery, contacto emergencia |
| `MEMORY.md` | Memoria duradera | Contexto clínico, decisiones, hallazgos pendientes, evolución, coordinación, notas |

**Incluidos en:** `salubrista-hah-core.tar.gz` (12KB)

---

## 3. Skills (9 módulos cognitivos)

| Skill | Descripción | Invocable por usuario |
|-------|-------------|----------------------|
| `intent-hospitalization` | Clasificación semántica de solicitudes (escala, modalidad, intención, producto) | No |
| `clarifier` | Solicitud de aclaración mínima para consultas ambiguas | No |
| `hospital-system-analyst` | Análisis y diseño de sistemas de hospitalización integrados (mode=analysis/design) | No |
| `hah-specialist` | Componente HD/HaH: elegibilidad, operaciones, dirección técnica, continuidad | No |
| `epi-vigilance` | Vigilancia epidemiológica: brotes, IAAS, surge, RAM, seguridad | No |
| `implementation-planner` | Planes de implementación: fases, responsables, riesgos, KPIs | No |
| `quality-auditor` | Evaluación, calidad y cumplimiento normativo | No |
| `product-builder` | Productos estructurados: tableros, mapas de riesgo, escenarios de decisión | No |
| `report-builder` | Informes formales para conducción humana | No |

Cada skill tiene un `SKILL.md` que define propósito, input/output, procedimiento y firma.

**Incluidos en:** `salubrista-hah-skills.tar.gz` (9KB)

---

## 4. Base de Conocimiento (Knowledge Base)

Montada en `/home/node/knowledge/salud/`:

### Corpus gestión-redes (componente intrahospitalario)

| URN | Ruta archivo |
|-----|-------------|
| `urn:salud:kb:gestion-redes-indice` | `salubrista/gestion-redes/00-indice.md` |
| `urn:salud:kb:gestion-redes-general` | `salubrista/gestion-redes/01-gestion-redes-general.md` |
| `urn:salud:kb:gestion-redes-unidades` | `salubrista/gestion-redes/02-unidades-asistenciales.md` |
| `urn:salud:kb:gestion-redes-urgencias` | `salubrista/gestion-redes/03-urgencias.md` |
| `urn:salud:kb:gestion-redes-salud-mental` | `salubrista/gestion-redes/04-salud-mental.md` |
| `urn:salud:kb:gestion-redes-herramientas` | `salubrista/gestion-redes/05-herramientas-anexos.md` |

### Corpus HD / hospital-domicilio

| URN | Ruta archivo |
|-----|-------------|
| `urn:salud:kb:hodom-reglamento-ds1-2022` | `hodom/normativa/01-reglamento-hodom-ds1-2022.md` |
| `urn:salud:kb:hodom-decreto-exento-31-2024` | `hodom/normativa/02-decreto-exento-31-2024-aprueba-norma-tecnica.md` |
| `urn:salud:kb:hodom-norma-tecnica-2024` | `hodom/normativa/03-norma-tecnica-hodom-2024.md` |
| `urn:salud:kb:hodom-direccion-tecnica` | `hodom/director/01-manual-direccion-tecnica.md` |
| `urn:salud:kb:hodom-manual-alta-complejidad` | `hodom/director/02-manual-alta-complejidad.md` |
| `urn:salud:kb:hodom-situacion-chile-2026` | `hodom/director/03-situacion-chile-2026.md` |

### Corpus razonamiento integrado

| URN | Ruta archivo |
|-----|-------------|
| `urn:salud:kb:firs-framework-integrado-razonamiento-salud` | `salubrista/framework-razonamiento-clinico-epidemiologico-gestion/firs-framework-integrado.md` |

---

## 5. Memoria Durable

Archivos en `memory/`:

| Archivo | Contenido |
|---------|-----------|
| `2026-03-24.md` | Sesión investigación académica HaH (113 fuentes, 28 ejes, aplicación HODOM HSC, procesamiento legacy 5.186 archivos) |
| `2026-03-25.md` | Memorias durables HODOM HSC: consolidado estratégico DT, 3 horizontes, prototipos web, brechas prioritarias |
| `2026-03-25-hodom-dt-consolidado.md` | Consolidado estratégico detallado para primera reunión DT HODOM HSC |
| `2026-03-27-0004.md` | Notas adicionales |
| `2026-03-27-boot-check.md` | Boot check |
| `2026-04-01-hodom-hsc-status.md` | Status HODOM HSC: brechas prioritarias, sueroterapia/oxigenoterapia reactivadas |
| `2026-04-02-1544.md` | 21 pacientes HODOM procesados con historias completas y síntesis ejecutivas |

**Incluidos en:** `salubrista-hah-memory.tar.gz` (12KB)

---

## 6. Datos de Salida (Output)

### Proyecto HODOM HSC (`output/hodom-hsc/`)

| Archivo | Descripción |
|---------|-------------|
| `analisis.md` | Análisis integral del dispositivo |
| `checklist-normativo.md` | 75 requisitos normativos/operativos |
| `historias-usuario.md` | Historias de usuario para sistema web |
| `inventario.md` | Inventario de recursos |
| `plan-capacitacion.md` | 5 módulos, 34 hrs, 20 sesiones |
| `presentacion-dt.md` | 16 slides + guión para presentación DT |
| `propuesta-ideal.md` | Propuesta de modelo ideal |
| `protocolos-clinicos.md` | 8 protocolos base |
| `specs-sistema-web.md` | Especificaciones sistema web |
| `consolidado-estrategico-dt-hodom-hsc-2026-03-25.md` | Documento madre estratégico |

### Pacientes (`output/hodom-pacientes-2026-04-01/`)
- 21 directorios (uno por paciente) con `historia-completa-hodom.md` y `sintesis-ejecutiva-hodom.md`

### Operacional (`output/operacional/`)
- `plan-90-dias-dt.md`
- `formato-briefing-matinal.md`

---

## 7. Federación Kora

| Agente | Gateway | Hook URL |
|--------|---------|----------|
| salubrista-hah (yo) | kora-salubrista:18830 | `http://kora-salubrista:18830/hooks/agent` |
| korax | kora-personal:18789 | `http://kora-personal:18789/hooks/agent` |
| steipete | kora-steipete:18810 | `http://kora-steipete:18810/hooks/agent` |

**Espacio compartido:**
- Propio: `/home/node/shared/salubrista-hah/`
- Federación (solo lectura): `/home/node/shared/federation/`
- Directorio de agentes: `/home/node/shared/federation/directorio-agentes.md`

---

## 8. Procedimiento de Reconstrucción Paso a Paso

### Paso 1: Instalar OpenClaw

```bash
# Instalar OpenClaw según documentación oficial
# https://docs.openclaw.ai
openclaw gateway start
```

### Paso 2: Crear estructura de workspace

```bash
mkdir -p ~/.openclaw/workspace/{skills,memory,inbox,output,sources}
mkdir -p ~/.openclaw/workspace/output/hodom-hsc
mkdir -p ~/.openclaw/workspace/output/operacional
mkdir -p ~/.openclaw/workspace/inbox/hodom-pacientes-2026-04-01
```

### Paso 3: Desplegar archivos core

```bash
# Descomprimir salubrista-hah-core.tar.gz en la raíz del workspace
tar xzf salubrista-hah-core.tar.gz -C ~/.openclaw/workspace/
```

Esto coloca: `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `USER.md`, `IDENTITY.md`, `HEARTBEAT.md`, `BOOTSTRAP.md`, `MEMORY.md`

### Paso 4: Desplegar skills

```bash
# Descomprimir salubrista-hah-skills.tar.gz en skills/
tar xzf salubrista-hah-skills.tar.gz -C ~/.openclaw/workspace/skills/
```

Esto crea 9 directorios de skill con sus respectivos `SKILL.md`.

### Paso 5: Montar knowledge bases

```bash
# Crear estructura de knowledge
mkdir -p /home/node/knowledge/salud/salubrista/gestion-redes
mkdir -p /home/node/knowledge/salud/salubrista/framework-razonamiento-clinico-epidemiologico-gestion
mkdir -p /home/node/knowledge/salud/hodom/normativa
mkdir -p /home/node/knowledge/salud/hodom/director

# Copiar archivos de corpus según la tabla en sección 4
# (Los archivos deben obtenerse del entorno original o del backup)
```

### Paso 6: Restaurar memoria

```bash
# Descomprimir salubrista-hah-memory.tar.gz en memory/
tar xzf salubrista-hah-memory.tar.gz -C ~/.openclaw/workspace/memory/
```

### Paso 7: Restaurar datos de salida (si se desea continuidad)

```bash
# Copiar output/hodom-hsc/ con documentos estratégicos
# Copiar output/hodom-pacientes-2026-04-01/ con 21 pacientes
# Copiar output/operacional/ con plan y briefing
```

### Paso 8: Configurar federación

```bash
mkdir -p /home/node/shared/salubrista-hah
mkdir -p /home/node/shared/federation
# Copiar directorio-agentes.md a /home/node/shared/federation/
```

### Paso 9: Configurar gateway

En la configuración del gateway OpenClaw:

```json
{
  "agents": {
    "salubrista-hah": {
      "model": "zai/glm-5.1",
      "channel": "telegram",
      "timezone": "America/Santiago"
    }
  }
}
```

### Paso 10: Verificar

```bash
openclaw gateway restart
openclaw status
# Enviar mensaje de prueba al agente vía Telegram
# Verificar que heartbeat responde HEARTBEAT_OK
# Verificar que memory_search funciona
# Verificar que kb_route resuelve URNs correctamente
```

---

## 9. Estado Actual y Limitaciones

| Aspecto | Estado |
|---------|--------|
| FSM completa | ✅ 11 estados, transiciones priorizadas |
| Skills operativas | ✅ 9 módulos con SKILL.md |
| Knowledge base | ✅ 15 URNs mapeados |
| Memoria histórica | ✅ 7 archivos de memoria con contexto clínico |
| Datos de pacientes | ✅ 21 pacientes con historias y síntesis |
| Consolidado estratégico DT | ✅ Documento madre completo |
| Federación | ✅ 3 agentes en directorio |
| Modelo activo | ⚠️ `zai/glm-5.1` — puede requerir configuración de API key |
| Workspace git | ❌ No inicializado como repositorio |
| Datos legacy | ⚠️ 5.186 archivos en inbox/ (419MB) — no incluidos en paquete core |

---

## 10. Archivos del Paquete

| Archivo | Tamaño | Contenido |
|---------|--------|-----------|
| `reconstruction-package.md` | Este archivo | Procedimiento completo de reconstrucción |
| `reconstruction-package.json` | 3.7KB | Metadatos en formato JSON |
| `salubrista-hah-core.tar.gz` | 12KB | 8 archivos core del workspace |
| `salubrista-hah-skills.tar.gz` | 9KB | 9 skills con SKILL.md |
| `salubrista-hah-memory.tar.gz` | 12KB | 7 archivos de memoria duradera |

**Total paquete core:** ~37KB (sin datos de pacientes ni legacy)

---

*Generado por salubrista-hah el 2026-04-05 21:45 UTC*
