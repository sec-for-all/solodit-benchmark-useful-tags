# Revert By Sending Dust Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/revert_by_sending_dust.json`

- Total findings: 7
- Impact distribution: MEDIUM 5, HIGH 2

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `amount` appears repeatedly across findings and is relevant to this tag.
2. `uint256` appears repeatedly across findings and is relevant to this tag.
3. `will` appears repeatedly across findings and is relevant to this tag.
4. `tlc` appears repeatedly across findings and is relevant to this tag.
5. `attacker` appears repeatedly across findings and is relevant to this tag.
6. `vesting` appears repeatedly across findings and is relevant to this tag.
7. `schedule` appears repeatedly across findings and is relevant to this tag.
8. `alice` appears repeatedly across findings and is relevant to this tag.
9. `revert` appears repeatedly across findings and is relevant to this tag.
10. `bob` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `transfer`-related logic appears frequently (51 mentions).
2. `deposit`-related logic appears frequently (43 mentions).
3. `set`-related logic appears frequently (35 mentions).
4. `mint`-related logic appears frequently (20 mentions).
5. `repay`-related logic appears frequently (17 mentions).
6. `borrow`-related logic appears frequently (9 mentions).
7. `approve`-related logic appears frequently (4 mentions).
8. `upgrade`-related logic appears frequently (4 mentions).

## Representative Function Mentions

1. `_totalSupply()`
2. `_assetBalance()`
3. `transferLPs()`
4. `balanceOf()`
5. `approveLpOwnership()`
6. `_computeVestedAmount()`
7. `_mintShares()`
8. `address()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
