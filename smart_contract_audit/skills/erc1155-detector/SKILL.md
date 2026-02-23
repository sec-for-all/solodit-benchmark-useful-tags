---
name: erc1155-detector
description: Detect erc1155-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# ERC1155 Detector

Use this skill when auditing `ERC1155`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `ERC1155` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `order` and related state/accounting side effects.
6. Code paths repeatedly mentioning `uint256` and related state/accounting side effects.
7. Code paths repeatedly mentioning `memory` and related state/accounting side effects.
8. Code paths repeatedly mentioning `sol` and related state/accounting side effects.

## Workflow

1. Verify safe transfer acceptance checks for single and batch transfer paths.
2. Check operator approvals and per-id balance accounting cannot be bypassed.
3. Ensure batch loops keep amount/id arrays aligned and length-equal.
4. Confirm receiver hooks cannot reenter and duplicate mint/burn/transfer effects.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
