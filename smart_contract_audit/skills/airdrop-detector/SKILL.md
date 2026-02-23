---
name: airdrop-detector
description: Detect airdrop-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Airdrop Detector

Use this skill when auditing `Airdrop`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Airdrop` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `nft` and related state/accounting side effects.
6. Code paths repeatedly mentioning `attacker` and related state/accounting side effects.
7. Code paths repeatedly mentioning `unwrap` and related state/accounting side effects.
8. Code paths repeatedly mentioning `tokenids` and related state/accounting side effects.

## Workflow

1. Verify claim eligibility proof binds recipient, amount, and campaign id in one hash.
2. Check one-time claim tracking so repeated claims or partial-claim replay are impossible.
3. Ensure token transfer result is handled and failed transfer cannot still mark claim as completed.
4. Validate leftover/expired airdrop withdrawal rights and timing cannot steal user allocations.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
