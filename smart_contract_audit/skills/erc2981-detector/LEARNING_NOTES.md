# ERC2981 Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/erc2981.json`

- Total findings: 6
- Impact distribution: MEDIUM 6

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `royalties` appears repeatedly across findings and is relevant to this tag.
2. `https` appears repeatedly across findings and is relevant to this tag.
3. `sol` appears repeatedly across findings and is relevant to this tag.
4. `com` appears repeatedly across findings and is relevant to this tag.
5. `github` appears repeatedly across findings and is relevant to this tag.
6. `royalty` appears repeatedly across findings and is relevant to this tag.
7. `will` appears repeatedly across findings and is relevant to this tag.
8. `than` appears repeatedly across findings and is relevant to this tag.
9. `recipients` appears repeatedly across findings and is relevant to this tag.
10. `code-423n4` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (17 mentions).
2. `mint`-related logic appears frequently (12 mentions).
3. `initialize`-related logic appears frequently (6 mentions).
4. `update`-related logic appears frequently (5 mentions).
5. `transfer`-related logic appears frequently (2 mentions).
6. `register`-related logic appears frequently (2 mentions).
7. `claim`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `initialize()`
2. `royaltyInfo()`
3. `update()`
4. `updateConfig()`
5. `address()`
6. `setRoyaltyInfo()`
7. `_validatePropertyChange()`
8. `getFees()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
