# Assembly Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/assembly.json`

- Total findings: 2
- Impact distribution: MEDIUM 1, HIGH 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `wad` appears repeatedly across findings and is relevant to this tag.
2. `https` appears repeatedly across findings and is relevant to this tag.
3. `github` appears repeatedly across findings and is relevant to this tag.
4. `com` appears repeatedly across findings and is relevant to this tag.
5. `sol` appears repeatedly across findings and is relevant to this tag.
6. `scalingfactor` appears repeatedly across findings and is relevant to this tag.
7. `price` appears repeatedly across findings and is relevant to this tag.
8. `blob` appears repeatedly across findings and is relevant to this tag.
9. `expwad` appears repeatedly across findings and is relevant to this tag.
10. `precisemul` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (26 mentions).
2. `mint`-related logic appears frequently (3 mentions).
3. `swap`-related logic appears frequently (3 mentions).
4. `transfer`-related logic appears frequently (2 mentions).
5. `update`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `exp()`
2. `preciseMul()`
3. `expWad()`
4. `preciseDiv()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
