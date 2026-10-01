# Documentation Requirements

## Requirements

- Identify Shieldstral 1.0 3B as the concrete released 3B-parameter Shieldstral model published by Mistral AI in September 2026.
- Preserve its source-backed role as a safety classifier for conversational AI inputs and outputs, including supported moderation categories only where current first-party sources define them.
- Preserve model architecture/base-model lineage, license, context length, prompting/classification contract, and deployment guidance only from current official release/model-card evidence.
- Keep benchmark results and comparisons scoped to their evaluated datasets, versions, prompts, and baselines rather than treating them as timeless safety guarantees.
- Keep hosted aliases, quantized artifacts, and service-specific moderation routes outside the trained-model identity.

## Validation

- The model is not conflated with Mistral's hosted moderation service or with generic guardrail concepts.
- Safety-classification capability is not described as deterministic prevention of harmful model behavior.
- Mutable availability and performance claims remain freshness-sensitive.
