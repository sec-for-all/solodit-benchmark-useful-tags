# Array Bound Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/array_bound.json`

- Total findings: 2
- Impact distribution: HIGH 1, MEDIUM 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `basetoken` appears repeatedly across findings and is relevant to this tag.
2. `waurapools` appears repeatedly across findings and is relevant to this tag.
3. `will` appears repeatedly across findings and is relevant to this tag.
4. `sol` appears repeatedly across findings and is relevant to this tag.
5. `added` appears repeatedly across findings and is relevant to this tag.
6. `rewardratelog` appears repeatedly across findings and is relevant to this tag.
7. `break` appears repeatedly across findings and is relevant to this tag.
8. `reward` appears repeatedly across findings and is relevant to this tag.
9. `https` appears repeatedly across findings and is relevant to this tag.
10. `github` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (10 mentions).
2. `update`-related logic appears frequently (7 mentions).
3. `withdraw`-related logic appears frequently (3 mentions).
4. `deposit`-related logic appears frequently (3 mentions).
5. `mint`-related logic appears frequently (1 mentions).
6. `liquidat`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `withdraw()`
2. `getUpdatedAccTokenPerShare()`
3. `_sendRewardsForNft()`
4. `updatePool()`
5. `setRewardPerSecond()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
