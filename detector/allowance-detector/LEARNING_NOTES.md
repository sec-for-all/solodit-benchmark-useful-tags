# Allowance Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/allowance.json`

- Total findings: 15
- Impact distribution: HIGH 9, MEDIUM 6

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `https` appears repeatedly across findings and is relevant to this tag.
2. `github` appears repeatedly across findings and is relevant to this tag.
3. `com` appears repeatedly across findings and is relevant to this tag.
4. `sol` appears repeatedly across findings and is relevant to this tag.
5. `allowance` appears repeatedly across findings and is relevant to this tag.
6. `uint256` appears repeatedly across findings and is relevant to this tag.
7. `sherlock-audit` appears repeatedly across findings and is relevant to this tag.
8. `blob` appears repeatedly across findings and is relevant to this tag.
9. `src` appears repeatedly across findings and is relevant to this tag.
10. `will` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (86 mentions).
2. `swap`-related logic appears frequently (81 mentions).
3. `approve`-related logic appears frequently (64 mentions).
4. `deposit`-related logic appears frequently (62 mentions).
5. `withdraw`-related logic appears frequently (33 mentions).
6. `transfer`-related logic appears frequently (25 mentions).
7. `redeem`-related logic appears frequently (16 mentions).
8. `mint`-related logic appears frequently (12 mentions).

## Representative Function Mentions

1. `withdraw()`
2. `allowance()`
3. `redeem()`
4. `_addLiquidity()`
5. `safeApprove()`
6. `_deposit()`
7. `deposit()`
8. `_setKeyManagerOf()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
