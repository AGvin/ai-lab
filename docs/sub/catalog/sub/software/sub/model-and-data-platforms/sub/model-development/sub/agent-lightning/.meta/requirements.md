# Documentation Requirements

## Requirements

- Present Agent Lightning as Microsoft's separately released open-source **model-development** framework for harnessed agentic reinforcement learning, not an inference runtime, hosted LLM API, pretrained model or general chat-agent framework.
- Keep the v1.0+ **LLM proxy/gateway, rollout controller, and trainer** within one product boundary; local/Kubernetes runners, verl training integration, and external model/harness support are version-sensitive components.
- Distinguish this product from PyTorch Lightning, OpenRLHF, verl and Microsoft Agent Framework. The separately released Agent Lightning Skill requires independent skill-identity review rather than automatic software/Agent Skills duplication.
- Preserve independently checked v1.0.2 non-prerelease publication (2026-09-29), Python >=3.12 requirement, and major v0.x/v1.0 architectural split; do not present the version as a permanent product identity.
- Attribute Qwen3.5-9B SWE-bench Verified improvement 41.8% to 56.4% on ~6,000 samples to original Microsoft Research experiments rather than AI Lab replication; do not infer broad benchmark dominance.
- Scope MIT licensing to repository software, not trained weights, evaluation datasets, output rights or integrated dependencies.
- Address execution of untrusted agent tools and local/Kubernetes code in rollouts using isolation, network boundaries, least-privilege credentials/RBAC, quotas, data minimization and reward-hacking checks. Never claim security audit or executed model training.
- Keep one canonical `produced-by` Microsoft relation and its precise inverse on the existing Microsoft entity; no new producer node.
- Preserve standard entity-relations rendering requirements and direct-child navigation; full cache/schema/CI/render remains a downstream gate.

## Validation

- Exactly one Agent Lightning software node under Model Development and one parent navigation entry.
- Microsoft producer and software node contain one matching directed inverse relation pair.
- Sources substantiate release identity and caveats; no unverified run or global catalog verification is asserted.
