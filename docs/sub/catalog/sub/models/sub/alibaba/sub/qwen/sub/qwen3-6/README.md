# Qwen3.6

Released dense and MoE vision-language checkpoints with separate weight identities and Apache-2.0 licensing.

## Decision and Operational Boundaries

- Preserve the exact member's input/output and license contract; do not turn toolkit options, quantizations, or hosted aliases into peer model identities.
- Dense 27B and MoE 35B-A3B have different total-weight requirements; active parameters are not a runtime memory estimate.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen](../../) |
| Produced by | [Qwen Team](../../../../../../../producers/sub/q/sub/qwen-team/) |
| Includes | [Qwen3.6-27B](./sub/models/sub/qwen3-6-27b/) |
| Includes | [Qwen3.6-35B-A3B](./sub/models/sub/qwen3-6-35b-a3b/) |

## Primary Sources

- [Official repository: QwenLM/Qwen3.8](https://github.com/QwenLM/Qwen3.8)
