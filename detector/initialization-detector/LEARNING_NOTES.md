# Initialization Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/initialization.json`

- Total findings: 15
- Impact distribution: MEDIUM 10, HIGH 5

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `sol` appears repeatedly across findings and is relevant to this tag.
2. `https` appears repeatedly across findings and is relevant to this tag.
3. `com` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `will` appears repeatedly across findings and is relevant to this tag.
6. `code-423n4` appears repeatedly across findings and is relevant to this tag.
7. `self` appears repeatedly across findings and is relevant to this tag.
8. `params` appears repeatedly across findings and is relevant to this tag.
9. `new` appears repeatedly across findings and is relevant to this tag.
10. `blob` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (72 mentions).
2. `initialize`-related logic appears frequently (51 mentions).
3. `mint`-related logic appears frequently (29 mentions).
4. `transfer`-related logic appears frequently (27 mentions).
5. `update`-related logic appears frequently (26 mentions).
6. `deposit`-related logic appears frequently (23 mentions).
7. `upgrade`-related logic appears frequently (10 mentions).
8. `swap`-related logic appears frequently (9 mentions).

## Representative Function Mentions

1. `address()`
2. `_holograph()`
3. `executeInflationRateUpdate()`
4. `constructor()`
5. `_setInitialized()`
6. `startInflation()`
7. `require()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
