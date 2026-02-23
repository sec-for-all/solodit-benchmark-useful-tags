# Account Abstraction Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/account_abstraction.json`

- Total findings: 6
- Impact distribution: LOW 1, MEDIUM 4, HIGH 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `https` appears repeatedly across findings and is relevant to this tag.
2. `sol` appears repeatedly across findings and is relevant to this tag.
3. `com` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `code-423n4` appears repeatedly across findings and is relevant to this tag.
6. `biconomy` appears repeatedly across findings and is relevant to this tag.
7. `smart-contract-wallet` appears repeatedly across findings and is relevant to this tag.
8. `initcode` appears repeatedly across findings and is relevant to this tag.
9. `userop` appears repeatedly across findings and is relevant to this tag.
10. `blob` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `update`-related logic appears frequently (6 mentions).
2. `upgrade`-related logic appears frequently (3 mentions).
3. `deposit`-related logic appears frequently (2 mentions).

## Representative Function Mentions

1. `validateUserOp()`
2. `throw_if()`
3. `_createSenderIfNeeded()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
