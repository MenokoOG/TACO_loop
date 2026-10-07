# ADR 0004: Escalation by stakes and likelihood

- Status: accepted (cut points to be set from data, see below)
- Date: 2026-10-07

## Context
The earlier design computed one Risk score as the product of five terms in [0, 1] (impact, probability of failure, exposure, irreversibility, total uncertainty) and escalated to a human above 0.50. A reviewer's Monte Carlo check (N = 500,000, scratch analysis, to be reproduced as a test in this repository) found the product exceeds 0.50 in about 0.08% of draws with uniform inputs and about 0.6% in a deliberately high-risk input distribution. Reaching 0.50 needs every term near 0.87. A product also cannot express "unlikely but irreversible and severe".

## Decision
Escalation is decided on two axes plus an override:

- **Stakes (S)** in [0, 1]: monotone non-decreasing in impact, irreversibility and exposure.
- **Likelihood (L)** in [0, 1]: probability of a bad outcome, monotone non-decreasing in the uncertainty profile.
- **Policy grid:** escalate to a human when `S >= s*` and `L >= l*`.
- **Override:** when `S` is at or above `s_hi` and the action is irreversible, escalate regardless of `L`.

The aggregation functions for S and L, and the cut points `s*`, `l*`, `s_hi`, are **policy-pack parameters**, not constants in code. They are chosen on the development scenario set to reach a stated escalation rate and miss rate, and then frozen before any evaluation run. A single scalar may still be computed for ranking and display, never for the escalation decision.

## Consequences
Escalation can fire on rare, severe, irreversible actions. Cut points become an experimental output rather than an opinion. Properties to test: monotonicity in each input, the override always escalates, and no parameter appears as a literal in logic.
