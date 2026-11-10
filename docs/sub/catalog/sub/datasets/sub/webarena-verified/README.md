# WebArena-Verified

WebArena-Verified is ServiceNow’s maintained, audited derivative of WebArena for evaluating web agents. It supplies a versioned task corpus and scoring contract, with corrections to task instructions and expected answers. Original WebArena research and the separate VisualWebArena benchmark retain their own identities.

## Evaluation contract

The current release contains 812 tasks, including a separately selected 258-task Hard subset. Typed JSON answers and captured network events support deterministic scoring and offline replay from HAR traces. Match the audited task revision, evaluator and environment to the run; a similar task ID does not make results comparable to original WebArena or VisualWebArena. Verification reduces identified measurement problems but does not establish that every remaining task or scorer is error-free.

## Distribution and operation

The repository’s release history scheduled public availability for December 4, 2025 and records PyPI and uvx/Docker distribution improvements in January and February 2026. Those are distribution changes within this benchmark. The repository uses Apache 2.0; provision and reset the documented web environments, authorize the agent’s test accounts and control access to network traces. Trace capture can include account or page data. BrowserGym and AgentLab remain separate environment and experiment tools.

## Relations

- Produced by: [ServiceNow](../../../producers/sub/s/sub/servicenow/)

## Official resources

- [WebArena-Verified repository](https://github.com/ServiceNow/webarena-verified)
- [Official documentation](https://servicenow.github.io/webarena-verified/)
- [Current documentation](https://servicenow.github.io/webarena-verified/latest/)
- [Repository license](https://github.com/ServiceNow/webarena-verified/blob/main/LICENSE)
