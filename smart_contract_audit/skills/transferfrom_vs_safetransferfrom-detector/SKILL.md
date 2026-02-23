---
name: transferfrom_vs_safetransferfrom-detector
description: Detect transferfrom vs safetransferfrom-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# transferFrom vs safeTransferFrom Detector

Use this skill when auditing `transferFrom vs safeTransferFrom`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `transferFrom vs safeTransferFrom` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `https` and related state/accounting side effects.
6. Code paths repeatedly mentioning `com` and related state/accounting side effects.
7. Code paths repeatedly mentioning `github` and related state/accounting side effects.
8. Code paths repeatedly mentioning `sol` and related state/accounting side effects.

## Workflow

1. Identify NFT transfers that should require receiver checks and confirm `safeTransferFrom` is used.
2. Check use of `transferFrom` to contracts does not lock NFTs permanently.
3. Verify receiver hook return values are enforced in safe transfer paths.
4. Confirm integrations choose transfer method based on recipient type assumptions correctly.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
