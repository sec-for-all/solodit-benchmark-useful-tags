---
name: add_subtract_match-detector
description: Detect add/subtract match-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Add/Subtract Match Detector

Use this skill when auditing `Add/Subtract Match`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Add/Subtract Match` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `usdc` and related state/accounting side effects.
6. Code paths repeatedly mentioning `pending` and related state/accounting side effects.
7. Code paths repeatedly mentioning `totalclaimablewithdrawals` and related state/accounting side effects.
8. Code paths repeatedly mentioning `withdrawal` and related state/accounting side effects.

## Workflow

1. Pair every increment with the corresponding decrement on the same state variable and execution phase.
2. Detect branches where add occurs but subtract is skipped (or vice versa), leaving permanent accounting drift.
3. Check loop and early-return paths for duplicate subtraction or missed rollback.
4. Assert invariant equations before/after each state transition (e.g., total = sum of parts).

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
