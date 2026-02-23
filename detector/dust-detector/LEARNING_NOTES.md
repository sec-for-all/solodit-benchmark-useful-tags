# Dust Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/dust.json`

- Total findings: 5
- Impact distribution: MEDIUM 5

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `amount` appears repeatedly across findings and is relevant to this tag.
2. `loan` appears repeatedly across findings and is relevant to this tag.
3. `will` appears repeatedly across findings and is relevant to this tag.
4. `cdot` appears repeatedly across findings and is relevant to this tag.
5. `pool` appears repeatedly across findings and is relevant to this tag.
6. `https` appears repeatedly across findings and is relevant to this tag.
7. `github` appears repeatedly across findings and is relevant to this tag.
8. `com` appears repeatedly across findings and is relevant to this tag.
9. `sol` appears repeatedly across findings and is relevant to this tag.
10. `dust` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (14 mentions).
2. `withdraw`-related logic appears frequently (12 mentions).
3. `deposit`-related logic appears frequently (12 mentions).
4. `transfer`-related logic appears frequently (12 mentions).
5. `burn`-related logic appears frequently (8 mentions).
6. `swap`-related logic appears frequently (8 mentions).
7. `mint`-related logic appears frequently (4 mentions).
8. `repay`-related logic appears frequently (3 mentions).

## Representative Function Mentions

1. `withdrawExcessRewards()`
2. `withdraw()`
3. `mint()`
4. `burn()`
5. `dodoMultiswap()`
6. `deposit()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
