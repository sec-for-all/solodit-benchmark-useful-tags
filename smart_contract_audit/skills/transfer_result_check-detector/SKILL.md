---
name: transfer_result_check-detector
description: Detect transfer result check-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Transfer Result Check Detector

Use this skill when auditing `Transfer Result Check`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Transfer Result Check` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `assets` and related state/accounting side effects.
6. Code paths repeatedly mentioning `sol` and related state/accounting side effects.
7. Code paths repeatedly mentioning `https` and related state/accounting side effects.
8. Code paths repeatedly mentioning `src` and related state/accounting side effects.

## Workflow

1. Find token/ETH transfer calls and ensure success boolean or revert is enforced.
2. Detect silent-failure paths where state is updated despite failed transfer.
3. Check low-level calls for returned data decoding and optional return handling.
4. Verify batched transfers handle partial failure according to explicit policy.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
