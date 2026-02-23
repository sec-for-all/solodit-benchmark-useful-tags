---
name: account_abstraction-detector
description: Detect account abstraction-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Account Abstraction Detector

Use this skill when auditing `Account Abstraction`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Account Abstraction` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `https` and related state/accounting side effects.
6. Code paths repeatedly mentioning `sol` and related state/accounting side effects.
7. Code paths repeatedly mentioning `com` and related state/accounting side effects.
8. Code paths repeatedly mentioning `github` and related state/accounting side effects.

## Workflow

1. Review validation flow (`validateUserOp`, nonce checks, signature checks) for replay or bypass paths.
2. Confirm paymaster/postOp accounting cannot undercharge gas or externalize debt to protocol.
3. Check smart-account execution path so unauthorized modules cannot call privileged operations.
4. Verify multisig and AA signer assumptions are not broken by `msg.sender == tx.origin` style checks.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
