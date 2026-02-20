#!/usr/bin/env python3
import os
import subprocess

# Nivel 1: Foundations
FOUNDATIONS = ['core', 'cat', 'sys']
# Nivel 2: Applied 
APPLIED = ['gn', 'gov', 'legal', 'mgmt']

def main():
    os.chdir('/Users/felixsanhueza/Developer/kora/knowledge/domains')
    
    # Create macro levels
    os.makedirs('../foundations', exist_ok=True)
    os.makedirs('../applied', exist_ok=True)
    os.makedirs('../applied/tde', exist_ok=True) # Explicit TDE domain
    
    for d in FOUNDATIONS:
        if os.path.isdir(d):
            print(f"Moving {d} -> ../foundations/{d}")
            subprocess.run(['git', 'mv', d, f'../foundations/{d}'])
            
    for d in APPLIED:
        if os.path.isdir(d):
            print(f"Moving {d} -> ../applied/{d}")
            subprocess.run(['git', 'mv', d, f'../applied/{d}'])

if __name__ == '__main__':
    main()
