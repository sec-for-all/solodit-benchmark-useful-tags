# EOA Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/eoa.json`

- Total findings: 2
- Impact distribution: HIGH 1, MEDIUM 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `zksync` appears repeatedly across findings and is relevant to this tag.
2. `wallet` appears repeatedly across findings and is relevant to this tag.
3. `smart` appears repeatedly across findings and is relevant to this tag.
4. `alice` appears repeatedly across findings and is relevant to this tag.
5. `eoa` appears repeatedly across findings and is relevant to this tag.
6. `ethereum` appears repeatedly across findings and is relevant to this tag.
7. `chains` appears repeatedly across findings and is relevant to this tag.
8. `different` appears repeatedly across findings and is relevant to this tag.
9. `will` appears repeatedly across findings and is relevant to this tag.
10. `same` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `claim`-related logic appears frequently (2 mentions).
2. `register`-related logic appears frequently (2 mentions).
3. `approve`-related logic appears frequently (1 mentions).
4. `set`-related logic appears frequently (1 mentions).
5. `update`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `registerBLSPublicKeys()`
2. `require()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
