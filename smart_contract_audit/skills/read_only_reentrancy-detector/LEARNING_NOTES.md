# Read-only Reentrancy Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/read_only_reentrancy.json`

- Total findings: 6
- Impact distribution: MEDIUM 2, HIGH 4

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `price` appears repeatedly across findings and is relevant to this tag.
2. `ordereddict` appears repeatedly across findings and is relevant to this tag.
3. `name` appears repeatedly across findings and is relevant to this tag.
4. `reentrancy` appears repeatedly across findings and is relevant to this tag.
5. `gas` appears repeatedly across findings and is relevant to this tag.
6. `uint256` appears repeatedly across findings and is relevant to this tag.
7. `virtual` appears repeatedly across findings and is relevant to this tag.
8. `pool` appears repeatedly across findings and is relevant to this tag.
9. `strategy` appears repeatedly across findings and is relevant to this tag.
10. `amount` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `deposit`-related logic appears frequently (43 mentions).
2. `transfer`-related logic appears frequently (41 mentions).
3. `liquidat`-related logic appears frequently (37 mentions).
4. `withdraw`-related logic appears frequently (25 mentions).
5. `update`-related logic appears frequently (20 mentions).
6. `swap`-related logic appears frequently (16 mentions).
7. `mint`-related logic appears frequently (15 mentions).
8. `set`-related logic appears frequently (14 mentions).

## Representative Function Mentions

1. `getReserves()`
2. `BASE_9()`
3. `_swap()`
4. `redeem()`
5. `IWell()`
6. `sharesToUnderlying()`
7. `underlyingToShares()`
8. `remove_liquidity()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
