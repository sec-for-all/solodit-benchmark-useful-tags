---
name: eip_4337-detector
description: Detect eip-4337-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# EIP-4337 Detector

Use this skill when auditing `EIP-4337`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `EIP-4337` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.

## Workflow

1. Review user operation validation for nonce, signature, and paymaster authorization.
2. Check validation and execution separation so side effects cannot occur during validation.
3. Verify aggregator/paymaster data cannot be swapped post-signature.
4. Ensure prefund and refund accounting cannot be exploited for free execution.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
