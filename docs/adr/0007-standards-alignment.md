# ADR 0007: Alignment with AI governance and engineering standards

- Status: accepted
- Date: 2026-10-07

## Context
TACO is meant for public-facing agents, which are in scope for AI governance rules and security guidance. The design should line up with recognised standards where it can. **This is alignment, not compliance**: TACO is a component, not a certified system, and no standard below is claimed as met. Sources were read through secondary summaries on 2026-10-07; each must be checked against its primary text before it is cited in anything public. Status notes record what is uncertain.

## Governance and security standards

| Source | What TACO takes from it | Status / caveat |
|---|---|---|
| NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1, July 2024) | Vocabulary and structure: Govern, Map, Measure, Manage. Experiments and policy packs map to Measure and Manage. | Voluntary framework, not a checklist |
| NIST AI 100-2 (adversarial machine learning taxonomy; 2025 edition confirmed) | Source for the injected-unknown types in the simulator: direct and indirect prompt injection, supply-chain and misuse categories. Feeds the adversarial-uncertainty estimator. | A 2026 edition was mentioned by one source and not confirmed |
| NIST CAISI AI Agent Standards Initiative (announced Feb 2026), NCCoE concept paper on agent identity and authorization, CAISI agent-hijacking evaluations | Agent hijacking (indirect prompt injection) is the central adversarial scenario. Identity and authorization belong to the host: TACO consumes an identity-bound authorization result and does not define identity. | Concept paper / draft work; no final standard found. Reported attack-success figures are second-hand and not used |
| OWASP Top 10 for LLM Applications 2026 (Excessive Agency) and OWASP Top 10 for Agentic Applications 2026 | "Least agency": the scope-restriction output of the speed policy is least agency scaled by uncertainty. Threat list for scenarios: goal hijack, tool misuse, privilege abuse, cascading failure. | Primary OWASP text not read; ranking number for Excessive Agency differs between summaries |
| EU AI Act, Articles 12 (record-keeping) and 14 (human oversight); Digital Omnibus, Regulation (EU) 2026/1744 | Escalation must let a person understand limits, spot anomalies, resist automation bias and override. So an escalation payload carries the uncertainty breakdown and rationale, never a default-approve. Every decision emits a record. | Reported high-risk dates: 2 Dec 2027 (Annex III), 2 Aug 2028 (Annex I). Verify in the Official Journal. TACO is not itself a high-risk system |
| US OMB M-25-21 (April 2025) minimum practices for high-impact AI, incl. human oversight, intervention and accountability; M-25-22 on acquisition | Relevant to federal-facing deployments. A human reviewer does not by itself remove high-impact status, so TACO supports oversight but is not a substitute for the other practices. | Sources conflict on the compliance deadline; memo text not retrieved |
| ISO/IEC 42001 (AI management system, certifiable) and ISO/IEC 23894 (AI risk management guidance) | Organisation-level. Versioned policy packs and decision records can serve as evidence for an operator's own management system. | Official ISO text not read; guidance only, not certifiable |

## Engineering standards
| Source | Plan |
|---|---|
| NIST SSDF (SP 800-218) and the generative-AI profile SP 800-218A | Follow secure development practices for the library; map practices in a later ADR |
| SLSA (build provenance), OpenSSF Scorecard, SBOM (CycloneDX or SPDX) | Add Scorecard in CI, publish an SBOM with releases, and aim for a stated SLSA build level. Targets set in a later ADR; exact SLSA level definitions to be taken from slsa.dev |
| OpenTelemetry GenAI semantic conventions | Decision records can be exported as spans. The conventions are still marked *Development*, so any exporter is optional and version-pinned |

## Decision
1. State alignment, never compliance, in public text. Each mapping above is tracked as a documented claim with its source.
2. Verify every row against its primary source before it appears in README, a paper or a client document.
3. Design consequences adopted now: decision records emitted on every call; escalation payloads carry an uncertainty breakdown and rationale and have no default approve; adversarial scenarios in the simulator are drawn from the NIST adversarial taxonomy and the OWASP agentic list; identity and authorization stay with the host (ADR 0006).

## Consequences
The project can be explained in the language reviewers already use. Some standards are still moving (agent identity, OpenTelemetry GenAI), so alignment is versioned and reviewed, not assumed.
