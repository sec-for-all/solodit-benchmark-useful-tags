# Access Control Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/access_control.json`

- Total findings: 49
- Impact distribution: MEDIUM 20, LOW 2, HIGH 27

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `sol` appears repeatedly across findings and is relevant to this tag.
2. `https` appears repeatedly across findings and is relevant to this tag.
3. `com` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `uint256` appears repeatedly across findings and is relevant to this tag.
6. `blob` appears repeatedly across findings and is relevant to this tag.
7. `code-423n4` appears repeatedly across findings and is relevant to this tag.
8. `public` appears repeatedly across findings and is relevant to this tag.
9. `attacker` appears repeatedly across findings and is relevant to this tag.
10. `new` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (219 mentions).
2. `deposit`-related logic appears frequently (118 mentions).
3. `withdraw`-related logic appears frequently (75 mentions).
4. `mint`-related logic appears frequently (75 mentions).
5. `update`-related logic appears frequently (68 mentions).
6. `swap`-related logic appears frequently (65 mentions).
7. `approve`-related logic appears frequently (61 mentions).
8. `transfer`-related logic appears frequently (58 mentions).

## Representative Function Mentions

1. `offer()`
2. `checkOrder()`
3. `insert()`
4. `setPreferredFeeType()`
5. `payableCall()`
6. `_useNonce()`
7. `withdrawAuction()`
8. `depositAuction()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
