---
name: deposit_reward_tokens-detector
description: Detect deposit/reward tokens-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Deposit/Reward tokens Detector

Use this skill when auditing `Deposit/Reward tokens`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Deposit/Reward tokens` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `sol` and related state/accounting side effects.
6. Code paths repeatedly mentioning `https` and related state/accounting side effects.
7. Code paths repeatedly mentioning `amount` and related state/accounting side effects.
8. Code paths repeatedly mentioning `com` and related state/accounting side effects.

## Workflow

1. Separate accounting for deposit token and reward token so one cannot be mistaken for the other.
2. Check reward accrual denominator uses staked supply, not reward token balance.
3. Verify token address updates cannot redirect rewards to attacker-controlled assets.
4. Confirm reward claim and deposit/withdraw sequencing cannot over-claim pending rewards.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
