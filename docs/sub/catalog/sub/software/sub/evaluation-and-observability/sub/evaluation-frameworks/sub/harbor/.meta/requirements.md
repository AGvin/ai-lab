# Documentation Requirements

## Requirements

- Identify Harbor as an independently released local/open-source framework for evaluating agents and language models in reproducible containerized tasks and generating rollouts for RL optimization.
- Preserve the software evaluator's primary catalog ownership under `software/evaluation-and-observability/evaluation-frameworks`, separate from benchmark datasets such as Terminal-Bench 2.0, SWE-bench Pro and standalone agent implementations.
- Its CLI/Python tooling can run arbitrary installed and provider-based agents, benchmarks and environments, parallelized through local Docker or supported cloud sandbox providers; treat those adapters, datasets and environment backends as configurable integrations rather than separate Harbor software identities.
- Distinguish software project provenance under `harbor-framework/harbor` from Terminal-Bench 2.0 dataset provenance and older Harbor repository redirects, without inventing a corporate platform owner.
- Keep supported agent integrations, benchmark registry versions, resource requirements, supported sandbox runtimes, cloud integrations, evaluation scoring and experiment APIs freshness-sensitive.
- Report benchmark results only alongside exact benchmark version, agent/model, harness version, environment, concurrency, time/tool/token budget, seed and validation protocol. Do not equate RL rollouts with benchmark ground-truth labels.
- Preserve the Harbor Framework Team's reciprocal producer provenance.

## Validation

- The evaluator tool is not mislabeled as a benchmark task dataset or hosted AI inference service.
- Current first-party repository, documentation and packaging links match the canonical software identity.
- Benchmark and model performance statements are scoped to reproducible harness configurations.
- `produced-by` and `produces` are reciprocal.
