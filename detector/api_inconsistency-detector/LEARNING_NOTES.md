# API Inconsistency Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/api_inconsistency.json`

- Total findings: 2
- Impact distribution: LOW 2

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `ierc20` appears repeatedly across findings and is relevant to this tag.
2. `interfaces` appears repeatedly across findings and is relevant to this tag.
3. `forge-std` appears repeatedly across findings and is relevant to this tag.
4. `sol` appears repeatedly across findings and is relevant to this tag.
5. `makerasset` appears repeatedly across findings and is relevant to this tag.
6. `get` appears repeatedly across findings and is relevant to this tag.
7. `recommended` appears repeatedly across findings and is relevant to this tag.
8. `unnecessary` appears repeatedly across findings and is relevant to this tag.
9. `eth` appears repeatedly across findings and is relevant to this tag.
10. `maker` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (5 mentions).
2. `transfer`-related logic appears frequently (2 mentions).
3. `swap`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `callExecutor()`
2. `decimals()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
