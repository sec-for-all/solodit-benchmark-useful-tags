# Rounding Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/rounding.json`

- Total findings: 32
- Impact distribution: HIGH 17, MEDIUM 15

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `uint256` appears repeatedly across findings and is relevant to this tag.
2. `amount` appears repeatedly across findings and is relevant to this tag.
3. `https` appears repeatedly across findings and is relevant to this tag.
4. `com` appears repeatedly across findings and is relevant to this tag.
5. `github` appears repeatedly across findings and is relevant to this tag.
6. `will` appears repeatedly across findings and is relevant to this tag.
7. `sol` appears repeatedly across findings and is relevant to this tag.
8. `rounding` appears repeatedly across findings and is relevant to this tag.
9. `shares` appears repeatedly across findings and is relevant to this tag.
10. `quote` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (182 mentions).
2. `deposit`-related logic appears frequently (102 mentions).
3. `mint`-related logic appears frequently (96 mentions).
4. `withdraw`-related logic appears frequently (71 mentions).
5. `borrow`-related logic appears frequently (65 mentions).
6. `claim`-related logic appears frequently (42 mentions).
7. `transfer`-related logic appears frequently (40 mentions).
8. `update`-related logic appears frequently (34 mentions).

## Representative Function Mentions

1. `_addLiquidity()`
2. `deposit()`
3. `_deposit()`
4. `buyShares()`
5. `buyQuote()`
6. `returnToLender()`
7. `_getMintAmounts()`
8. `mulFloor()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
