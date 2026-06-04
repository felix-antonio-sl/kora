"""Deploy generated _BUILD outputs into local runtime directories."""

from dataclasses import dataclass
from pathlib import Path
import shutil

from .artifacts import load_markdown_parts
from .config import KORA_ROOT
from .transmute import (
    _build_claude_code_skill_target_path,
    _build_codex_skill_target_path,
    _build_opencode_skill_target_path,
    _build_openclaw_skill_target_path,
    _build_target_path,
    _openclaw_agent_workspace_name,
    _resolve_agent_path,
    _resolve_skill_path,
)


LOCAL_DEPLOY_TARGETS = ("claude-code", "codex", "opencode", "openclaw")


@dataclass(frozen=True)
class DeployOperation:
    target: str
    artifact_kind: str
    label: str
    source: Path
    destination: Path
    operation: str


@dataclass(frozen=True)
class DeployCollision:
    operation: DeployOperation
    destination: Path


def _display_path(path: Path) -> str:
    resolved = path.expanduser()
    try:
        return resolved.relative_to(KORA_ROOT).as_posix()
    except ValueError:
        return str(resolved)


def _normalize_home(home: str | Path | None) -> Path:
    return Path(home).expanduser() if home else Path.home()


def _normalize_targets(targets: list[str] | tuple[str, ...] | None) -> tuple[str, ...]:
    if not targets:
        raise ValueError(
            "Provide at least one --target. "
            f"Supported: {', '.join(LOCAL_DEPLOY_TARGETS)}"
        )
    selected = tuple(targets)
    unknown = [target for target in selected if target not in LOCAL_DEPLOY_TARGETS]
    if unknown:
        raise ValueError(
            f"Unsupported deploy target(s): {', '.join(unknown)}. "
            f"Supported: {', '.join(LOCAL_DEPLOY_TARGETS)}"
        )
    return selected


def _require_source(path: Path, *, is_dir: bool, target: str, ref: str) -> None:
    exists = path.is_dir() if is_dir else path.is_file()
    if exists:
        return
    build_ref = path
    try:
        build_ref = path.relative_to(KORA_ROOT)
    except ValueError:
        pass
    raise FileNotFoundError(
        f"Missing build artifact for {target}: {build_ref}. "
        f"Run `python3 toolchain/kora transmute --target {target} --agent {ref}` first."
    )


def _agent_build_operation(target: str, agent_md: Path, home: Path) -> DeployOperation:
    name = agent_md.parent.name
    build_dir = _build_target_path(agent_md.parent, target)

    if target == "claude-code":
        source = build_dir / f"{name}.md"
        destination = home / ".claude" / "agents" / f"{name}.md"
        operation = "file"
    elif target == "codex":
        source = build_dir / name
        destination = home / ".codex" / "skills" / name
        operation = "directory"
    elif target == "opencode":
        source = build_dir / "agents" / f"{name}.md"
        destination = home / ".config" / "opencode" / "agents" / f"{name}.md"
        operation = "file"
    elif target == "openclaw":
        frontmatter, _ = load_markdown_parts(agent_md)
        if not isinstance(frontmatter, dict):
            frontmatter = {}
        workspace_name = _openclaw_agent_workspace_name(frontmatter, name)
        source = build_dir / "workspace"
        destination = home / "openclaw-fleet" / "workspaces" / workspace_name
        operation = "directory"
    else:
        raise ValueError(f"Unsupported agent deploy target: {target}")

    _require_source(
        source,
        is_dir=(operation == "directory"),
        target=target,
        ref=f"{agent_md.parent.parent.name}/{name}",
    )
    return DeployOperation(
        target=target,
        artifact_kind="agent",
        label=name,
        source=source,
        destination=destination,
        operation=operation,
    )


def _skill_build_dir(target: str, skill_md: Path) -> Path:
    if target == "claude-code":
        return _build_claude_code_skill_target_path(skill_md)
    if target == "codex":
        return _build_codex_skill_target_path(skill_md)
    if target == "opencode":
        return _build_opencode_skill_target_path(skill_md)
    if target == "openclaw":
        return _build_openclaw_skill_target_path(skill_md)
    raise ValueError(f"Unsupported skill deploy target: {target}")


def _skill_build_operation(
    target: str,
    skill_md: Path,
    home: Path,
    *,
    openclaw_workspace: str,
) -> DeployOperation:
    name = skill_md.parent.name
    build_dir = _skill_build_dir(target, skill_md)

    if target == "claude-code":
        source = build_dir / name
        destination = home / ".claude" / "skills" / name
    elif target == "codex":
        source = build_dir / name
        destination = home / ".codex" / "skills" / name
    elif target == "opencode":
        source = build_dir / name
        destination = home / ".config" / "opencode" / "skills" / name
    elif target == "openclaw":
        if not openclaw_workspace.strip():
            raise ValueError("--openclaw-workspace is required for openclaw skill deploy")
        source = build_dir / "skills" / name
        destination = (
            home / "openclaw-fleet" / "workspaces" / openclaw_workspace / "skills" / name
        )
    else:
        raise ValueError(f"Unsupported skill deploy target: {target}")

    _require_source(
        source,
        is_dir=True,
        target=target,
        ref=f"{skill_md.parent.parent.name}/{name}",
    )
    return DeployOperation(
        target=target,
        artifact_kind="skill",
        label=name,
        source=source,
        destination=destination,
        operation="directory",
    )


def build_deploy_plan(
    *,
    agent: str | None = None,
    skill: str | None = None,
    targets: list[str] | tuple[str, ...] | None = None,
    home: str | Path | None = None,
    openclaw_workspace: str = "main",
) -> list[DeployOperation]:
    """Return deploy operations for an agent or skill build."""
    if bool(agent) == bool(skill):
        raise ValueError("Provide exactly one of --agent or --skill")

    home_path = _normalize_home(home)
    selected_targets = _normalize_targets(targets)

    if agent:
        agent_md = _resolve_agent_path(agent)
        return [_agent_build_operation(target, agent_md, home_path) for target in selected_targets]

    skill_md = _resolve_skill_path(skill or "")
    return [
        _skill_build_operation(
            target,
            skill_md,
            home_path,
            openclaw_workspace=openclaw_workspace,
        )
        for target in selected_targets
    ]


def _copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def _copy_directory(source: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)


def _file_contents_equal(left: Path, right: Path) -> bool:
    return left.read_bytes() == right.read_bytes()


def _operation_collisions(operation: DeployOperation) -> list[DeployCollision]:
    source = operation.source
    destination = operation.destination
    collisions: list[DeployCollision] = []

    if operation.operation == "file":
        if destination.exists() and (
            not destination.is_file() or not _file_contents_equal(source, destination)
        ):
            collisions.append(DeployCollision(operation, destination))
        return collisions

    if operation.operation == "directory":
        if destination.exists() and not destination.is_dir():
            return [DeployCollision(operation, destination)]
        if not destination.exists():
            return []
        for source_file in sorted(path for path in source.rglob("*") if path.is_file()):
            relative = source_file.relative_to(source)
            destination_file = destination / relative
            if destination_file.exists() and (
                not destination_file.is_file()
                or not _file_contents_equal(source_file, destination_file)
            ):
                collisions.append(DeployCollision(operation, destination_file))
        return collisions

    raise ValueError(f"Unsupported deploy operation: {operation.operation}")


def collect_collisions(operations: list[DeployOperation]) -> list[DeployCollision]:
    collisions: list[DeployCollision] = []
    for operation in operations:
        collisions.extend(_operation_collisions(operation))
    return collisions


def _collision_message(collisions: list[DeployCollision]) -> str:
    shown = collisions[:20]
    lines = [
        "Refusing to overwrite existing runtime file(s) with different content:",
        *[f"- {_display_path(collision.destination)}" for collision in shown],
    ]
    if len(collisions) > len(shown):
        lines.append(f"- ... {len(collisions) - len(shown)} more")
    lines.append("Rerun with --overwrite if replacing those files is intentional.")
    return "\n".join(lines)


def deploy_operations(
    operations: list[DeployOperation],
    *,
    dry_run: bool = True,
    overwrite: bool = False,
) -> None:
    collisions = collect_collisions(operations)
    if collisions and not overwrite and not dry_run:
        raise FileExistsError(_collision_message(collisions))

    for operation in operations:
        if dry_run:
            continue
        if operation.operation == "file":
            _copy_file(operation.source, operation.destination)
        elif operation.operation == "directory":
            _copy_directory(operation.source, operation.destination)
        else:
            raise ValueError(f"Unsupported deploy operation: {operation.operation}")


def cmd_deploy_builds(
    *,
    agent: str | None = None,
    skill: str | None = None,
    targets: list[str] | tuple[str, ...] | None = None,
    home: str | Path | None = None,
    openclaw_workspace: str = "main",
    dry_run: bool = True,
    overwrite: bool = False,
) -> None:
    operations = build_deploy_plan(
        agent=agent,
        skill=skill,
        targets=targets,
        home=home,
        openclaw_workspace=openclaw_workspace,
    )

    artifact_kind = "agent" if agent else "skill"
    artifact_ref = agent or skill or ""
    mode = "[dry-run] " if dry_run else ""
    print(f"=== KORA Deploy Builds: {artifact_kind} {artifact_ref} ===\n")
    for operation in operations:
        print(f"{mode}{operation.target}: {operation.artifact_kind} {operation.label}")
        print(f"  source: {_display_path(operation.source)}")
        print(f"  dest:   {_display_path(operation.destination)}")

    collisions = collect_collisions(operations)
    if collisions:
        print("\nOverwrite collisions:")
        for collision in collisions[:20]:
            print(f"  {_display_path(collision.destination)}")
        if len(collisions) > 20:
            print(f"  ... {len(collisions) - 20} more")
        if dry_run and not overwrite:
            print("  Apply would fail unless --overwrite is provided.")

    if collisions and not dry_run and not overwrite:
        raise SystemExit(_collision_message(collisions))

    deploy_operations(operations, dry_run=dry_run, overwrite=overwrite)
    if dry_run:
        print("\nDry-run complete; no files written. Use --apply to deploy.")
    else:
        print(f"\nDeployed {len(operations)} build output(s).")
