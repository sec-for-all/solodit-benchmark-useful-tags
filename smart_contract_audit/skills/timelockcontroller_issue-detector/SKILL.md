---
name: timelockcontroller_issue-detector
description: Detect timelockcontroller issue-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# TimelockController Issue Detector

Use this skill when auditing `TimelockController Issue`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `TimelockController Issue` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.

## Workflow

1. Verify proposer/executor/canceller roles map to intended governance policy.
2. Check operation id construction includes target, value, calldata, predecessor, and salt.
3. Ensure delay changes cannot be self-shortened without required governance path.
4. Confirm execute/cancel cannot bypass dependency (`predecessor`) requirements.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
