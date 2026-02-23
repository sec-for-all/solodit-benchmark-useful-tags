---
name: erc721-detector
description: Detect erc721-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# ERC721 Detector

Use this skill when auditing `ERC721`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `ERC721` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `uint256` and related state/accounting side effects.
6. Code paths repeatedly mentioning `order` and related state/accounting side effects.
7. Code paths repeatedly mentioning `memory` and related state/accounting side effects.
8. Code paths repeatedly mentioning `sol` and related state/accounting side effects.

## Workflow

1. Verify ownership and approval checks on transfer and burn paths.
2. Check safe transfer receiver callbacks and prevent unauthorized token seizure.
3. Ensure token existence checks gate metadata and transfer operations.
4. Confirm mint sequencing cannot duplicate token ids under concurrent calls.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
