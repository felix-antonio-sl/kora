import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"
SCRIPT_PATH = SCRIPTS_DIR / "kora"
FIXTURES = ROOT / "tests" / "fixtures"
GENERATED_DOCS = ROOT / "docs" / "generated"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


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
