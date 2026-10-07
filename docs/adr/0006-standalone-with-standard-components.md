# ADR 0006: Standalone, built on standard components

- Status: accepted
- Date: 2026-10-07
- Supplements: ADR 0002

## Context
TACO is its own project. It does not depend on, and is not defined in terms of, any other internal project. Public-facing agents already run on common stacks, so TACO should plug into them, not require a bespoke harness.

## Decision
1. **The core has no third-party runtime dependencies** and knows nothing about any framework.
2. **Adapters are the anti-corruption layer.** Each adapter translates an external system's types into TACO's own immutable types and back. External types never appear in core signatures. Adapters ship as optional extras.
3. **Hard guards (permission, safety) come from the host.** The reference adapter targets [Cedar](https://docs.cedarpolicy.com/). Facts relied on: Cedar is default-deny, a matching `forbid` overrides any `permit`, and **a policy that errors is ignored during evaluation**. Therefore the adapter must validate policies against a schema, test every `forbid` policy, and treat any adapter or evaluation error as deny. The choice of Python binding is open and unverified.
4. **Human escalation integrates with LangGraph** through an optional adapter: an `escalate` verdict maps to `interrupt()` with a rationale payload and resumes with a human decision. This needs a checkpointer; the adapter documents that and pins a tested LangGraph version because the interrupt API has changed between releases.
5. **A plain-Python path stays first-class.** Using TACO must not require LangGraph or Cedar.

## Consequences
TACO can be tried in different stacks. More surface to test at the adapter edge. Reference sources: Cedar documentation (security and policy pages) and the LangGraph human-in-the-loop and checkpointer documentation.
