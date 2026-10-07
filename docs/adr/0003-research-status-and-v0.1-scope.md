# ADR 0003: Research status and v0.1 scope

- Status: accepted
- Date: 2026-10-07

## Context
TACO started as a white paper and a set of equations. A review of that material found equations that do not behave as described, unvalidated inputs, and parts that no planned experiment tests. The project is being rebuilt from the start with current tooling.

## Decision
1. **TACO is a research project.** Its question: how do we increase the rate of correct decisions by AI agents when they face unknowns, at inference time, in public-facing deployments? The earlier white paper is historical background, not a specification.
2. **Clean-room rebuild.** Earlier documents and code are inputs to read, not material to import. Every definition in this repository is restated, justified and tested here.
3. **v0.1 scope (in):** observation-quality and uncertainty-profile inputs, an escalation rule (ADR 0004), a boolean hard gate supplied by the host, a speed/verification/scope policy table, action selection, an audit record payload, and a simulation package with Experiment 1.
4. **v0.1 scope (out):** memory recall, the "subliminal" bias loop, human-review probability/drift models and memory write-gates from the earlier drafts, any API server, database or UI, and a composite benchmark score as a headline result.
5. Out-of-scope items return only if an experiment motivates them, via a new ADR.

## Consequences
A smaller, testable core. Some earlier ideas are dropped until evidence supports them. Nothing in this repository claims a result before an experiment produces one.
