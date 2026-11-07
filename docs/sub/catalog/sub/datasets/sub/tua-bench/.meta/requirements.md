# Documentation Requirements

## Requirements

- Present TUA-Bench as a released benchmark for evaluating general-purpose terminal-use agents on realistic command-line tasks.
- Preserve its benchmark identity and distinguish its task design, evaluation harness, environment/runtime assumptions, and published results from Terminal-Bench, Long-Horizon Terminal-Bench, SWE-bench, and generic shell-agent tooling.
- Keep agent/model leaderboard results, task inventory, harness versions, environment backends, and evaluation settings as freshness-sensitive and run-scoped.
- Do not turn the Harbor-compatible execution path, Docker/Podman support, example agents, or model provider settings into separate benchmark identities.

## Validation

- TUA-Bench remains a benchmark/dataset identity rather than a terminal agent or sandbox product.
- Claims about comparative agent performance remain tied to the cited release/run configuration.

## Scoped original-source qualification — 2026-11-08

- **TUA-Bench (Terminal-Use Agent Benchmark)** is Meta/Facebook Research's original **2026** benchmark of **120 execution-based CLI tasks** for general-purpose terminal agents across everyday digital and scientific workflows. Its benchmark data, task preparation and scoring are distinct from Terminal-Bench, Long-Horizon Terminal-Bench, SWE-bench and the underlying Harbor evaluation software.
- The first-party repository requires `setup-env` to download or generate some test assets; task execution uses container backends such as Docker/Podman and can invoke model/provider APIs. Its benchmark leaderboard is specific to model, agent, reasoning configuration, resource limits, task state and iteration; it is not a universal agent rating or evidence this catalog performed a terminal run. Treat downloaded assets and arbitrary commands as untrusted, never run them on privileged hosts with production credentials.
- Original first-party sources: https://github.com/facebookresearch/TUA-Bench ; https://arxiv.org/abs/2606.28480
- One inherited source gate qualifies the original published terminal-task identity, 120-task public release and harness/dependency boundaries only. No task/environment downloads, executions, score validation, licensing/security or complete schema/cache/CI/renderer checks, clean/final delivery.
