# Decimals Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/decimals.json`

- Total findings: 45
- Impact distribution: MEDIUM 23, LOW 1, HIGH 21

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `decimals` appears repeatedly across findings and is relevant to this tag.
2. `uint256` appears repeatedly across findings and is relevant to this tag.
3. `https` appears repeatedly across findings and is relevant to this tag.
4. `com` appears repeatedly across findings and is relevant to this tag.
5. `github` appears repeatedly across findings and is relevant to this tag.
6. `amount` appears repeatedly across findings and is relevant to this tag.
7. `price` appears repeatedly across findings and is relevant to this tag.
8. `sol` appears repeatedly across findings and is relevant to this tag.
9. `will` appears repeatedly across findings and is relevant to this tag.
10. `blob` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (129 mentions).
2. `deposit`-related logic appears frequently (98 mentions).
3. `swap`-related logic appears frequently (76 mentions).
4. `withdraw`-related logic appears frequently (55 mentions).
5. `mint`-related logic appears frequently (44 mentions).
6. `transfer`-related logic appears frequently (29 mentions).
7. `redeem`-related logic appears frequently (28 mentions).
8. `claim`-related logic appears frequently (21 mentions).

## Representative Function Mentions

1. `exp()`
2. `from18()`
3. `IController()`
4. `type()`
5. `decimals()`
6. `from18Safe()`
7. `preciseMul()`
8. `balance()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
