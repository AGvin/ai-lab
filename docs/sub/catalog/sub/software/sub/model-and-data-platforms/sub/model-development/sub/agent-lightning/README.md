# Agent Lightning

Agent Lightning is an open-source agentic reinforcement-learning framework from Microsoft Research. Its v1.0 architecture enables **harnessed agentic RL**: training reuses an agent's existing tools, context and control-flow harness through a model-API proxy instead of reimplementing the harness inside the trainer.

## Scope and boundaries

- **API gateway / LLM proxy**, **rollout controller**, and **trainer** form one software system. Agent rollouts can run locally or as Kubernetes Jobs, with training integrated into a verl backend; these components are not separate product identities.
- Agent Lightning is distinct from **PyTorch Lightning**, **OpenRLHF**, **verl**, and Microsoft Agent Framework. Integration does not imply common ownership or interchangeable behavior. The separately released *Agent Lightning Skill* for coding-agent optimization is a different distribution surface, not the framework.
- The checked [v1.0.2 stable release](https://github.com/microsoft/agent-lightning/releases/tag/v1.0.2) was published **2026-09-29**, and its package requires **Python 3.12+**. The v0.x implementation is legacy; GPU stack, supported trainers/harnesses, dependencies and algorithms are version-sensitive.

## Reported evaluation and safe use

Microsoft Research reports that a Qwen3.5-9B coding-agent training pipeline using about 6,000 samples improved SWE-bench Verified Pass@1 from 41.8% to 56.4%. A separate MoE coding-agent experiment appears in the v1.0.2 release. These are **publisher results**, not independently reproduced AI Lab measurements or a general recommendation ranking.

Agent rollouts can execute tools and untrusted code. Isolate local/Kubernetes runners, limit credentials and network access, enforce RBAC and resource quotas, minimize sensitive trace data, and check reward hacking before running on real workloads. An MIT-licensed implementation does not automatically clear model weights, training datasets or dependency licenses. No live training or GPU verification was performed.

## Relations

- Produced by: [Microsoft](../../../../../../../producers/sub/m/sub/microsoft/)

## Official resources

- [Source repository](https://github.com/microsoft/agent-lightning)
- [Release v1.0.2](https://github.com/microsoft/agent-lightning/releases/tag/v1.0.2)
- [Stable documentation](https://microsoft.github.io/agent-lightning/stable/)
- [Microsoft Research v1.0 publication](https://www.microsoft.com/en-us/research/blog/agent-lightning-v1-0-a-3500-line-lightweight-agentic-rl-framework-for-training-agents-with-real-harnesses/)
- [MIT source license](https://github.com/microsoft/agent-lightning/blob/main/LICENSE)
