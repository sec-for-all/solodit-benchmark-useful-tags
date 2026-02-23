# Chainlink Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/chainlink.json`

- Total findings: 25
- Impact distribution: MEDIUM 21, HIGH 3, LOW 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `price` appears repeatedly across findings and is relevant to this tag.
2. `https` appears repeatedly across findings and is relevant to this tag.
3. `chainlink` appears repeatedly across findings and is relevant to this tag.
4. `com` appears repeatedly across findings and is relevant to this tag.
5. `github` appears repeatedly across findings and is relevant to this tag.
6. `uint256` appears repeatedly across findings and is relevant to this tag.
7. `will` appears repeatedly across findings and is relevant to this tag.
8. `sol` appears repeatedly across findings and is relevant to this tag.
9. `blob` appears repeatedly across findings and is relevant to this tag.
10. `stale` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `update`-related logic appears frequently (124 mentions).
2. `set`-related logic appears frequently (103 mentions).
3. `borrow`-related logic appears frequently (19 mentions).
4. `liquidat`-related logic appears frequently (9 mentions).
5. `pause`-related logic appears frequently (9 mentions).
6. `transfer`-related logic appears frequently (7 mentions).
7. `upgrade`-related logic appears frequently (5 mentions).
8. `swap`-related logic appears frequently (5 mentions).

## Representative Function Mentions

1. `solidity()`
2. `latestRoundData()`
3. `_createActionInfo()`
4. `latestAnswer()`
5. `registerMessage()`
6. `IPrice()`
7. `getPrice()`
8. `IPriceOracle()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
