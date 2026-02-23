---
name: revert_by_sending_dust-detector
description: Detect revert by sending dust-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Revert By Sending Dust Detector

Use this skill when auditing `Revert By Sending Dust`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Revert By Sending Dust` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `amount` and related state/accounting side effects.
6. Code paths repeatedly mentioning `uint256` and related state/accounting side effects.
7. Code paths repeatedly mentioning `will` and related state/accounting side effects.
8. Code paths repeatedly mentioning `tlc` and related state/accounting side effects.

## Workflow

1. Find operations that iterate over token holdings and can be disrupted by tiny unsolicited balances.
2. Check loops and assumptions that `balance == 0` for unsupported assets.
3. Verify attacker-sent dust cannot force division-by-zero or revert-only branches.
4. Add ignore-list or minimum-threshold handling for dust balances in sensitive flows.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
