#!/usr/bin/env python3
"""
KORA Transmuter - Masive URN Refactor (KORA 2.0)

This script scans all yaml, yml and md files in the KORA monorepo
and refactors URNs from the old format:
urn:knowledge:koda:{domain}:{artifact}:{version}
to the new format:
urn:{namespace}:{type}:{artifact}:{version}
"""

import os
import re
import yaml
from pathlib import Path

# Mapping domain to new type
# OLD DOMAINS: agents, skills, tools, catalog, core, domains
TYPE_MAP = {
    'agents': 'agent',
    'skills': 'skill',
    'tools': 'doc',  # Changed based on user's preference to keep it as doc/sys
    'catalog': 'catalog',
    'core': 'kb',
    'domains': 'kb'
}

# Mapping specific artifacts to namespaces based on known context
# If an artifact is not here, we default to 'kora'
NAMESPACE_MAP = {
    'goreologo': 'gn',
    'analista-presupuestario': 'gn',
    'auditor-gore': 'gn',
    'arquitecto-gore': 'gn',
    'gestion_prpto_2026_koda': 'gn',
    'ley_presupuestos_2026_glosas_gores_2026_koda': 'gn',
    'goreNubleCQs_Master': 'gn',
    'manual-ag-fx-v2': 'fxsl',
    'ag-gateway': 'fxsl',
}


def compute_new_urn(old_urn):
    """
    Translates: urn:knowledge:koda:agents:goreologo:1.0.0
    To:         urn:gn:agent:goreologo:1.0.0
    """
    # Regex for standard KODA URN
    # Parts: 1=knowledge, 2=koda, 3=domain, 4=artifact, 5=version
    match = re.match(r'^urn:(knowledge):([a-z0-9-]+):([a-z0-9-]+):([a-z0-9-]+):(.+)$', old_urn)
    
    if not match:
        return old_urn
        
    _, old_ns_base, domain, artifact, version = match.groups()
    
    # 1. Determine Type
    new_type = TYPE_MAP.get(domain, domain)
    
    # 2. Determine Namespace
    # Default is kora. We override if artifact is known to belong to a specific tenant.
    new_ns = 'kora'
    if old_ns_base != 'koda':
        new_ns = old_ns_base # keep if it was e.g. urn:knowledge:gn:...
        
    for k, v in NAMESPACE_MAP.items():
        if k in artifact:
            new_ns = v
            break
            
    # Assemble New URN
    return f"urn:{new_ns}:{new_type}:{artifact}:{version}"

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all URNs in the file text using regex
    # We look for urn:knowledge:...
    old_urns = set(re.findall(r'(urn:knowledge:[a-z0-9-]+:[a-z0-9-]+:[a-z0-9-]+:[a-z0-9.-]+(?:|latest|stable))', content))
    
    if not old_urns:
        return False, 0
    
    new_content = content
    replacements = 0
    
    for old_urn in old_urns:
        new_urn = compute_new_urn(old_urn)
        if new_urn != old_urn:
            new_content = new_content.replace(old_urn, new_urn)
            replacements += 1
            print(f"  [REPLACE] {old_urn} -> {new_urn}")
            
    if replacements > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, replacements
    
    return False, 0

def main():
    base_dir = Path('/Users/felixsanhueza/Developer/kora')
    extensions = ['.yaml', '.yml', '.md', '.json']
    
    print("Starting KORA URN Transmutation...")
    
    total_files = 0
    total_replacements = 0
    
    for ext in extensions:
        for file_path in base_dir.rglob(f'*{ext}'):
            # Skip .git and scripts to not break ourselves
            if '.git' in str(file_path) or 'scripts/kora_transmuter' in str(file_path):
                continue
                
            changed, count = process_file(file_path)
            if changed:
                total_files += 1
                total_replacements += count
                print(f"Updated {file_path.relative_to(base_dir)} ({count} replacements)")
                
    print(f"\nTransmutation complete! Modified {total_files} files with {total_replacements} URN replacements.")

if __name__ == '__main__':
    main()
