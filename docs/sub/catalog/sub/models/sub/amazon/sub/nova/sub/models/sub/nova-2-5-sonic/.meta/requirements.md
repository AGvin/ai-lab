# Documentation Requirements

## Requirements

- Identify Amazon Nova 2.5 Sonic at canonical ID `catalog/models/amazon/nova/models/nova-2-5-sonic`.
- Preserve the trained identity, family membership and upstream producer separately from hosted routes, runtime packages and mirrored artifacts.

## Validation

- Use primary identity and operational references and retain the reciprocal catalog relation.

## Decision and operational boundaries

- Preserve this canonical boundary: Released successor to Nova 2 Sonic with the same documented bidirectional streaming API surface. Official sources conflict on context: the October 5, 2026 announcement says 256K tokens, while the current Nova product page says up to 1M. No single unqualified capacity is asserted here. The service card excludes real-time speech-to-speech translation and customer fine-tuning. System prompts and configurations are customization controls, and migration still needs workload retesting.
- AWS announced general availability on October 5, 2026. The service card describes compatibility with Nova 2 Sonic APIs, voices and languages while asking customers to retest their own use cases. [Nova 2.5 Sonic general availability announcement](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-nova-2.5-Sonic/) [Nova 2.5 Sonic service card](https://docs.aws.amazon.com/ai/responsible-ai/nova-2-5-sonic/overview.html)
- Context evidence conflicts: the dated announcement states `256K`, while the current product page states up to `1M`. Verify the chosen deployed route before budgeting session memory; do not silently select one figure as universal. [Nova 2.5 Sonic general availability announcement](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-nova-2.5-Sonic/) [Amazon Nova models](https://aws.amazon.com/nova/models/)
- The service card supports speech/text interaction over a bidirectional stream. It excludes real-time speech-to-speech translation and customer fine-tuning; system prompts and configuration remain available controls. [Nova 2.5 Sonic service card](https://docs.aws.amazon.com/ai/responsible-ai/nova-2-5-sonic/overview.html)
