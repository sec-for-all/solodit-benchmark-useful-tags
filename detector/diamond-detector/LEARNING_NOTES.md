# Diamond Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/diamond.json`

- Total findings: 1
- Impact distribution: HIGH 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `sol` appears repeatedly across findings and is relevant to this tag.
2. `appstorage` appears repeatedly across findings and is relevant to this tag.
3. `global` appears repeatedly across findings and is relevant to this tag.
4. `dexmanagerfacet` appears repeatedly across findings and is relevant to this tag.
5. `getstorage` appears repeatedly across findings and is relevant to this tag.
6. `pattern` appears repeatedly across findings and is relevant to this tag.
7. `swapper` appears repeatedly across findings and is relevant to this tag.
8. `variable` appears repeatedly across findings and is relevant to this tag.
9. `overlap` appears repeatedly across findings and is relevant to this tag.
10. `uses` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `swap`-related logic appears frequently (5 mentions).

## Representative Function Mentions

1. `getStorage()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
