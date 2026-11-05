# DeepSeek-V3.2

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Ultimate beneficial ownership and control rights have not been verified. This is not a finding of Russian ownership or adoption clearance; see the [provenance policy](../../../../../../../../../project/sub/policies/sub/russia-linked-ai/).

## Checkpoint and evidence

DeepSeek's released V3.2 checkpoint supports reasoning with tool use and DeepSeek Sparse Attention. It is distinct from V3.2-Exp and V3.2-Speciale; Speciale's reasoning-only tool limitation must not be assigned to this checkpoint. The publisher licenses repository code and weights under MIT. Its updated message encoding and output parsing require integration-specific validation; the supplied parser does not recover malformed output. Benchmark superiority is publisher evidence, not independently reproduced here.

## Integration boundary

Use V3.2-specific encoding and robust output validation. The card states that its developer role is limited to search-agent scenarios and is not accepted by the official API. Sandbox tools and require authorization for consequential actions. Do not equate a hosted API alias with an immutable checkpoint revision.

Source review: 2026-11-05. No weights, remote code, model inference or tools were executed for this profile. Source-scoped documentation acceptance does not establish deployment readiness or ownership clearance.

## Relations

- Member of: [DeepSeek model family](../..//)

## Official resources

- [First-party model card](https://huggingface.co/deepseek-ai/DeepSeek-V3.2)
- [Exact upstream license](https://huggingface.co/deepseek-ai/DeepSeek-V3.2/blob/main/LICENSE)
