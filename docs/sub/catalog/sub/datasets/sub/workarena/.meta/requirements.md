# Documentation Requirements

## Requirements

- Identify WorkArena as ServiceNow's published benchmark family for browser agents completing ServiceNow workplace knowledge-work tasks; do not conflate it with BrowserGym or AgentLab evaluation infrastructure.
- Preserve its distinct 2024 task tiers: WorkArena-L1 has 19,912 instances across 33 atomic task types; WorkArena++ has 682 compositional planning/reasoning tasks with multiple configurations. The first-party repository and task components are shared, so do not duplicate WorkArena++ as another family merely because of its paper/release name.
- Evaluation depends on provisioned and authenticated ServiceNow instances. First-party benchmark instance assets have a gated-access process; distinguish access to published code from permission to use an evaluation instance.
- Pin tier (L1 versus ++/L2/L3), task set, repository/version, environment instance state, reset procedure, evaluator and agent settings before comparing task-success results.
- Keep WorkArena's controlled enterprise ServiceNow workflow evaluation distinct from WebArena's demo-like self-hosted shopping/social sites, OSWorld's desktop environment, and original Mind2Web's offline trajectory/action-prediction tasks.
- Treat BrowserGym, AgentLab, Playwright and the benchmark package as tooling/dependencies, not alternate canonical dataset or producer identities. Preserve ServiceNow research ownership and its reciprocal relation.

## Validation

- The first-party WorkArena repository substantiates atomic and compositional task counts, separate research publications and gated ServiceNow instance access.
- The WorkArena `produced-by` endpoint is reciprocated by the existing ServiceNow producer's exact `produces` endpoint.
