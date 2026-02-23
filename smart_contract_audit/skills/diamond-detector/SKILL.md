---
name: diamond-detector
description: Detect diamond-related vulnerabilities in Solidity/EVM code using patterns learned from full-tag findings.
---

# Diamond Detector

Use this skill when auditing `Diamond`-related protocol logic in Solidity/EVM code.

## Detection Targets

1. Tag-specific failure patterns associated with `Diamond` logic.
2. State transitions where protocol invariants can be broken.
3. User-controlled inputs that influence sensitive calculations or permissions.
4. Interactions with external contracts, tokens, or cross-domain components tied to this tag.
5. Code paths repeatedly mentioning `sol` and related state/accounting side effects.
6. Code paths repeatedly mentioning `appstorage` and related state/accounting side effects.
7. Code paths repeatedly mentioning `global` and related state/accounting side effects.
8. Code paths repeatedly mentioning `dexmanagerfacet` and related state/accounting side effects.

## Workflow

1. Check facet cut permissions and ensure only authorized entity can add/replace/remove selectors.
2. Verify selector collisions cannot shadow security-critical functions.
3. Inspect shared storage slot layout across facets for corruption risks.
4. Confirm loupe/introspection reports active selectors correctly after upgrades.

## Remediation Patterns

1. Enforce explicit invariants around critical state transitions.
2. Harden input validation and boundary checks tied to this tag.
3. Reorder logic to commit safe state before risky external effects when applicable.
4. Isolate privileged or high-risk operations behind strict guards and deterministic checks.
5. Add regression tests for adversarial scenarios extracted from historical findings in this tag.
