---
name: rebasing_tokens-detector
description: Detect rebasing tokens-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Rebasing Tokens Detector

Use this skill when auditing `Rebasing Tokens`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Rebasing Tokens` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `await` and related state/accounting side effects.
6. Code paths repeatedly mentioning `amount` and related state/accounting side effects.
7. Code paths repeatedly mentioning `const` and related state/accounting side effects.
8. Code paths repeatedly mentioning `ethers` and related state/accounting side effects.

## Workflow

1. Check integrations that store absolute token balances across rebases.
2. Verify share-based accounting is used where rebasing assets are supported.
3. Inspect reward/fee calculations for balance changes that happen without transfer events.
4. Confirm debt and collateral logic cannot be broken by sudden supply rebase events.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
