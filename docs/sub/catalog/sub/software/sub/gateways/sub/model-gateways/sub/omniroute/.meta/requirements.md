# Documentation Requirements

## Requirements

- Identify OmniRoute as self-hostable model-gateway software that provides a unified API/proxy layer across multiple AI providers, accounts, and compatible model backends.
- Preserve its primary placement under `gateways/model-gateways`: OmniRoute coordinates model-provider access, translation, routing, fallback, quotas, and operational policy rather than acting as a model, inference engine, or hosted model provider itself.
- Explain the OpenAI-compatible client boundary and provider abstraction at a durable level without freezing the current provider count, free-tier count, routing-strategy count, supported-model count, or other fast-moving inventory figures.
- Treat API-key, OAuth, browser/CLI-account, self-hosted, and custom-compatible integrations as provider-access mechanisms owned by OmniRoute rather than separate canonical AI Lab products unless a future integration has an independently justified identity.
- Distinguish self-hosting the gateway from self-hosting inference. Requests routed to remote providers may transmit prompts, tool inputs, images, or other request content to those upstream services; do not present local OmniRoute deployment as a guarantee of local/private inference.
- Keep MCP, A2A, memory, guardrails, token compression, cost telemetry, provider-health handling, desktop/PWA surfaces, and CLI/IDE compatibility as product capabilities. Do not create duplicate canonical nodes merely because those capabilities have substantial internal modules or adapters.
- Preserve the current security configuration boundary when discussed: sensitive stored credentials are protected by the documented encryption-at-rest path when the operator configures the required storage-encryption key, while current upstream security documentation also describes a plaintext passthrough mode when that key is absent.
- Treat TLS/browser fingerprinting, CLI compatibility shaping, local MITM support, and similar compatibility surfaces as operator-sensitive functionality. Describe them for authorized interoperability and troubleshooting; do not frame them as permission to evade provider controls, fraud detection, account restrictions, or upstream terms.
- Treat provider quotas, free-token estimates, prices, performance comparisons, benchmark figures, supported-client counts, releases, and other mutable product state as freshness-sensitive and source-backed when expanded.
- Treat vendor comparison tables and OmniRoute-produced benchmark or savings claims as self-reported evidence rather than independent AI Lab evaluation.
- Preserve the current repository's MIT licensing only as the source-backed open-source software license; do not infer licensing or legal terms for separately operated websites, upstream providers, or third-party integrations from that repository license.
- Do not infer a canonical `produced-by` relation solely from the repository account, sponsorship, current website branding, or downstream commercial relationships. Add producer/ownership relations only when an authoritative source establishes the relevant product identity clearly enough for a stable graph edge.
- Include the current official site, documentation surface, and source repository from canonical entity metadata.

## Validation

- OmniRoute remains a model gateway rather than a model provider, inference runtime, hosted model API, or Agent Skill collection.
- Self-hosted gateway deployment is not conflated with local inference or guaranteed prompt privacy.
- Mutable counts, free-tier totals, benchmarks, prices, provider availability, and compatibility details are not frozen as timeless facts.
- Security-sensitive compatibility features are not described as universal evasion mechanisms or guarantees against upstream enforcement.
- No unsupported producer or legal-ownership relation is asserted.
- Official resource links match canonical entity metadata.
