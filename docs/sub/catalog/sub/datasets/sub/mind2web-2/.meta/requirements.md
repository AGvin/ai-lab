# Documentation Requirements

## Requirements

- Identify Mind2Web 2 as the NeurIPS 2025 Datasets & Benchmarks long-horizon agentic-search evaluation of complex, time-varying information synthesis and citation-backed answers, not as the original stepwise web UI-action dataset.
- Preserve the independently published Agent-as-a-Judge framework assessing answer quality and grounding to cited web evidence. The public evaluation scripts for both development and test sets were released on 2025-10-23.
- Record the reproducibility boundary: pin task split, agent answer/citation artifact, fetched webpage cache, evaluator script and `--eval_version`; dynamic website content and judge revisions can invalidate cross-run score comparisons.
- Keep this research/evidence synthesis benchmark distinct from offline Mind2Web action prediction, Online-Mind2Web live website navigation, and unrelated generic search question datasets.
- Treat the benchmark tasks, evaluation harness, judge prompts, webpage caching dependencies and assessed models as separate roles; do not duplicate a dataset simply because the evaluation scripts and leaderboard are distributed alongside it.
- Attribute the first-party research and repository to Ohio State NLP Group and preserve coauthor affiliations without claiming sole ownership over collaborating institutions.

## Validation

- The official benchmark repository documents NeurIPS 2025 Datasets & Benchmarks, public development/test evaluation scripts and the reproducible cached-page evaluation method.
- The producer `produces` relation exactly reciprocates `catalog/datasets/mind2web-2`.
