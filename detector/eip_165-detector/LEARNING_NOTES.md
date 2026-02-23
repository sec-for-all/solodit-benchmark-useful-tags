# EIP-165 Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/eip_165.json`

- Total findings: 5
- Impact distribution: LOW 3, MEDIUM 2

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `interface` appears repeatedly across findings and is relevant to this tag.
2. `supportsinterface` appears repeatedly across findings and is relevant to this tag.
3. `https` appears repeatedly across findings and is relevant to this tag.
4. `erc-165` appears repeatedly across findings and is relevant to this tag.
5. `github` appears repeatedly across findings and is relevant to this tag.
6. `com` appears repeatedly across findings and is relevant to this tag.
7. `dss` appears repeatedly across findings and is relevant to this tag.
8. `interfaceid` appears repeatedly across findings and is relevant to this tag.
9. `erc165` appears repeatedly across findings and is relevant to this tag.
10. `sol` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (7 mentions).
2. `register`-related logic appears frequently (7 mentions).
3. `upgrade`-related logic appears frequently (5 mentions).
4. `transfer`-related logic appears frequently (4 mentions).
5. `update`-related logic appears frequently (4 mentions).

## Representative Function Mentions

1. `supportsInterface()`
2. `bytes4()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
