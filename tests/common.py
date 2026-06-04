import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# Topologia v5 (reorg 2026-04-18): artifacts/ agrupa agents/skills/knowledge;
# toolchain/ reemplaza scripts/. Se mantiene fallback para forks historicos.
_new_artifacts = ROOT / "artifacts"
if _new_artifacts.exists():
    AGENTS_ROOT = _new_artifacts / "agents"
    SKILLS_ROOT = _new_artifacts / "skills"
    KNOWLEDGE_ROOT = _new_artifacts / "knowledge"
else:
    AGENTS_ROOT = ROOT / "artifacts" / "agents" if (ROOT / "artifacts" / "agents").exists() else ROOT / "agents"
    SKILLS_ROOT = ROOT / "artifacts" / "skills" if (ROOT / "artifacts" / "skills").exists() else ROOT / "skills"
    KNOWLEDGE_ROOT = ROOT / "artifacts" / "knowledge" if (ROOT / "artifacts" / "knowledge").exists() else ROOT / "knowledge"

TOOLCHAIN_DIR = ROOT / "toolchain" if (ROOT / "toolchain").exists() else ROOT / "scripts"
SCRIPTS_DIR = TOOLCHAIN_DIR  # alias backwards-compat
SCRIPT_PATH = TOOLCHAIN_DIR / "kora"
FIXTURES = ROOT / "tests" / "fixtures"
GENERATED_DOCS = ROOT / "docs" / "generated"

if str(TOOLCHAIN_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLCHAIN_DIR))


FRAGUA_ROOT = AGENTS_ROOT / "_FRAGUA"
TALLER_ROOT = SKILLS_ROOT / "_TALLER"

ACTIVE_TARGETS = frozenset({"claude-code", "codex", "openclaw", "hermes", "opencode"})
PAUSED_TARGETS = frozenset({"gemini", "mastra", "agentskills"})


def run_cli(*args, check=True):
    return subprocess.run(
        [sys.executable, str(SCRIPT_PATH), *args],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=check,
    )


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_path(path):
    """Normalizador canonico de paths — colapsa isomorfismos de plataforma.

    En macOS, tempfile.TemporaryDirectory entrega paths bajo /var/folders/...
    que son symlinks a /private/var/folders/...; los CLI internos de KORA
    canonizan via Path.resolve() antes de imprimir, por lo que toda
    comparacion entre rutas observadas y rutas construidas debe pasar por
    este normalizador. En Linux es idempotente.

    Acepta str o Path; devuelve str con la forma canonica.
    """
    return str(Path(os.fspath(path)).resolve())


def assert_path_in_output(test_case, output, path, msg=None):
    """Asercion portable: la representacion canonica de `path` aparece en `output`.

    Reemplaza el antipatron assertIn(str(path), output), que falla en macOS
    cuando el CLI canonizo `/var/...` a `/private/var/...` pero el test
    construyo la cadena esperada sin resolve.
    """
    canonical = canonical_path(path)
    if canonical not in output:
        detail = msg or f"canonical path not found in output: {canonical!r}"
        test_case.fail(f"{detail}\n--- output ---\n{output}")


def has_productive_workspaces():
    """Return True si existen workspaces de agente en AGENTS/{ns}/{name}/ productivos.

    En la arquitectura v8 (pipeline descentralizado), todos los workspaces
    pueden estar en staging (`artifacts/agents/_FRAGUA/INBOX/`) durante reprocesamiento
    del fleet. Tests que presumen fleet productivo deben skip cuando el
    estado no los tiene.
    """
    if not AGENTS_ROOT.exists():
        return False
    for ns_dir in AGENTS_ROOT.iterdir():
        if not ns_dir.is_dir() or ns_dir.name.startswith((".", "_")):
            continue
        for ws_dir in ns_dir.iterdir():
            if ws_dir.is_dir() and not ws_dir.name.startswith((".", "_")) and (ws_dir / "AGENT.md").is_file():
                return True
    return False


def has_productive_workspace(workspace_ref):
    namespace, name = workspace_ref.split("/", 1)
    return (AGENTS_ROOT / namespace / name / "AGENT.md").is_file()


def agent_workspace_path(workspace_ref, *, include_staging=True):
    from kora_lib.workspaces import find_agent_workspace

    resolved = find_agent_workspace(workspace_ref, include_staging=include_staging)
    if resolved is not None:
        return resolved
    namespace, name = workspace_ref.split("/", 1)
    return AGENTS_ROOT / namespace / name


def has_agent_workspace(workspace_ref, *, include_staging=True):
    return (agent_workspace_path(workspace_ref, include_staging=include_staging) / "AGENT.md").is_file()


def _find_staged_skill_dir(ns, name):
    from kora_lib.artifacts import load_yaml_safe
    from kora_lib.lifecycle import is_deprecated_status, is_retired_status, read_declared_status

    target_urn = f"urn:{ns}:artefacto:{name}"
    if not TALLER_ROOT.exists():
        return None
    candidates = []
    for skill_path in sorted(TALLER_ROOT.glob("**/SKILL.md")):
        if "_BUILD" in skill_path.parts:
            continue
        doc, err = load_yaml_safe(skill_path)
        if err or not isinstance(doc, dict):
            continue
        if doc.get("_manifest", {}).get("urn") != target_urn:
            continue
        status = read_declared_status(doc)
        rebuild = doc.get("extensions", {}).get("kora", {}).get("rebuild", {})
        if (
            is_deprecated_status(status)
            or is_retired_status(status)
            or (isinstance(rebuild, dict) and rebuild.get("required") is True and rebuild.get("current_is_source") is False)
        ):
            continue
        rel = skill_path.parent.relative_to(SKILLS_ROOT).as_posix()
        direct_namespaced = rel.endswith(f"/{ns}/{name}")
        candidates.append((0 if direct_namespaced else 1, len(rel), skill_path.parent))
    if not candidates:
        return None
    return sorted(candidates, key=lambda item: (item[0], item[1], item[2].as_posix()))[0][2]


def skill_artifact_dir(ns, name, *, include_staging=True):
    productive = SKILLS_ROOT / ns / name
    if (productive / "SKILL.md").is_file():
        return productive
    direct = SKILLS_ROOT / name
    if (direct / "SKILL.md").is_file():
        return direct
    if include_staging:
        staged = _find_staged_skill_dir(ns, name)
        if staged is not None:
            return staged
    return productive
