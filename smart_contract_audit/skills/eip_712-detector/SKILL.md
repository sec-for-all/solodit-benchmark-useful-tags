---
name: eip_712-detector
description: Detect eip-712-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# EIP-712 Detector

Use this skill when auditing `EIP-712`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `EIP-712` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `sol` and related state/accounting side effects.
6. Code paths repeatedly mentioning `uint256` and related state/accounting side effects.
7. Code paths repeatedly mentioning `https` and related state/accounting side effects.
8. Code paths repeatedly mentioning `github` and related state/accounting side effects.

## Workflow

1. Verify domain separator fields (name, version, chainId, verifyingContract) match signed payload expectations.
2. Check struct hash type strings and field order exactly match off-chain signer implementation.
3. Ensure nonce/deadline are included and consumed once.
4. Confirm signature reuse across contracts/chains is blocked by domain separation.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
