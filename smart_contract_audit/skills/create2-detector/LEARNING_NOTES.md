# CREATE2 Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/create2.json`

- Total findings: 2
- Impact distribution: MEDIUM 2

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `attacker` appears repeatedly across findings and is relevant to this tag.
2. `blocklist` appears repeatedly across findings and is relevant to this tag.
3. `https` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `com` appears repeatedly across findings and is relevant to this tag.
6. `code-423n4` appears repeatedly across findings and is relevant to this tag.
7. `fiatdao-findings` appears repeatedly across findings and is relevant to this tag.
8. `creation` appears repeatedly across findings and is relevant to this tag.
9. `target` appears repeatedly across findings and is relevant to this tag.
10. `result` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `initialize`-related logic appears frequently (4 mentions).
2. `update`-related logic appears frequently (2 mentions).
3. `mint`-related logic appears frequently (1 mentions).
4. `transfer`-related logic appears frequently (1 mentions).
5. `set`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `createProxy()`
2. `deployHatsSignerGateAndSafe()`
3. `deployMultiHatsSignerGateAndSafe()`
4. `isContract()`
5. `_isContract()`
6. `createLock()`
7. `increaseAmount()`
8. `increaseUnlockTime()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
