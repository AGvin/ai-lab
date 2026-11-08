# Documentation Requirements

## Requirements

- Present RealReplicaBench as the released stateful long-horizon benchmark for business workflows executed against high-fidelity reproducible replicas of real online services.
- Preserve its current released scope of 107 tasks spanning CLI, browser, file, and API/MCP workflows plus text-only, browser-text, and vision-required capability slices.
- Keep the benchmark's mock-service replicas, harness/package, task suite, evaluated agents/models, leaderboards, and Business Arena companion work separate from the benchmark identity unless independently materialized.
- Preserve the split licensing boundary between harness/source code and task-suite data, and treat release versions, task counts, graders, mock-service coverage, and reported results as freshness-sensitive.

## Validation

- RealReplicaBench remains a benchmark/dataset identity rather than a business agent, SaaS platform, or generic evaluation harness.
- Claims about model performance remain tied to the cited release and exact benchmark configuration.

## Scoped original-source qualification — 2026-11-08

- **Commerce Agent Bench** is Accio/Alibaba International's currently named original 2026 benchmark, **formerly RealReplicaBench**; the publisher explicitly documents a **rename of the same project**, not an independently accepted new dataset. Preserve the canonical `catalog/datasets/realreplicabench` identity until metadata, reader, navigation and inbound references are reconciled together; do not count the renamed title as another benchmark.
- The current publisher's **v1.3.1 107-task** release has **53 CLI, 28 browser, 16 file, 10 API/MCP** tasks, with **65 text-only, 20 browser-text-capable and 22 vision-required** slices. Each task runs against reproducible stateful mock business/service replicas and a versioned verifier; these are not authorized production SaaS accounts, real purchases or independent business-agent competence certifications.
- The publisher splits **Apache-2.0 code/harness** from **CC BY 4.0 task data**, with additional third-party notices for mirrored stylesheets, fonts, icons and recorded API responses. The published model results are specific to benchmark version, image digest, harness, judge, provider/endpoint and policy; task-level raw result bundles currently lack independently hosted immutable checksums. Trademark and third-party asset rights remain distinct.
- First-party sources: https://github.com/Accio-org/CommerceAgentBench ; https://commerce-agent-bench.site.accio.ai/ .
- Accepted one existing renamed benchmark's publisher/version/method/source boundary only. Canonical entity/reader and inbound-link rename reconciliation is pending and uncredited; no agent execution, commercial platform access, score reproducibility guarantee, full rights/security/legal review, repository-wide schema/cache/CI/render, clean or final gate.
