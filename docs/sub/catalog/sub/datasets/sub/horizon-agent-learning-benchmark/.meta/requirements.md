# Documentation Requirements

## Requirements

- Present Horizon as a long-horizon agent-learning benchmark measuring whether agents can acquire useful knowledge from long prior histories and apply it in later environment tasks.
- Preserve public/private task boundaries, Harbor integration, submission workflow, dataset identity, reference-agent role, and scoring/evaluation details from current upstream sources.
- Keep the benchmark distinct from memory frameworks or agent harnesses even when reference agents implement retrieval/memory strategies.
- Treat leaderboard results, task counts, dataset revisions, supported runners, and infrastructure requirements as freshness-sensitive.

## Validation

- Horizon remains a benchmark/dataset identity centered on long-horizon learning/adaptation.

## Scoped original-source qualification — 2026-11-08

- **Horizon** is Orin Labs' original long-horizon agent-learning benchmark, testing whether agents can extract reusable knowledge from previous first-person trajectories and apply it to later environment tasks. Its benchmark identity is distinct from the reference agent, generic memory products, model training corpora and the Harbor runner.
- The publisher currently keeps **most benchmark tasks and histories private** to reduce overfitting. Public Harbor cases and the separate `orinlabs/horizon-example-traces` distribution are illustrative subsets, not the complete hidden benchmark. The original repository describes an average private trace of roughly **30 million tokens**, while public example traces are considerably smaller. Exact task count, trace revision, holdout policy and model/agent configuration must be pinned before interpreting scores.
- Agent submissions run against privately hosted evaluation after public smoke checks; outcomes combine accuracy, speed and cost and depend on task trace ingestion, harness, available tools, sandbox separation and exact agent-model stack. Long trace contents, API credentials and any private user artifacts are not authorized for unrestricted redistribution.
- Original publisher sources: https://github.com/orinlabs/horizon ; https://huggingface.co/datasets/orinlabs/horizon-example-traces .
- Accepted scope is one existing benchmark identity and public/private task, trace and evaluator-access boundaries only. No private test access, actual Harbor agent execution, independent score reproduction, corpus rights/security/legal audit, whole-repo schema/cache/CI/render, clean or final acceptance.
