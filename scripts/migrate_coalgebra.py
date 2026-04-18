#!/usr/bin/env python3
"""Migrador one-shot: agrega shape coalgebraico (autoria-spec v1.1 §3.5) a los 7 productivos.

Deriva mecanicamente desde el shape existente:
- artefacto.plan.fsm desde plan.estados + plan.estado_inicial + plan.estado_terminal.
- artefacto.interfaz.polinomio desde artefacto.interfaz.herramientas.
- artefacto.invariantes.sub_coalgebra_segura inicialmente = todos los estados
  (conservadora: el autor refina despues marcando estados inseguros fuera de la sub-coalgebra).
- Marca extensions.kora.verificacion_coalgebraica: true.

Idempotente: si los campos ya existen, no se sobreescriben.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.kora_lib.artifacts import load_markdown_parts, dump_yaml_frontmatter_and_body


def derive_fsm(plan: dict) -> dict:
    """Extrae FSM normalizado desde plan.estados."""
    inicial = plan.get("estado_inicial")
    terminal = plan.get("estado_terminal")
    estados_list = plan.get("estados") or []

    all_ids = []
    transiciones = {}
    for s in estados_list:
        if not isinstance(s, dict):
            continue
        sid = s.get("id")
        if not sid:
            continue
        all_ids.append(sid)
        raw = s.get("transiciones")
        destinos = []
        if isinstance(raw, list):
            for t in raw:
                if isinstance(t, dict):
                    dest = t.get("destino")
                    if dest and dest not in destinos:
                        destinos.append(dest)
        # Estado terminal: self-loop [terminal] se interpreta como absorbente -> []
        if sid == terminal:
            destinos = [d for d in destinos if d != terminal]
        transiciones[sid] = destinos

    terminales = [terminal] if terminal in all_ids else []
    # Si no se declaro explicitamente, detectar estados sin salida como terminales
    if not terminales:
        terminales = [s for s in all_ids if not transiciones.get(s)]
    return {
        "inicial": inicial,
        "terminales": terminales,
        "transiciones": transiciones,
    }


def derive_polinomio(interfaz: dict) -> dict:
    """Deriva interface polynomial P(U) = Σ_{p ∈ Positions} U^{Directions(p)}.

    Cada herramienta es una posicion; las direcciones son 'ok' y 'error' como
    observaciones minimas. El autor refina despues con direcciones especificas.
    """
    herramientas = interfaz.get("herramientas") or []
    posiciones = []
    direcciones = {}
    for h in herramientas:
        if isinstance(h, str):
            name = h
        elif isinstance(h, dict):
            name = h.get("nombre") or h.get("name") or h.get("tool")
        else:
            continue
        if not name:
            continue
        posiciones.append(name)
        direcciones[name] = ["ok", "error"]
    return {"posiciones": posiciones, "direcciones": direcciones}


def migrate_file(agent_md: Path, dry_run: bool = False):
    fm, body = load_markdown_parts(agent_md)
    if not isinstance(fm, dict):
        return False, "no frontmatter"

    artefacto = fm.get("artefacto")
    if not isinstance(artefacto, dict):
        return False, "no artefacto.*"

    changed = False
    plan = artefacto.get("plan") or {}
    if isinstance(plan, dict) and "fsm" not in plan:
        plan["fsm"] = derive_fsm(plan)
        artefacto["plan"] = plan
        changed = True

    interfaz = artefacto.get("interfaz") or {}
    if isinstance(interfaz, dict) and "polinomio" not in interfaz:
        interfaz["polinomio"] = derive_polinomio(interfaz)
        artefacto["interfaz"] = interfaz
        changed = True

    invariantes = artefacto.get("invariantes") or {}
    if isinstance(invariantes, dict) and "sub_coalgebra_segura" not in invariantes:
        # Conservadora: todos los estados alcanzables son "seguros" por defecto
        fsm = plan.get("fsm") or {}
        transiciones = fsm.get("transiciones") or {}
        all_states = set([fsm.get("inicial")]) if fsm.get("inicial") else set()
        for src, dsts in transiciones.items():
            all_states.add(src)
            for d in (dsts or []):
                all_states.add(d)
        invariantes["sub_coalgebra_segura"] = sorted(s for s in all_states if s)
        artefacto["invariantes"] = invariantes
        changed = True

    # Flag de activacion del check estricto
    kora_ext = fm.setdefault("extensions", {}).setdefault("kora", {})
    if kora_ext.get("verificacion_coalgebraica") is not True:
        kora_ext["verificacion_coalgebraica"] = True
        changed = True

    if changed and not dry_run:
        dump_yaml_frontmatter_and_body(agent_md, fm, body, lint_guard=False)
    return changed, "ok" if changed else "no-op"


def main():
    dry_run = "--dry-run" in sys.argv
    agents = sorted((ROOT / "AGENTS").glob("*/*/AGENT.md"))
    agents = [a for a in agents if "_FRAGUA" not in str(a)]
    migrated = 0
    for a in agents:
        changed, msg = migrate_file(a, dry_run=dry_run)
        prefix = "[DRY] " if dry_run else ""
        rel = a.relative_to(ROOT)
        print(f"{prefix}{rel}: {msg}")
        if changed:
            migrated += 1
    print(f"\n{'[DRY] ' if dry_run else ''}Migrated: {migrated}/{len(agents)}")


if __name__ == "__main__":
    main()
