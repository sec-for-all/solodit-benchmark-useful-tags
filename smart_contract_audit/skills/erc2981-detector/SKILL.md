---
name: erc2981-detector
description: Detect erc2981-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# ERC2981 Detector

Use this skill when auditing `ERC2981`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `ERC2981` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `royalties` and related state/accounting side effects.
6. Code paths repeatedly mentioning `https` and related state/accounting side effects.
7. Code paths repeatedly mentioning `sol` and related state/accounting side effects.
8. Code paths repeatedly mentioning `com` and related state/accounting side effects.

## Workflow

1. Verify `royaltyInfo` returns valid recipient and amount for given sale price.
2. Check royalty basis points and denominator usage to prevent overpayment.
3. Ensure royalty overrides per-token vs default follow intended precedence.
4. Confirm updates to royalty parameters are properly permissioned.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
