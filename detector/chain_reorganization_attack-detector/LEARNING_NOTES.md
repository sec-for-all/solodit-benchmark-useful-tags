# Chain Reorganization Attack Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/chain_reorganization_attack.json`

- Total findings: 18
- Impact distribution: MEDIUM 13, HIGH 5

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `https` appears repeatedly across findings and is relevant to this tag.
2. `com` appears repeatedly across findings and is relevant to this tag.
3. `block` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `will` appears repeatedly across findings and is relevant to this tag.
6. `have` appears repeatedly across findings and is relevant to this tag.
7. `funds` appears repeatedly across findings and is relevant to this tag.
8. `blocks` appears repeatedly across findings and is relevant to this tag.
9. `network` appears repeatedly across findings and is relevant to this tag.
10. `re-org` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `deposit`-related logic appears frequently (21 mentions).
2. `claim`-related logic appears frequently (18 mentions).
3. `set`-related logic appears frequently (16 mentions).
4. `transfer`-related logic appears frequently (9 mentions).
5. `liquidat`-related logic appears frequently (5 mentions).
6. `withdraw`-related logic appears frequently (4 mentions).
7. `update`-related logic appears frequently (3 mentions).
8. `mint`-related logic appears frequently (2 mentions).

## Representative Function Mentions

1. `act()`
2. `move()`
3. `comment()`
4. `confirmTransaction()`
5. `attack()`
6. `defend()`
7. `forgive()`
8. `post()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
