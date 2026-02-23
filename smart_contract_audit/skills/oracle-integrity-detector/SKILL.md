---
name: oracle-integrity-detector
description: Detect oracle-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Oracle Detector

Use this skill when auditing `Oracle`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Oracle` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `price` and related state/accounting side effects.
6. Code paths repeatedly mentioning `https` and related state/accounting side effects.
7. Code paths repeatedly mentioning `com` and related state/accounting side effects.
8. Code paths repeatedly mentioning `github` and related state/accounting side effects.

## Workflow

1. Check price freshness controls (`updatedAt`, heartbeat, staleness limits) for every consumed feed.
2. Verify decimals normalization and quote/base direction before price usage.
3. Inspect spot/TWAP choice and liquidity assumptions against manipulation scenarios.
4. Confirm fallback oracle routing and failure handling cannot return unsafe defaults.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
