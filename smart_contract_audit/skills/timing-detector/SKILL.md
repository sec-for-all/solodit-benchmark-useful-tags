---
name: timing-detector
description: Detect timing-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Timing Detector

Use this skill when auditing `Timing`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Timing` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `await` and related state/accounting side effects.
6. Code paths repeatedly mentioning `timestamp` and related state/accounting side effects.
7. Code paths repeatedly mentioning `block` and related state/accounting side effects.
8. Code paths repeatedly mentioning `https` and related state/accounting side effects.

## Workflow

1. Inspect timestamp/block-number based checks for exploitable windows.
2. Check deadline comparisons (`<` vs `<=`) for one-block bypass opportunities.
3. Verify epoch rollover and period reset code cannot be front-run for unfair advantage.
4. Ensure time-dependent rewards/fees cannot be manipulated via tiny timing offsets.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
