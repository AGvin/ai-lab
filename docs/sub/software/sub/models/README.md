# Models

Canonical documentation for AI model providers, families, generations, specialized lines, versions, and concrete model artifacts.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Documentation hierarchy

Organize canonical model documentation from broad ownership to the exact model being evaluated:

1. **Provider** — the organization that develops or publishes the models, such as OpenAI, Anthropic, Google, Alibaba, DeepSeek, Mistral AI, Black Forest Labs, or pyannoteAI.
2. **Family** — the provider's main model family or ecosystem, such as GPT, Claude, Gemini, Qwen, DeepSeek, Mistral, FLUX, or Whisper.
3. **Generation or specialized line** — a numbered generation or a distinct workload-oriented branch, such as Qwen3, GPT-5.6, Qwen3-Coder, or speaker diarization.
4. **Version or named model** — a concrete released model or named variant, such as Qwen3 14B, GPT-5.6 Sol, Claude Sonnet 5, FLUX.1-schnell, or Community-1.
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

The current inventory covers the exact hosted and local candidates used by the model-selection and environment-profile guides, including GPT-5.6 tiers, Claude Sonnet 5, Gemini 3.6 Flash, DeepSeek V4 Flash, Qwen3 and Qwen3-Coder variants, Mistral Small 4, Whisper, FLUX.1-schnell, and pyannote Community-1.

## Child nodes

- [`openai/`](./sub/openai/) — GPT and Whisper model families and versions.
- [`anthropic/`](./sub/anthropic/) — Anthropic Claude models.
- [`google/`](./sub/google/) — Google Gemini models.
- [`deepseek/`](./sub/deepseek/) — DeepSeek model families and versions.
- [`alibaba/`](./sub/alibaba/) — Alibaba and Qwen Team model families and versions.
- [`mistral-ai/`](./sub/mistral-ai/) — Mistral AI models.
- [`black-forest-labs/`](./sub/black-forest-labs/) — FLUX image-generation models.
- [`pyannote/`](./sub/pyannote/) — speech-processing and speaker-diarization models.
- [`image-generation/`](./sub/image-generation/) — capability-oriented navigation for image-generation models.
- [`multimodal/`](./sub/multimodal/) — capability-oriented navigation for multimodal models.

## Scope

Use this node for canonical provider, family, generation, version, and model-artifact documentation. Do not place inference tools, model platforms, assistants, task-oriented recommendations, or cross-model comparisons here unless the page is specifically about the model itself.
