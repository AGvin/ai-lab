# BenchFlow

**BenchFlow** is an Apache-2.0 Python SDK and CLI for evaluating AI agents against task environments. It runs ACP-compatible agents through a Rollout lifecycle with Scenes, tasks, verifiers and scored results. It is distinct from the [SkillsBench benchmark dataset](../../../../../../../datasets/sub/skillsbench/) and from the separately attributed publishing project.

## Evaluation role and boundaries

BenchFlow provides `bench eval` workflows, multi-agent/multi-round configurations, task execution and captured results/trajectories. Supported sandbox backends include local Docker and separately configured external backends; model providers, paid resources, task contents and agent harnesses have their own versions and costs. Agent evaluation claims from a publisher are not independent AI Lab benchmark results.

## Release compatibility

- Verified public stable release: **v0.7.11 (2026-10-16)**; Python **3.12+**. Public CLI entrypoints: `bench` and `benchflow`.
- The `main` branch declares **0.7.12.dev0**, a development version. An experimental Rust `bench` preview is a separate, incomplete release path and is not the same stable Python CLI.
- SkillsBench **v1.1** declares a BenchFlow requirement **`>=0.6.3,<0.7`**, excluding v0.7.11. Reproducible use requires matching the dataset manifest, runtime release, task pin and verifier. Scores from different versions are not automatically comparable.

## Security, privacy and rights

Task, oracle and verifier code may execute arbitrary operations, while agent and sandbox integrations can consume API credits and expose credentials. Use authorized disposable isolation, least-privilege secrets, network limits and cost caps; published verifier hardening is not an independently tested guarantee.

**Do not upload agent trajectories by default.** The optional `bench traj upload` workflow can transfer redacted work-session content off-device. Human review, privacy/consent checks and an authorized destination are required; automatic redaction cannot be assumed to catch all secrets or confidential files.

The code repository declares Apache-2.0; independently check third-party task licenses, model/provider terms and contributed assets. Current legal incorporation, ultimate beneficial ownership and indirect geopolitical stakes of the publisher have not been independently established.

## Relations

- Produced by: [BenchFlow publishing project](../../../../../../../producers/sub/b/sub/benchflow/).
- Separate task dataset: [SkillsBench](../../../../../../../datasets/sub/skillsbench/).

## Original resources

- [Official source](https://github.com/benchflow-ai/benchflow)
- [Published v0.7.11](https://github.com/benchflow-ai/benchflow/releases/tag/v0.7.11)
- [Python package](https://pypi.org/project/benchflow/)
- [Sandbox hardening reference](https://github.com/benchflow-ai/benchflow/blob/main/docs/sandbox-hardening.md)
- [Release channels](https://github.com/benchflow-ai/benchflow/blob/main/docs/release.md)
