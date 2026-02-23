---
name: read_only_reentrancy-detector
description: Detect read-only reentrancy-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Read-only Reentrancy Detector

Use this skill when auditing `Read-only Reentrancy`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Read-only Reentrancy` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `price` and related state/accounting side effects.
6. Code paths repeatedly mentioning `ordereddict` and related state/accounting side effects.
7. Code paths repeatedly mentioning `name` and related state/accounting side effects.
8. Code paths repeatedly mentioning `reentrancy` and related state/accounting side effects.

## Workflow

1. Locate view/read functions that can be reentered during state-changing external interactions.
2. Check cached price/share values read during callbacks for inconsistency with pending state changes.
3. Verify any read-derived decision (health checks, pricing, limits) cannot be manipulated mid-transaction.
4. Use callback-capable token/pool hooks to test stale-read exploitation without direct state write reentry.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
