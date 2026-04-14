# Repository Guidelines

## Project Structure & Module Organization
`specs/` defines the governing KORA rules. `schemas/` holds JSON schemas for agent and config validation. `scripts/kora` is the supported CLI entrypoint, with implementation in `scripts/kora_lib/`. Executable workspaces live under `AGENTS/`, published knowledge under `KNOWLEDGE/`, and supporting source material under `source/`. Tests are in `tests/`, while regenerated outputs belong in `docs/generated/` and the materialized catalog lives in `catalog/`.

Treat generated artifacts as derived state: prefer regenerating them through the CLI instead of editing them by hand.

## Build, Test, and Development Commands
Install dependencies with:

```bash
python3 -m pip install -r requirements.txt
```

Core contributor commands:

```bash
python3 scripts/kora index                  # rebuild catalog data
python3 scripts/kora health --strict        # detect broken URNs and graph issues
python3 scripts/kora validate --profile strict
python3 scripts/kora sync-docs              # refresh docs/generated/*
python3 -m unittest discover -s tests       # run the full test suite
```

After structural changes, the normal sequence is `migrate`, `index`, `health`, `validate`, then `sync-docs`.

## Coding Style & Naming Conventions
Python uses 4-space indentation, `snake_case` for functions/modules, and `PascalCase` for `unittest.TestCase` classes. Keep CLI additions inside `scripts/kora_lib/` and expose them via `scripts/kora`. Favor small, direct functions and explicit argument parsing over hidden side effects.

Markdown artifacts should follow the repo’s KORA conventions in `specs/`. Use stable, descriptive filenames and preserve existing uppercase top-level namespaces such as `AGENTS/` and `KNOWLEDGE/`.

## Testing Guidelines
The repo’s automated checks are primarily `unittest`-based, with test files named `test_*.py`. Add or update tests in `tests/` whenever changing CLI behavior, schema enforcement, migrations, or generated outputs. If a change affects derived docs or catalog content, regenerate them and verify the matching tests still pass.

## Commit & Pull Request Guidelines
Recent history follows conventional-style subjects such as `feat(opm): ...` and `refactor(docs): ...`. Prefer `type(scope): imperative summary`, keep scopes specific, and write the subject in one line.

PRs should state the affected area, list the commands you ran, and call out any regenerated artifacts. Include screenshots only when a rendered document or visual output changed.
