# Oracle Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/oracle.json`

- Total findings: 59
- Impact distribution: MEDIUM 34, HIGH 24, LOW 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `price` appears repeatedly across findings and is relevant to this tag.
2. `https` appears repeatedly across findings and is relevant to this tag.
3. `com` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `sol` appears repeatedly across findings and is relevant to this tag.
6. `uint256` appears repeatedly across findings and is relevant to this tag.
7. `will` appears repeatedly across findings and is relevant to this tag.
8. `chainlink` appears repeatedly across findings and is relevant to this tag.
9. `blob` appears repeatedly across findings and is relevant to this tag.
10. `return` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `set`-related logic appears frequently (223 mentions).
2. `update`-related logic appears frequently (144 mentions).
3. `borrow`-related logic appears frequently (82 mentions).
4. `liquidat`-related logic appears frequently (61 mentions).
5. `swap`-related logic appears frequently (59 mentions).
6. `mint`-related logic appears frequently (38 mentions).
7. `redeem`-related logic appears frequently (27 mentions).
8. `transfer`-related logic appears frequently (20 mentions).

## Representative Function Mentions

1. `commit()`
2. `commitRequested()`
3. `latestRoundData()`
4. `latestAnswer()`
5. `_calculateSpTknPerBase()`
6. `fillOrder()`
7. `solidity()`
8. `require()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
