# Harbor

Harbor is an open-source framework for running reproducible language-model and agent evaluations in containerized tasks and collecting trajectories for reinforcement-learning workflows.

## Evaluation role and boundaries

Its CLI and Python tooling coordinate agents, benchmarks and task environments across Docker and supported cloud sandboxes. Terminal-Bench, SWE-bench and other datasets retain their own identities, and generated RL rollouts are not ground-truth benchmark labels.

## Reproducibility and operational safeguards

Pin benchmark revision, model, agent harness, task environment, sandbox backend, evaluator, concurrency, tool/token/time budgets and seed. Running arbitrary agent code requires sandbox isolation, restricted credentials and dataset authorization. Claims about rankings must include reproducible evaluation conditions.

## Relations

- Produced by: [Harbor Framework Team](../../../../../../../producers/sub/h/sub/harbor-framework/)

## Official resources

- [Documentation](https://harborframework.com/docs/)
- [Source](https://github.com/harbor-framework/harbor)
