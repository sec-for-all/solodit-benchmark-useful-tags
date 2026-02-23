---
name: token_order-detector
description: Detect token order-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Token Order Detector

Use this skill when auditing `Token Order`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Token Order` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `token0` and related state/accounting side effects.
6. Code paths repeatedly mentioning `price0cumulativelast` and related state/accounting side effects.
7. Code paths repeatedly mentioning `price1cumulativelast` and related state/accounting side effects.
8. Code paths repeatedly mentioning `order` and related state/accounting side effects.

## Workflow

1. Check pair/pool/token ordering assumptions (token0/token1) in pricing and accounting.
2. Verify formula direction changes when token order flips.
3. Ensure stored order and runtime discovered order are reconciled before computation.
4. Test both token permutations for symmetric correctness.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
