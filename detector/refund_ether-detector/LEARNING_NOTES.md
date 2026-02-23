# Refund Ether Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/refund_ether.json`

- Total findings: 12
- Impact distribution: MEDIUM 10, HIGH 2

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `amount` appears repeatedly across findings and is relevant to this tag.
2. `eth` appears repeatedly across findings and is relevant to this tag.
3. `https` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `com` appears repeatedly across findings and is relevant to this tag.
6. `sol` appears repeatedly across findings and is relevant to this tag.
7. `sent` appears repeatedly across findings and is relevant to this tag.
8. `will` appears repeatedly across findings and is relevant to this tag.
9. `code-423n4` appears repeatedly across findings and is relevant to this tag.
10. `balance` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `borrow`-related logic appears frequently (36 mentions).
2. `transfer`-related logic appears frequently (30 mentions).
3. `deposit`-related logic appears frequently (24 mentions).
4. `swap`-related logic appears frequently (18 mentions).
5. `redeem`-related logic appears frequently (15 mentions).
6. `withdraw`-related logic appears frequently (10 mentions).
7. `repay`-related logic appears frequently (7 mentions).
8. `update`-related logic appears frequently (6 mentions).

## Representative Function Mentions

1. `getEthPayout()`
2. `depositAndRepay()`
3. `close()`
4. `_payoutEth()`
5. `addCollateral()`
6. `addCredit()`
7. `increaseCredit()`
8. `depositAndClose()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
