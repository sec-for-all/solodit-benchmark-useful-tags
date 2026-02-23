---
name: array_bound-detector
description: Detect array bound-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Array Bound Detector

Use this skill when auditing `Array Bound`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Array Bound` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `basetoken` and related state/accounting side effects.
6. Code paths repeatedly mentioning `waurapools` and related state/accounting side effects.
7. Code paths repeatedly mentioning `will` and related state/accounting side effects.
8. Code paths repeatedly mentioning `sol` and related state/accounting side effects.

## Workflow

1. Check every indexed read/write for explicit `index < length` enforcement.
2. Inspect unchecked loops and manual pointer arithmetic for off-by-one access.
3. Verify externally supplied array lengths are constrained before nested iteration.
4. Confirm slicing/copy logic cannot read uninitialized or unrelated memory slots.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
