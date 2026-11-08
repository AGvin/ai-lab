# Documentation Requirements

## Requirements

- Present Agents' Last Exam (ALE) as the Berkeley RDI/RDI Foundation benchmark for long-horizon, economically valuable digital work across broad occupational coverage.
- Preserve the boundary between the full expert-sourced evaluation corpus and the public repository subset; do not imply that every evaluated task or hidden reference is publicly distributed.
- Keep the `ale_run` evaluation framework, reference harnesses, frontier model results, O*NET/SOC taxonomy inputs, and individual industry tasks separate from the benchmark identity.
- Treat public task counts, occupational/industry coverage, hidden-evaluation policy, sandbox runtime, graders, leaderboard results, and corpus expansion as freshness-sensitive.

## Validation

- ALE remains a benchmark/dataset identity rather than an agent harness, labor-market taxonomy, or commercial evaluation service.
- Comparative agent-performance claims remain tied to the cited evaluation release and run configuration.

## Scoped original-source qualification — 2026-11-08

- **Agents' Last Exam (ALE)** is the original June 2026 UC Berkeley RDI / RDI Foundation long-horizon professional-work agent benchmark. The authors evaluated over **1,500 expert-sourced tasks** across 55 occupations; the current public runnable selection is not the same as that full research corpus or the `ale_run` harness.
- The current publisher-owned `rdi-berkeley/agents-last-exam` **v1.1** guide selects **122 active tasks after 30 retirements**, including 119 CPU-capable and three GPU tasks. Preserve original v1 vs v1.1 task manifests and pinned images, graders, environment and sandbox setup. The existing `MaxIntelligenceAgency/ALE-Benchmark` reference is a historical link requiring separate metadata/source reconciliation, not a distinct benchmark identity.
- Original publisher **Apache-2.0 software** and **CC BY 4.0 task data** license claims are component scoped; third-party applications, environments and sample assets retain separate rights and operational risks. Publisher scores require pinned task revisions, graders, agent scaffolds and runtime; none were executed or independently validated here.
- First-party sources: https://github.com/rdi-berkeley/agents-last-exam ; https://rdi.berkeley.edu/blog/agents-last-exam/ .
- Scoped acceptance: existing original dataset/benchmark source, publication, versioned task scope and rights/evaluation boundaries only. No new entity or metadata gate, task execution, source link/reader repair, full rights/privacy/security/legal review, schema/cache/CI/render, clean or final delivery.
