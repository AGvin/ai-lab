# Documentation Requirements

## Requirements

- Identify GroqCloud as Groq LLC's hosted cloud service for API access to AI models and Groq-provided compound systems.
- Preserve the current lifecycle distinction between production models/systems and preview models; do not present preview availability as production-stable service coverage.
- Keep third-party model identity, model licensing, model lifecycle, and model-specific limitations with their proper owners rather than attributing them to Groq merely because GroqCloud serves them.
- Preserve the current data-handling boundary at a stable level: usage metadata is retained, while inference customer inputs/outputs are not retained by default except where a feature requires retention or limited platform-protection handling applies.
- Keep exact model inventory, throughput, pricing, rate limits, context limits, regions, retention controls, and other mutable service state source-backed and time-scoped when expanded.
- Render the standard `entity-relations` block from validated current-entity relations.
- Include current official GroqCloud documentation, Privacy Policy, and Services Agreement references.

## Validation

- Preview models are not described as production-stable merely because they are currently callable.
- GroqCloud remains a hosted service profile and does not duplicate third-party model profiles.
- Data-retention wording preserves the documented exceptions instead of overstating zero retention.
- The `produces` / `produced-by` relation pair resolves consistently to Groq LLC.
