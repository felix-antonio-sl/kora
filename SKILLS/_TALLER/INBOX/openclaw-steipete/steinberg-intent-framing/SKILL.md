---
name: steinberg-intent-framing
description: Compress vague requests into an executable intent contract before dispatch. Use when the request is broad, fuzzy, high-blast-radius, mixes design and implementation, lacks a clear beneficiary or success criterion, or when the agent risks compensating for ambiguity with throughput, tooling, or premature coding.
---

# Steinberg Intent Framing

Do not replace unclear intent with more code.

## Goal

Turn a fuzzy ask into a small contract that is strong enough to guide execution.

## Output contract

Compress the request into:
- beneficiary
- desired change
- expected benefit
- success criterion
- minimum eval
- autonomy limit
- main risk

## Workflow

1. Name the real beneficiary.
2. State the desired change in one sentence.
3. Separate expected benefit from implementation detail.
4. Define the smallest success criterion that proves direction.
5. Set a minimum eval, what must be checked before calling it good.
6. Name the autonomy limit, what the agent may decide vs what needs human confirmation.
7. Name the main risk.

## Use this when

- the user ask is broad but urgent
- the scope is large or politically loaded
- multiple paths are possible and drift risk is high
- architecture and implementation are mixed together
- the user wants speed but framing is still weak

## Avoid

- converting framing into a giant spec
- inventing strategic goals not present in the ask
- pretending success criteria exist when they do not
- using throughput to hide ambiguity

## Good framing style

- brief
- sharp
- operational
- no motivational filler
- no fake certainty

## When to read more

For examples and anti-patterns, read `references/examples.md`.
