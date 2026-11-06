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
