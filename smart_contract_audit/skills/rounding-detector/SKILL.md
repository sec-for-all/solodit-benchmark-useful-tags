---
name: rounding-detector
description: Detect rounding-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Rounding Detector

Use this skill when auditing `Rounding`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Rounding` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `uint256` and related state/accounting side effects.
6. Code paths repeatedly mentioning `amount` and related state/accounting side effects.
7. Code paths repeatedly mentioning `https` and related state/accounting side effects.
8. Code paths repeatedly mentioning `com` and related state/accounting side effects.

## Workflow

1. Locate integer division and fixed-point math where truncation direction changes payouts or debt.
2. Check whether rounding consistently favors protocol or user as intended by spec.
3. Test repeated small operations for cumulative rounding extraction.
4. Verify preview/quote functions use the same rounding mode as execution functions.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
