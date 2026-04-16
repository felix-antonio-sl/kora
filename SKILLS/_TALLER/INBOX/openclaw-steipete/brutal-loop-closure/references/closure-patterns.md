# Closure patterns

## Small local fix

Use:
- targeted test
- quick typecheck if relevant
- repo status

Stop when:
- the exact failure mode is covered
- no wider surface was touched

## Medium feature slice

Use:
- tests for touched package
- build for affected app/package
- one realistic usage path
- repo status

Stop when:
- behavior is demonstrated
- integration surface is checked

## High-blast-radius change

Use:
- broader tests
- build(s)
- boundary checks
- scenario replay or live validation
- repo status and artifact review

Stop when:
- the risky boundary is verified
- the summary names remaining uncertainty honestly

## Failure handling

If validation fails:
- do not soften it
- name the failing command
- name the suspected cause
- decide whether to fix now or stop with a crisp blocker
