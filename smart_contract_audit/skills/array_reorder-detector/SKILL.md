---
name: array_reorder-detector
description: Detect array reorder-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Array Reorder Detector

Use this skill when auditing `Array Reorder`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Array Reorder` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `order` and related state/accounting side effects.
6. Code paths repeatedly mentioning `index` and related state/accounting side effects.
7. Code paths repeatedly mentioning `https` and related state/accounting side effects.
8. Code paths repeatedly mentioning `github` and related state/accounting side effects.

## Workflow

1. Inspect swap-and-pop and sorting paths to ensure companion mappings are updated to new indices.
2. Check order-dependent logic (priority, queue, ranking) after reorder operations.
3. Verify signatures/proofs referencing array position include stable identifiers, not mutable indices.
4. Confirm reorder does not let users front-run into favorable positions unfairly.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
