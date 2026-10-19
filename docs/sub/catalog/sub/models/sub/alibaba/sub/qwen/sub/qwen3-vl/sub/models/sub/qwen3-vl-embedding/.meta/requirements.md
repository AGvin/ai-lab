# Documentation Requirements

## Requirements

- Identify Qwen3-VL-Embedding as the released multimodal embedding model based on Qwen3-VL for unified text, image, and video representations.
- Preserve retrieval/search/clustering/tagging positioning and cross-modal embedding behavior only while supported by current first-party documentation.
- Keep Qwen3-VL-Embedding distinct from generative Qwen3-VL members, text-only embedding services, rerankers, and the Model Studio hosting service.
- Treat embedding dimensions, input limits, modality/token accounting, pricing, regions, quotas, runtime/provider support, and benchmark results as freshness-sensitive.
- Attribute retrieval/quality comparisons to Alibaba/Qwen or the cited evaluator.

## Decision and Operational Boundaries

- qwen3-vl-embedding is the named hosted model for unified vectors from text, image, video, or mixed input.
- Its output is an embedding representation, not generated text or an independently established reranker result; distinguish retrieval stages despite overlapping marketing descriptions.
- Do not assign the sizes, license, or embedding dimensions of an open Qwen3-VL-Embedding checkpoint to this unversioned hosted identity without an exact mapping.
- Keep query/document preprocessing and vector dimensions compatible across an index; enforce source-document access rights independently of vector similarity.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node remains a concrete embedding model identity under Qwen3-VL.
- Hosted-service pricing/region facts are not generalized into permanent model architecture.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
