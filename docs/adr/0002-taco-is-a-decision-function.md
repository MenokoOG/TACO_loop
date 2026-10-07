# ADR 0002: TACO is a decision function, not an agent

- Status: accepted
- Date: 2026-10-07

## Context
TACO targets inference-time decisions by public-facing agents facing unknowns (incomplete, stale, contradictory or hostile input). Agents already sit inside harnesses that own permissions, execution and records. A second gate and a second audit chain would duplicate and may contradict them.

## Decision
`taco_loop` is a pure decision function. Input: observation quality, an uncertainty profile, candidate actions with their attributes, and a versioned policy. Output: a verdict (allow, allow with N checks, restrict scope, escalate to a human, block) and a rationale record.

It does not execute actions, hold credentials, sign records, or replace the host harness's permission and authorization layer. Hard permission and safety guards are inputs supplied by the harness. The library emits a record payload; the harness is free to hash, sign and store it in its own ledger.

## Consequences
One gate decides allow or deny; TACO decides how much deliberation, scope restriction and human involvement a decision gets. The library stays small, deterministic and testable, and can be dropped into different harnesses. Any reference audit chain in this repository exists for simulation and tests only.
