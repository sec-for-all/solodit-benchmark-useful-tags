---
name: eip_2981-detector
description: Detect eip-2981-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# EIP-2981 Detector

Use this skill when auditing `EIP-2981`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `EIP-2981` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `royalties` and related state/accounting side effects.
6. Code paths repeatedly mentioning `https` and related state/accounting side effects.
7. Code paths repeatedly mentioning `interfaceid` and related state/accounting side effects.
8. Code paths repeatedly mentioning `sol` and related state/accounting side effects.

## Workflow

1. Verify royalty recipient and amount are computed from sale price with correct denominator.
2. Check royalty percentage caps to prevent >100% payouts.
3. Ensure royalty config updates are permissioned and evented.
4. Confirm marketplace integration handles zero-recipient or zero-royalty cases safely.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
