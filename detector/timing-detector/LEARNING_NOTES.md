# Timing Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/timing.json`

- Total findings: 9
- Impact distribution: MEDIUM 8, HIGH 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `await` appears repeatedly across findings and is relevant to this tag.
2. `timestamp` appears repeatedly across findings and is relevant to this tag.
3. `block` appears repeatedly across findings and is relevant to this tag.
4. `https` appears repeatedly across findings and is relevant to this tag.
5. `com` appears repeatedly across findings and is relevant to this tag.
6. `accounts` appears repeatedly across findings and is relevant to this tag.
7. `github` appears repeatedly across findings and is relevant to this tag.
8. `const` appears repeatedly across findings and is relevant to this tag.
9. `ethers` appears repeatedly across findings and is relevant to this tag.
10. `will` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `deposit`-related logic appears frequently (53 mentions).
2. `set`-related logic appears frequently (40 mentions).
3. `update`-related logic appears frequently (27 mentions).
4. `withdraw`-related logic appears frequently (17 mentions).
5. `liquidat`-related logic appears frequently (16 mentions).
6. `borrow`-related logic appears frequently (15 mentions).
7. `claim`-related logic appears frequently (13 mentions).
8. `pause`-related logic appears frequently (10 mentions).

## Representative Function Mentions

1. `claim()`
2. `_updatePrice()`
3. `pauseForUpdate()`
4. `getAccountData()`
5. `getDepositsSinceLastUpdate()`
6. `updateDistribution()`
7. `CLOCK_MODE()`
8. `withdraw()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
