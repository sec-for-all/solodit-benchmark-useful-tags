---
name: token_existence-detector
description: Detect token existence-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Token Existence Detector

Use this skill when auditing `Token Existence`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Token Existence` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `https` and related state/accounting side effects.
6. Code paths repeatedly mentioning `github` and related state/accounting side effects.
7. Code paths repeatedly mentioning `com` and related state/accounting side effects.
8. Code paths repeatedly mentioning `code-423n4` and related state/accounting side effects.

## Workflow

1. Verify every token-id operation checks existence before read/write.
2. Check burn paths clear existence markers and approvals consistently.
3. Ensure metadata queries for nonexistent ids follow expected revert/return policy.
4. Confirm mint race conditions cannot expose transient nonexistent state to external calls.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
