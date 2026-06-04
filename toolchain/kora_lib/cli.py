import argparse

# atomize retirado 2026-05-20 (adr-retiro-atomize-y-lecciones-koda); modulo
# atomize.py vive ahora bajo legacy_migration/ como referencia historica.
from .audit import cmd_health
from .catalog import cmd_index, cmd_resolve
from .checks import run_checks, run_fixes, all_checks, CheckResult
from .commands import cmd_migrate, cmd_stats_json, cmd_sync_docs
from .deploy import LOCAL_DEPLOY_TARGETS, cmd_deploy_builds
from .graph import cmd_graph
from .host import cmd_host, cmd_install_hooks, warn_if_secondary
from .intake import cmd_intake
from .kb_graph import cmd_kb_graph
from .promote import cmd_promote, cmd_deprecate, cmd_promote_cohort
from .recovery import cmd_recovery_inventory
from .transmute import cmd_transmute, cmd_ingest, cmd_roundtrip_check, cmd_deploy_status, cmd_record_invocation, SUPPORTED_TARGETS
from .validation import cmd_lint_md, cmd_validate


def main():
    parser = argparse.ArgumentParser(description="KORA Monorepo CLI")
    subparsers = parser.add_subparsers(dest="command", help="Sub-commands")

    subparsers.add_parser("index", help="Rebuild the catalog from source artifacts")

    p_resolve = subparsers.add_parser("resolve", help="Resolve a URN to a local file path")
    p_resolve.add_argument("urn", help="The URN to resolve")

    p_health = subparsers.add_parser("health", help="Check for broken URNs across files")
    p_health.add_argument("--strict", action="store_true", help="Exit non-zero when health issues exist")

    p_validate = subparsers.add_parser("validate", help="Validate KORA agent workspaces against the schema")
    p_validate.add_argument(
        "--profile",
        choices=("legacy", "transitional", "strict"),
        default="transitional",
        help="Validation profile",
    )
    p_validate.add_argument(
        "--cohort",
        choices=("meta-kora", "dev", "ops", "domains"),
        default=None,
        help="Validate only one migration cohort",
    )
    p_lint_md = subparsers.add_parser("lint-md", help="Lint published KORA/MD artifacts")
    p_lint_md.add_argument(
        "paths",
        nargs="*",
        help="Markdown file or directory to lint. Defaults to artifacts/knowledge/ and the tracked staging zones.",
    )
    p_lint_md.add_argument(
        "--max-lines-per-h2",
        type=int,
        default=None,
        help="Maximum allowed lines per primary ## chunk; defaults by document family",
    )
    p_lint_md.add_argument(
        "--fix",
        action="store_true",
        help="Apply safe structural auto-fixes before linting",
    )

    p_stats = subparsers.add_parser("stats", help="Show monorepo statistics for workspaces and catalog entries")
    p_stats.add_argument("--json", action="store_true", help="Emit stats as JSON")

    p_migrate = subparsers.add_parser("migrate", help="Apply codemods to move workspaces toward the current spec")
    p_migrate.add_argument(
        "--profile",
        "--perfil",
        dest="profile",
        choices=("legacy", "transitional", "strict", "v2-agentfile", "a-autoria"),
        default="transitional",
        help=(
            "Migration profile. "
            "a-autoria: forced one-pass migration to autoria-spec v1.2 (idempotent). "
            "v2-agentfile: auto-derive vector_ontologico from legacy shape."
        ),
    )
    p_migrate.add_argument("--dry-run", action="store_true", help="Report only; do not write files")
    p_migrate.add_argument(
        "--cohort",
        choices=("meta-kora", "dev", "ops", "domains"),
        default=None,
        help="Migrate only one cohort of workspaces",
    )

    subparsers.add_parser("sync-docs", help="Regenerate public docs from live repo statistics")
    p_graph = subparsers.add_parser("graph", help="Emit the typed categorical graph of the repo")
    p_graph.add_argument("--json", action="store_true", help="Emit graph as JSON")
    subparsers.add_parser("intake", help="Show status of source files vs knowledge artifacts")

    # atomize subcommand retirado 2026-05-20 (familia atomic retirada del corpus normativo).

    p_kb_graph = subparsers.add_parser("kb-graph", help="Materialize the knowledge graph from artifacts/knowledge/ artifacts")
    p_kb_graph.add_argument("--json", action="store_true", help="Write graph as JSON to docs/generated/")
    p_kb_graph.add_argument("--check-cycles", action="store_true", help="Exit non-zero if cycles exist in depends graph")
    p_kb_graph.add_argument("--orphans", action="store_true", help="Emit orphan classification report to docs/generated/kb-orphans.md")

    p_promote = subparsers.add_parser("promote", help="Promote a draft artifact from artifacts/knowledge/_SCRIPTORIUM/REVIEW/ to artifacts/knowledge/")
    p_promote.add_argument("path", nargs="?", default=None, help="Path to the draft artifact to promote (omitir si se usa --cohort)")
    p_promote.add_argument(
        "--review",
        default=None,
        help="Optional acceptance review path for atomic bundles; ignored for non-atomic families",
    )
    p_promote.add_argument(
        "--cohort",
        default=None,
        help="Batch-promote all drafts in artifacts/knowledge/_SCRIPTORIUM/REVIEW/{ns}/ as a cohort",
    )

    p_deprecate = subparsers.add_parser("deprecate", help="Dual de promote: marca artefacto productivo como deprecado o retirado")
    p_deprecate.add_argument("path", help="Path al artefacto productivo (AGENT.md / SKILL.md / KNOWLEDGE archivo)")
    p_deprecate.add_argument("--supersedes", default=None, help="URN del artefacto que lo reemplaza (validado contra catalogo)")
    p_deprecate.add_argument("--force", action="store_true", help="Deprecar incluso si hay dependientes activos")
    p_deprecate.add_argument("--retire", action="store_true", help="Transicion deprecado -> retirado (solo regimen agentico)")

    p_transmute = subparsers.add_parser("transmute", help="Proyecta KORA IR a runtime target con matriz de preservacion")
    p_transmute.add_argument("--target", required=True, choices=SUPPORTED_TARGETS,
                             help=f"Runtime target ({', '.join(SUPPORTED_TARGETS)})")
    p_transmute.add_argument("--agent", required=True,
                             help="Agent reference as namespace/name (e.g., kora/curator)")
    p_transmute.add_argument("--dry-run", action="store_true",
                             help="Show what would be done without writing files")
    p_transmute.add_argument("--force-paused", action="store_true",
                             help="Forzar transmutacion hacia target en pausa (gemini, mastra, agentskills)")

    p_roundtrip = subparsers.add_parser("roundtrip-check", help="Verifica la dualidad T_target ∘ Lift_target ≈ id para una habilidad")
    p_roundtrip.add_argument("--target", default="agentskills", choices=["agentskills"],
                              help="Runtime target (solo agentskills en v1.0)")
    p_roundtrip.add_argument("--agent", required=True, help="Skill reference (ns/nombre o nombre)")

    subparsers.add_parser("deploy-status", help="Compara hash IR vs hash deployado en runtimes locales")

    p_deploy = subparsers.add_parser("deploy-builds", help="Despliega outputs _BUILD a runtimes locales")
    p_deploy_artifact = p_deploy.add_mutually_exclusive_group(required=True)
    p_deploy_artifact.add_argument("--agent", help="Agent reference as namespace/name")
    p_deploy_artifact.add_argument("--skill", help="Skill reference as namespace/name")
    p_deploy.add_argument(
        "--target",
        action="append",
        required=True,
        choices=LOCAL_DEPLOY_TARGETS,
        help=(
            "Runtime target. Repeat to deploy multiple targets; "
            "required to avoid accidental broad deploys."
        ),
    )
    p_deploy.add_argument("--home", default=None, help="Home directory for runtime destinations")
    p_deploy.add_argument(
        "--openclaw-workspace",
        default="main",
        help="OpenClaw workspace for skill deploys (default: main)",
    )
    p_deploy_mode = p_deploy.add_mutually_exclusive_group()
    p_deploy_mode.add_argument("--apply", action="store_true", help="Write files; default is dry-run")
    p_deploy_mode.add_argument("--dry-run", action="store_true", help="Report without writing files")
    p_deploy.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow replacing existing runtime files whose content differs",
    )

    p_record = subparsers.add_parser("record-invocation", help="Registra invocacion, retrieval, lead time y verified_at")
    p_record.add_argument("--agent-urn", required=True)
    p_record.add_argument("--input-text", required=True)
    p_record.add_argument("--output-text", required=True)
    p_record.add_argument("--eval-result", required=True)
    p_record.add_argument("--retrieval-urn", action="append", default=[])
    p_record.add_argument("--verified-path", action="append", default=[])
    p_record.add_argument("--source-path", action="append", default=[])

    p_ingest = subparsers.add_parser("ingest", help="Ingesta inversa Lift_R — eleva artefacto runtime foraneo a KORA IR")
    p_ingest.add_argument("--from", dest="from_runtime", required=True,
                          choices=("claude-code", "codex", "gemini", "opencode", "openclaw"),
                          help="Runtime fuente del artefacto foraneo")
    p_ingest.add_argument("--file", help="Path al archivo del artefacto (claude-code / codex / gemini / opencode)")
    p_ingest.add_argument("--workspace", help="Path al workspace (openclaw)")
    p_ingest.add_argument("--namespace", default="kora", help="Namespace KORA destino (default: kora)")
    p_ingest.add_argument("--dry-run", action="store_true", help="Reportar sin escribir")

    p_check = subparsers.add_parser("check", help="Run unified maintenance checks (composable check algebra)")
    p_check.add_argument("--scope", choices=("artifact", "workspace", "repo"), default=None,
                         help="Filter checks by scope")
    p_check.add_argument("--severity", choices=("critical", "high", "medium", "low"), default=None,
                         help="Minimum severity to report")
    p_check.add_argument("--phase", choices=("index", "verify", "lint", "graph"), default=None,
                         help="Filter checks by phase")
    p_check.add_argument("--path", default=None, help="Restrict to a subtree (relative to repo root)")
    p_check.add_argument("--fix", action="store_true", help="Auto-apply canonical fixes where available")
    p_check.add_argument("--list", action="store_true", dest="list_checks",
                         help="List all registered checks without running them")
    p_check.add_argument("--strict", action="store_true", help="Exit non-zero if any check fails")

    p_host = subparsers.add_parser("host", help="Show host role (primary/secondary) per urn:kora:kb:host-roles")
    p_host.add_argument("--verbose", "-v", action="store_true", help="Show actual hostname/machine_id even if matching marker")
    subparsers.add_parser("install-hooks", help="Install KORA versioned git hooks for this clone")
    subparsers.add_parser("doctor", help="Salud operativa agregada (host + checks + staging + handoffs)")
    p_recovery = subparsers.add_parser("recovery-inventory", help="Inventaria KORA canonico vs runtimes locales")
    p_recovery.add_argument("--json", action="store_true", help="Emit inventory as JSON")
    p_recovery.add_argument("--output", default=None, help="Write inventory to a file instead of stdout")

    args = parser.parse_args()

    if args.command == "index":
        cmd_index()
    elif args.command == "resolve":
        cmd_resolve(args.urn)
    elif args.command == "health":
        cmd_health(strict=args.strict)
    elif args.command == "validate":
        cmd_validate(profile=args.profile, cohort=args.cohort)
    elif args.command == "lint-md":
        cmd_lint_md(paths=args.paths, max_lines_per_h2=args.max_lines_per_h2, fix=args.fix)
    elif args.command == "stats":
        cmd_stats_json(json_output=args.json)
    elif args.command == "migrate":
        warn_if_secondary("migrate")
        cmd_migrate(profile=args.profile, dry_run=args.dry_run, cohort=args.cohort)
    elif args.command == "sync-docs":
        cmd_sync_docs()
    elif args.command == "graph":
        cmd_graph(json_output=args.json)
    elif args.command == "intake":
        cmd_intake()
    elif args.command == "kb-graph":
        cmd_kb_graph(json_output=args.json, check_cycles=args.check_cycles, orphans=args.orphans)
    elif args.command == "promote":
        warn_if_secondary("promote")
        if args.cohort:
            cmd_promote_cohort(args.cohort)
        else:
            if not args.path:
                parser.error("promote: path is required unless --cohort is used")
            cmd_promote(args.path, review_path_str=args.review)
    elif args.command == "deprecate":
        warn_if_secondary("deprecate")
        cmd_deprecate(args.path, supersedes=args.supersedes, force=args.force, retire=args.retire)
    elif args.command == "transmute":
        cmd_transmute(target=args.target, agent=args.agent, dry_run=args.dry_run, force_paused=args.force_paused)
    elif args.command == "roundtrip-check":
        cmd_roundtrip_check(agent_ref=args.agent, target=args.target)
    elif args.command == "deploy-status":
        cmd_deploy_status()
    elif args.command == "deploy-builds":
        cmd_deploy_builds(
            agent=args.agent,
            skill=args.skill,
            targets=args.target,
            home=args.home,
            openclaw_workspace=args.openclaw_workspace,
            dry_run=not args.apply,
            overwrite=args.overwrite,
        )
    elif args.command == "record-invocation":
        cmd_record_invocation(
            agent_urn=args.agent_urn,
            input_text=args.input_text,
            output_text=args.output_text,
            eval_result=args.eval_result,
            retrieval_urns=args.retrieval_urn,
            verified_paths=args.verified_path,
            source_paths=args.source_path,
        )
    elif args.command == "ingest":
        cmd_ingest(from_runtime=args.from_runtime, file=args.file,
                   workspace=args.workspace, namespace=args.namespace,
                   dry_run=args.dry_run)
    elif args.command == "check":
        if args.list_checks:
            checks = all_checks()
            print(f"=== KORA Check Registry ({len(checks)} checks) ===\n")
            for c in sorted(checks, key=lambda x: (x.phase, x.severity, x.id)):
                deps = f" (depends: {', '.join(c.depends)})" if c.depends else ""
                print(f"  [{c.severity.upper():8s}] {c.id:24s} scope={c.scope:10s} phase={c.phase:6s} — {c.description}{deps}")
        else:
            print("=== KORA Maintenance Check Pipeline ===\n")
            result = run_checks(
                scope_filter=args.scope,
                severity_min=args.severity,
                phase_filter=args.phase,
                path_filter=args.path,
                emit=True,
            )
            if args.fix and result.diagnostics:
                print(f"\n--- Applying fixes ---")
                fixed = run_fixes(result.diagnostics, emit=True)
                print(f"Fixed {fixed} issue(s)")
            print(f"\n=== Summary ===")
            print(f"  Checks run: {result.checks_run}")
            print(f"  Passed: {result.checks_passed}")
            print(f"  Failed: {result.checks_failed}")
            if result.by_severity:
                print(f"  By severity: {result.by_severity}")
            if result.diagnostics:
                print(f"  Total diagnostics: {len(result.diagnostics)}")
            if args.strict and not result.ok:
                raise SystemExit(1)
    elif args.command == "host":
        cmd_host(verbose=args.verbose)
    elif args.command == "install-hooks":
        cmd_install_hooks()
    elif args.command == "doctor":
        from .doctor import cmd_doctor
        cmd_doctor()
    elif args.command == "recovery-inventory":
        cmd_recovery_inventory(json_output=args.json, output=args.output)
    else:
        parser.print_help()
