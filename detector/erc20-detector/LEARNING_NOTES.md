# ERC20 Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/erc20.json`

- Total findings: 27
- Impact distribution: LOW 2, HIGH 10, MEDIUM 15

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `sol` appears repeatedly across findings and is relevant to this tag.
2. `https` appears repeatedly across findings and is relevant to this tag.
3. `com` appears repeatedly across findings and is relevant to this tag.
4. `amount` appears repeatedly across findings and is relevant to this tag.
5. `github` appears repeatedly across findings and is relevant to this tag.
6. `erc20` appears repeatedly across findings and is relevant to this tag.
7. `will` appears repeatedly across findings and is relevant to this tag.
8. `pool` appears repeatedly across findings and is relevant to this tag.
9. `uint256` appears repeatedly across findings and is relevant to this tag.
10. `blob` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `transfer`-related logic appears frequently (313 mentions).
2. `set`-related logic appears frequently (162 mentions).
3. `withdraw`-related logic appears frequently (55 mentions).
4. `approve`-related logic appears frequently (52 mentions).
5. `liquidat`-related logic appears frequently (42 mentions).
6. `deposit`-related logic appears frequently (34 mentions).
7. `mint`-related logic appears frequently (21 mentions).
8. `burn`-related logic appears frequently (16 mentions).

## Representative Function Mentions

1. `withdraw()`
2. `type()`
3. `address()`
4. `safeApprove()`
5. `from18()`
6. `owner()`
7. `redeem()`
8. `from18Safe()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
