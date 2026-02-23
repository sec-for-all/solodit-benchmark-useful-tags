# Chain ID Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/chain_id.json`

- Total findings: 1
- Impact distribution: MEDIUM 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `ids` appears repeatedly across findings and is relevant to this tag.
2. `wormholedata` appears repeatedly across findings and is relevant to this tag.
3. `wormhole` appears repeatedly across findings and is relevant to this tag.
4. `evm` appears repeatedly across findings and is relevant to this tag.
5. `lifi` appears repeatedly across findings and is relevant to this tag.
6. `lifidata` appears repeatedly across findings and is relevant to this tag.
7. `different` appears repeatedly across findings and is relevant to this tag.
8. `than` appears repeatedly across findings and is relevant to this tag.
9. `solidity` appears repeatedly across findings and is relevant to this tag.
10. `recipient` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `swap`-related logic appears frequently (2 mentions).
2. `set`-related logic appears frequently (2 mentions).
3. `transfer`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. No stable function-name pattern extracted.

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
