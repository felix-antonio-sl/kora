# KORA Health Fix Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Llevar `kora health` de 554 URNs rotos a 0 errores reales.

**Architecture:** Cuatro frentes independientes: (1) ampliar el indexador para capturar `.md` con frontmatter, (2) mejorar el health checker con allowlist de namespaces ignorados, (3) auto-generar un script de transmutación de URNs truncados, (4) regenerar catálogo y verificar.

**Tech Stack:** Python 3 (stdlib: `re`, `yaml`, `pathlib`, `glob`), `scripts/kora` CLI

---

## Diagnóstico de Raíz

| Categoría | Conteo | Causa | Fix |
|-----------|--------|-------|-----|
| A: `.md` con `_manifest` no indexados | ~3 URNs únicos | `kora index` solo escanea `.yml`/`.yaml` | Ampliar indexador |
| B: Catálogo desactualizado | ~40 refs en catalog | Catálogo manual no regenerado | `kora index` |
| C: URNs truncados en contenido | ~38 URNs únicos | Transmutador solo actualizó refs bien formadas (con versión) | Script de mapeo |
| D: URNs placeholder en specs/ejemplos | ~20 URNs | Health no tiene allowlist de namespaces fake | Agregar ignorelist |

---

## Task 1: Ampliar `kora index` para indexar `.md` con frontmatter

**Files:**
- Modify: `scripts/kora`

**Context:** El comando `kora index` escanea solo `*.yml/*.yaml`. Los archivos
`knowledge/foundations/core/kora/md-spec.md` y `openclaw-agent-spec.md` tienen
`_manifest.urn` válido pero nunca son registrados en el catálogo.

**Step 1: Localizar la función de escaneo**

En `scripts/kora`, buscar la función `cmd_index()`. La sección de escaneo usa
`glob.glob('**/*.yml', ...)` + `glob.glob('**/*.yaml', ...)`.

**Step 2: Agregar escaneo de `.md` con frontmatter**

Añadir soporte para archivos `.md` que contengan un bloque YAML frontmatter entre `---`:

```python
# Dentro del loop de escaneo, agregar:
for f in glob.glob("**/*.md", recursive=True):
    if any(skip in f for skip in SKIP_DIRS):
        continue
    try:
        with open(f) as fp:
            content = fp.read()
        # Extraer bloque frontmatter: primer --- ... ---
        if content.startswith("---"):
            end = content.find("\n---", 3)
            if end > 0:
                frontmatter = content[3:end]
                data = yaml.safe_load(frontmatter)
                if data and "_manifest" in data and "urn" in data.get("_manifest", {}):
                    process_artifact(f, data)  # usar la misma lógica de indexado
    except Exception:
        pass
```

**Step 3: Verificar que md-spec y openclaw-agent-spec aparecen en el catálogo**

```bash
python3 scripts/kora index
grep -E "md-spec|openclaw-agent-spec|spec:2.0.0" catalog/catalog_master_kora.yml
```

Expected: 3 matches mostrando los nuevos URNs indexados.

**Step 4: Commit**

```bash
git add scripts/kora
git commit -m "feat(kora-index): soporte de .md files con _manifest frontmatter"
```

---

## Task 2: Mejorar health checker con ignorelist de namespaces placeholder

**Files:**
- Modify: `scripts/kora` (función `cmd_health`)

**Context:** El health checker reporta URNs de specs/ejemplos como
`urn:myorg:domain:artifact:1.0.0`, `urn:ns:*`, `urn:external:*`, `urn:sanixai:*`
como "rotos". Son placeholders intencionales en documentación de ejemplo.

**Step 1: Agregar set de namespaces ignorados**

En `cmd_health()`, justo antes del loop de escaneo:

```python
IGNORED_NAMESPACES = {
    "myorg", "namespace", "ns", "org", "sanixai",
    "external", "goreos", "tooling",
}

def is_ignored_urn(urn: str) -> bool:
    """URNs de ejemplo/placeholder que no deben validarse."""
    parts = urn.split(":")
    if len(parts) >= 2 and parts[1] in IGNORED_NAMESPACES:
        return True
    return False
```

**Step 2: Aplicar filtro en el loop de validación**

```python
for f_urn in found_urns:
    if is_ignored_urn(f_urn):
        continue  # skip placeholder URNs
    if f_urn not in known_urns:
        print(f"[BROKEN] In {file_path.relative_to(KORA_ROOT)}: {f_urn}")
        broken_links += 1
```

**Step 3: Verificar que los placeholders ya no aparecen**

```bash
python3 scripts/kora health 2>&1 | grep -E "myorg|sanixai|urn:ns:|urn:org:|urn:external:"
```

Expected: sin output (0 matches).

**Step 4: Commit**

```bash
git add scripts/kora
git commit -m "fix(kora-health): ignorar namespaces placeholder en validación de URNs"
```

---

## Task 3: Script de mapeo para URNs truncados en contenido

**Files:**
- Create: `scripts/fix_truncated_urns.py`

**Context:** En archivos de contenido (agentes, knowledge bases), hay referencias
a URNs sin versión ni sufijo completo, heredadas de la era pre-transmutador. Por ejemplo:
`urn:knowledge:koda:gov:lexicon` debería ser `urn:knowledge:koda:gov:lexicon_wikiguias:1.0.0`.

El transmutador original solo procesaba URNs bien formados (con versión). Los truncados
sobrevivieron.

**Step 1: Construir el mapeo completo de URNs truncados → URNs reales**

```python
# scripts/fix_truncated_urns.py
TRUNCATED_URN_MAP = {
    # GOV
    "urn:knowledge:koda:gov:anonimizacion": "urn:knowledge:koda:gov:anonimizacion_datos_v2:1.0.0",
    "urn:knowledge:koda:gov:calidad":        "urn:knowledge:koda:gov:calidad_web:1.0.0",
    "urn:knowledge:koda:gov:capacitaciones": "urn:knowledge:koda:gov:capacitaciones_tde:1.0.0",
    "urn:knowledge:koda:gov:catalogo":       "urn:knowledge:koda:gov:catalogo_cpat_nuble:1.0.0",
    "urn:knowledge:koda:gov:claveunica":     "urn:knowledge:koda:gov:claveunica_tyc:1.0.0",
    "urn:knowledge:koda:gov:cloud":          "urn:knowledge:koda:gov:cloud_publica:1.0.0",
    "urn:knowledge:koda:gov:cpat":           "urn:knowledge:koda:gov:cpat_completa:1.0.0",
    "urn:knowledge:koda:gov:datos":          "urn:knowledge:koda:gov:datos_administracion_estado:1.0.0",
    "urn:knowledge:koda:gov:diseno":         "urn:knowledge:koda:gov:diseno_servicios:1.0.0",
    "urn:knowledge:koda:gov:gobierno":       "urn:knowledge:koda:gov:gobierno_digital_2030:1.0.0",
    "urn:knowledge:koda:gov:identidad":      "urn:knowledge:koda:gov:identidad_digital:1.0.0",
    "urn:knowledge:koda:gov:intro":          "urn:knowledge:koda:gov:intro_tde:1.0.0",
    "urn:knowledge:koda:gov:lexicon":        "urn:knowledge:koda:gov:lexicon_wikiguias:1.0.0",
    "urn:knowledge:koda:gov:metadatos":      "urn:knowledge:koda:gov:metadatos_documentos:1.0.0",
    "urn:knowledge:koda:gov:metodologia":    "urn:knowledge:koda:gov:metodologia_proyectos_tic:1.0.0",
    "urn:knowledge:koda:gov:orientaciones":  "urn:knowledge:koda:gov:orientaciones_gestion_tic:1.0.0",
    "urn:knowledge:koda:gov:principios":     "urn:knowledge:koda:gov:principios_objetivos:1.0.0",
    "urn:knowledge:koda:gov:rat":            "urn:knowledge:koda:gov:rat_datos_personales:1.0.0",
    "urn:knowledge:koda:gov:reglamento":     "urn:knowledge:koda:gov:reglamento_tde_ds4:1.0.0",
    "urn:knowledge:koda:gov:seguridad":      "urn:knowledge:koda:gov:seguridad_ciberseguridad_v1:1.0.0",
    "urn:knowledge:koda:gov:simple":         "urn:knowledge:koda:gov:simple_saas:1.0.0",
    "urn:knowledge:koda:gov:sistema":        "urn:knowledge:koda:gov:sistema_tde_2025:1.0.0",
    # LEGAL
    "urn:knowledge:koda:legal:acoso":        "urn:knowledge:koda:legal:acoso_laboral:1.0.0",
    "urn:knowledge:koda:legal:confianza":    "urn:knowledge:koda:legal:confianza_legitima:1.0.0",
    "urn:knowledge:koda:legal:contratacion": "urn:knowledge:koda:legal:contratacion_publica:1.0.0",
    "urn:knowledge:koda:legal:deberes":      "urn:knowledge:koda:legal:deberes_prohibiciones:1.0.0",
    "urn:knowledge:koda:legal:derechos":     "urn:knowledge:koda:legal:derechos_especiales:1.0.0",
    "urn:knowledge:koda:legal:feriados":     "urn:knowledge:koda:legal:feriados_permisos:1.0.0",
    "urn:knowledge:koda:legal:formacion":    "urn:knowledge:koda:legal:formacion_especialistas:1.0.0",
    "urn:knowledge:koda:legal:ingreso":      "urn:knowledge:koda:legal:ingreso_carrera:1.0.0",
    "urn:knowledge:koda:legal:intro":        "urn:knowledge:koda:legal:intro_estatutos:1.0.0",
    "urn:knowledge:koda:legal:jornada":      "urn:knowledge:koda:legal:jornada_calificaciones:1.0.0",
    "urn:knowledge:koda:legal:legislacion":  "urn:knowledge:koda:legal:legislacion_ia_chile:1.0.0",
    "urn:knowledge:koda:legal:ley":          "urn:knowledge:koda:legal:ley_21180_tde:1.0.0",
    "urn:knowledge:koda:legal:nt":           "urn:knowledge:koda:legal:nt_documentos_expedientes:1.0.0",
    "urn:knowledge:koda:legal:responsabilidad": "urn:knowledge:koda:legal:responsabilidad_admin:1.0.0",
    # SYS
    "urn:knowledge:koda:sys:hub":      "urn:knowledge:koda:sys:hub_agentes:1.0.0",
    "urn:knowledge:koda:sys:test":     "urn:knowledge:koda:sys:test_strategy:1.0.0",
    "urn:knowledge:koda:sys:workflow": "urn:knowledge:koda:sys:workflow_wikiguias:1.0.0",
    # AGENTS
    "urn:knowledge:koda:agents:arquitecto-gore": "urn:kora:agent:arquitecto-gore:1.0.0",
}
```

**Step 2: Implementar función de búsqueda y reemplazo seguro**

```python
import re, glob, sys
from pathlib import Path

def fix_file(path: str, mapping: dict, dry_run: bool = False) -> int:
    """Reemplaza URNs truncados en un archivo. Retorna número de cambios."""
    with open(path) as f:
        content = f.read()

    original = content
    changes = 0

    # Ordenar por longitud descendente para evitar reemplazos parciales
    for old_urn, new_urn in sorted(mapping.items(), key=lambda x: -len(x[0])):
        # Solo reemplazar si el URN termina en boundary (no tiene sufijo adicional)
        pattern = re.escape(old_urn) + r'(?=["\s\n,\]\)>]|$)'
        new_content = re.sub(pattern, new_urn, content)
        if new_content != content:
            changes += content.count(old_urn) - new_content.count(old_urn)  # approximate
            content = new_content

    if content != original:
        if not dry_run:
            with open(path, 'w') as f:
                f.write(content)
        return 1
    return 0

def main():
    dry_run = "--dry-run" in sys.argv
    root = Path(__file__).parent.parent

    extensions = ["**/*.yml", "**/*.yaml", "**/*.md"]
    skip_dirs = {".git", "scripts", "docs/plans"}

    modified = 0
    for pattern in extensions:
        for f in root.glob(pattern):
            if any(skip in str(f) for skip in skip_dirs):
                continue
            modified += fix_file(str(f), TRUNCATED_URN_MAP, dry_run=dry_run)

    action = "Would modify" if dry_run else "Modified"
    print(f"{action} {modified} files.")

if __name__ == "__main__":
    main()
```

**Step 3: Dry-run para verificar scope**

```bash
python3 scripts/fix_truncated_urns.py --dry-run
```

Expected: "Would modify X files." (debería ser ~50-70 archivos).

**Step 4: Ejecutar el fix**

```bash
python3 scripts/fix_truncated_urns.py
```

**Step 5: Verificar manualmente un archivo modificado**

```bash
grep "urn:knowledge:koda:gov:lexicon" knowledge/applied/gov/intro_tde.yml
```

Expected: la referencia ahora muestra el URN completo con versión.

**Step 6: Commit**

```bash
git add -u
git commit -m "fix: actualizar URNs truncados a formato completo con versión"
```

---

## Task 4: Regenerar catálogo y auditar residuales

**Files:**
- Auto-generated: `catalog/catalog_master_kora.yml`

**Step 1: Regenerar catálogo con kora index actualizado**

```bash
python3 scripts/kora index
```

Expected: "Successfully indexed N artifacts" (N > 245, ahora incluye .md files).

**Step 2: Ejecutar health check completo**

```bash
python3 scripts/kora health 2>&1 | tee /tmp/health_report.txt
tail -3 /tmp/health_report.txt
```

Expected: número de broken URNs significativamente menor.

**Step 3: Analizar residuales por categoría**

```bash
# URNs truly missing (no son placeholders, no son truncados)
python3 scripts/kora health 2>&1 | grep BROKEN | sed 's/.*: //' | sort -u
```

Clasificar residuales:
- **Artefactos que nunca se crearon** (urn:kora:gn:bpmn-c4:1.0.0, etc.) → Se marcan como `TODO: crear artefacto`
- **Referencias a repos satélite** (urn:fxsl:*, urn:gn:kb:*) → Son cross-repo, health debe ignorarlos o aceptarlos
- **Agentes OpenClaw bootstrap** (urn:gn:agent-bootstrap:*) → Son del nuevo formato, aún no creados

**Step 4: Decidir política para URNs cross-repo**

Agregar a `cmd_health()` un conjunto de namespaces externos conocidos que se ignoran:

```python
EXTERNAL_NAMESPACES = {
    "fxsl",   # repositorio satélite fxsl
    "gn",     # gore nuble (repositorio satélite)
    "tde",    # repositorio satélite tde
    "orko",   # repositorio satélite orko
}
```

O alternativamente, solo reportar como WARNING (no BROKEN) los URNs de namespaces externos.

**Step 5: Health check final**

```bash
python3 scripts/kora health
```

Expected: `Found 0 broken URN references.` o solo warnings de cross-repo.

**Step 6: Commit**

```bash
git add catalog/catalog_master_kora.yml scripts/kora
git commit -m "fix(health): catálogo regenerado + política de namespaces externos"
```

---

## Verificación Final

```bash
# Debe terminar con 0 errores reales
python3 scripts/kora health

# Debe indexar los .md con manifest
python3 scripts/kora index
grep "md-spec\|openclaw-agent-spec\|spec:2.0.0" catalog/catalog_master_kora.yml

# Los URNs truncados deben estar corregidos
grep -r "urn:knowledge:koda:gov:lexicon[^_]" knowledge/ | wc -l  # debe ser 0
```
