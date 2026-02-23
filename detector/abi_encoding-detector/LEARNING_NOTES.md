# ABI Encoding Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/abi_encoding.json`

- Total findings: 4
- Impact distribution: MEDIUM 4

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `bytes` appears repeatedly across findings and is relevant to this tag.
2. `cidnft` appears repeatedly across findings and is relevant to this tag.
3. `tokenuri` appears repeatedly across findings and is relevant to this tag.
4. `https` appears repeatedly across findings and is relevant to this tag.
5. `abi` appears repeatedly across findings and is relevant to this tag.
6. `github` appears repeatedly across findings and is relevant to this tag.
7. `com` appears repeatedly across findings and is relevant to this tag.
8. `encodepacked` appears repeatedly across findings and is relevant to this tag.
9. `memory` appears repeatedly across findings and is relevant to this tag.
10. `sol` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `mint`-related logic appears frequently (16 mentions).
2. `liquidat`-related logic appears frequently (14 mentions).
3. `set`-related logic appears frequently (4 mentions).
4. `transfer`-related logic appears frequently (3 mentions).

## Representative Function Mentions

1. `executeAutomationCloseOrderCallback()`
2. `getTradeValuePure()`
3. `getTradeValue()`
4. `matchAdvancedOrders()`
5. `keccak256()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
