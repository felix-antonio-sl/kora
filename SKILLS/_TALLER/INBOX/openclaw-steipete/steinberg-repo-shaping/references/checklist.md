# Repo shaping checklist

## Root clarity
- Can a newcomer understand where app, core, infra, docs, and scripts live?
- Is there one obvious way to run, test, and build?
- Does the root tell the truth about current state?

## Operational surfaces
- Are common tasks exposed through package scripts, Make, or CLI?
- Is deploy or debug trapped in tribal knowledge?
- Are logs and generated artifacts easy to reach?

## Boundaries
- Do package and directory boundaries match the real architecture?
- Are there giant mixed-responsibility folders?
- Is shared code truly shared, or just a dumping ground?

## Documentation locality
- Do subsystem docs sit near the subsystem?
- Are historical docs clearly archived?
- Is the repo polluted by stale plans that look active?

## Context cost smells
- too many large files
- duplicate docs with different truth values
- confusing naming
- hidden scripts nobody discovers
- fixtures/examples not tied to validation

## High-value fixes
- create one-command workflows
- archive stale docs
- split hotspots
- add local subsystem README-equivalent docs only where leverage is real
- expose realistic fixtures and validation paths
