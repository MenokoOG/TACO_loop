# Contributing

Thanks for looking. This is a research project, so evidence matters more than enthusiasm.

## Ground rules

- Code is Apache-2.0; documentation is CC BY 4.0. By contributing you agree your work is offered under those terms.
- **Sign off every commit** (`git commit -s`). That adds a `Signed-off-by:` line and means you agree to the [Developer Certificate of Origin](https://developercertificate.org/). CI checks for it.
- Never invent results, benchmarks or citations. If something is unproven, write "unproven".
- Describe, don't glorify. Say what the code does, not what it will revolutionise.
- One change per pull request, branched from `main`. Delete the branch after merge.

## Code

- Python 3.13+, type-annotated, `mypy --strict` and `ruff` clean.
- Tests come with the code. Behaviour you can state as an invariant gets a property-based test (Hypothesis).
- Parameters live in the policy pack, never as literals in logic.
- Architecture decisions are recorded as ADRs in `docs/adr/` (numbered, never rewritten, superseded by a new ADR).

## Experiments

Experiments are pre-registered: the spec is committed before the run. Changes after the first run are logged as amendments, never silent edits. Failed hypotheses are published.

## Changelog and versions

Update `CHANGELOG.md` under `[Unreleased]`. Versions follow Semantic Versioning (0.x until the API settles).
