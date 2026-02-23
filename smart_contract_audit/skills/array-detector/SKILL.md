---
name: array-detector
description: Detect array-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Array Detector

Use this skill when auditing `Array`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Array` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `uint256` and related state/accounting side effects.
6. Code paths repeatedly mentioning `order` and related state/accounting side effects.
7. Code paths repeatedly mentioning `https` and related state/accounting side effects.
8. Code paths repeatedly mentioning `github` and related state/accounting side effects.

## Workflow

1. Review push/pop/delete patterns and ensure index-to-item mappings stay synchronized.
2. Check iteration over mutable arrays for skipped/duplicated processing after in-loop mutation.
3. Verify arrays used for payouts or permissions cannot be user-inflated to force gas exhaustion.
4. Confirm deduplication rules when array semantics require uniqueness.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
