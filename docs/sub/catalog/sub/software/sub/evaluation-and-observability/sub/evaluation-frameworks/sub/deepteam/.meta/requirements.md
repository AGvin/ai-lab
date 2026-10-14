# Documentation Requirements

## Requirements

- Identify DeepTeam as the distinct open-source Python adversarial/red-team testing framework produced by Confident AI and available independently of the hosted Confident AI evaluation platform, not merely a feature of DeepEval or Giskard.
- Preserve first-party published **v1.0.9 (2025-11-12)** non-prerelease boundary and Apache-2.0 `LICENSE.md`. The current project `pyproject.toml` also names `deepteam==1.0.9`, with Python **>=3.9,<3.14**, a `deepteam` CLI and a dependency on separately cataloged DeepEval.
- Cover automated single-/multi-turn jailbreak and prompt-injection adversarial scenarios, privacy and harmful-output vulnerabilities, configurable LLM evaluators and project red-team pipelines. CLI, SDK integrations, guardrails and optional external coding-agent harnesses are functions of the same DeepTeam product, not standalone canonical catalog peers.
- **Security/operation:** attack tests may invoke real agents, tools, retrieval systems and third-party model APIs. Use explicit permission and isolated test environments, synthetic/non-sensitive data, spending/rate caps, and safe handling of traces or sensitive responses. A passed scan does not establish real-world security or compliance.
- Distinguish DeepTeam from the generalized DeepEval assessment suite (dependency), Giskard `giskard-scan` optional integration, Snyk Agent Scan, and the hosted Confident AI reporting plane.
- Attribute exact `produced-by` / `produces` reciprocity to the existing `catalog/producers/c/confident-ai-inc` identity; preserve the producer's DeepEval relation.

## Validation

- First-party repository README, `pyproject.toml`, `LICENSE.md` and non-prerelease release v1.0.9 corroborate identity, package, license, Python support and CLI.
- Updated Confident AI producer contains exact reciprocal `produces` targets for both DeepEval and DeepTeam.
