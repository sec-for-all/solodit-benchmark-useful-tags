---
name: eip_4524-detector
description: Detect eip-4524-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# EIP-4524 Detector

Use this skill when auditing `EIP-4524`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `EIP-4524` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `recipient` and related state/accounting side effects.
6. Code paths repeatedly mentioning `reason` and related state/accounting side effects.
7. Code paths repeatedly mentioning `https` and related state/accounting side effects.
8. Code paths repeatedly mentioning `erc20` and related state/accounting side effects.

## Workflow

1. Verify royalty transfer callbacks follow the EIP-4524 expected receiver flow.
2. Check callback failure handling so token transfer and royalty settlement stay consistent.
3. Ensure royalty metadata and payout fields cannot be spoofed by token sender.
4. Confirm reentrancy from royalty hooks cannot alter sale settlement amounts.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
