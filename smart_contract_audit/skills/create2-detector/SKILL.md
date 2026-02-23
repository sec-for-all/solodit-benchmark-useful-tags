---
name: create2-detector
description: Detect create2-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# CREATE2 Detector

Use this skill when auditing `CREATE2`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `CREATE2` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `attacker` and related state/accounting side effects.
6. Code paths repeatedly mentioning `blocklist` and related state/accounting side effects.
7. Code paths repeatedly mentioning `https` and related state/accounting side effects.
8. Code paths repeatedly mentioning `github` and related state/accounting side effects.

## Workflow

1. Verify salt derivation includes user/context fields required to prevent address collisions.
2. Check predicted address assumptions against actual init code hash used at deployment.
3. Ensure CREATE2 factory cannot be used to front-run and occupy precomputed addresses maliciously.
4. Confirm re-deployment protections after selfdestruct or upgrade flows.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
