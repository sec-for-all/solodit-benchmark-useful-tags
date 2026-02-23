---
name: api_inconsistency-detector
description: Detect api inconsistency-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# API Inconsistency Detector

Use this skill when auditing `API Inconsistency`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `API Inconsistency` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `ierc20` and related state/accounting side effects.
6. Code paths repeatedly mentioning `interfaces` and related state/accounting side effects.
7. Code paths repeatedly mentioning `forge-std` and related state/accounting side effects.
8. Code paths repeatedly mentioning `sol` and related state/accounting side effects.

## Workflow

1. Compare paired functions that should be equivalent (view vs stateful, internal vs external wrappers) and list parameter/return differences.
2. Detect inconsistent revert behavior for the same invalid input across endpoints.
3. Check event emission parity across equivalent state changes.
4. Confirm units, decimals, and access requirements are identical for APIs with the same business meaning.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
