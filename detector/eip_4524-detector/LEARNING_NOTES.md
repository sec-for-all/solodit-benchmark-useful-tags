# EIP-4524 Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/eip_4524.json`

- Total findings: 1
- Impact distribution: MEDIUM 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `recipient` appears repeatedly across findings and is relevant to this tag.
2. `reason` appears repeatedly across findings and is relevant to this tag.
3. `https` appears repeatedly across findings and is relevant to this tag.
4. `erc20` appears repeatedly across findings and is relevant to this tag.
5. `eip-4524` appears repeatedly across findings and is relevant to this tag.
6. `github` appears repeatedly across findings and is relevant to this tag.
7. `com` appears repeatedly across findings and is relevant to this tag.
8. `erc165` appears repeatedly across findings and is relevant to this tag.
9. `revert` appears repeatedly across findings and is relevant to this tag.
10. `holographerc20` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `transfer`-related logic appears frequently (6 mentions).
2. `register`-related logic appears frequently (2 mentions).
3. `update`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. No stable function-name pattern extracted.

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
