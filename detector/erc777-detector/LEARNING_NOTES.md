# ERC777 Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/erc777.json`

- Total findings: 11
- Impact distribution: MEDIUM 7, HIGH 4

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `https` appears repeatedly across findings and is relevant to this tag.
2. `github` appears repeatedly across findings and is relevant to this tag.
3. `com` appears repeatedly across findings and is relevant to this tag.
4. `erc777` appears repeatedly across findings and is relevant to this tag.
5. `amount` appears repeatedly across findings and is relevant to this tag.
6. `sol` appears repeatedly across findings and is relevant to this tag.
7. `uint256` appears repeatedly across findings and is relevant to this tag.
8. `code-423n4` appears repeatedly across findings and is relevant to this tag.
9. `order` appears repeatedly across findings and is relevant to this tag.
10. `will` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `transfer`-related logic appears frequently (79 mentions).
2. `set`-related logic appears frequently (44 mentions).
3. `swap`-related logic appears frequently (36 mentions).
4. `deposit`-related logic appears frequently (29 mentions).
5. `mint`-related logic appears frequently (28 mentions).
6. `redeem`-related logic appears frequently (16 mentions).
7. `withdraw`-related logic appears frequently (15 mentions).
8. `claim`-related logic appears frequently (12 mentions).

## Representative Function Mentions

1. `redeem()`
2. `owner()`
3. `deposit()`
4. `BASE_9()`
5. `_swap()`
6. `_redeem()`
7. `transferFrom()`
8. `underlyingBalance()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
