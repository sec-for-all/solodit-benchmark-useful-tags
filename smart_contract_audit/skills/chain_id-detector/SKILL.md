---
name: chain_id-detector
description: Detect chain id-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Chain ID Detector

Use this skill when auditing `Chain ID`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Chain ID` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `ids` and related state/accounting side effects.
6. Code paths repeatedly mentioning `wormholedata` and related state/accounting side effects.
7. Code paths repeatedly mentioning `wormhole` and related state/accounting side effects.
8. Code paths repeatedly mentioning `evm` and related state/accounting side effects.

## Workflow

1. Verify signatures include chain id in signed domain or payload.
2. Check cached chain id values are refreshed correctly after forks or L2 migration.
3. Ensure cross-chain components reject messages with unexpected chain id.
4. Confirm permit/order replay across chains is impossible when contract addresses match.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
