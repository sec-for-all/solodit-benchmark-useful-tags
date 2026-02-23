---
name: erc20-detector
description: Detect erc20-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# ERC20 Detector

Use this skill when auditing `ERC20`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `ERC20` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `sol` and related state/accounting side effects.
6. Code paths repeatedly mentioning `https` and related state/accounting side effects.
7. Code paths repeatedly mentioning `com` and related state/accounting side effects.
8. Code paths repeatedly mentioning `amount` and related state/accounting side effects.

## Workflow

1. Check transfer/transferFrom return value handling for non-standard tokens.
2. Verify totalSupply and balance updates preserve conservation across mint/burn/transfer.
3. Inspect allowance edge cases (infinite allowance, approve race).
4. Confirm fee-on-transfer/rebasing tokens are handled explicitly where assumptions require standard ERC20 behavior.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
