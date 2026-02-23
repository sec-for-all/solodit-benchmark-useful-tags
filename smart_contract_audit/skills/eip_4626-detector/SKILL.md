---
name: eip_4626-detector
description: Detect eip-4626-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# EIP-4626 Detector

Use this skill when auditing `EIP-4626`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `EIP-4626` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `shares` and related state/accounting side effects.
6. Code paths repeatedly mentioning `uint256` and related state/accounting side effects.
7. Code paths repeatedly mentioning `assets` and related state/accounting side effects.
8. Code paths repeatedly mentioning `https` and related state/accounting side effects.

## Workflow

1. Check `convertToShares`/`convertToAssets`, `preview*`, and `deposit/mint/withdraw/redeem` stay mathematically consistent.
2. Verify first-deposit and low-liquidity states cannot be used to manipulate share price.
3. Ensure fee logic is applied symmetrically to preview and execution functions.
4. Confirm totalAssets reflects real claimable assets, excluding phantom balances.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
