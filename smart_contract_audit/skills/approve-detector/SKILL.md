---
name: approve-detector
description: Detect approve-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Approve Detector

Use this skill when auditing `Approve`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Approve` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `sol` and related state/accounting side effects.
6. Code paths repeatedly mentioning `amount` and related state/accounting side effects.
7. Code paths repeatedly mentioning `approve` and related state/accounting side effects.
8. Code paths repeatedly mentioning `github` and related state/accounting side effects.

## Workflow

1. Identify approval update paths and enforce zero-first or safe-increase/safe-decrease pattern where needed.
2. Check signatures/permits for spender, value, nonce, and deadline binding.
3. Verify approvals cannot be granted to forbidden addresses (self, zero, malicious router) where policy disallows.
4. Confirm approval events and stored values remain consistent after failed downstream calls.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
