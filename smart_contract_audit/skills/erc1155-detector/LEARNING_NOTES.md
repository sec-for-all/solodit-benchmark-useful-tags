# ERC1155 Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/erc1155.json`

- Total findings: 17
- Impact distribution: MEDIUM 2, HIGH 15

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `order` appears repeatedly across findings and is relevant to this tag.
2. `uint256` appears repeatedly across findings and is relevant to this tag.
3. `memory` appears repeatedly across findings and is relevant to this tag.
4. `sol` appears repeatedly across findings and is relevant to this tag.
5. `create` appears repeatedly across findings and is relevant to this tag.
6. `https` appears repeatedly across findings and is relevant to this tag.
7. `com` appears repeatedly across findings and is relevant to this tag.
8. `github` appears repeatedly across findings and is relevant to this tag.
9. `safe` appears repeatedly across findings and is relevant to this tag.
10. `internal` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (273 mentions).
2. `transfer`-related logic appears frequently (127 mentions).
3. `burn`-related logic appears frequently (34 mentions).
4. `mint`-related logic appears frequently (29 mentions).
5. `swap`-related logic appears frequently (22 mentions).
6. `borrow`-related logic appears frequently (22 mentions).
7. `claim`-related logic appears frequently (18 mentions).
8. `update`-related logic appears frequently (18 mentions).

## Representative Function Mentions

1. `uniswapV2Call()`
2. `onERC1155Receive()`
3. `transferFrom()`
4. `setFallbackHandler()`
5. `doTokenIdsIntersect()`
6. `takeOrders()`
7. `safeTransferFrom()`
8. `matchOneToManyOrders()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
