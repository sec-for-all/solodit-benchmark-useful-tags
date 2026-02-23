# Reentrancy Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/reentrancy.json`

- Total findings: 59
- Impact distribution: HIGH 39, MEDIUM 20

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `uint256` appears repeatedly across findings and is relevant to this tag.
2. `sol` appears repeatedly across findings and is relevant to this tag.
3. `https` appears repeatedly across findings and is relevant to this tag.
4. `com` appears repeatedly across findings and is relevant to this tag.
5. `github` appears repeatedly across findings and is relevant to this tag.
6. `reentrancy` appears repeatedly across findings and is relevant to this tag.
7. `will` appears repeatedly across findings and is relevant to this tag.
8. `attacker` appears repeatedly across findings and is relevant to this tag.
9. `amount` appears repeatedly across findings and is relevant to this tag.
10. `memory` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (413 mentions).
2. `transfer`-related logic appears frequently (331 mentions).
3. `withdraw`-related logic appears frequently (248 mentions).
4. `mint`-related logic appears frequently (222 mentions).
5. `deposit`-related logic appears frequently (200 mentions).
6. `borrow`-related logic appears frequently (126 mentions).
7. `claim`-related logic appears frequently (124 mentions).
8. `liquidat`-related logic appears frequently (107 mentions).

## Representative Function Mentions

1. `redeem()`
2. `checkTransaction()`
3. `deposit()`
4. `checkAfterExecution()`
5. `withdraw()`
6. `rageQuit()`
7. `settleAuction()`
8. `deboost()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
