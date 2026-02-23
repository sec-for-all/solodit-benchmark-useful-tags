---
name: eip_165-detector
description: Detect eip-165-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# EIP-165 Detector

Use this skill when auditing `EIP-165`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `EIP-165` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `interface` and related state/accounting side effects.
6. Code paths repeatedly mentioning `supportsinterface` and related state/accounting side effects.
7. Code paths repeatedly mentioning `https` and related state/accounting side effects.
8. Code paths repeatedly mentioning `erc-165` and related state/accounting side effects.

## Workflow

1. Check `supportsInterface` returns true for exactly implemented interfaces and false otherwise.
2. Verify inheritance/override order does not drop parent interface support.
3. Ensure external trust decisions based on EIP-165 also verify expected function behavior.
4. Confirm interface id constants are correct and not custom-mistyped values.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
