# Documentation Requirements

## Requirements

- Present `datasets/` as the factual catalog owner for identifiable concrete AI-relevant datasets and dataset families whose provenance, composition, versions, licenses, access, and intended uses have durable reader value.
- Keep reusable dataset concepts and methodology with concept/learning owners. In particular, do not duplicate the `Evaluation Datasets` concept, benchmark methodology, scoring rules, metrics, evaluation results, or implementation tutorials here.
- Distinguish a concrete dataset from a benchmark that uses it, from an evaluation harness/software implementation, and from a hosted dataset platform.
- Preserve source-backed provenance, construction and curation context, version/variant identity, intended and unsupported uses, licensing/access constraints, known contamination or leakage concerns, and important coverage limitations only to the depth supported by current upstream sources.
- Treat dataset contents, revisions, variants, mirrors, licenses, access paths, and benchmark membership as version-sensitive facts where applicable; do not silently compare materially different revisions as the same dataset.
- Materialize children only for concrete source-backed datasets with durable AI Lab value. Do not create empty training/evaluation/modality taxonomy branches for symmetry.
- Render the standard direct-child navigation from the validated materialized child projection.

- For the materialized TheAgentCompany child, preserve the 1.0.0 task dataset's independent identity, 175-task version pin, producer-identity deferral, third-party service/backup rights and privileged-runtime safety boundaries; do not equate task instructions with a fixed evaluator or score.
- For the materialized GSM-Symbolic child, preserve Apple's independently published 2024 symbolic GSM8K-derived evaluation dataset, the distinct main/p1/p2 configurations and original GSM8K provenance, exact generated-data CC BY-NC-ND 4.0 restrictions versus the separate software grant, and Apple Inc. producer relation; no variant is an independently accepted dataset.
- For the materialized PaperBench child, preserve OpenAI's independent 2025 20-paper ICML research-replication benchmark dataset and 8,316 rubric criteria, original Git-LFS source and data/third-party paper rights boundaries, three-stage execution risk, and distinction from PaperBench Code-Dev, JudgeEval and MLE-bench.
- For the materialized AgentHarm child, preserve the original Gray Swan AI and UK AISI joint 2024 safety-benchmark research, paper total versus smaller public dataset availability, safe handling of harmful examples, purpose-restricted MIT-like data license, and version-sensitive current Inspect Evals grading differences.
- For the materialized AgentHarm child, distinguish 110/440 original reported harmful agent tasks from the released 44 public-test and 8 validation base behaviors, retain paired benign/chat views, original Gray Swan AI and UK AISI co-research, MIT-like but safety-purpose-restricted dataset rights and evolving Inspect Evals grader semantics without importing misuse prompts.

## Validation

- Every child represents an identifiable dataset or dataset family rather than a generic dataset concept, benchmark score, leaderboard, software harness, or transient hosted view.
- Dataset and benchmark identities are not collapsed when the benchmark includes additional task, protocol, scoring, or reporting semantics.
- Provenance, version, license/access, and intended-use claims are source-backed and scoped to the applicable release or variant.
- Navigation exposes only materialized children and does not imply that the initial dataset set is exhaustive.
