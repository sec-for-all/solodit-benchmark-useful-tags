# Approve Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/approve.json`

- Total findings: 18
- Impact distribution: HIGH 9, MEDIUM 9

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `sol` appears repeatedly across findings and is relevant to this tag.
2. `amount` appears repeatedly across findings and is relevant to this tag.
3. `approve` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `uint256` appears repeatedly across findings and is relevant to this tag.
6. `https` appears repeatedly across findings and is relevant to this tag.
7. `com` appears repeatedly across findings and is relevant to this tag.
8. `redeem` appears repeatedly across findings and is relevant to this tag.
9. `allowance` appears repeatedly across findings and is relevant to this tag.
10. `lock` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `approve`-related logic appears frequently (144 mentions).
2. `set`-related logic appears frequently (83 mentions).
3. `withdraw`-related logic appears frequently (63 mentions).
4. `redeem`-related logic appears frequently (62 mentions).
5. `transfer`-related logic appears frequently (58 mentions).
6. `deposit`-related logic appears frequently (10 mentions).
7. `mint`-related logic appears frequently (8 mentions).
8. `swap`-related logic appears frequently (6 mentions).

## Representative Function Mentions

1. `approve()`
2. `redeem()`
3. `withdraw()`
4. `safeApprove()`
5. `transferFrom()`
6. `withdrawToken()`
7. `redeemToken()`
8. `_setKeyManagerOf()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
