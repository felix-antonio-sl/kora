from .catalog import build_catalog_lookup, load_catalog
from .config import KORA_ROOT
from .graph import build_reference_graph
from .workspaces import fragment_exists


def cmd_health(strict=False):
    print("Checking Kora Monorepo Health (Broken links)...")
    doc = load_catalog()
    if not doc or "Catalog" not in doc:
        print("Error: Catalog not found or invalid. Run 'kora index' first.")
        raise SystemExit(1)

    known_urns, urn_to_entry = build_catalog_lookup(doc)
    scanned_files, edges = build_reference_graph()

    broken_links = 0
    broken_fragments = 0
    broken_agent_routes = 0
    invalid_config_entries = 0

    for edge in edges:
        if edge.kind in ("XRef", "TracesTo", "AllowsKB"):
            if not edge.target.startswith("urn:"):
                if edge.kind == "AllowsKB":
                    print(
                        f"[CONFIG] In {edge.source.relative_to(KORA_ROOT)}: non-URN entry '{edge.target}'"
                    )
                    invalid_config_entries += 1
                continue

            if edge.target not in known_urns:
                label = "CONFIG" if edge.kind == "AllowsKB" else "BROKEN"
                print(f"[{label}] In {edge.source.relative_to(KORA_ROOT)}: {edge.target}")
                if edge.kind == "AllowsKB":
                    invalid_config_entries += 1
                else:
                    broken_links += 1
                continue

            if edge.fragment and not fragment_exists(urn_to_entry[edge.target]["file"], edge.fragment):
                print(f"[BROKEN-FRAGMENT] In {edge.source.relative_to(KORA_ROOT)}: {edge.target}#{edge.fragment}")
                broken_fragments += 1

        elif edge.kind == "RoutesToAgent":
            namespace, name = edge.target.split("/", 1)
            if not (KORA_ROOT / "agents" / namespace / name).is_dir():
                print(f"[BROKEN-AGENT] In {edge.source.relative_to(KORA_ROOT)}: {edge.target}")
                broken_agent_routes += 1

    total_broken = broken_links + broken_fragments + broken_agent_routes + invalid_config_entries
    print(f"\nHealth check complete. Scanned {scanned_files} files.")
    if total_broken == 0:
        print("All URN references are healthy!")
    else:
        if broken_links > 0:
            print(f"  {broken_links} broken URN reference(s) in file content.")
        if broken_fragments > 0:
            print(f"  {broken_fragments} broken URN fragment reference(s).")
        if broken_agent_routes > 0:
            print(f"  {broken_agent_routes} broken cross-agent route(s).")
        if invalid_config_entries > 0:
            print(f"  {invalid_config_entries} broken/invalid URN(s) in agent config.json allowed_kb.")
        print(f"  Total: {total_broken} issue(s) found.")
        if strict:
            raise SystemExit(1)
