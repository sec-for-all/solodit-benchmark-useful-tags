# EIP-4626 Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/eip_4626.json`

- Total findings: 9
- Impact distribution: MEDIUM 7, HIGH 2

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `shares` appears repeatedly across findings and is relevant to this tag.
2. `uint256` appears repeatedly across findings and is relevant to this tag.
3. `assets` appears repeatedly across findings and is relevant to this tag.
4. `https` appears repeatedly across findings and is relevant to this tag.
5. `com` appears repeatedly across findings and is relevant to this tag.
6. `github` appears repeatedly across findings and is relevant to this tag.
7. `amount` appears repeatedly across findings and is relevant to this tag.
8. `code-423n4` appears repeatedly across findings and is relevant to this tag.
9. `publicvault` appears repeatedly across findings and is relevant to this tag.
10. `return` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `deposit`-related logic appears frequently (86 mentions).
2. `withdraw`-related logic appears frequently (71 mentions).
3. `set`-related logic appears frequently (69 mentions).
4. `mint`-related logic appears frequently (52 mentions).
5. `redeem`-related logic appears frequently (34 mentions).
6. `approve`-related logic appears frequently (20 mentions).
7. `transfer`-related logic appears frequently (15 mentions).
8. `burn`-related logic appears frequently (6 mentions).

## Representative Function Mentions

1. `redeem()`
2. `withdraw()`
3. `totalAssets()`
4. `minDepositAmount()`
5. `safeApprove()`
6. `require()`
7. `_redeemFutureEpoch()`
8. `mint()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
