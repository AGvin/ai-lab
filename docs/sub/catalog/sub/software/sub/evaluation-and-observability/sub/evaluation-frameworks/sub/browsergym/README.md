# BrowserGym

BrowserGym is ServiceNow's open-source, Gymnasium-compatible framework for interactive browser-task environments and reproducible agent evaluation.

## Evaluation role and boundaries

BrowserGym supplies task observation/action interfaces and adapters for benchmark environments such as WorkArena and WebArena. The core, experiment utilities and benchmark-specific adapters are modules in one software family; external benchmark tasks retain their own maintainers and datasets. AgentLab separately orchestrates agent experiments.

## Reproducibility and operational safeguards

Reproducible runs require matching adapter version, task definitions, site fixtures, authentication, environment resets and scoring logic. Some benchmark environments require gated access. Run agents in disposable browsers against approved test environments rather than production sites by default.

## Relations

- Produced by: [ServiceNow](../../../../../../../producers/sub/s/sub/servicenow/)

## Official resources

- [Source](https://github.com/ServiceNow/BrowserGym)
