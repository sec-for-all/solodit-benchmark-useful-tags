---
name: transferfrom_vs_transfer-detector
description: Detect transferfrom vs transfer-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# transferFrom vs transfer Detector

Use this skill when auditing `transferFrom vs transfer`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `transferFrom vs transfer` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.

## Workflow

1. Check token movement paths for correct function choice based on caller authority.
2. Verify `transferFrom` calls have prior allowance/approval and proper spender identity.
3. Detect places using `transfer` where funds are pulled from third parties.
4. Ensure event/accounting assumptions align with selected transfer method.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
