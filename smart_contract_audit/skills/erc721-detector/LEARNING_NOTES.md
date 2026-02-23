# ERC721 Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/erc721.json`

- Total findings: 21
- Impact distribution: HIGH 7, LOW 1, MEDIUM 13

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `uint256` appears repeatedly across findings and is relevant to this tag.
2. `order` appears repeatedly across findings and is relevant to this tag.
3. `memory` appears repeatedly across findings and is relevant to this tag.
4. `sol` appears repeatedly across findings and is relevant to this tag.
5. `https` appears repeatedly across findings and is relevant to this tag.
6. `create` appears repeatedly across findings and is relevant to this tag.
7. `github` appears repeatedly across findings and is relevant to this tag.
8. `com` appears repeatedly across findings and is relevant to this tag.
9. `internal` appears repeatedly across findings and is relevant to this tag.
10. `fulfillment` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (262 mentions).
2. `transfer`-related logic appears frequently (130 mentions).
3. `mint`-related logic appears frequently (64 mentions).
4. `approve`-related logic appears frequently (51 mentions).
5. `burn`-related logic appears frequently (43 mentions).
6. `update`-related logic appears frequently (23 mentions).
7. `claim`-related logic appears frequently (20 mentions).
8. `swap`-related logic appears frequently (15 mentions).

## Representative Function Mentions

1. `permit()`
2. `transferFrom()`
3. `safeTransferFrom()`
4. `setFallbackHandler()`
5. `uniswapV2Call()`
6. `_safeMint()`
7. `bytes4()`
8. `onERC721Received()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
