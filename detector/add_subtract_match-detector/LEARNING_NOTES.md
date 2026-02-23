# Add/Subtract Match Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/add_subtract_match.json`

- Total findings: 2
- Impact distribution: LOW 1, HIGH 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `usdc` appears repeatedly across findings and is relevant to this tag.
2. `pending` appears repeatedly across findings and is relevant to this tag.
3. `totalclaimablewithdrawals` appears repeatedly across findings and is relevant to this tag.
4. `withdrawal` appears repeatedly across findings and is relevant to this tag.
5. `uint256` appears repeatedly across findings and is relevant to this tag.
6. `operator` appears repeatedly across findings and is relevant to this tag.
7. `staking` appears repeatedly across findings and is relevant to this tag.
8. `voting` appears repeatedly across findings and is relevant to this tag.
9. `power` appears repeatedly across findings and is relevant to this tag.
10. `funds` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `withdraw`-related logic appears frequently (41 mentions).
2. `deposit`-related logic appears frequently (16 mentions).
3. `claim`-related logic appears frequently (15 mentions).
4. `set`-related logic appears frequently (4 mentions).
5. `update`-related logic appears frequently (3 mentions).
6. `approve`-related logic appears frequently (2 mentions).
7. `mint`-related logic appears frequently (1 mentions).
8. `transfer`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `requestWithdrawal()`
2. `getTokenVotingPower()`
3. `_stake()`
4. `_unstake()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
