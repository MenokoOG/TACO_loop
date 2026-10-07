# ADR 0001: Record architecture decisions

- Status: accepted
- Date: 2026-10-07

## Context
TACO is a research project whose parameters and definitions are policy choices. Without a written record, choices drift and results cannot be reproduced or audited.

## Decision
Every decision that shapes the model, the code boundaries, the experiment or the claims is recorded as a numbered ADR in `docs/adr/`. ADRs are immutable once accepted. A change is a new ADR that supersedes the old one.

## Consequences
Decisions are reviewable and citable. Small overhead per decision.
