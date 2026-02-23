---
name: access-control-detector
description: Detect access control-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Access Control Detector

Use this skill when auditing `Access Control`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Access Control` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `sol` and related state/accounting side effects.
6. Code paths repeatedly mentioning `https` and related state/accounting side effects.
7. Code paths repeatedly mentioning `com` and related state/accounting side effects.
8. Code paths repeatedly mentioning `github` and related state/accounting side effects.

## Workflow

1. List privileged mutators (`set*`, `update*`, `register*`, `withdraw*`) and confirm each has the intended role/owner gate.
2. Check role-admin graph so no low-privilege role can grant itself higher privileges.
3. Verify caller authorization and subject authorization both hold (caller cannot act on arbitrary victim resources).
4. For bridge/admin entrypoints, enforce authenticated sender/domain checks before state mutation.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
