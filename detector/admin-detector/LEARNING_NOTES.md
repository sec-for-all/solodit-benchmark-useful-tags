# Admin Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/admin.json`

- Total findings: 36
- Impact distribution: MEDIUM 25, HIGH 11

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `sol` appears repeatedly across findings and is relevant to this tag.
2. `https` appears repeatedly across findings and is relevant to this tag.
3. `com` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `will` appears repeatedly across findings and is relevant to this tag.
6. `code-423n4` appears repeatedly across findings and is relevant to this tag.
7. `external` appears repeatedly across findings and is relevant to this tag.
8. `uint256` appears repeatedly across findings and is relevant to this tag.
9. `solidity` appears repeatedly across findings and is relevant to this tag.
10. `funds` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (185 mentions).
2. `withdraw`-related logic appears frequently (82 mentions).
3. `update`-related logic appears frequently (71 mentions).
4. `transfer`-related logic appears frequently (70 mentions).
5. `deposit`-related logic appears frequently (34 mentions).
6. `swap`-related logic appears frequently (32 mentions).
7. `pause`-related logic appears frequently (29 mentions).
8. `approve`-related logic appears frequently (20 mentions).

## Representative Function Mentions

1. `calculateAndDistributeManagerFees()`
2. `address()`
3. `withdraw()`
4. `issue()`
5. `disableTrading()`
6. `allowance()`
7. `deposit()`
8. `setManager()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
