import argparse

from .audit import cmd_health
from .catalog import cmd_index, cmd_resolve
from .commands import cmd_migrate, cmd_stats_json, cmd_sync_docs
from .graph import cmd_graph
from .intake import cmd_intake
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
        help="Markdown file or directory to lint. Defaults to knowledge/ and drafts/",
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
        choices=("legacy", "transitional", "strict"),
        default="transitional",
        help="Migration profile",
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
        cmd_migrate(profile=args.profile, dry_run=args.dry_run, cohort=args.cohort)
    elif args.command == "sync-docs":
        cmd_sync_docs()
    elif args.command == "graph":
        cmd_graph(json_output=args.json)
    elif args.command == "intake":
        cmd_intake()
    else:
        parser.print_help()
