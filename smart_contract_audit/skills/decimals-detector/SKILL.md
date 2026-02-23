---
name: decimals-detector
description: Detect decimals-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Decimals Detector

Use this skill when auditing `Decimals`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Decimals` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `decimals` and related state/accounting side effects.
6. Code paths repeatedly mentioning `uint256` and related state/accounting side effects.
7. Code paths repeatedly mentioning `https` and related state/accounting side effects.
8. Code paths repeatedly mentioning `com` and related state/accounting side effects.

## Workflow

1. Find all price, share, and amount formulas that mix tokens/feeds with different decimals.
2. Confirm each formula applies exactly one normalization step per operand into a common precision.
3. Check mul/div ordering to avoid truncation that systematically favors one side.
4. Test extreme decimals pairs (6/18, 8/18, 0/18) for overvaluation and undervaluation outcomes.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
