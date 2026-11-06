# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Robostral Navigate 8B as Mistral's first embodied navigation model using RGB images plus natural-language instructions to drive robot navigation.
- Preserve the single-RGB-camera/no-depth/LiDAR boundary and benchmark claims only as first-party evidence, not universal hardware requirements or deployment guarantees.
- Treat availability, supported robot embodiments, runtime packaging, benchmark results, and deployment guidance as freshness-sensitive.

## Validation

- Membership resolves to Robostral.

## Source-backed profile

- Required reader orientation: Robostral Navigate 8B is Mistral AI’s embodied-navigation model, introduced in July 2026 for RGB observations and natural-language instructions.
- Preserve this model-scoped fact: The 8B model predicts a next target location and orientation by pointing in the current image; it can use local-frame displacement when the target is outside the field of view. [Robostral Navigate release](https://mistral.ai/news/robostral-navigate/)
- Preserve this model-scoped fact: Mistral’s lifecycle register lists Robostral Navigate as active. Its release page offers contact with the robotics team rather than documenting a public weight download or serverless API. [Robostral Navigate lifecycle](https://legal.mistral.ai/ai-governance/models/robostral-navigate/) [Robostral Navigate release](https://mistral.ai/news/robostral-navigate/)

## Operational and interpretation boundaries

- Explain this boundary: A single RGB camera is the model’s documented observation interface. Navigation benchmark results do not establish collision avoidance, fail-safe actuation or safe operation on every robot. Robot control and physical safeguards remain separate system responsibilities. [Robostral Navigate technical report](https://arxiv.org/abs/2607.20785)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
