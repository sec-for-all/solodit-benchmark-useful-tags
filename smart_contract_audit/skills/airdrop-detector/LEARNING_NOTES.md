# Airdrop Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/airdrop.json`

- Total findings: 1
- Impact distribution: MEDIUM 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `nft` appears repeatedly across findings and is relevant to this tag.
2. `attacker` appears repeatedly across findings and is relevant to this tag.
3. `unwrap` appears repeatedly across findings and is relevant to this tag.
4. `tokenids` appears repeatedly across findings and is relevant to this tag.
5. `wrap` appears repeatedly across findings and is relevant to this tag.
6. `pair` appears repeatedly across findings and is relevant to this tag.
7. `fractional` appears repeatedly across findings and is relevant to this tag.
8. `some` appears repeatedly across findings and is relevant to this tag.
9. `air` appears repeatedly across findings and is relevant to this tag.
10. `one` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `swap`-related logic appears frequently (6 mentions).
2. `transfer`-related logic appears frequently (4 mentions).
3. `mint`-related logic appears frequently (2 mentions).
4. `burn`-related logic appears frequently (2 mentions).
5. `set`-related logic appears frequently (2 mentions).
6. `deposit`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `getAirDrop()`
2. `wrap()`
3. `unwrap()`
4. `getAirdrop()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
