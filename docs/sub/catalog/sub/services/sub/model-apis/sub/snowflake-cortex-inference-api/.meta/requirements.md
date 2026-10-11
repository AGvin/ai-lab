# Documentation Requirements

## Requirements

- Identify Snowflake Cortex Inference API as Snowflake's released managed model-inference REST API inside the Snowflake service perimeter, with current OpenAI-style Chat Completions and Anthropic-style Messages compatibility for supported model routes.
- Preserve its primary role as hosted model API access, distinct from Snowflake Cortex AI SQL Functions, Cortex Agents, Cortex Search and Snowflake's other data-warehouse product surfaces; the shared Cortex brand does not by itself merge the separate operational semantics.
- Keep model-provider interoperability, native versus proxy invocation, API formats, endpoint paths, supported regions/clouds, governance data boundary, rate limits, authentication and billing fresh against first-party docs.
- Do not infer training/manufacturing provenance for externally developed OpenAI, Anthropic, DeepSeek, Mistral, Meta or other models merely because Snowflake hosts their inference.
- Treat Cortex feature-specific preview status separately from currently generally available inference functions, not as a blanket release status for every Cortex feature.
- Scope response compatibility, endpoint/task support and availability to the actual documented revisions; similar JSON does not guarantee feature-equivalent third-party SDK behavior.

## Validation

- The service is a managed inference/API surface rather than a trained model or local runtime.
- Product boundaries for SQL functions, agents and search services remain explicit.
- Snowflake producer inverse link matches the service's forward provenance.
