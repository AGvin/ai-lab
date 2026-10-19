# Qwen3.8-2.4T-A95B

Qwen3.8-2.4T-A95B is the concrete Qwen3.8 model released on 2026-08-12.

## Scope and boundaries

- The official distinction between approximately 2.4T total parameters and 95B active parameters without inferring unpublished expert-routing details.
- Exact artifacts, quantizations, provider routes, benchmark state, and deployment recommendations remains outside intrinsic model identity unless separately materialized.

## Relations

- Member of: [`catalog/models/alibaba/qwen/qwen3-8`](../../../..//)

## Decision and Operational Boundaries

Qwen3.8-2.4T-A95B is the released text-only, thinking-only checkpoint with 2.4T total and 95B active parameters.

- Use its Qwen3.8-Max license rather than the repository's Apache badge. Commercial MaaS/AI Work Assistant businesses above USD 50 million aggregate revenue during any consecutive 12 months require a separate license; the limited internal-use exception does not permit third-party access.
- The license also requires prominent model attribution above its specified user/revenue thresholds; consult the exact license before distribution or commercial deployment.
- Keep native 262,144-token context and documented extension to 1,010,000 separate from the hosted Max service's multimodal, non-thinking, and built-in-tool features.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- <https://github.com/QwenLM/Qwen3.8>

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3.8](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [Official model card or license: Qwen/Qwen3.8-2.4T-A95B/blob/main/LICENSE](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/main/LICENSE)
