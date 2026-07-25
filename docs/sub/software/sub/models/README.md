# Models

Canonical documentation for AI model providers, families, generations, specialized lines, versions, and concrete model artifacts.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Documentation hierarchy

Organize canonical model documentation from broad ownership to the exact model being evaluated:

1. **Provider** — the organization that develops or publishes the models, such as OpenAI, Anthropic, Google, Alibaba, DeepSeek, Mistral AI, or Meta.
2. **Family** — the provider's main model family or ecosystem, such as GPT, Claude, Gemini, Qwen, DeepSeek, Mistral, or Llama.
3. **Generation or specialized line** — a numbered generation or a distinct workload-oriented branch, such as Qwen3, Qwen2.5, Qwen Coder, QwQ, or QVQ.
4. **Version or named model** — a concrete released model generation or named variant, such as Qwen3-Coder, Qwen3-Coder-Next, GPT-5.6 Sol, or Claude Sonnet 5.
5. **Artifact or deployment variant** — an exact downloadable artifact, quantization, hosted API snapshot, or deployment-specific variant when that distinction materially affects evaluation or operation.

Each level owns only the information shared by its descendants. Comparison and recommendation pages should link to these canonical pages instead of duplicating model descriptions.

## Page responsibilities

- The provider page describes the provider, available model families, access methods, licensing patterns, and provider-wide constraints.
- The family page describes the family taxonomy and links to its generations and specialized lines.
- The generation or specialized-line page records characteristics shared by that branch and links to concrete versions.
- The concrete model page records capabilities, modalities, architecture where documented, context limits, deployment options, licensing, hardware requirements, limitations, evidence, and evaluation date.
- Quantization and deployment-specific details normally remain on the concrete model page unless a distinct artifact requires its own canonical page.

## Maintenance workflow

Maintain the canonical model inventory before comparison and recommendation pages depend on it:

1. audit every model referenced by task guides, portfolio profiles, benchmarks, and recommendations;
2. add or update the required provider, family, generation, specialized-line, concrete-model, and artifact nodes;
3. record exact hosted API identities and downloadable artifacts separately when their behavior or operating constraints differ;
4. preserve aliases, dated snapshots, replacements, and deprecations without creating duplicate canonical identities;
5. keep quantizations and deployment variants attached to the correct base model unless a distinct artifact needs its own page;
6. update affected comparisons, evidence dates, and limitations whenever the canonical model identity or operating facts change.

The current inventory includes OpenAI GPT models, Anthropic Claude models, Google Gemini models, DeepSeek models, Alibaba Qwen families and versions, and Mistral models referenced by the selection guides.

For Qwen, preserve the family taxonomy rather than documenting only isolated coding models. The canonical Qwen branch should cover the general Qwen generations and specialized lines such as Qwen Coder, QwQ, and QVQ, including the concrete Qwen3-Coder and Qwen3-Coder-Next pages required by the current comparisons.

## Child nodes

- [`openai/`](./sub/openai/) — OpenAI model families and versions.
- [`anthropic/`](./sub/anthropic/) — Anthropic model families and versions.
- [`google/`](./sub/google/) — Google model families and versions.
- [`deepseek/`](./sub/deepseek/) — DeepSeek model families and versions.
- [`alibaba/`](./sub/alibaba/) — Alibaba and Qwen Team model families and versions.
- [`mistral-ai/`](./sub/mistral-ai/) — Mistral AI model families and versions.
- [`image-generation/`](./sub/image-generation/) — image generation models.
- [`multimodal/`](./sub/multimodal/) — multimodal models.

## Scope

Use this node for canonical provider, family, generation, version, and model-artifact documentation. Do not place inference tools, model platforms, assistants, task-oriented recommendations, or cross-model comparisons here unless the page is specifically about the model itself.
