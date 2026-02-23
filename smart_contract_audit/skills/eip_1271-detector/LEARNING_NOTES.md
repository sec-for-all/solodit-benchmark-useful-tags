# EIP-1271 Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/eip_1271.json`

- Total findings: 2
- Impact distribution: MEDIUM 1, HIGH 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `hacker` appears repeatedly across findings and is relevant to this tag.
2. `uint256` appears repeatedly across findings and is relevant to this tag.
3. `transaction` appears repeatedly across findings and is relevant to this tag.
4. `memory` appears repeatedly across findings and is relevant to this tag.
5. `proxy` appears repeatedly across findings and is relevant to this tag.
6. `signatures` appears repeatedly across findings and is relevant to this tag.
7. `returns` appears repeatedly across findings and is relevant to this tag.
8. `eip1271_magic_value` appears repeatedly across findings and is relevant to this tag.
9. `test` appears repeatedly across findings and is relevant to this tag.
10. `sol` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (7 mentions).
2. `update`-related logic appears frequently (5 mentions).
3. `transfer`-related logic appears frequently (2 mentions).
4. `approve`-related logic appears frequently (1 mentions).
5. `upgrade`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `address()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
