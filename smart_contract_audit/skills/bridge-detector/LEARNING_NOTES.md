# Bridge Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/bridge.json`

- Total findings: 7
- Impact distribution: MEDIUM 2, HIGH 5

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `will` appears repeatedly across findings and is relevant to this tag.
2. `receiver` appears repeatedly across findings and is relevant to this tag.
3. `sol` appears repeatedly across findings and is relevant to this tag.
4. `erc20` appears repeatedly across findings and is relevant to this tag.
5. `https` appears repeatedly across findings and is relevant to this tag.
6. `github` appears repeatedly across findings and is relevant to this tag.
7. `com` appears repeatedly across findings and is relevant to this tag.
8. `destination` appears repeatedly across findings and is relevant to this tag.
9. `orchestrator` appears repeatedly across findings and is relevant to this tag.
10. `symbol` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `swap`-related logic appears frequently (16 mentions).
2. `set`-related logic appears frequently (15 mentions).
3. `update`-related logic appears frequently (6 mentions).
4. `transfer`-related logic appears frequently (2 mentions).
5. `approve`-related logic appears frequently (2 mentions).
6. `withdraw`-related logic appears frequently (1 mentions).
7. `deposit`-related logic appears frequently (1 mentions).
8. `pause`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. No stable function-name pattern extracted.

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
