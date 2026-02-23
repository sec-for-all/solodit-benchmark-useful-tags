# Transfer Result Check Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/transfer_result_check.json`

- Total findings: 3
- Impact distribution: MEDIUM 2, HIGH 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `assets` appears repeatedly across findings and is relevant to this tag.
2. `sol` appears repeatedly across findings and is relevant to this tag.
3. `https` appears repeatedly across findings and is relevant to this tag.
4. `src` appears repeatedly across findings and is relevant to this tag.
5. `alice` appears repeatedly across findings and is relevant to this tag.
6. `prizevault` appears repeatedly across findings and is relevant to this tag.
7. `balanceof` appears repeatedly across findings and is relevant to this tag.
8. `asserteq` appears repeatedly across findings and is relevant to this tag.
9. `yieldvault` appears repeatedly across findings and is relevant to this tag.
10. `com` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (80 mentions).
2. `transfer`-related logic appears frequently (46 mentions).
3. `withdraw`-related logic appears frequently (30 mentions).
4. `deposit`-related logic appears frequently (15 mentions).
5. `redeem`-related logic appears frequently (15 mentions).
6. `burn`-related logic appears frequently (8 mentions).
7. `mint`-related logic appears frequently (3 mentions).
8. `liquidat`-related logic appears frequently (3 mentions).

## Representative Function Mentions

1. `withdraw()`
2. `redeem()`
3. `_withdraw()`
4. `burn()`
5. `previewWithdraw()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
