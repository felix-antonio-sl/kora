# Repository Guidelines

## Project Structure & Module Organization

This repository is a workspace-style monorepo. Core reference material lives in `docs/` (`activa/` for active knowledge, `archivo/` for archived material, `inbox/` for untriaged files). Operational memory and GTD files live in `memory/`, especially `memory/gtd/*.md`. Reusable agent behaviors are stored in `skills/*/SKILL.md`. Runnable code is mostly under `projects/`, with the main tested Python package in `projects/leychile-sdk/leychile/`; its tests and fixtures live in `projects/leychile-sdk/tests/`. Small automation entrypoints also exist in `scripts/` and project-local shell scripts such as `projects/air-bridge/start.sh`.

## Build, Test, and Development Commands

Run commands from the relevant project directory, not the repo root.

- `cd projects/leychile-sdk && pip install -e ".[dev]"`: install the SDK plus test and lint dependencies.
- `cd projects/leychile-sdk && pytest`: run the Python test suite.
- `cd projects/leychile-sdk && ruff check .`: lint Python sources.
- `cd projects/leychile-sdk && python -m leychile`: exercise the package entrypoint locally.
- `cd projects/air-bridge && ./start.sh --foreground`: run the bridge in the foreground for debugging.

## Coding Style & Naming Conventions

Python targets 3.10+, uses 4-space indentation, type hints, and module-level docstrings where helpful. Follow the existing `leychile` style: `snake_case` for functions and modules, `PascalCase` for classes, and short, explicit method names. Shell scripts should start with `#!/usr/bin/env bash` and `set -euo pipefail`. Keep Markdown filenames descriptive and usually lowercase with hyphens, for example `architecture-multi-openclaw-slack.md`.

## Testing Guidelines

`pytest` is configured in `projects/leychile-sdk/pyproject.toml` with tests under `tests/`. Name files `test_*.py` and keep fixtures in `tests/fixtures/` or `conftest.py`. Add or update tests for parser, query, cache, or search behavior whenever SDK code changes. There is no repo-wide coverage gate, but new code should ship with direct tests for the touched behavior.

## Commit & Pull Request Guidelines

Recent history uses concise conventional prefixes such as `feat:`, `refactor:`, `memory:`, and `daily:`. Keep commit subjects imperative and scoped, for example `feat: add cache invalidation for query results`. Pull requests should include: a short problem statement, the affected paths, test or verification notes, and screenshots only when UI files such as `canvas/index.html` change. Avoid bundling unrelated memory, docs, and code changes in one PR.
