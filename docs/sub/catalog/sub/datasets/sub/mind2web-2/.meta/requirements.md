# Documentation Requirements

## Requirements

- Identify Mind2Web 2 as the NeurIPS 2025 Datasets & Benchmarks long-horizon agentic-search evaluation of complex, time-varying information synthesis and citation-backed answers, not as the original stepwise web UI-action dataset.
- Preserve the independently published Agent-as-a-Judge framework assessing answer quality and grounding to cited web evidence. The public evaluation scripts for both development and test sets were released on 2025-10-23.
- Record the reproducibility boundary: pin task split, agent answer/citation artifact, fetched webpage cache, evaluator script and `--eval_version`; dynamic website content and judge revisions can invalidate cross-run score comparisons.
- Keep this research/evidence synthesis benchmark distinct from offline Mind2Web action prediction, Online-Mind2Web live website navigation, and unrelated generic search question datasets.
- Treat the benchmark tasks, evaluation harness, judge prompts, webpage caching dependencies and assessed models as separate roles; do not duplicate a dataset simply because the evaluation scripts and leaderboard are distributed alongside it.
- Attribute the first-party research and repository to Ohio State NLP Group and preserve coauthor affiliations without claiming sole ownership over collaborating institutions.

- Render the complete visible current-node relation set through the standard `entity-relations` component as a provenance block; preserve relation semantics and canonical target identities.
- Render an `official-resources` block with this explicit selection from canonical references: [Mind2Web 2 repository and evaluation instructions](https://github.com/OSU-NLP-Group/Mind2Web-2); [Mind2Web 2 project site](https://osu-nlp-group.github.io/Mind2Web-2/).

## Validation

- The official benchmark repository documents NeurIPS 2025 Datasets & Benchmarks, public development/test evaluation scripts and the reproducible cached-page evaluation method.
- The producer `produces` relation exactly reciprocates `catalog/datasets/mind2web-2`.

## Scoped original-source qualification — 2026-11-08

- **Mind2Web 2** is Ohio State NLP Group's independently released **2025** long-horizon **agentic search and grounded synthesis** benchmark, distinct from its original offline web-action **Mind2Web** and live-browser **Online-Mind2Web**. It requires complete answers supported by source URLs, judged by a separate **Agent-as-a-Judge** system rather than mere click/action accuracy.
- The publisher released evaluator scripts for public development and test splits by **2025-10-23**. A reproducible evaluation pins task split, agent answer/citation files, **cached cited webpages and capture time**, selected `--eval_version`, model-provider judge and retrieval/tool limitations. Mutable online sources and judge versions prevent automatic score comparability; official code using API keys or Chrome capture tools should run with least-privilege access and no secrets in benchmark artifacts.
- First-party sources: https://github.com/OSU-NLP-Group/Mind2Web-2 ; https://osu-nlp-group.github.io/Mind2Web-2/ .
- One already materialized original dataset identity and its 2025 source/grading/cache boundary accepted only; no webpage scraping, actual agent/judge execution, third-party web-content rights/privacy review, independent published score replication, full schema/cache/CI/render, clean or final credit.
