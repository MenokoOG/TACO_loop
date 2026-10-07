# ADR 0005: Evaluation protocol

- Status: accepted
- Date: 2026-10-07

## Context
The guiding idea is the field maxim "slow is smooth, smooth is fast": deliberation matched to what is unknown should pay for itself through less rework and fewer bad actions. A test that only counts unsafe actions cannot show that, and a controller that never acts would pass it.

## Decision
1. **Primary metric: correct decisions per unit of total effort.** Effort = steps + verification passes + rework after a bad action + human wait time. The effort model and its weights are written into the experiment spec before the run, and swept for sensitivity.
2. **Guard metrics:** unsafe-action rate, and task success (non-inferiority margin stated and justified in the spec).
3. **Baselines:** B0 ungated; B1 single-confidence cutoff; B2 always escalate; B3 random escalation at the treatment's own escalation rate.
4. **Compare at equal escalation rate** and report risk-coverage curves, not single operating points.
5. **Independent effect model.** What a verification pass does in the simulator is fixed in advance from a model that does not depend on TACO's own formulas.
6. **Miscalibration sweep.** Add bias and noise to the simulated uncertainty inputs and report where TACO stops beating B1.
7. **Independent reviewer.** Someone other than the author reads the scenario generator before the locked evaluation run, and one scenario family is held out and unused during development. The run waits for the reviewer. Reviewer: not yet named.
8. **Pre-registration.** The spec is committed before the run. Changes after the first run are logged as amendments, never silent edits. Failed hypotheses are published.

## Consequences
A result can contradict the idea. The experiment is slower to build and stronger as evidence. It tests a control law given simulated uncertainty, not performance on real traffic, and every write-up must say so.
