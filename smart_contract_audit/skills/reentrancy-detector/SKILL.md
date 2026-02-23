---
name: reentrancy-detector
description: Detect reentrancy-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Reentrancy Detector

Use this skill when auditing `Reentrancy`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Reentrancy` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `uint256` and related state/accounting side effects.
6. Code paths repeatedly mentioning `sol` and related state/accounting side effects.
7. Code paths repeatedly mentioning `https` and related state/accounting side effects.
8. Code paths repeatedly mentioning `com` and related state/accounting side effects.

## Workflow

1. Identify external calls made before completing critical state updates.
2. Test callback entry from ERC777/ERC721/ERC1155 hooks and low-level call recipients.
3. Check cross-function reentry where function B touches state partially updated by function A.
4. Verify lock coverage across all mutable entrypoints that share accounting state.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
