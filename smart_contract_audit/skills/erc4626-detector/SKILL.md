---
name: erc4626-detector
description: Detect erc4626-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# ERC4626 Detector

Use this skill when auditing `ERC4626`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `ERC4626` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `shares` and related state/accounting side effects.
6. Code paths repeatedly mentioning `assets` and related state/accounting side effects.
7. Code paths repeatedly mentioning `uint256` and related state/accounting side effects.
8. Code paths repeatedly mentioning `https` and related state/accounting side effects.

## Workflow

1. Test deposit/mint and withdraw/redeem parity under fee and rounding scenarios.
2. Check donation and inflation attacks around low-share-supply states.
3. Ensure `max*` and `preview*` functions match actual execution constraints.
4. Verify asset/share decimal conversion is consistent across all methods.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
