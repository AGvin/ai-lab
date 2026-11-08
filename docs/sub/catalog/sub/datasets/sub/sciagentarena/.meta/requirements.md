# Documentation Requirements

## Requirements

- Present SciAgentArena as the released cross-domain benchmark for evaluating AI agents on interactive, real-world scientific-research scenarios.
- Preserve its distinguishing scope of approximately 200 tasks across multiple scientific domains with stepwise verification and an agent-agnostic interactive environment.
- Keep evaluated agents/models, scientific software, task-domain source material, and benchmark harness components separate from the benchmark identity unless independently materialized.
- Treat task inventory, domain coverage, verification criteria, harness versions, baselines, and reported results as freshness-sensitive.

## Validation

- SciAgentArena remains a benchmark/dataset identity rather than a scientific agent product or research workflow framework.
- Claims about agent strengths/failures remain tied to the cited benchmark release and evaluation configuration.

## Scoped original-source qualification — 2026-11-08

- **SciAgentArena** is the original June 2026 multi-institution scientific-agent benchmark described in the first-party project and Microsoft Research paper, with **approximately 200 interactive tasks** across **five scientific domains** and **four task categories**. Its stepwise verification and agent-agnostic runner distinguish it from static scientific question-answer corpora and from any one agent or laboratory product.
- The official research page reports experiments with **18 agent configurations**, assessing task completion, stability, reliability, scientific reasoning and resource/cost behavior. Publisher study outcomes vary by domain and model configuration; reported strengths on well-defined analyses do not establish general scientific discovery, trustworthy autonomous clinical advice or independently reproduced biological findings.
- Tasks, domain data, benchmark execution environment, scientific tools and external model endpoints have independent access, copyright, privacy and execution risks. The living benchmark's task inventory and leaderboard may change, so references to counts and results must retain version and publication context.
- First-party sources: https://sciagentarena.github.io/ ; https://www.microsoft.com/en-us/research/publication/benchmarking-ai-agents-for-addressing-scientific-challenges-across-scales/ .
- Scoped source qualification covers one pre-existing research benchmark's authorship, public task/method description and release boundaries only. No task data downloaded, model run, clinical validity or material rights/security/legal assessment, global schema/cache/CI/render, clean or final gate.
