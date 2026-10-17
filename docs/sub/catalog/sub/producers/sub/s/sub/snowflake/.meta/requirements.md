# Documentation Requirements

## Requirements

- Identify Snowflake as the operating provider of Snowflake Cortex's managed model inference API surface within Snowflake's data platform.
- Preserve Snowflake as the **current maintainer** of the independent MIT Python TruLens evaluation/tracing framework after the 2024 TruEra technology/team acquisition; TruEra is the historical origin, not a current Snowflake-hosted-model API.
- Keep Snowflake-hosted model inference, Snowflake Cortex AI Functions, Cortex Agents, Cortex Search and Snowflake's managed warehousing services conceptually separate; they may share a billing/account model without becoming identical product identities.
- Treat enterprise data governance, region availability, pricing, model menus, authentication and platform support as mutable service/provider facts.
- Do not infer Snowflake authorship of externally trained OpenAI, Anthropic, Meta or other models merely because it serves them.

## Validation

- Reciprocal `produces` relation resolves to managed Cortex Inference API; separate `maintains` link exactly reciprocates the TruLens software `maintained-by` relation.
- Provider ownership and trained model authorship are not conflated.
