# Documentation Requirements

## Requirements

- Identify the Glean enterprise service as a connected, **permissions-aware knowledge workspace and assistant**, not a foundation model, generic vector database, self-hosted code package, or all source services combined.
- Official first-party docs describe enterprise search and source-grounded answers, personalized retrieval, drafting and actions across supported connected applications. Search is one function of the broader product; retain one durable hosted product identity.
- Explain the security model as **connector-/source-permission-aware** retrieval with citations and per-user identity rather than implying all organization documents are equally visible. A connector error or stale ACL mirror can still affect operational correctness; no independent penetration test was made.
- Distinguish a connector's original source ownership and terms from Glean's indexed workspace. Enterprise content, chat history, generated summaries and actions can cross different processors and provider boundaries.
- Admins should review connector OAuth scopes, ACL synchronization, least-privilege identities, data residency, retention, audit logs, approval for external actions and contractual model-data processing. Treat enterprise integrations as high-value secrets.
- Connector inventory, price/plan, exact feature availability, accuracy and sync latency change; use live Glean docs without inventing fixed SLA, number of connectors or unconditional compliance.
- No tenant created, connection granted, enterprise query run, source-permission audit or whole-catalog clean pass performed.

## Validation

- One canonical service reader under the selected category and one relative index link; distinct source software, model, content and operator boundaries remain explicit.
- First-party evidence supports the scoped profile only. Do not infer runtime tests, full rights/contract audits or repository-wide clean status.
