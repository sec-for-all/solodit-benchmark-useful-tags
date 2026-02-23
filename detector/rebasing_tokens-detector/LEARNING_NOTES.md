# Rebasing Tokens Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/rebasing_tokens.json`

- Total findings: 4
- Impact distribution: MEDIUM 3, HIGH 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `await` appears repeatedly across findings and is relevant to this tag.
2. `amount` appears repeatedly across findings and is relevant to this tag.
3. `const` appears repeatedly across findings and is relevant to this tag.
4. `ethers` appears repeatedly across findings and is relevant to this tag.
5. `accounts` appears repeatedly across findings and is relevant to this tag.
6. `exploit` appears repeatedly across findings and is relevant to this tag.
7. `https` appears repeatedly across findings and is relevant to this tag.
8. `github` appears repeatedly across findings and is relevant to this tag.
9. `com` appears repeatedly across findings and is relevant to this tag.
10. `eusd` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `deposit`-related logic appears frequently (78 mentions).
2. `set`-related logic appears frequently (40 mentions).
3. `withdraw`-related logic appears frequently (34 mentions).
4. `borrow`-related logic appears frequently (15 mentions).
5. `transfer`-related logic appears frequently (13 mentions).
6. `mint`-related logic appears frequently (6 mentions).
7. `approve`-related logic appears frequently (2 mentions).
8. `redeem`-related logic appears frequently (2 mentions).

## Representative Function Mentions

1. `deposit()`
2. `withdraw()`
3. `checkWithdrawal()`
4. `rigidRedemption()`
5. `excessIncomeDistribution()`
6. `IERC20()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
