# Documentation Requirements

## Requirements

- Identify Qwen Team as the canonical producer team for the Qwen model series represented in the catalog.
- Preserve the validated organizational boundary to Alibaba Cloud without inferring ownership or a stronger parent/child relation.
- Keep concrete model, version, artifact, deployment, and provider details in their corresponding canonical model or service owners.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Content Specification

- Use `Qwen Team` as the page title.
- State concisely that Qwen Team develops the represented Qwen models at Alibaba Cloud.
- Include the official Qwen website and official Qwen GitHub organization.

## Validation

- The page does not infer `owned-by`, `parent-of`, or another stronger organizational relation from the documented structural relationship.
- Model details remain in model-domain pages rather than being duplicated here.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.

## Model Navigation

- Keep the produced-model navigation synchronized with the current canonical relation projection as model-series entries are added; retain capability, license, deployment, and data-handling detail on the linked model pages.

## Source-backed identity and operating scope

The reader must preserve the following boundaries and their source basis.

Qwen Team develops the represented Qwen model series and tools at Alibaba Cloud. Its official GitHub organization and project repositories establish that publishing relationship, while Qwen Studio's first-party app listing identifies Alibaba Cloud as the publisher of the end-user assistant. Model families, the Qwen Code agent and the assistant workspace retain separate product identities. [Qwen GitHub organization](https://github.com/QwenLM) · [Qwen Code](https://github.com/QwenLM/qwen-code) · [Qwen Studio](https://play.google.com/store/apps/details?hl=en-US&id=ai.qwenlm.chat.android).

Choose an exact artifact and license before deployment. A repository's code license is not a license for every checkpoint: for example, the Qwen2.5-Coder-3B-Instruct card declares the Qwen Research license, and the Qwen3.8 repository directs users to the license accompanying the selected weights. [Coder model card](https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct) · [Qwen3.8 repository](https://github.com/QwenLM/Qwen3.8).

Hosted assistant use, Alibaba Cloud Model Studio API use and running downloaded weights have different data and access boundaries. Model Studio's retention policy applies to that platform and its eligible configurations; it should not be transferred to Qwen Studio merely because the products share the Qwen name. [Model Studio retention](https://www.alibabacloud.com/help/en/model-studio/data-retention-policy) · [Qwen Studio listing](https://play.google.com/store/apps/details?hl=en-US&id=ai.qwenlm.chat.android).

## Reader projection

- Render every non-hidden current-entity relation in its semantic group, ordered by explicit order, canonical target display name and target ID. Preserve source/contributor, organizational and product distinctions.
- Include the official resources from canonical references as readable links. Navigation to a related catalog entry must resolve to its reader, not to metadata.
- Keep changing version, plan, availability and policy details qualified by the cited source; no general offline, license or privacy guarantee follows from producer attribution.
