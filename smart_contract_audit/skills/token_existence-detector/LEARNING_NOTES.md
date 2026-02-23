# Token Existence Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/token_existence.json`

- Total findings: 4
- Impact distribution: MEDIUM 4

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `https` appears repeatedly across findings and is relevant to this tag.
2. `github` appears repeatedly across findings and is relevant to this tag.
3. `com` appears repeatedly across findings and is relevant to this tag.
4. `code-423n4` appears repeatedly across findings and is relevant to this tag.
5. `sol` appears repeatedly across findings and is relevant to this tag.
6. `blob` appears repeatedly across findings and is relevant to this tag.
7. `src` appears repeatedly across findings and is relevant to this tag.
8. `astaria` appears repeatedly across findings and is relevant to this tag.
9. `bfc58b42109b839528ab1c21dc9803d663df898` appears repeatedly across findings and is relevant to this tag.
10. `nft` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `transfer`-related logic appears frequently (22 mentions).
2. `set`-related logic appears frequently (22 mentions).
3. `withdraw`-related logic appears frequently (5 mentions).
4. `borrow`-related logic appears frequently (2 mentions).
5. `deposit`-related logic appears frequently (1 mentions).
6. `mint`-related logic appears frequently (1 mentions).
7. `liquidat`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `tokenURI()`
2. `fillOrder()`
3. `require()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
