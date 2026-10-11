# Documentation Requirements

## Requirements

- Identify Petri as the open-source automated behavioral/auditing framework originally released by Anthropic and currently maintained by Meridian Labs as Inspect Petri.
- Preserve the current auditor/target/judge architecture, multi-turn simulated environments, seed scenarios, scoring, parallel audits, Dish realism extension, and Bloom integration only while current upstream documentation supports them.
- Keep Petri distinct from fixed benchmark datasets, Bloom's targeted evaluation-suite generation, Inspect AI itself, model system cards, and hosted evaluation services.
- Treat versioned architecture, CLI/Python APIs, provider integrations, judge/auditor defaults, seed libraries, Dish/Bloom extensions, result schemas, and release behavior as freshness-sensitive.
- Preserve the transfer boundary: Anthropic remains original producer provenance while Meridian Labs is current maintainer/steward.
- Do not treat automated auditor/judge scores as ground truth; results depend on seeds, target/scaffold, auditor/judge models, prompts, tools, and evaluation version.

## Validation

- Petri remains evaluation/auditing software rather than a benchmark leaderboard.
- Original production and current maintenance relations are both represented without conflation.
- Evaluation claims stay configuration-scoped.
