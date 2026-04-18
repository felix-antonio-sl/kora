import json
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
