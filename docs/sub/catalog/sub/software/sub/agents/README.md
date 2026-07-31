# Agents

Agent products are grouped by where their agent actions can run:

- [`local/`](./sub/local/) — actions run in the user's environment, even when the agent uses hosted models or services;
- [`hybrid/`](./sub/hybrid/) — the same product supports both local execution and a separate producer-operated cloud execution environment.

This separation distinguishes the execution model without treating every agent that calls a hosted model as hybrid. Hosted-only agents are documented under [development services](../../../services/sub/development/sub/agents/).
