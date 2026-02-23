---
name: erc777-detector
description: Detect erc777-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# ERC777 Detector

Use this skill when auditing `ERC777`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `ERC777` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `https` and related state/accounting side effects.
6. Code paths repeatedly mentioning `github` and related state/accounting side effects.
7. Code paths repeatedly mentioning `com` and related state/accounting side effects.
8. Code paths repeatedly mentioning `erc777` and related state/accounting side effects.

## Workflow

1. Review send/operatorSend paths that trigger hooks (`tokensToSend`, `tokensReceived`).
2. Check hook-triggered reentrancy around balance and allowance updates.
3. Verify ERC1820 registry lookups cannot be spoofed to unexpected hook targets.
4. Ensure protocol integrations do not assume ERC20-only behavior when token is ERC777.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
