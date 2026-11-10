# DeepSeek-R1

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Ultimate beneficial ownership or governance/control rights have not been fully verified. This is not a finding of Russian ownership or adoption clearance. See the [provenance policy](../../../../../../../../../project/sub/policies/sub/russia-linked-ai/).

## Checkpoint and evidence

DeepSeek-R1 is the original released reasoning checkpoint based on DeepSeek-V3-Base, distinct from R1-Zero, R1-0528 and Qwen/Llama distilled checkpoints. The card reports 671B total/37B active parameters, MoE and 128K context. Activated count is not storage or serving-memory demand. The publisher declares MIT for original code and weights; distilled models retain distinct upstream Qwen/Llama obligations. The card's historical Transformers support statement and Hub-generated loading examples differ; current runtime compatibility has not been validated. Benchmark claims are not independently reproduced.

## Integration boundary

Pin the exact original R1 revision; do not silently substitute an API alias, later release or distilled model. Review remote code and confirm serving support independently before loading. Isolate generated code and tool execution; validate outputs and resource requirements.

Source review: 2026-11-05. No weights, remote code, model inference or tools were executed. Source-scoped documentation acceptance does not establish deployment readiness.

## Relations

- Member of: [DeepSeek](../../)

## Official resources

- [First-party model card](https://huggingface.co/deepseek-ai/DeepSeek-R1)
- [Original R1 license](https://github.com/deepseek-ai/DeepSeek-R1/blob/main/LICENSE)
