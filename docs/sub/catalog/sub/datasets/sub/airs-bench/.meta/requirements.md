# Documentation Requirements

## Requirements

- Present AIRS-Bench as a released AI Research Science benchmark for end-to-end AI-research capabilities of LLM agents.
- Keep benchmark tasks, datasets, evaluation preparation, agent-environment dependencies, scoring, and baseline-result claims traceable to the current Meta/Facebook Research release.
- Distinguish benchmark infrastructure from the external agent frameworks used to run evaluated agents.
- Treat dataset revisions, task coverage, baseline models, and reported results as freshness-sensitive.

## Validation

- AIRS-Bench remains a benchmark/dataset identity rather than an agent framework.

## Scoped original-source qualification — 2026-11-08

- **AIRS-Bench** is Meta/Facebook Research's original **2026** AI Research Science benchmark of **20 end-to-end ML research tasks** drawn from 17 published papers and 16 datasets. Each task is a problem/dataset/metric specification with reference SOTA, not 20 independent new datasets or a generic research-agent framework.
- The first-party `facebookresearch/airs-bench` repository exposes task specs for two scaffold ecosystems, **aira-dojo** and **MLGym**, with preparation and grading scripts; the different harness representations are not duplicate benchmark task identities. Reported averages, Elo and submission metrics require exact agent+model, seeds, data, score normalization and execution budget. The upstream codebase states **CC BY-NC 4.0**, while underlying task datasets may have independent licenses and network/download requirements.
- First-party sources: https://github.com/facebookresearch/airs-bench ; https://arxiv.org/abs/2602.06855
- Source gate qualifies one existing original publisher/task-release identity, task/data/scaffold boundaries and noncommercial/source-data rights caveats only. No task dataset downloaded, research-agent or grader execution, comprehensive data rights audit, full CI/renderer, clean or final gate.
