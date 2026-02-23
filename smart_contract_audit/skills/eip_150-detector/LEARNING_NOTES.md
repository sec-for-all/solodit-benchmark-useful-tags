# EIP-150 Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/eip_150.json`

- Total findings: 1
- Impact distribution: HIGH 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `gas` appears repeatedly across findings and is relevant to this tag.
2. `https` appears repeatedly across findings and is relevant to this tag.
3. `com` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `left` appears repeatedly across findings and is relevant to this tag.
6. `code-423n4` appears repeatedly across findings and is relevant to this tag.
7. `uint256` appears repeatedly across findings and is relevant to this tag.
8. `holograph-findings` appears repeatedly across findings and is relevant to this tag.
9. `dev` appears repeatedly across findings and is relevant to this tag.
10. `gasleft` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (2 mentions).
2. `update`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `executeJob()`
2. `nonRevertingBridgeCall()`
3. `call()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
