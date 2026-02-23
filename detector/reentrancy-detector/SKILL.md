---
name: reentrancy-detector
description: Detect exploitable reentrancy in Solidity/EVM code, including classic CEI violations, token-hook reentrancy (ERC777/ERC721/ERC1155), and cross-function reentrancy paths.
---

# Reentrancy Detector

Use this skill when auditing smart contracts for reentrancy risk.

## Detection Targets

Focus on these high-yield patterns:

1. External interaction before critical state update.
2. Missing or bypassable reentrancy lock on write paths.
3. Token callback reentry surfaces:
   - ERC777 `tokensReceived`
   - ERC721/ERC1155 `onERC721Received` / `onERC1155Received`
   - `safeTransferFrom`, `_safeMint`, `_safeTransfer`
4. Cross-function reentrancy:
   - Function A makes external call, callback enters function B that shares mutable state.
5. Read-only reentrancy where stale reads can corrupt accounting/pricing.

## Workflow

1. Build write-path map:
   - List functions that mutate balances, debts, shares, positions, rewards, approvals, limits.
2. Mark interaction points:
   - Low-level `.call`, token transfer/mint/burn, router/bridge/oracle callbacks, hook-based token ops.
3. For each interaction point, verify CEI:
   - Checks first, then all state commits, then external call.
4. Check lock coverage:
   - Ensure lock exists on every reachable write path touching shared state, not only one function.
5. Attempt callback path:
   - Model attacker contract fallback/hook to reenter same or sibling function before state finalization.
6. Validate exploitability:
   - Confirm an invariant can be broken (double claim, over-mint, over-withdraw, debt bypass, limit bypass).

## False Positive Filters

Only report as valid if at least one is true:

1. State used for permission/accounting is updated after external interaction.
2. Lock is absent, incorrectly scoped, or can be bypassed by entering another mutable function.
3. Callback-capable token flow exists and can be attacker-controlled.

Downgrade or reject if:

1. External call is to trusted immutable contract with no user-controlled callback path.
2. Reentry can happen but no value/invariant impact is possible.
3. Lock and CEI both hold across all reachable paths.

## Severity Heuristic

1. High: direct fund theft, over-mint, debt cancellation, or protocol insolvency.
2. Medium: grief/DoS, temporary accounting skew, unfair fee bypass with bounded loss.
3. Low: theoretical or non-exploitable reentry without economic impact.

## Output Format

For each finding, output:

1. `title`: short exploit statement.
2. `location`: file + function + line.
3. `root_cause`: precise ordering or lock flaw.
4. `attack_path`: step-by-step callback/reentry sequence.
5. `impact`: concrete asset/state consequence.
6. `confidence`: high/medium/low with justification.
7. `fix`: CEI reorder, lock hardening, pull pattern, callback-safe transfer pattern.

## Remediation Patterns

1. Move all state commits before external calls.
2. Add non-reentrant lock on all shared-state write entry points.
3. Split sensitive write logic from callback-triggering transfer/mint code.
4. Use pull-payment patterns where practical.
5. Recompute critical values after external interactions when unavoidable.
