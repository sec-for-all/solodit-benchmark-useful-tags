---
name: assembly-detector
description: Detect assembly-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Assembly Detector

Use this skill when auditing `Assembly`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Assembly` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `wad` and related state/accounting side effects.
6. Code paths repeatedly mentioning `https` and related state/accounting side effects.
7. Code paths repeatedly mentioning `github` and related state/accounting side effects.
8. Code paths repeatedly mentioning `com` and related state/accounting side effects.

## Workflow

1. Review memory pointer usage (`0x40`) to avoid overlapping allocations and stale memory reads.
2. Check `calldatacopy`/`mstore` length calculations for truncation or overflow.
3. Verify assembly return/revert data uses correct offset and length.
4. Confirm type casting/sign extension in assembly matches Solidity-level expectations.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
