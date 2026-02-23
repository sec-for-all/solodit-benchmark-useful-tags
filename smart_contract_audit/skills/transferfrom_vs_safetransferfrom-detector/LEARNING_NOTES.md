# transferFrom vs safeTransferFrom Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/transferfrom_vs_safetransferfrom.json`

- Total findings: 14
- Impact distribution: MEDIUM 13, HIGH 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `https` appears repeatedly across findings and is relevant to this tag.
2. `com` appears repeatedly across findings and is relevant to this tag.
3. `github` appears repeatedly across findings and is relevant to this tag.
4. `sol` appears repeatedly across findings and is relevant to this tag.
5. `blob` appears repeatedly across findings and is relevant to this tag.
6. `code-423n4` appears repeatedly across findings and is relevant to this tag.
7. `erc20` appears repeatedly across findings and is relevant to this tag.
8. `transferfrom` appears repeatedly across findings and is relevant to this tag.
9. `return` appears repeatedly across findings and is relevant to this tag.
10. `src` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `transfer`-related logic appears frequently (142 mentions).
2. `set`-related logic appears frequently (9 mentions).
3. `approve`-related logic appears frequently (5 mentions).
4. `claim`-related logic appears frequently (4 mentions).
5. `pause`-related logic appears frequently (4 mentions).
6. `withdraw`-related logic appears frequently (3 mentions).
7. `burn`-related logic appears frequently (3 mentions).
8. `redeem`-related logic appears frequently (2 mentions).

## Representative Function Mentions

1. `safeTransferFrom()`
2. `transferFrom()`
3. `ERC20()`
4. `IERC20()`
5. `transfer()`
6. `safeTransfer()`
7. `require()`
8. `unstake()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
