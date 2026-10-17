# Documentation Requirements

## Requirements

- Identify MLPerf Endpoints v0.7 as MLCommons' independently released initial benchmark suite/results framework for comparing deployed model-serving endpoints across providers and systems, distinct from MLPerf Inference traditional batch submission rounds and individual model benchmark datasets.
- Preserve the v0.7 foundation-release boundary and limited initial coverage, with first results published July 28, 2026 and subsequent roadmap for v1.0 not considered already released.
- Capture the four linked outcome dimensions measured for an endpoint configuration: throughput, interactivity, P95 time-to-first-token (TTFT), and concurrency. Do not generalize any benchmark curve beyond its exact model, hardware, software, workload and submitted configuration.
- Separate reproducible benchmark rules and public submitted-results datasets from the live visualization/leaderboard platform; future rolling submissions are not a distinct benchmark identity solely because new results appear.
- Treat scope, eligibility, collection format, supported tests, metrics, normalization rules, public providers, result snapshots and reviewer procedures as version-sensitive.
- Preserve producer provenance through the canonical MLCommons relation and its inverse `produces`.

## Validation

- The suite and published release/version are identifiable, independently useful and source-backed.
- Published results are scoped to exact workload, system and methodology, not universal hardware/model claims.
- The official MLCommons producer is resolved bidirectionally.
