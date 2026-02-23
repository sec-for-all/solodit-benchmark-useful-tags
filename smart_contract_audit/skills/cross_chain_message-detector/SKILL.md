---
name: cross_chain_message-detector
description: Detect cross chain message-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Cross Chain Message Detector

Use this skill when auditing `Cross Chain Message`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Cross Chain Message` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `status` and related state/accounting side effects.
6. Code paths repeatedly mentioning `chakrasettlementhandler` and related state/accounting side effects.
7. Code paths repeatedly mentioning `txid` and related state/accounting side effects.
8. Code paths repeatedly mentioning `source` and related state/accounting side effects.

## Workflow

1. Bind each inbound message to source chain, source contract, destination contract, and nonce.
2. Consume nonce/message hash once; reject duplicates.
3. Check payload decoding and action dispatch so arbitrary function execution is impossible.
4. Verify bridge relayer privileges cannot bypass governance checks on destination chain.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
