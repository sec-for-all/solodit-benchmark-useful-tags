---
name: eip_4758-detector
description: Detect eip-4758-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# EIP-4758 Detector

Use this skill when auditing `EIP-4758`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `EIP-4758` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.

## Workflow

1. Identify assumptions that rely on `SELFDESTRUCT` semantics and mark incompatible behavior.
2. Check cleanup/redeployment patterns that depend on code removal.
3. Verify upgrade/factory flows do not assume storage reset via selfdestruct.
4. Confirm kill-switch design remains effective without account deletion side effects.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
