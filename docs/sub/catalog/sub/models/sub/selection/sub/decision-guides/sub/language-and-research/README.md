# Language and Research Model Selection

Choose models for language, research, writing, translation, summarization, question answering, extraction, and classification tasks by the exact information and output contract.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Task scope

This area covers general assistance, reasoning and problem solving, research and synthesis, writing and editing, translation and localization, summarization, question answering, information extraction, and text classification.

A model that performs well on one language task is not automatically suitable for another. Evaluate the actual language, direction, domain, context length, source-grounding requirements, output format, terminology constraints, and failure cost.

## Decision criteria

Prefer the least expensive validated route that reaches the required acceptance tier. Compare:

- semantic correctness and unsupported additions;
- omission rate and instruction retention;
- source grounding and citation/evidence behavior when required;
- terminology, style, register, and structured-output fidelity;
- long-context behavior and context-selection quality;
- deterministic format checks and human correction effort;
- latency, retries, reviewer time, and cost per accepted result.

Use task-specific child pages when evaluation dimensions materially diverge. Translation/localization, research synthesis, extraction, classification, and creative writing should not share one undifferentiated ranking.

## Broad candidate evaluation set

These candidates preserve useful broad text/reasoning/research hypotheses from the legacy model and portfolio documentation after current first-party identity/capability revalidation. They are **starting points for bounded experiments, not a universal language-model ranking**.

| Candidate | Evaluate for | Evidence state | Main boundary |
| --- | --- | --- | --- |
| [Qwen3 8B](../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-8b/) | Economical local/private preprocessing, classification, summarization, and draft work where measured latency and quality are acceptable | Provider-documented multilingual reasoning/instruction model; legacy AI Lab candidate hypothesis | The represented quantized/local route requires exact artifact/runtime evaluation; compact size does not establish reviewer, orchestrator, or high-quality research reliability |
| [Qwen3 14B](../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-14b/) | Stronger local/private drafting, summarization, reasoning, and general assistance when a resident generalist is useful | Provider-documented multilingual reasoning/instruction model; legacy AI Lab candidate hypothesis | The legacy resident-model framing is deployment evidence, not an intrinsic recommendation; compare accepted-result gain against smaller and hosted routes |
| [GPT-5.6 Luna](../../../reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/luna/) | High-volume hosted text work, classification, extraction, drafting, and other bounded tasks where the lowest-cost GPT-5.6 tier is worth testing | Current provider positioning plus legacy AI Lab candidate hypothesis | Lowest token price does not imply lowest accepted-result cost; omissions, retries, verification, and escalation frequency must be measured |
| [GPT-5.6 Terra](../../../reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/terra/) | Hosted professional reasoning, synthesis, writing, and long-context language work where capability/cost balance matters | Current provider positioning plus legacy AI Lab candidate hypothesis | Mutable hosted surface and accepted-result economics require current validation; provider tiering is not independent quality evidence |
| [GPT-5.6 Sol](../../../reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/sol/) | Difficult reasoning, research, synthesis, or other capability-first professional language work | Current provider positioning for complex reasoning/research; legacy AI Lab candidate hypothesis | Stronger positioning does not remove source-grounding, verification, cost, or task-specific acceptance requirements |
| [Claude Sonnet 5](../../../reference/sub/producers/sub/anthropic/sub/claude/sub/sonnet/sub/models/sub/sonnet-5/) | Long-context reasoning, knowledge work, synthesis, writing/review, and instruction-heavy language workflows | Current provider-documented reasoning/knowledge-work strengths; legacy AI Lab candidate hypothesis | Provider benchmark claims and long context do not establish factual grounding, terminology fidelity, or best accepted-result cost |
| [DeepSeek V4 Flash](../../../reference/sub/producers/sub/deepseek/sub/deepseek/sub/deepseek-v4/sub/models/sub/deepseek-v4-flash/) | Economical long-context reasoning and text workflows where hosted cost efficiency is a material hypothesis | Current provider-documented long-context reasoning model; legacy AI Lab candidate hypothesis | Data/privacy boundary, instruction following, output quality, aliases/availability, and accepted-result economics require explicit evaluation |
| [Mistral Small 4](../../../reference/sub/producers/sub/mistral-ai/sub/mistral-small/sub/models/sub/mistral-small-4/) | Self-hosted general assistance and reasoning where open weights, long context, and one multimodal generalist are useful hypotheses | Current provider-documented general-instruction/reasoning model; legacy AI Lab candidate hypothesis | Large total-weight/infrastructure footprint and runtime maturity can dominate the decision; low active-parameter count is not a residency estimate |

Candidate membership does not imply a recommendation state. Pin the exact model/version/artifact or hosted ID, record the task corpus and evaluation date, and recheck mutable aliases, prices, limits, availability, tool surfaces, and data-path constraints before a material decision.

Translation-specific hypotheses belong in [Translation and Localization](./sub/translation-and-localization/) rather than being duplicated here.

Link intrinsic facts from [Model Reference](../../../reference/); keep task evidence and conclusions in selection.
