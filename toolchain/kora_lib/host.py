"""Host role identity for KORA.

Implementa la doctrina `urn:kora:kb:host-roles` v1.1.0.

El rol del host se declara en `~/.kora/host.yml` (fuera del repo).
Si el marker no existe, el host se interpreta como `secondary`.
"""

from __future__ import annotations

import socket
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Literal, Optional

import yaml

from .config import KORA_ROOT, TOOLCHAIN_ROOT


Role = Literal["primary", "secondary"]
Source = Literal["marker", "default"]

MARKER_PATH = Path.home() / ".kora" / "host.yml"
MACHINE_ID_PATH = Path("/etc/machine-id")
GIT_HOOKS_DIR = TOOLCHAIN_ROOT / "git-hooks"
PRE_PUSH_HOOK = GIT_HOOKS_DIR / "pre-push"


@dataclass(frozen=True)
class HostRole:
    role: Role
    source: Source
    hostname: Optional[str]
    machine_id: Optional[str]
    declared_at: Optional[str]
    declared_by: Optional[str]
    notes: Optional[str]
    marker_path: Path
    consistent: bool

    @property
    def is_primary(self) -> bool:
        return self.role == "primary"

    @property
    def is_secondary(self) -> bool:
        return self.role == "secondary"


def _read_machine_id() -> Optional[str]:
    try:
        return MACHINE_ID_PATH.read_text(encoding="utf-8").strip() or None
    except OSError:
        return None


def _read_hostname() -> str:
    return socket.gethostname()


def read_host_role(marker_path: Optional[Path] = None) -> HostRole:
    """Lee el marker local; default secondary si ausente."""
    path = marker_path or MARKER_PATH
    actual_hostname = _read_hostname()
    actual_machine_id = _read_machine_id()

    if not path.exists():
        return HostRole(
            role="secondary",
            source="default",
            hostname=actual_hostname,
            machine_id=actual_machine_id,
            declared_at=None,
            declared_by=None,
            notes=None,
            marker_path=path,
            consistent=True,
        )

    try:
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}
    except (OSError, yaml.YAMLError):
        data = {}
    if not isinstance(data, dict):
        data = {}
    declared_role = str(data.get("role", "secondary")).strip().lower()
    if declared_role not in ("primary", "secondary"):
        declared_role = "secondary"

    declared_hostname = data.get("hostname")
    declared_machine_id = data.get("machine_id")
    consistent = True
    if declared_hostname and actual_hostname and declared_hostname != actual_hostname:
        consistent = False
    if declared_machine_id and actual_machine_id and declared_machine_id != actual_machine_id:
        consistent = False

    return HostRole(
        role=declared_role,  # type: ignore[arg-type]
        source="marker",
        hostname=declared_hostname or actual_hostname,
        machine_id=declared_machine_id or actual_machine_id,
        declared_at=data.get("declared_at"),
        declared_by=data.get("declared_by"),
        notes=data.get("notes"),
        marker_path=path,
        consistent=consistent,
    )


def warn_if_secondary(command_name: str, stream=sys.stderr) -> HostRole:
    """Emite warning a stderr si el host es secondary y devuelve el HostRole.

    Las mutaciones siguen permitidas — esta capa es enforcement `manual`.
    """
    role = read_host_role()
    if role.is_secondary:
        stream.write(
            f"[host-roles] aviso: '{command_name}' se esta ejecutando en host "
            f"secondary (source={role.source}). El SSOT operacional vive en el "
            f"host primary. Trabajar en rama feature y proponer cambios via PR.\n"
        )
    if not role.consistent:
        stream.write(
            f"[host-roles] aviso: marker {role.marker_path} no coincide con la "
            f"maquina real (hostname/machine_id divergen). Corregir antes de operar.\n"
        )
    return role


def can_push_master(role: Optional[HostRole] = None) -> bool:
    """Return True cuando el host puede pushear directo a origin/master."""
    current = role or read_host_role()
    return current.is_primary and current.consistent


def pre_push_master_guard(stream=sys.stderr, marker_path: Optional[Path] = None) -> int:
    """Exit-code helper para el hook pre-push.

    Devuelve 0 si el host puede pushear a master; 1 si debe bloquearse.
    """
    role = read_host_role(marker_path=marker_path)
    if can_push_master(role):
        return 0

    stream.write(
        "[host-roles] bloqueado: push directo a origin/master permitido solo "
        "desde host primary consistente.\n"
    )
    stream.write(
        f"[host-roles] role={role.role} source={role.source} marker={role.marker_path}\n"
    )
    if not role.consistent:
        stream.write("[host-roles] marker no coincide con hostname/machine_id reales.\n")
    stream.write("[host-roles] flujo secondary: push a rama feature y PR.\n")
    return 1


def install_git_hooks(
    repo_root: Path = KORA_ROOT,
    hooks_dir: Path = GIT_HOOKS_DIR,
    runner: Callable[..., subprocess.CompletedProcess] = subprocess.run,
) -> Path:
    """Configura core.hooksPath para usar los hooks versionados de KORA."""
    if not (hooks_dir / "pre-push").exists():
        raise FileNotFoundError(f"No existe hook pre-push en {hooks_dir}")

    try:
        hooks_config_value = hooks_dir.relative_to(repo_root).as_posix()
    except ValueError:
        hooks_config_value = str(hooks_dir)

    runner(
        ["git", "config", "core.hooksPath", hooks_config_value],
        cwd=str(repo_root),
        check=True,
    )
    return hooks_dir


def cmd_install_hooks() -> None:
    """Instala los hooks git versionados para este clon."""
    hooks_dir = install_git_hooks()
    print(f"Git hooks instalados: core.hooksPath={hooks_dir.relative_to(KORA_ROOT).as_posix()}")
    print("pre-push: bloquea push directo a origin/master si role != primary o marker inconsistente.")


def cmd_host(verbose: bool = False) -> None:
    """Imprime el rol y metadata del host."""
    role = read_host_role()
    actual_hostname = _read_hostname()
    actual_machine_id = _read_machine_id()

    print(f"role:         {role.role}")
    print(f"source:       {role.source}")
    print(f"marker:       {role.marker_path}")
    print(f"hostname:     {role.hostname or '(desconocido)'}")
    if verbose or role.hostname != actual_hostname:
        print(f"  actual:     {actual_hostname}")
    print(f"machine_id:   {role.machine_id or '(desconocido)'}")
    if verbose or (role.machine_id and role.machine_id != actual_machine_id):
        print(f"  actual:     {actual_machine_id or '(no leible)'}")
    if role.declared_at:
        print(f"declared_at:  {role.declared_at}")
    if role.declared_by:
        print(f"declared_by:  {role.declared_by}")
    if role.notes:
        print(f"notes:        {role.notes}")
    if not role.consistent:
        print()
        print("AVISO: el marker no coincide con la maquina real.")
        print("       Esto indica que el marker fue copiado entre maquinas.")
        print("       Corregir antes de operar (ver governance/host-roles.md §5).")
    if role.source == "default":
        print()
        print("Marker ausente — host interpretado como secondary por default.")
        print(f"Para declarar este host como primary o secondary, crear {role.marker_path}")
        print("conforme a urn:kora:kb:host-roles §5.")


__all__ = [
    "HostRole",
    "Role",
    "MARKER_PATH",
    "GIT_HOOKS_DIR",
    "PRE_PUSH_HOOK",
    "can_push_master",
    "pre_push_master_guard",
    "install_git_hooks",
    "read_host_role",
    "warn_if_secondary",
    "cmd_install_hooks",
    "cmd_host",
]
