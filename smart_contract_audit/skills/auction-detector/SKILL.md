---
name: auction-detector
description: Detect auction-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Auction Detector

Use this skill when auditing `Auction`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Auction` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `auction` and related state/accounting side effects.
6. Code paths repeatedly mentioning `price` and related state/accounting side effects.
7. Code paths repeatedly mentioning `bid` and related state/accounting side effects.
8. Code paths repeatedly mentioning `https` and related state/accounting side effects.

## Workflow

1. Verify bid acceptance rules: minimum increment, deadline, and bidder eligibility.
2. Check settlement picks exactly one winner and cannot be executed twice.
3. Confirm refund path always returns losing bids and cannot be blocked by recipient behavior.
4. Inspect final asset transfer so non-winners cannot withdraw auctioned collateral.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
