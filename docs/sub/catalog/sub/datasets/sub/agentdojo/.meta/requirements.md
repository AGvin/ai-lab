# Documentation Requirements

## Requirements

- Describe AgentDojo as the published ETH Zurich-led NeurIPS 2024 benchmark of prompt-injection attacks and defenses against LLM agents that perform tasks with tools, not as a generic malware/security product or a provider's LLM evaluation API.
- Preserve its original benchmark task/attack-surface suites, legitimate user goals, attacker controls, tool-response and environment boundary, measurable attack/defense outcome criteria, and experimental methodology only as supported by official source and paper.
- Separate the identifiable research benchmark/task suite from the separately evolving Python library, runtime, installation, detectors, defense implementations and evaluation wrappers. The upstream warns that its package API is still under development, which does not turn the peer-reviewed benchmark into an unpublished draft.
- Attribute original research and maintained upstream stewardship to ETH Zurich's security research group, while acknowledging the named Invariant Labs coauthor affiliations rather than implying ETH Zurich authored every related attack/defense implementation.
- Keep released evaluation revisions, tested environments, model/tool setups, contamination and exploit-surface scope, reproducibility conditions and quantitative success rates version-sensitive.
- Distinguish AgentDojo security/prompt-injection evaluations from the broader AIRS-Bench research benchmark and from unrelated agent functionality/safety testing.

## Validation

- The benchmark remains distinct from the mutable AgentDojo Python API and security tooling.
- Primary research authorship/provenance is qualified, with a reciprocal ETH Zurich producer link.
- Prompt-injection evaluation results are not compared across incompatible task/attack/defense configurations.

## Scoped original-source qualification — 2026-11-08

- **AgentDojo** is the published **NeurIPS 2024 Datasets and Benchmarks** research benchmark for prompt-injection attacks and defenses involving LLM agents, with first-party repository maintained by the **ETH Zurich SPY Lab** and contributors affiliated with **Invariant Labs**. It models legitimate user tasks, attacker influence through tool/environment inputs, and observable attack/defense outcomes.
- The **AgentDojo Python package API** remains explicitly **under development** according to the upstream README; this does not make the original peer-reviewed research benchmark an unpublished draft. A code library, model-specific defender, attack harness and result explorer are not separate dataset identities or evidence of real-world safety.
- Verified publisher sources: https://github.com/ethz-spylab/agentdojo and https://agentdojo.spylab.ai/ ; original paper: https://openreview.net/forum?id=m1YYAQjO3w
- Source-qualified existing research dataset identity and publisher/publication scope only. No agent/tool injection experiments, independent safety effectiveness, complete dataset content/rights verification, full legal/security/privacy audit, repository-wide schema/cache/CI/render, reader repair, clean or final credit.
