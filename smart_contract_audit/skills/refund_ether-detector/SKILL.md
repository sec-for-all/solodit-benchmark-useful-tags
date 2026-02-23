---
name: refund_ether-detector
description: Detect refund ether-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Refund Ether Detector

Use this skill when auditing `Refund Ether`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Refund Ether` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `amount` and related state/accounting side effects.
6. Code paths repeatedly mentioning `eth` and related state/accounting side effects.
7. Code paths repeatedly mentioning `https` and related state/accounting side effects.
8. Code paths repeatedly mentioning `github` and related state/accounting side effects.

## Workflow

1. Review refund code paths for amount calculation, recipient selection, and duplicate refund prevention.
2. Ensure refund failure cannot lock core operation unless policy explicitly requires atomicity.
3. Check pull-vs-push refund design to avoid recipient fallback griefing.
4. Verify refund accounting updates happen before external ETH transfer when required.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
