# Documentation Requirements

## Requirements

- Identify Inspect AI (Python package `inspect-ai`) as the UK AI Security Institute's independently installable MIT-licensed large-language-model and agent-evaluation framework, not as a dataset, hosted model API, or the UK government's complete regulatory program.
- Preserve first-party evaluation functionality: prompt/scorer and model-graded evaluations, tool usage, multi-turn agent tasks, external model backends and extensible Python task implementations. The upstream also distributes a mutable catalog of prebuilt evaluations, not independently owned duplicate benchmarks by default.
- Distinguish the framework and evaluation-task library from government-held model evaluations, independent benchmark families (for example BrowseComp/OSWorld), and third-party evaluated model providers; disclose the origin and conditions of every task when citing a score.
- Pin `inspect-ai` package, evaluation task implementation/split, model/backend version, inference settings, tool/solver and scorer, external dependencies, run seeds where applicable, and model-judge evaluation version for reproducibility. Official release 0.3.278 was published 2026-10-09; latest-version claims are freshness-sensitive.
- Evaluation runs may execute agent tools, contact paid model APIs and send private prompt/data/log content to provider endpoints. Run untrusted tool-use tests in authorized sandboxes with least-privilege credentials, bounded budgets and governed trace retention.
- Preserve first-party UK AI Security Institute stewardship under its official UKGovernmentBEIS upstream and exact producer provenance; do not infer that evaluated models or unrelated third-party tasks are UK government intellectual property.

## Validation

- The first-party repo and `inspect.aisi.org.uk` documentation verify released software, evaluation scope and UK AI Security Institute authorship.
- The `produced-by` link is reciprocated by the UK AI Security Institute `produces` relation.
