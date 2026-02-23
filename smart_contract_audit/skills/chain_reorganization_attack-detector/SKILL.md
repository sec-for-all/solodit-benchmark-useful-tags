---
name: chain_reorganization_attack-detector
description: Detect chain reorganization attack-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Chain Reorganization Attack Detector

Use this skill when auditing `Chain Reorganization Attack`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Chain Reorganization Attack` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `https` and related state/accounting side effects.
6. Code paths repeatedly mentioning `com` and related state/accounting side effects.
7. Code paths repeatedly mentioning `block` and related state/accounting side effects.
8. Code paths repeatedly mentioning `github` and related state/accounting side effects.

## Workflow

1. Locate actions finalized after too few confirmations and mark reorg-sensitive state transitions.
2. Ensure payout/mint logic waits required confirmation depth before irreversible effects.
3. Check duplicate processing protection when the same event appears in competing branches.
4. Verify watchers/oracles handle block rollback without stale state commitment.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
