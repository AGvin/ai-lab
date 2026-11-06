# Documentation Requirements

## Requirements

- Identify Snowflake Cortex Inference API as Snowflake's released managed model-inference REST API inside the Snowflake service perimeter, with current OpenAI-style Chat Completions and Anthropic-style Messages compatibility for supported model routes.
- Preserve its primary role as hosted model API access, distinct from Snowflake Cortex AI SQL Functions, Cortex Agents, Cortex Search and Snowflake's other data-warehouse product surfaces; the shared Cortex brand does not by itself merge the separate operational semantics.
- Keep model-provider interoperability, native versus proxy invocation, API formats, endpoint paths, supported regions/clouds, governance data boundary, rate limits, authentication and billing fresh against first-party docs.
- Do not infer training/manufacturing provenance for externally developed OpenAI, Anthropic, DeepSeek, Mistral, Meta or other models merely because Snowflake hosts their inference.
- Treat Cortex feature-specific preview status separately from currently generally available inference functions, not as a blanket release status for every Cortex feature.
- Scope response compatibility, endpoint/task support and availability to the actual documented revisions; similar JSON does not guarantee feature-equivalent third-party SDK behavior.

- Render the identity, provenance and operational context recorded in canonical `entity.identity_note`; keep version-sensitive claims and official resources aligned with the cited first-party sources.

- Render the standard `entity-relations` block from validated current-entity relations, ordered by explicit numeric order, target canonical name and target ID; resolve every visible target to its reader.

## Validation

- The service is a managed inference/API surface rather than a trained model or local runtime.
- Product boundaries for SQL functions, agents and search services remain explicit.
- Snowflake producer inverse link matches the service's forward provenance.

## Scoped original-source qualification — 2026-11-06

- Snowflake Cortex Inference API is Snowflake-managed REST model inference, separate from Cortex AI SQL Functions, Agents and Search. Snowflake documents OpenAI-style Chat Completions and Anthropic Messages for eligible Claude routes. A requester's default role needs SNOWFLAKE.CORTEX_USER or SNOWFLAKE.CORTEX_REST_API_USER; narrower REST-only permissions do not remove pre-existing broad Cortex grants.
- Request-format compatibility does not guarantee every provider tool, SDK, model or region works. Verify model route, Snowflake grants, cross-region processing, data-governance and consumption charges before production use.
- Verified first-party source 1: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api
- This source qualification accepts only the existing hosted-service identity and bounded claims. It does not establish full freshness, legal/ownership/license clearance, independent security or performance, authenticated endpoints, complete schema/cache/CI/render, clean pass or final delivery.
