# Documentation Requirements

## Requirements

- Identify BenchFlow as an independently published, installable Apache-2.0 Python SDK and `bench`/`benchflow` command-line environment framework for controlled agent/task evaluation, not a benchmark dataset, a model, a hosted execution service, an independently verified corporation or the experimental Rust CLI release.
- Preserve source-backed features: ACP-compatible agents, Scene/Role/Turn and Rollout lifecycle, native/legacy task packages, executable verifiers/rewards, captured trajectories, and Docker/Daytona/Modal-type sandbox backends. These are capabilities documented upstream, not locally verified performance or security guarantees.
- Pin the specific software release and agent/benchmark/task revision, sandbox implementation, model/provider, evaluation mode, scorer/verifier and output handling for reproducibility. The original public release `v0.7.11` dated 2026-10-16 targets Python >=3.12 and exposes the `bench` and `benchflow` scripts; current main `0.7.12.dev0` is not a public stable release.
- Disclose version conflict: the original SkillsBench v1.1 dataset registry demands BenchFlow `>=0.6.3,<0.7`, so public BenchFlow v0.7.11 is outside its compatible range. Do not mix results or claim direct plug-and-play compatibility without checking versioned task manifests.
- Treat task `environment/`, `oracle/`, `verifier/` and agent process code as untrusted. Run only in isolated disposable sandbox backends, use least privilege and bounded network, restrict authentication and API cost, and verify permissions before executing third-party workflows. Published sandbox hardening is a publisher claim, not an AI Lab penetration test.
- **Trajectories and logs can reveal private source, messages, secrets and tools.** Do not run `bench traj upload` or share work sessions without human preview, redaction review, authorization and an acceptable retention policy; the project's claimed local redaction is not a complete exfiltration guarantee.
- Separate the official Apache-2.0 source license from the rights, task contents, environment images, generated outputs, external model/provider costs and contributor materials. Exact corporate operator, ultimate beneficial ownership and any indirect Russian stakes have not been independently audited. No geopolitical Tier 1/2 claim without verifiable current evidence.
- Maintain the canonical `produced-by` link to `catalog/producers/b/benchflow` with reciprocal `produces`, and a local reader link to the distinct SkillsBench dataset. Retain the producer's existing SkillsBench relationship, with no duplicate producer acceptance credit.

## Validation

- Source source-of-truth is the first-party `benchflow-ai/benchflow` repository and tagged release plus `pyproject.toml`; verify no alias collision with original `SkillsBench` dataset or BenchFlow publisher.
- The canonical software entity, requirements, reader, parent category entry and inverse producer controls resolve; public runtime trials, complete hidden ownership licensing clearance and whole-catalog CI remain unverified.
