"""kora doctor — agregador de salud operativa.

Compone diagnostico vivo en una sola llamada:

- rol del host (host-roles)
- check --strict (resultado)
- deploy-status (counts ok/stale/missing/unsupported)
- staging counts (INBOX/REVIEW por capa)
- handoff freshness (ultimo handoff + dias)
- politica handoffs (cumplimiento ultima semana)

No es un check categorial — es lectura humana del estado. El gate normativo
sigue siendo `kora check --strict`. Esto solo agrupa lo que el operador
pregunta cuando se sienta a trabajar: "estoy verde?".
"""
from __future__ import annotations

from datetime import datetime, timezone, timedelta
from pathlib import Path

from .checks import run_checks
from .config import (
    AGENTS_ROOT,
    SKILLS_ROOT,
    KNOWLEDGE_ROOT,
    KORA_ROOT,
)
from .host import read_host_role


def _staging_counts() -> dict:
    """Conteos por capa de staging."""
    out = {}
    for label, root, stages in (
        ("agentes (_FRAGUA)", AGENTS_ROOT / "_FRAGUA", ("INBOX", "REVIEW")),
        ("skills (_TALLER)", SKILLS_ROOT / "_TALLER", ("INBOX", "REVIEW")),
        ("knowledge (_SCRIPTORIUM)", KNOWLEDGE_ROOT / "_SCRIPTORIUM", ("INBOX", "REVIEW")),
    ):
        per_stage = {}
        for stage in stages:
            stage_dir = root / stage
            if stage_dir.exists():
                per_stage[stage] = sum(
                    1 for p in stage_dir.iterdir()
                    if p.is_dir() and not p.name.startswith("_")
                )
            else:
                per_stage[stage] = 0
        out[label] = per_stage
    return out


def _last_handoff() -> tuple[Path | None, int | None]:
    """Devuelve (path-del-handoff-mas-reciente, dias-desde-hoy)."""
    candidates: list[Path] = []
    for d in (KORA_ROOT / "docs" / "handoffs",):
        if not d.exists():
            continue
        for p in d.glob("*.md"):
            name = p.name
            if name.startswith("handoff-") or name[:4].isdigit():
                candidates.append(p)
    if not candidates:
        return None, None

    def _date_from_name(p: Path) -> str | None:
        name = p.stem
        if name.startswith("handoff-"):
            name = name[len("handoff-"):]
        if len(name) >= 10 and name[4] == "-" and name[7] == "-":
            return name[:10]
        return None

    dated = [(p, _date_from_name(p)) for p in candidates]
    dated = [(p, d) for p, d in dated if d]
    if not dated:
        return None, None
    dated.sort(key=lambda x: x[1], reverse=True)
    latest_path, latest_date = dated[0]
    today = datetime.now(timezone.utc).date()
    try:
        d = datetime.fromisoformat(latest_date).date()
        days = (today - d).days
    except ValueError:
        days = None
    return latest_path, days


def _handoffs_last_n_days(days: int) -> int:
    """Cuenta handoffs en los ultimos N dias (por nombre de archivo)."""
    cutoff = datetime.now(timezone.utc).date() - timedelta(days=days)
    count = 0
    for d in (KORA_ROOT / "docs" / "handoffs",):
        if not d.exists():
            continue
        for p in d.glob("*.md"):
            name = p.stem
            if not (name.startswith("handoff-") or name[:4].isdigit()):
                continue
            stem = name[len("handoff-"):] if name.startswith("handoff-") else name
            if len(stem) < 10 or stem[4] != "-" or stem[7] != "-":
                continue
            try:
                d_handoff = datetime.fromisoformat(stem[:10]).date()
            except ValueError:
                continue
            if d_handoff >= cutoff:
                count += 1
    return count


def _deploy_status_summary() -> dict:
    """Recuento por status de deploy-status sin imprimir el detalle."""
    from .transmute import build_deploy_status_report
    try:
        report = build_deploy_status_report()
    except Exception:  # pragma: no cover — defensivo
        return {}
    return report.get("summary", {})


def cmd_doctor() -> None:
    """Imprime salud operativa agregada."""
    print("=== KORA Doctor ===\n")

    role = read_host_role()
    role_label = role.role.upper()
    consistency = "ok" if role.consistent else "INCONSISTENTE"
    print(f"Host:       {role_label} ({consistency})")
    print(f"  hostname: {role.hostname or '(desconocido)'}")
    if role.declared_at:
        print(f"  desde:    {role.declared_at}")
    print()

    print("Checks (kora check --strict):")
    result = run_checks(emit=False)
    status = "verde" if result.ok else "rojo"
    print(f"  {status}: {result.checks_passed}/{result.checks_run} pasaron")
    if not result.ok:
        by_sev = result.by_severity
        sev_str = ", ".join(
            f"{sev}={by_sev[sev]}" for sev in ("critical", "high", "medium", "low")
            if by_sev.get(sev)
        )
        print(f"  diagnosticos: {sev_str}")
    print()

    print("Staging:")
    for label, counts in _staging_counts().items():
        per = " | ".join(f"{stage}={n}" for stage, n in counts.items())
        print(f"  {label}: {per}")
    print()

    deploy = _deploy_status_summary()
    if deploy:
        print("Deploys:")
        for status, n in sorted(deploy.items()):
            print(f"  {status}: {n}")
        print()

    handoff_path, days_since = _last_handoff()
    print("Handoffs:")
    if handoff_path:
        rel = handoff_path.relative_to(KORA_ROOT)
        when = f"hace {days_since}d" if days_since is not None else "fecha desconocida"
        print(f"  ultimo: {rel} ({when})")
    else:
        print("  (ninguno encontrado)")
    last7 = _handoffs_last_n_days(7)
    print(f"  ultima semana: {last7} archivos (politica: 1/semana max)")
    print(f"  nota:   excepciones por canario/incidente no se descuentan auto")
    print(f"  politica: docs/plans/2026-05-07-politica-handoffs.md")
    print()

    overall_ok = result.ok and role.consistent
    print(f"Resultado: {'OPERATIVO' if overall_ok else 'ATENCION REQUERIDA'}")
