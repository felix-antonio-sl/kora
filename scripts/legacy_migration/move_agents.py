#!/usr/bin/env python3
"""
Ejecuta la reubicación física de agentes según el plan de clustering semántico (MBT v2).
"""
import os
import subprocess

AGENTS_MAPPING = {
    # 1. CORE
    "architect": "core",
    "smith": "core",
    "transformer": "core",
    "taskmaster": "core",
    "orquestador-generico": "core",
    "guardian": "core",
    # 2. ENGINEERING
    "ingeniero-software-composicional": "engineering",
    "ingeniero-sistemas-composicional": "engineering",
    "ingeniero-moltbot-composicional": "engineering",
    "ingeniero-openclaw-composicional": "engineering",
    "ingeniero-goreos": "engineering",
    # 3. ARCHITECTURE
    "arquitecto-sistemas-informacion": "architecture",
    "arquitecto-automatizacion-organizacional": "architecture",
    "arquitecto-categorico": "architecture",
    "arquitecto-orko": "architecture",
    "ontologista-gist": "architecture",
    "cartographer": "architecture",
    "modelador-mbt": "architecture",
    "pensador-generador": "architecture",
    "omega": "architecture",
    # 4. DOMAIN
    "goreologo": "domain/gorenuble",
    "gobernador-virtual": "domain/gorenuble",
    "dgi-virtual": "domain/gorenuble",
    "erp-gore": "domain/gorenuble",
    "crm-ipr": "domain/gorenuble",
    "eacs": "domain/gorenuble",
    "digitrans": "domain/tde",
    "digitrans-gore": "domain/tde",
    "asesor-juridico": "domain/legal_med",
    "abogado-legislacion-medica": "domain/legal_med",
    "medico-urgencias": "domain/legal_med",
    "visionario": "domain/strategy",
    "estratega-comunicacional": "domain/strategy",
    "banca-inversion": "domain/strategy",
    "ar-virtual": "domain/strategy",
    # 5. QA_OPS
    "tester": "qa_ops",
    "sim-orchestrator": "qa_ops",
    "ci-assistant": "qa_ops",
}

# Add korvo
AGENTS_MAPPING["korvo-assistant"] = "qa_ops"  # Consider korvo an ops tool


def main():
    os.chdir("/Users/felixsanhueza/Developer/kora/agents")

    # Create dirs
    clusters = set(AGENTS_MAPPING.values())
    for cluster in clusters:
        os.makedirs(cluster, exist_ok=True)

    for agent, cluster in AGENTS_MAPPING.items():
        if os.path.isdir(agent):
            target = f"{cluster}/{agent}"
            print(f"Moving {agent} -> {target}")
            # Use git mv since user initialized git
            subprocess.run(["git", "mv", agent, target])

    # Check leftovers
    print("\nLeftover directories in agents/ root:")
    subprocess.run(["ls", "-d", "*/"])


if __name__ == "__main__":
    main()
