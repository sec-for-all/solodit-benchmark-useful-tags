# Calldata Findings - Full Learning Notes

Source: `extracted_from_api/useful_tags_findings/calldata.json`

- Total findings: 1
- Impact distribution: MEDIUM 1

## Coverage Confirmation

All findings in this tag file were processed (full-file learning, no sampling).

## Repeated Signals

1. `swap` appears repeatedly across findings and is relevant to this tag.
2. `exchangefee` appears repeatedly across findings and is relevant to this tag.
3. `https` appears repeatedly across findings and is relevant to this tag.
4. `github` appears repeatedly across findings and is relevant to this tag.
5. `com` appears repeatedly across findings and is relevant to this tag.
6. `sol` appears repeatedly across findings and is relevant to this tag.
7. `sherlock-audit` appears repeatedly across findings and is relevant to this tag.
8. `cardtopuppermit` appears repeatedly across findings and is relevant to this tag.
9. `hardenedtopupproxy` appears repeatedly across findings and is relevant to this tag.
10. `mover` appears repeatedly across findings and is relevant to this tag.

## Frequent Action Surfaces

1. `swap`-related logic appears frequently (9 mentions).

## Representative Function Mentions

1. `CardTopupPermit()`
2. `nonReentrant()`

## Detector Design Inputs

1. Prioritize high-impact state transitions first.
2. Track authorization, accounting, and external interaction boundaries around tag-related logic.
3. Validate invariant preservation before and after user-controlled operations.
