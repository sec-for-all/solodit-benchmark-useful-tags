# ERC4626 Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/erc4626.json`

- Total findings: 28
- Impact distribution: LOW 2, MEDIUM 16, HIGH 10

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `shares` appears repeatedly across findings and is relevant to this tag.
2. `assets` appears repeatedly across findings and is relevant to this tag.
3. `uint256` appears repeatedly across findings and is relevant to this tag.
4. `https` appears repeatedly across findings and is relevant to this tag.
5. `amount` appears repeatedly across findings and is relevant to this tag.
6. `com` appears repeatedly across findings and is relevant to this tag.
7. `sol` appears repeatedly across findings and is relevant to this tag.
8. `github` appears repeatedly across findings and is relevant to this tag.
9. `src` appears repeatedly across findings and is relevant to this tag.
10. `will` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (374 mentions).
2. `deposit`-related logic appears frequently (355 mentions).
3. `mint`-related logic appears frequently (175 mentions).
4. `withdraw`-related logic appears frequently (140 mentions).
5. `redeem`-related logic appears frequently (92 mentions).
6. `transfer`-related logic appears frequently (91 mentions).
7. `approve`-related logic appears frequently (40 mentions).
8. `burn`-related logic appears frequently (22 mentions).

## Representative Function Mentions

1. `_totalSupply()`
2. `withdraw()`
3. `redeem()`
4. `_assetBalance()`
5. `deposit()`
6. `totalAssets()`
7. `require()`
8. `minDepositAmount()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
