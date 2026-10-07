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

## Relationship to TACO
Not new: asking for help or abstaining under uncertainty, gating actions, human override, audit logs. Hypothesised contribution (unproven): a *graded* response (speed, verification depth, scope, escalation) driven by a typed uncertainty profile, tested against a one-number confidence cutoff.
