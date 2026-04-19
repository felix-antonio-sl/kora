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
    KNOWLEDGE_ROOT = _new_artifacts / "knowledge"
else:
    AGENTS_ROOT = ROOT / "artifacts" / "agents" if (ROOT / "artifacts" / "agents").exists() else ROOT / "agents"
    KNOWLEDGE_ROOT = ROOT / "artifacts" / "knowledge" if (ROOT / "artifacts" / "knowledge").exists() else ROOT / "knowledge"

TOOLCHAIN_DIR = ROOT / "toolchain" if (ROOT / "toolchain").exists() else ROOT / "scripts"
SCRIPTS_DIR = TOOLCHAIN_DIR  # alias backwards-compat
SCRIPT_PATH = TOOLCHAIN_DIR / "kora"
FIXTURES = ROOT / "tests" / "fixtures"
GENERATED_DOCS = ROOT / "docs" / "generated"

if str(TOOLCHAIN_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLCHAIN_DIR))


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
            if ws_dir.is_dir() and not ws_dir.name.startswith((".", "_")):
                return True
    return False
