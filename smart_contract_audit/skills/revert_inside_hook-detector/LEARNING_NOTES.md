# Revert Inside Hook Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/revert_inside_hook.json`

- Total findings: 4
- Impact distribution: HIGH 3, MEDIUM 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `credit` appears repeatedly across findings and is relevant to this tag.
2. `sol` appears repeatedly across findings and is relevant to this tag.
3. `will` appears repeatedly across findings and is relevant to this tag.
4. `https` appears repeatedly across findings and is relevant to this tag.
5. `github` appears repeatedly across findings and is relevant to this tag.
6. `com` appears repeatedly across findings and is relevant to this tag.
7. `auction` appears repeatedly across findings and is relevant to this tag.
8. `giantlp` appears repeatedly across findings and is relevant to this tag.
9. `return` appears repeatedly across findings and is relevant to this tag.
10. `nft` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `transfer`-related logic appears frequently (25 mentions).
2. `burn`-related logic appears frequently (9 mentions).
3. `set`-related logic appears frequently (9 mentions).
4. `withdraw`-related logic appears frequently (6 mentions).
5. `deposit`-related logic appears frequently (6 mentions).
6. `borrow`-related logic appears frequently (3 mentions).
7. `update`-related logic appears frequently (2 mentions).
8. `mint`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `settleZoraAuction()`
2. `endAuction()`
3. `_settleZoraAuction()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
