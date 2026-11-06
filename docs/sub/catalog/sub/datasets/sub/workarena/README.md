# WorkArena

WorkArena is ServiceNow’s benchmark family for agents performing workplace tasks through a ServiceNow browser interface. It combines task definitions, generated instances and success checks for enterprise knowledge work. BrowserGym supplies an environment framework and AgentLab experiment tooling; neither is an alternative identity for the benchmark.

## Task tiers

WorkArena-L1 contains 33 atomic task types with 19,912 instances. WorkArena++ adds 682 compositional tasks that exercise planning and reasoning across task configurations. The L1, L2 and L3 settings must be identified alongside task selection, repository revision, evaluator and agent configuration. Shared source and task components do not make every tier’s results directly comparable.

## Evaluation access

Evaluation requires a provisioned, authenticated ServiceNow instance and a defined reset procedure. Current first-party instructions use gated WorkArena instance assets with an approval and authentication process; access to public code alone does not grant an instance. The repository uses Apache 2.0. The supplied instances permit benchmarking, evaluation and research, excluding training, production and sensitive, proprietary or personally identifiable data storage. Availability and data persistence are not guaranteed. Use authorized benchmark accounts, separate instance and model credentials, and record environment state.

## Relations

- Produced by: [ServiceNow](../../../producers/sub/s/sub/servicenow/)

## Official resources

- [WorkArena repository](https://github.com/ServiceNow/WorkArena)
- [Official website](https://servicenow.github.io/WorkArena/)
- [Benchmark instance access](https://huggingface.co/datasets/ServiceNow/WorkArena-Instances)
- [Repository license](https://github.com/ServiceNow/WorkArena/blob/main/LICENSE)
