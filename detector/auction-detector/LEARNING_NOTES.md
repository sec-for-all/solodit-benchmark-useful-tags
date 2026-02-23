# Auction Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/auction.json`

- Total findings: 16
- Impact distribution: LOW 2, HIGH 4, MEDIUM 10

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `auction` appears repeatedly across findings and is relevant to this tag.
2. `price` appears repeatedly across findings and is relevant to this tag.
3. `bid` appears repeatedly across findings and is relevant to this tag.
4. `https` appears repeatedly across findings and is relevant to this tag.
5. `weth` appears repeatedly across findings and is relevant to this tag.
6. `com` appears repeatedly across findings and is relevant to this tag.
7. `github` appears repeatedly across findings and is relevant to this tag.
8. `usdc` appears repeatedly across findings and is relevant to this tag.
9. `will` appears repeatedly across findings and is relevant to this tag.
10. `uint256` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (238 mentions).
2. `deposit`-related logic appears frequently (68 mentions).
3. `withdraw`-related logic appears frequently (51 mentions).
4. `claim`-related logic appears frequently (50 mentions).
5. `mint`-related logic appears frequently (33 mentions).
6. `borrow`-related logic appears frequently (30 mentions).
7. `update`-related logic appears frequently (16 mentions).
8. `transfer`-related logic appears frequently (14 mentions).

## Representative Function Mentions

1. `bid()`
2. `participateToAuction()`
3. `claimAuction()`
4. `settleAuction()`
5. `startRebalance()`
6. `refund()`
7. `requestWithdrawal()`
8. `cancelBid()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
