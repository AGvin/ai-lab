# Documentation Requirements

## Requirements

- Provide model-domain navigation for model families produced by OpenAI.
- Keep canonical OpenAI producer identity and broader company/product description in the canonical producer page.
- Preserve the GPT and Whisper family identities while presenting all materialized OpenAI model children.
- Keep mutable hosted-access, pricing, safeguards, product-plan availability, and deployment terms outside this model-domain view.

## Content Specification

- Use `OpenAI models` as the page title.
- Link the canonical OpenAI producer page under `catalog/producers/`.
- Render all materialized direct model and model-family children from the canonical tree, including GPT and Whisper.
- State only the minimum access distinction useful for navigation: GPT is represented primarily through hosted named models in this catalog, while Whisper is a downloadable model family.
- Include the official OpenAI model catalog and Whisper repository as research references.

## Excluded Residual Content

The legacy provider-level page notes that exact availability, pricing, licensing, safeguards, supported features, and deployment requirements vary by model or artifact. Preserve those mutable or deployment-specific concerns in the relevant concrete model, service/product, deployment/workflow, or decision-support owner rather than duplicating them here.

## Validation

- The page does not duplicate the canonical OpenAI producer profile.
- Both GPT and Whisper family links resolve to canonical model nodes.
- Mutable service properties are not presented as stable producer-view facts.

## Source-scoped operating boundaries

- Hosted API availability, product routing, and downloadable releases have separate access and lifecycle conditions. Exact model pages identify those conditions; an API catalog entry alone does not establish access for every account [OpenAI open-weight FAQ](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss).
- Deprecation and shutdown are separate events. Historical identities remain useful when they explain a published migration deadline [API deprecations](https://developers.openai.com/api/docs/deprecations).

## Source evidence

- [OpenAI model catalog](https://developers.openai.com/api/docs/models).
- [Open-weight FAQ](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss).
- [API deprecations](https://developers.openai.com/api/docs/deprecations).
