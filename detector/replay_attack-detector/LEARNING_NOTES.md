# Replay Attack Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/replay_attack.json`

- Total findings: 14
- Impact distribution: MEDIUM 10, HIGH 4

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `https` appears repeatedly across findings and is relevant to this tag.
2. `sol` appears repeatedly across findings and is relevant to this tag.
3. `com` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `uint256` appears repeatedly across findings and is relevant to this tag.
6. `bytes32` appears repeatedly across findings and is relevant to this tag.
7. `deadline` appears repeatedly across findings and is relevant to this tag.
8. `code-423n4` appears repeatedly across findings and is relevant to this tag.
9. `order` appears repeatedly across findings and is relevant to this tag.
10. `same` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `deposit`-related logic appears frequently (37 mentions).
2. `mint`-related logic appears frequently (30 mentions).
3. `redeem`-related logic appears frequently (21 mentions).
4. `set`-related logic appears frequently (18 mentions).
5. `transfer`-related logic appears frequently (7 mentions).
6. `approve`-related logic appears frequently (4 mentions).
7. `repay`-related logic appears frequently (3 mentions).
8. `claim`-related logic appears frequently (2 mentions).

## Representative Function Mentions

1. `changeOrder()`
2. `setComplete()`
3. `changeRecipientAddress()`
4. `allocateFunds()`
5. `require()`
6. `test_stopRentBatch_payOrders_allDifferentLenders()`
7. `IERC721SeaDrop()`
8. `acceptInvite()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
