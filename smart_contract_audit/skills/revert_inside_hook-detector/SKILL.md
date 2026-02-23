---
name: revert_inside_hook-detector
description: Detect revert inside hook-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Revert Inside Hook Detector

Use this skill when auditing `Revert Inside Hook`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Revert Inside Hook` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `credit` and related state/accounting side effects.
6. Code paths repeatedly mentioning `sol` and related state/accounting side effects.
7. Code paths repeatedly mentioning `will` and related state/accounting side effects.
8. Code paths repeatedly mentioning `https` and related state/accounting side effects.

## Workflow

1. Review hook callbacks (`onTransferReceived`, `tokensReceived`, NFT receiver hooks) for hard reverts.
2. Ensure external hook failure cannot permanently block user withdrawals or settlements.
3. Check try/catch or fail-open/fail-closed policy is explicit and consistent.
4. Verify hook invocation order does not commit irreversible state before potential revert.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
