# Cross Chain Message Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/cross_chain_message.json`

- Total findings: 2
- Impact distribution: HIGH 2

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `status` appears repeatedly across findings and is relevant to this tag.
2. `chakrasettlementhandler` appears repeatedly across findings and is relevant to this tag.
3. `txid` appears repeatedly across findings and is relevant to this tag.
4. `source` appears repeatedly across findings and is relevant to this tag.
5. `cross-chain` appears repeatedly across findings and is relevant to this tag.
6. `uint256` appears repeatedly across findings and is relevant to this tag.
7. `handler` appears repeatedly across findings and is relevant to this tag.
8. `solidity` appears repeatedly across findings and is relevant to this tag.
9. `failed` appears repeatedly across findings and is relevant to this tag.
10. `mode` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (52 mentions).
2. `burn`-related logic appears frequently (14 mentions).
3. `mint`-related logic appears frequently (10 mentions).
4. `transfer`-related logic appears frequently (4 mentions).
5. `deposit`-related logic appears frequently (3 mentions).
6. `update`-related logic appears frequently (2 mentions).

## Representative Function Mentions

1. `receive()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
