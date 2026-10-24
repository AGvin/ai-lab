# Documentation Requirements

## Requirements

- Identify ServiceNow AgentLab as the separately published framework for developing, running and evaluating browser agents on BrowserGym task environments with agent implementations and experiment/reproducibility helpers; it is not the benchmark dataset itself.
- Preserve agent-experiment orchestration, parallel runs through Ray, trace/result collection, configurable LLM/model/provider wrappers and unified benchmarking as features of the one `AgentLab` framework.
- Keep BrowserGym as the task environment/adapter layer and AgentLab as agent/experiment/evaluation tooling; original WorkArena, WebArena, WebArena-Verified and related benchmarks retain their own canonical dataset identities and producers.
- Distinguish `AgentLab` research infrastructure from managed production agent platforms, browser-session vendors and standalone model-evaluation packages; first-party project explicitly says not a consumer product.
- Pin AgentLab release (first-party latest tag as of review **v0.4.2**), BrowserGym adapter, task/version split, reproducibility seed, model and prompt configs, environment state and evaluator before comparing reported benchmark outcome or third-party agent claims.
- Keep the repo's named research contributors and linked papers source-backed, not as universal authority for independent benchmark maintainers; preserve ServiceNow producer inverse.

## Validation

- The first-party maintained repository substantiates released installable software and the distinct source/task/evaluation or hosted boundary.
- Pinning sources and operating environment does not conflate upstream benchmark or downstream service identity.
- Exact producer inverse resolves to the existing ServiceNow or Browser Use source-of-truth entity.
