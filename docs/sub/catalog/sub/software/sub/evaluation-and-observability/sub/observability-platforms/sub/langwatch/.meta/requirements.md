# Documentation Requirements

## Requirements

- Identify LangWatch as a separately deployable, open-core observability/evaluation/control platform for agents and coding assistants from the LangWatch project, distinct from Langfuse, Arize Phoenix, Opik, LangSmith and generic model gateways.
- Preserve non-prerelease **v3.20.1 (2026-10-02)** for the published server, with first-party release variants `v3.20.1`, `langwatch@v3.20.1` and `langwatch-3.20.1` representing server/package/chart release surfaces, not three independent catalog products. The official self-hosted quick start is `npx @langwatch/server`; production deployments require explicit self-hosting configuration.
- Cover tracing/observability, LLM and agent evaluations, simulation testing, prompt controls, coding-agent session/cost review and integrated model routing/governance as capabilities of one software identity. Hosted LangWatch Cloud, CLI launchers, language SDKs and built-in AI Gateway features are not duplicate software/managed service peers without separately verified independent lifecycle.
- **Licensing:** the repository root `LICENSE.md` is Apache-2.0 and SDKs are described as MIT. The independent `enterprise/LICENSE.md` covers enterprise capabilities (including SSO/SCIM, audit-log access and gateway webhooks) and requires a genuine commercial license to enable/use them in production. Do not describe every source directory or feature as uniformly Apache-2.0, free or permissively redistributable.
- **Trust and deployment:** trace payloads, prompts, agent outputs, workspace identities, API keys and coding-assistant sessions may contain private content. Validate consent, retention, tenant isolation, data residency, gateway credentials, telemetry egress and production capacity/security per deployment. Self-hosted, hosted and restricted enterprise features have materially different trust boundaries.
- Attribute the current publisher as LangWatch with the first-party enterprise license naming Reasoning Engine B.V. as the legal rights holder. Reconcile exact `produced-by` / `produces` relation to `catalog/producers/l/langwatch`.

## Validation

- Official repository README, v3.20.1 server release, root `LICENSE.md`, `enterprise/LICENSE.md`, and self-host documentation support release, license and deployment boundaries.
- Both ends of the software-producer relation resolve to matching canonical IDs.
