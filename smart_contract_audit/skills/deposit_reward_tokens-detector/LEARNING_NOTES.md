# Deposit/Reward tokens Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/deposit_reward_tokens.json`

- Total findings: 18
- Impact distribution: MEDIUM 5, HIGH 13

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `sol` appears repeatedly across findings and is relevant to this tag.
2. `https` appears repeatedly across findings and is relevant to this tag.
3. `amount` appears repeatedly across findings and is relevant to this tag.
4. `com` appears repeatedly across findings and is relevant to this tag.
5. `github` appears repeatedly across findings and is relevant to this tag.
6. `uint256` appears repeatedly across findings and is relevant to this tag.
7. `rewards` appears repeatedly across findings and is relevant to this tag.
8. `will` appears repeatedly across findings and is relevant to this tag.
9. `blob` appears repeatedly across findings and is relevant to this tag.
10. `reward` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `deposit`-related logic appears frequently (81 mentions).
2. `transfer`-related logic appears frequently (65 mentions).
3. `withdraw`-related logic appears frequently (40 mentions).
4. `mint`-related logic appears frequently (26 mentions).
5. `claim`-related logic appears frequently (25 mentions).
6. `burn`-related logic appears frequently (24 mentions).
7. `update`-related logic appears frequently (24 mentions).
8. `approve`-related logic appears frequently (19 mentions).

## Representative Function Mentions

1. `openPositionFarm()`
2. `closePositionFarm()`
3. `_getDepositedBalance()`
4. `user_checkpoint()`
5. `ERC20()`
6. `mint()`
7. `withdrawInternal()`
8. `batch()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
