# Documentation Requirements

## Requirements

- Identify BenchFlow as the original SkillsBench open-source publishing project/organization (GitHub `benchflow-ai`, Hugging Face `benchflow`), not a separately verified incorporated legal person, model vendor or owner of all individual third-party contributions.
- Distinguish the BenchFlow SDK/CLI software framework (`benchflow-ai/benchflow`) from the SkillsBench benchmark dataset (`benchflow-ai/skillsbench`), the task oracle/verifier code, evaluated models, external sandbox provider and leaderboard results. The original dataset and separate software have distinct reciprocal producer relations.
- Treat published v1.1's 87 pinned task packages and its 0.6.x runtime requirement as version-scoped facts. The original paper's 86 tasks and mainline 1.2 contributor notes are not an identical tagged benchmark set.
- Preserve original repository Apache-2.0 and Hugging Face metadata Apache-2.0 declarations, while not claiming universal rights over contributed third-party assets, benchmark data extraction or agent trajectory redistribution.
- Explain hazards from arbitrary task/oracle/verifier execution, cloud sandbox charges, API-key exposure and potential training/evaluation contamination. Review applicable ownership, permission and privacy facts independently before assigning corporate or geopolitical risk labels.
- Maintain two `produces` relations, one for SkillsBench and one for the independent BenchFlow SDK/CLI software, each with exact reciprocal `produced-by` relation and reader links.

## Validation

- One research/open-source publisher identity, not an assertion of incorporation or ultimate beneficial ownership.
- Exactly two distinct `produces` edges point to `catalog/datasets/skillsbench` and `catalog/software/evaluation-and-observability/evaluation-frameworks/benchflow`; do not double-count the publisher.
- Dataset ↔ producer readers and references resolve; no full runtime, provenance or legal audit is implied.
