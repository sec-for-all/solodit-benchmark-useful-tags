---
name: admin-detector
description: Detect admin-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Admin Detector

Use this skill when auditing `Admin`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Admin` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `sol` and related state/accounting side effects.
6. Code paths repeatedly mentioning `https` and related state/accounting side effects.
7. Code paths repeatedly mentioning `com` and related state/accounting side effects.
8. Code paths repeatedly mentioning `github` and related state/accounting side effects.

## Workflow

1. Enumerate all admin-only operations and verify a single authoritative admin source is used.
2. Check admin transfer/accept flows for two-step handover and zero-address protection.
3. Verify emergency admin powers cannot bypass mandatory safety checks (timelock/limits) unintentionally.
4. Confirm admin parameter updates emit events and cannot silently overwrite critical addresses.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
