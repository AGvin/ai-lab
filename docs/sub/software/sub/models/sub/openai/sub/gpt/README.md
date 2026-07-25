# GPT Model Family

OpenAI's GPT family contains general-purpose language and multimodal models used across reasoning, coding, tool use, analysis, and conversational workloads.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Scope

This node documents the GPT model family itself. ChatGPT is a hosted assistant product that can route requests across different model configurations; it is not the canonical name of the underlying model family.

Use child nodes for concrete GPT generations and released variants. Keep ChatGPT-specific availability, plan limits, model-picker labels, automatic routing, and product behavior under the assistant documentation rather than duplicating them here.

## Current family structure

The currently relevant general-purpose line is GPT-5.6. OpenAI documents three API tiers in this generation:

- **GPT-5.6 Sol** — the flagship tier for complex professional work;
- **GPT-5.6 Terra** — a balanced capability-and-cost tier;
- **GPT-5.6 Luna** — the cost-efficient tier for high-volume workloads.

Earlier GPT-5.x generations and specialized Codex variants remain distinct released models or historical lines and should receive their own canonical pages when they are referenced by comparisons, deployment notes, or migration guidance.

## Access and naming boundaries

- API model identifiers and aliases belong to concrete model pages because they can change independently of the family description.
- ChatGPT labels such as Instant, Medium, High, Extra High, and Pro describe product-level routing or reasoning configurations, not separate canonical GPT families.
- The `chat-latest` API alias tracks the latest Instant model used in ChatGPT and is not recommended as a stable production substitute for a named GPT model.
- Hosted access, pricing, safeguards, and feature support must be verified against the current official model catalog before adoption.

## Documentation order

1. Create the GPT-5.6 generation node.
2. Create concrete pages for Sol, Terra, and Luna.
3. Add earlier GPT-5.x or Codex-related pages only when required by current comparisons or practical guidance.
4. Link model-selection pages to these canonical pages instead of repeating model descriptions.

## Related pages

- [OpenAI models](../../)
- [Models](../../../..)
- [Assistants](../../../../../assistants/)
- [General repository disclaimer](../../../../../../disclaimer/)

## Sources

- [OpenAI model catalog](https://developers.openai.com/api/docs/models)
- [OpenAI all-model catalog](https://developers.openai.com/api/docs/models/all)
- [OpenAI GPT-5.6 model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [GPT-5.6 in ChatGPT](https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt/)
