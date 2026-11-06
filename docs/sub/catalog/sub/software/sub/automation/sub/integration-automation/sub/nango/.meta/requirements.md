# Documentation Requirements

## Requirements

- Identify Nango as a source-available product integration platform for OAuth/API-key connections, token refresh, authenticated proxying, TypeScript integration Functions, sync/events and agent/MCP action tooling, distinct from generic visual no-code automation and OAuth identity-providers themselves.
- Preserve one Nango platform identity across vendor-operated cloud, BYOC/private deployment and self-managed editions. Nango's first-party repository describes Auth, Proxy and Functions as platform primitives; a new SDK, connector, tool schema or hosted plan is not a new canonical product.
- Record the distribution license as **Elastic License 2.0** (source-available with use restrictions), not unconditionally OSI-approved open source; compare free self-host feature limitations, paid cloud and BYOC entitlements against the version/plan at evaluation time.
- Distinguish vendor-operated Nango Cloud, vendor-operated enterprise BYOC in the customer's environment and customer-operated Enterprise Self-Managed deployments.
- State the free self-hosted edition's Auth/Proxy feature boundary. Its documented trust model is one trusted organization: separate accounts are not hardened isolation for mutually untrusted users, and signups are enabled by default.
- Preserve the documented Self-Managed encryption condition: without a configured direct or KMS-wrapped encryption key, credentials are stored unencrypted, persisted-record storage/retrieval fails instead of falling back to plaintext, and Connect UI requires a key. The fail-closed record behavior must not be generalized to credentials.
- Keep the integration code and third-party API permissions under the adopting user/operator's control. AI-generated integration Functions require code review, OAuth scope restriction, idempotency/retry safety, secrets isolation and validation for write actions; generic maintained connector counts change.
- Separate Nango's multi-tenant credential broker/integration runtime from Composio's hosted agent-tool marketplace, Arcade policy/governance runtime, Activepieces/n8n visual flow builders and Pipedream hosted integration runtime.
- Pin source revision, API compatibility, execution state, integration provider, account scoping, sync cursor, webhook retries, deployment data stores and licensing to compare implementations reproducibly.

## Validation

- First-party published documentation and/or repository demonstrates an existing usable product, with install/deployment boundary correctly distinguished.
- Exact reciprocal producer relation resolves to one canonical organization rather than any evaluated integration/tool provider.
- Source-available/managed feature and licensing claims are versioned, never silently generalized.
