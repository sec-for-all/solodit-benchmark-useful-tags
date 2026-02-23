---
name: dust-detector
description: Detect dust-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Dust Detector

Use this skill when auditing `Dust`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Dust` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `amount` and related state/accounting side effects.
6. Code paths repeatedly mentioning `loan` and related state/accounting side effects.
7. Code paths repeatedly mentioning `will` and related state/accounting side effects.
8. Code paths repeatedly mentioning `cdot` and related state/accounting side effects.

## Workflow

1. Locate minimum-amount checks and ensure operations reject dust that breaks accounting assumptions.
2. Check repeated dust deposits/withdrawals cannot grief queues or inflate state size.
3. Verify dust remainder handling does not strand user funds permanently.
4. Confirm rounding of tiny amounts cannot leak value over many repetitions.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
