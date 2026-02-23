# EIP-712 Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/eip_712.json`

- Total findings: 6
- Impact distribution: MEDIUM 5, HIGH 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `sol` appears repeatedly across findings and is relevant to this tag.
2. `uint256` appears repeatedly across findings and is relevant to this tag.
3. `https` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `com` appears repeatedly across findings and is relevant to this tag.
6. `bytes` appears repeatedly across findings and is relevant to this tag.
7. `bytes32` appears repeatedly across findings and is relevant to this tag.
8. `blob` appears repeatedly across findings and is relevant to this tag.
9. `keccak256` appears repeatedly across findings and is relevant to this tag.
10. `digest` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `mint`-related logic appears frequently (23 mentions).
2. `set`-related logic appears frequently (12 mentions).
3. `update`-related logic appears frequently (3 mentions).
4. `pause`-related logic appears frequently (1 mentions).

## Representative Function Mentions

1. `test_sig()`
2. `test_sigShouldBe()`
3. `checkSignature()`
4. `_hashTypedDataV4()`
5. `hashStruct()`
6. `setProfileMetadataURIWithSig()`
7. `postWithSig()`
8. `commentWithSig()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
