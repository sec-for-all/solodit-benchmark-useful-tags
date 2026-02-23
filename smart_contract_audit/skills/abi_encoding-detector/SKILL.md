---
name: abi_encoding-detector
description: Detect abi encoding-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# ABI Encoding Detector

Use this skill when auditing `ABI Encoding`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `ABI Encoding` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `bytes` and related state/accounting side effects.
6. Code paths repeatedly mentioning `cidnft` and related state/accounting side effects.
7. Code paths repeatedly mentioning `tokenuri` and related state/accounting side effects.
8. Code paths repeatedly mentioning `https` and related state/accounting side effects.

## Workflow

1. Inspect every `abi.encode`, `abi.encodePacked`, and decode site for type/length alignment between producer and consumer.
2. Flag packed-encoding usage where two dynamic values or mixed-width integers can collide after concatenation.
3. Check selector construction (`abi.encodeWithSelector`/`abi.encodeWithSignature`) for argument order and width mismatches.
4. Verify off-chain signed payload encoding matches on-chain decoding fields exactly, including array and struct layout.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
