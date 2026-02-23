---
name: oracle-integrity-detector
description: Detect oracle integration flaws in Solidity/EVM protocols, including stale price usage, decimal normalization bugs, unsafe spot pricing, L2 sequencer issues, and incomplete feed validation.
---

# Oracle Integrity Detector

Use this skill when auditing price-dependent logic (lending, liquidation, mint/redeem, collateral checks, fee math, AMM adapters).

## Detection Targets

Prioritize these high-frequency oracle failures:

1. Stale or frozen data accepted as valid.
2. Missing feed sanity checks (round completeness, invalid/negative/zero answers).
3. Decimal/scale mismatch across feeds/tokens (e.g., 6/8/18 confusion).
4. Unsafe spot pricing instead of manipulation-resistant TWAP.
5. L2 sequencer downtime not handled before consuming L2 feeds.
6. Outlier/min-max boundary behavior not handled.
7. Token order inversion when adapting pool price (base/quote flipped).

## Workflow

1. Map all price consumers:
   - Liquidation, borrowing power, mint/redeem, swap quote guards, risk limits, fee settlement.
2. Trace each consumer to oracle source(s):
   - Chainlink/Pyth/Tellor/Uniswap/Balancer/custom adapters.
3. Validate freshness and liveness:
   - Check timestamp/heartbeat threshold, stale rejection path, fallback behavior.
4. Validate data integrity:
   - Ensure answer > 0, round completeness checks, bounded values, revert handling.
5. Validate normalization:
   - Confirm consistent precision scaling across all feeds and token decimals.
6. Validate manipulation resistance:
   - Check TWAP window length, pool liquidity assumptions, anti-flash-loan assumptions.
7. Validate L2 safety:
   - Require sequencer-up check and grace period before trusting prices.
8. Validate directionality:
   - Confirm base/quote token orientation and returned unit semantics.

## False Positive Filters

Only report as valid if at least one is true:

1. A realistic stale/invalid/manipulated price can pass checks and change protocol decisions.
2. Decimal mismatch can materially over/under-price assets.
3. Spot/TWAP design allows economically feasible manipulation at current assumptions.

Downgrade or reject if:

1. Failing branch reverts safely before state change.
2. Redundant independent checks prevent bad price consumption.
3. Exploit requires impossible liquidity or privileged oracle control not in scope.

## Severity Heuristic

1. High: insolvency risk, bad debt, under-collateralized borrowing, liquidation bypass, large mispricing extraction.
2. Medium: bounded mispricing, temporary DoS, constrained economic advantage.
3. Low: edge-case misread with negligible protocol impact.

## Output Format

For each finding, output:

1. `title`: concise oracle failure statement.
2. `location`: file + function + line.
3. `oracle_path`: consumer -> adapter -> feed/pool.
4. `root_cause`: freshness/validation/scale/manipulation/direction flaw.
5. `attack_path`: concrete steps with required market conditions.
6. `impact`: exact accounting/risk consequence.
7. `confidence`: high/medium/low with assumptions.
8. `fix`: explicit guard/normalization/TWAP/sequencer/fallback change.

## Remediation Patterns

1. Enforce per-feed freshness threshold and fail-closed handling.
2. Validate round completeness and answer bounds before use.
3. Standardize to one internal precision and normalize once at adapter boundary.
4. Prefer robust TWAP with configured window and minimum liquidity assumptions.
5. Add L2 sequencer checks plus post-recovery grace period.
6. Add fallback oracle strategy with explicit precedence and failover rules.
7. Unit-test base/quote direction and decimal conversions with adversarial cases.
