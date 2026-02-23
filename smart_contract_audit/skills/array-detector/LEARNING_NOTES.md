# Array Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/array.json`

- Total findings: 5
- Impact distribution: HIGH 3, MEDIUM 2

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `uint256` appears repeatedly across findings and is relevant to this tag.
2. `order` appears repeatedly across findings and is relevant to this tag.
3. `https` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `com` appears repeatedly across findings and is relevant to this tag.
6. `length` appears repeatedly across findings and is relevant to this tag.
7. `erc20tokenstoinclude` appears repeatedly across findings and is relevant to this tag.
8. `sol` appears repeatedly across findings and is relevant to this tag.
9. `index` appears repeatedly across findings and is relevant to this tag.
10. `proposedliquidationamount` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `liquidat`-related logic appears frequently (35 mentions).
2. `deposit`-related logic appears frequently (15 mentions).
3. `set`-related logic appears frequently (8 mentions).
4. `approve`-related logic appears frequently (3 mentions).
5. `initialize`-related logic appears frequently (3 mentions).
6. `redeem`-related logic appears frequently (3 mentions).
7. `withdraw`-related logic appears frequently (1 mentions).
8. `transfer`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. No stable function-name pattern extracted.

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
