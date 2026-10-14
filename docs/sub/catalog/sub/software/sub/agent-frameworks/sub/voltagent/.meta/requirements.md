# Documentation Requirements

## Requirements

- Identify VoltAgent as the independently installable, open-source TypeScript/JavaScript agent framework published as `@voltagent/core`, distinct from Mastra, LangGraph, Vercel AI SDK and the separate VoltOps Console observability/operations platform.
- Preserve first-party non-prerelease **`@voltagent/core@2.11.0` (2026-09-28)** and **MIT** project/package licensing. The current monorepo declares **Node >=20**; check actual package/runtime support and peer `ai`/`zod` dependencies before production adoption. Do not confuse monorepo `0.1.0` metadata with the released core package version.
- Describe typed tool-using agents, multi-agent coordination, model-provider integration, memory, guardrails, MCP connectivity, and workflow composition as framework capabilities. Built-in evals, workflow packages, tracing adapters and third-party provider connectors are component/integration surfaces, not independently owned standalone products.
- Keep hosted/self-hosted VoltOps Console, coding-agent dashboards, telemetry/observability, deployment and premium platform services outside the core framework identity; separate service/software ownership requires independent evidence and explicit catalog value assessment.
- **Security and operations:** agent tools and configured workflows may execute network/API calls, retrieve untrusted inputs and store user content. Enforce explicit tool permissions, credential segmentation, scoped memory storage, model-provider privacy/cost limits and observability-data retention; integrations are not default isolation guarantees.
- Reuse first-party `VoltAgent Inc.` ownership substantiated by source `LICENCE`, with exact `produced-by` / `produces` relation to `catalog/producers/v/voltagent-inc`.

## Validation

- Official GitHub repository README, core `package.json`, dated release and `LICENCE` support package identity, published version, MIT grant and runtime metadata.
- VoltAgent software and VoltAgent Inc. producer relation targets agree exactly.
