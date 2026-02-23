---
name: erc721checkpointable-detector
description: Detect erc721checkpointable-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# ERC721Checkpointable Detector

Use this skill when auditing `ERC721Checkpointable`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `ERC721Checkpointable` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.

## Workflow

1. Verify checkpoint writes on mint, burn, and transfer update voting/history correctly.
2. Check checkpoint lookup for past blocks returns deterministic values.
3. Ensure delegation changes cannot skip checkpoint updates.
4. Confirm checkpoint arrays remain ordered and append-only.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
