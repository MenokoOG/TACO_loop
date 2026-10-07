# References and prior art

Listed so the project is positioned honestly against existing work. Abstract-level reading unless noted. Open each source before citing it elsewhere.

## Foundations
- Boyd, J. — OODA loop lineage. Primary sources: "Destruction and Creation" (1976), "Patterns of Conflict", "Organic Design for Command and Control", "The Essence of Winning and Losing" (1995).
- Kephart, J. and Chess, D. (2003). The Vision of Autonomic Computing. *IEEE Computer* 36(1). (Monitor-Analyze-Plan-Execute over shared knowledge.)
- NIST AI Risk Management Framework 1.0, NIST AI 100-1 (2023): Govern, Map, Measure, Manage.

## Abstention, deferral, calibration
- El-Yaniv, R. and Wiener, Y. (2010). On the Foundations of Noise-free Selective Classification. *JMLR* 11. https://www.jmlr.org/papers/v11/el-yaniv10a.html (risk–coverage trade-off)
- Madras, D., Pitassi, T. and Zemel, R. (2018). Predict Responsibly: Improving Fairness and Accuracy by Learning to Defer. NeurIPS. https://proceedings.neurips.cc/paper/2018/hash/09d37c08f7b129e96277388757530c72-Abstract.html
- Angelopoulos, A. and Bates, S. A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification. https://arxiv.org/abs/2107.07511
- Ren, A. et al. (2023). Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners (KnowNo). CoRL. https://arxiv.org/abs/2307.01928

## Gates and runtime enforcement
- Alshiekh, M. et al. (2018). Safe Reinforcement Learning via Shielding. AAAI. https://arxiv.org/abs/1708.08611
- AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents. https://arxiv.org/abs/2503.18666
- Harnessing Embodied Agents: Runtime Governance for Policy-Constrained Execution. https://arxiv.org/abs/2604.07833
- What Can Be Enforced? A Theory of Certified Runtime Safety for Tool-Using Agents. https://arxiv.org/abs/2607.22868

## Agents and abstention (2026)
- Agentic Abstention: Do Agents Know When to Stop Instead of Act? https://arxiv.org/abs/2606.28733
- AgentAbstain: Do LLM Agents Know When Not to Act? https://arxiv.org/abs/2607.10059
- ReDAct: Uncertainty-Aware Deferral for LLM Agents. https://arxiv.org/abs/2604.07036
- Preventing Premature Commitment in Coding Agents with an Evidence-Conditioned Execution Layer (ECLoop). https://arxiv.org/abs/2607.28815

## Standards and guidance (see ADR 0007; verify primary text before citing)
- NIST AI RMF 1.0 (AI 100-1) and Generative AI Profile (AI 600-1): DOI 10.6028/NIST.AI.600-1
- NIST AI 100-2 E2025, Adversarial Machine Learning taxonomy: DOI 10.6028/NIST.AI.100-2e2025
- NIST CAISI AI Agent Standards Initiative (Feb 2026); NIST NCCoE concept paper on software and AI agent identity and authorization
- OWASP Top 10 for LLM Applications 2026; OWASP Top 10 for Agentic Applications 2026
- EU AI Act, Articles 12 and 14; Digital Omnibus Regulation (EU) 2026/1744
- US OMB M-25-21 and M-25-22 (April 2025)
- ISO/IEC 42001; ISO/IEC 23894
- NIST SP 800-218 (SSDF) and SP 800-218A; SLSA (slsa.dev); OpenSSF Scorecard; CycloneDX and SPDX
- OpenTelemetry GenAI semantic conventions (status: Development)
- Cedar policy language: https://docs.cedarpolicy.com/
- LangGraph human-in-the-loop and checkpointer documentation: https://docs.langchain.com/oss/python/langgraph/human-in-the-loop

## Relationship to TACO
Not new: asking for help or abstaining under uncertainty, gating actions, human override, audit logs. Hypothesised contribution (unproven): a *graded* response (speed, verification depth, scope, escalation) driven by a typed uncertainty profile, tested against a one-number confidence cutoff.
