---
name: eip_150-detector
description: Detect eip-150-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# EIP-150 Detector

Use this skill when auditing `EIP-150`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `EIP-150` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `gas` and related state/accounting side effects.
6. Code paths repeatedly mentioning `https` and related state/accounting side effects.
7. Code paths repeatedly mentioning `com` and related state/accounting side effects.
8. Code paths repeatedly mentioning `github` and related state/accounting side effects.

## Workflow

1. Review low-level calls that assume full gas forwarding and account for 63/64 rule.
2. Ensure downstream call failure from reduced gas cannot leave partially committed state.
3. Check gas-stipend dependent logic (`transfer`/`send`) for compatibility with target receivers.
4. Verify retry/fallback behavior when inner call gets insufficient gas.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
