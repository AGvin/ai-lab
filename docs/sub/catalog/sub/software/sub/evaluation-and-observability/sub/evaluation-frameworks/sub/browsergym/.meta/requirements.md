# Documentation Requirements

## Requirements

- Identify BrowserGym as ServiceNow's released Python Gymnasium-compatible interactive browser-task environment for research/evaluation, not as any one benchmark dataset or hosted end-to-end browser agent service.
- Preserve its unified task/observation/action environment API, benchmark adapters and reproducible task reset/evaluation hooks as infrastructure for running WebArena, WorkArena, VisualWebArena, AssistantBench, and other external suites.
- The official project publishes `browsergym`, `browsergym-core`, optional `browsergym-experiments` and benchmark-specific adapters. These are distributions/modules of one framework family and do not imply that ServiceNow owns every included benchmark or site.
- Distinguish BrowserGym task environment from the separately maintained ServiceNow AgentLab experiment/orchestration framework (Ray-scale parallel agent runs, agent implementations, metrics) and from Playwright browser automation.
- Benchmark availability and result comparability depend on package/adaptor version, underlying benchmark task revision, site fixture provisioning, authentication, environment reset, model/browser state and evaluation script; specific WorkArena access may be gated.
- Official repository cautions the research infrastructure is not a consumer product. Apply sandboxed/disposable browser environments and never run arbitrary agent actions against production sites by default.
- Preserve first-party ServiceNow ownership and reciprocal producer inverse without transferring ownership of upstream benchmarks.

## Validation

- The first-party maintained repository substantiates released installable software and the distinct source/task/evaluation or hosted boundary.
- Pinning sources and operating environment does not conflate upstream benchmark or downstream service identity.
- Exact producer inverse resolves to the existing ServiceNow or Browser Use source-of-truth entity.
