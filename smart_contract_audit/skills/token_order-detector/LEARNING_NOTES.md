# Token Order Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/token_order.json`

- Total findings: 1
- Impact distribution: HIGH 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `token0` appears repeatedly across findings and is relevant to this tag.
2. `price0cumulativelast` appears repeatedly across findings and is relevant to this tag.
3. `price1cumulativelast` appears repeatedly across findings and is relevant to this tag.
4. `order` appears repeatedly across findings and is relevant to this tag.
5. `token1` appears repeatedly across findings and is relevant to this tag.
6. `factory` appears repeatedly across findings and is relevant to this tag.
7. `pair` appears repeatedly across findings and is relevant to this tag.
8. `uniswap` appears repeatedly across findings and is relevant to this tag.
9. `matches` appears repeatedly across findings and is relevant to this tag.
10. `internal` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `swap`-related logic appears frequently (10 mentions).
2. `register`-related logic appears frequently (2 mentions).
3. `update`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `IUniswapV2Factory()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
