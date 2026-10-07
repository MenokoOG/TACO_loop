# TACO Loop

**Take in unknowns → Assess and align → Choose correctly → Operate and observe the outcome.**

TACO is a research project on one question: *how do we increase the rate of correct decisions by AI agents when they face unknowns?*

It targets **inference-time decisions by public-facing agents**: the moment between "the model proposes an action" and "the action runs", when the input may be incomplete, stale, contradictory or hostile. The idea comes from a field maxim, *slow is smooth, smooth is fast*: deliberation scaled to what is unknown should pay for itself through less rework and fewer bad actions.

> **Core law:** unknown data must increase decision discipline, not model confidence.

## Status

**Pre-alpha. Research. No results yet.** Nothing in this repository has been validated. Claims below are hypotheses until an experiment in `docs/` says otherwise.

## What this will be

A small, dependency-light Python library of a *decision function*. Given an observation-quality estimate, an uncertainty profile, candidate actions and a policy, it returns a verdict (allow, allow with N checks, restrict scope, escalate to a human, block) and a rationale record. It does not execute actions, hold credentials, sign anything, or replace the permission system of the harness around the agent. A simulation package will test it against simple baselines.

## What this is not

- Not an agent, and not a replacement for a permission or authorization layer.
- Not proven to reduce bad decisions. That is what the first experiment is for.
- Not a claim of certainty: it bounds and manages uncertainty, it does not remove it.

## Repository layout

```
src/taco_loop/   library (pre-alpha, empty)
tests/           tests (property-based tests come first)
docs/adr/        architecture decision records
docs/references.md  prior art and sources
```

## Development

Python 3.13 or newer. Details will land with the first real module; see `CONTRIBUTING.md`.

## Licence

Code: Apache-2.0 (`LICENSE`). Documentation and prose: CC BY 4.0 (`docs/LICENSE-docs.md`).

## Author

Lawrence Jefferson II (MenokoOG).

*LAHA — Love All Humans Always.*
