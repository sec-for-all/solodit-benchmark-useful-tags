# Array Reorder Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/array_reorder.json`

- Total findings: 3
- Impact distribution: MEDIUM 2, HIGH 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `order` appears repeatedly across findings and is relevant to this tag.
2. `index` appears repeatedly across findings and is relevant to this tag.
3. `https` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `com` appears repeatedly across findings and is relevant to this tag.
6. `auction` appears repeatedly across findings and is relevant to this tag.
7. `length` appears repeatedly across findings and is relevant to this tag.
8. `await` appears repeatedly across findings and is relevant to this tag.
9. `blob` appears repeatedly across findings and is relevant to this tag.
10. `will` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (5 mentions).
2. `claim`-related logic appears frequently (4 mentions).
3. `approve`-related logic appears frequently (3 mentions).
4. `redeem`-related logic appears frequently (3 mentions).
5. `mint`-related logic appears frequently (2 mentions).
6. `withdraw`-related logic appears frequently (1 mentions).
7. `swap`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `claimFromIndividualPlugin()`
2. `removePlugin()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
