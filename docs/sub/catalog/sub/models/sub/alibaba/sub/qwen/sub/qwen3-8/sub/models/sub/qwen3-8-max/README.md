# Qwen3.8-Max

Qwen3.8-Max is the stable Qwen3.8 model identity exposed as `qwen3.8-max` by Alibaba Cloud Model Studio.

## Scope and boundaries

- Dated service snapshots such as `qwen3.8-max-0902` as versioned snapshots of Qwen3.8-Max rather than peer model identities unless a later source establishes an independent model identity.
- Mutable serving aliases, regional availability, quotas, pricing, and provider routing remains outside intrinsic model identity.
- Only source-backed capabilities and limits; re-check current first-party Model Studio documentation before updating mutable service facts.

## Decision and Operational Boundaries

Qwen3.8-Max is the independently documented hosted model ID qwen3.8-max, distinct from its released text-only 2.4T-A95B checkpoint.

- The service supports image/text/video input and text output, with a documented one-million-token context; exact input/output budgets and tools remain region- and snapshot-specific.
- Keep dated snapshots such as 0902 beneath the stable identity and do not assume a rolling alias reproduces an earlier snapshot.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- <https://docs.modelstudio.console.alibabacloud.com/en/model-studio/qwen3-8-max>
- <https://www.alibabacloud.com/help/en/model-studio/newly-released-models>

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3.8](../../../../) |

## Primary Sources

- [Alibaba Cloud: qwen3 8 max](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- [Official model card or license: Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
