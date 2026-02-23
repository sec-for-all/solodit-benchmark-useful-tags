---
name: calldata-detector
description: Detect calldata-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Calldata Detector

Use this skill when auditing `Calldata`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Calldata` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `swap` and related state/accounting side effects.
6. Code paths repeatedly mentioning `exchangefee` and related state/accounting side effects.
7. Code paths repeatedly mentioning `https` and related state/accounting side effects.
8. Code paths repeatedly mentioning `github` and related state/accounting side effects.

## Workflow

1. Inspect dynamic-offset decoding and ensure offsets point inside calldata bounds.
2. Check nested dynamic types for overlapping or forged length fields.
3. Verify function selectors map to intended parameter schema only.
4. Confirm calldata forwarding preserves expected argument layout across proxy/router layers.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
