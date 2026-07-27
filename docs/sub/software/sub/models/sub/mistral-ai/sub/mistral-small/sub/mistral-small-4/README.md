# Mistral Small 4

Mistral Small 4 is Mistral AI's open-weight multimodal model for general instruction, reasoning, coding, agentic, document, and visual workloads.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Classification

- Model type: general-purpose multimodal instruction, reasoning, coding, and agentic model
- Scale class: [LLM](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/) in the current AI Lab comparison context
- Architecture: [Sparse — Mixture of Experts](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/mixture-of-experts/)
- Frontier status: not assessed for this exact model and workload scope
- Ecosystem status: emerging; exact runtime, quantization, and adoption maturity remain under review

The product name `Small` does not make this an SLM. Total model capacity, full weight residency, infrastructure requirements, and the current comparison context place it in the LLM group.

## Official profile

- Canonical identity: Mistral Small 4 119B A6B
- Hosted model ID: `mistral-small-2603`
- Official model repository: `mistralai/Mistral-Small-4-119B-2603`
- Access forms: Mistral API, AI Studio, and official open-weight distribution
- License: Apache-2.0
- Architecture: Mixture of Experts with 128 experts and four active per token
- Parameters: 119B total and 6.5B activated per token in the current official model card and model-selection documentation
- Context window: 256K tokens
- Modalities: text and image input; text output
- Reasoning: configurable reasoning effort
- Tooling: native function calling and JSON output

The launch article used different active-parameter accounting language: 6B active excluding embedding and output layers, and 8B when those layers are included. Record the source and definition when comparing active counts rather than treating the figures as contradictory model identities.

## Artifacts and deployment

The official base repository is approximately 242 GB at verification time and includes multiple weight layouts. Mistral also publishes an official NVFP4 checkpoint and an EAGLE speculative-decoding assistant.

Current Mistral model-selection documentation reports a GPU-memory range of approximately 60–238 GB depending on deployment precision and configuration. This is not a consumer single-GPU model by default. Validate the exact checkpoint, runtime, tensor parallelism, image path, context, concurrency, and accepted-result quality.

Open weights and a low active-parameter count do not imply low storage, low memory residency, unrestricted use, or simple operations.

## Selection guidance

Evaluate Mistral Small 4 for:

- self-hosted multimodal general assistance;
- reasoning and coding workloads that benefit from one unified model;
- image and document understanding;
- agentic workflows with function calling;
- organizations that require Apache-2.0 open weights and can support large-model infrastructure.

Reject or escalate when infrastructure, runtime maturity, latency, multimodal behavior, accepted-result quality, or operational responsibility does not justify the deployment.

## Evidence boundary

Identity, architecture, parameter figures, modalities, context, license, hosted model ID, and official artifacts were verified from current Mistral documentation and the official Hugging Face repository on 2026-07-27. Hosted pricing, aliases, infrastructure fit, throughput, and quality remain mutable or deployment-specific.

## Related pages

- [Mistral Small model family](../../)
- [Mistral AI models](../../../..)
- [Small and Large Language Models](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/)
- [Mixture of Experts](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/mixture-of-experts/)
- [Choosing Models for AI Agents](../../../../../../../../../../../notes/sub/comparisons/sub/model-selection/sub/agents/)

## Sources

- [Mistral Small 4 model documentation](https://docs.mistral.ai/models/model-cards/mistral-small-4-0-26-03)
- [Introducing Mistral Small 4](https://mistral.ai/news/mistral-small-4/)
- [Mistral Small 4 official Hugging Face repository](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)
- [Mistral Small 4 NVFP4 checkpoint](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603-NVFP4)
