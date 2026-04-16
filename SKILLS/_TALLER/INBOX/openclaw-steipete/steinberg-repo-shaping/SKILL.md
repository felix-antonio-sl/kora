---
name: steinberg-repo-shaping
description: Shape repositories to be operable, agent-friendly, and low-friction. Use when organizing a repo, auditing structure, reducing context cost, clarifying docs, deciding file/package boundaries, exposing key operations as CLI commands, or when a codebase feels harder to navigate and steer than it should.
---

# Steinberg Repo Shaping

Treat repo shape as context engineering.

## Goal

Make the repository easier to understand, operate, change, and validate for both humans and agents.

## What good shape looks like

- structure is obvious from the root
- important operations have direct commands
- subsystem docs live near the code they explain
- names are clear and stable
- giant files are split at meaningful seams
- runtime, data, and UI boundaries are legible
- examples and fixtures are easy to find
- logs, DB, env, and deploy paths are not tribal knowledge

## Audit order

1. Root layout
2. Operational surfaces, scripts, CLI, make targets, package scripts
3. Subsystem boundaries
4. Documentation locality
5. File size and responsibility hotspots
6. Examples, fixtures, and test realism
7. Build, run, validate, and deploy ergonomics

## Strong interventions

Recommend changes like:
- move docs next to subsystems
- split oversized files by responsibility, not by arbitrary line count
- add one-command entry points for common operations
- make env/auth examples concrete
- create a clearer root narrative
- reduce duplicate or stale docs
- expose logs and validation paths directly

## Avoid

- reorganizing for aesthetics only
- adding folder depth without leverage
- introducing tooling layers that hide the real system
- broad moves without an explicit blast-radius reason

## Output

Return:
- current repo shape assessment
- top structural frictions
- proposed shape improvements
- blast radius of each change
- what can be done incrementally vs what needs coordinated refactor

## When to read more

For concrete repo checkpoints, read `references/checklist.md`.
