---
_manifest:
  urn: urn:dev:skill:close-the-loop:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Verificar que el trabajo de cada obrero cumple el estándar mínimo de calidad antes de aceptarlo.

## Input/Output

- **Input:** WorkerResult: { worker_id, exit_code, compile_status, lint_status, test_results, diff }
- **Output:** Verdict: { status: green|red, issues: [], corrective_actions: [] }

## Procedimiento

1. Compiló sin errores? Si no → RED.
2. Lint pasó? Si no → RED (pero puede ser auto-fixable).
3. Tests pasaron? Si no → RED.
4. Commits son atómicos (un commit por paquete)? Si no → WARN.
5. Diff es coherente con la intención del paquete? Revisar a nivel arquitectónico, no line-by-line.
6. Si RED: formular instrucciones correctivas para re-despacho.
7. Si GREEN: aceptar y reportar.
8. Steinberger: "Don't read all the code. Watch the stream, look at key parts."

## Signature Output

```
## Verification
- Compile: [ok|fail]
- Lint: [ok|fail — N warnings]
- Tests: [ok|fail — N/M passed]
- Commits: [atomic|multiple]
- Architecture coherence: [ok|concern: ...]
- Verdict: [GREEN|RED]
- Corrective: [instrucciones si RED]
```
