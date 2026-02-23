---
name: bridge-detector
description: Detect bridge-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Bridge Detector

Use this skill when auditing `Bridge`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Bridge` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `will` and related state/accounting side effects.
6. Code paths repeatedly mentioning `receiver` and related state/accounting side effects.
7. Code paths repeatedly mentioning `sol` and related state/accounting side effects.
8. Code paths repeatedly mentioning `erc20` and related state/accounting side effects.

## Workflow

1. Authenticate inbound bridge messages by trusted sender, source chain id, and expected domain separator.
2. Ensure message ids/nonces are consumed once to prevent replay.
3. Check token mint/unlock amount uses canonical decimals conversion for source vs destination assets.
4. Verify pause/kill-switch can stop bridge execution without trapping already verified withdrawals.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
