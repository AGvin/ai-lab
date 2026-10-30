# Documentation Requirements

## Identity and provenance

- Identify exact pretrained **base** checkpoint `yandex/AliceAI-Foundation-80B-A3B-Base`, released September 21, 2026, separately trained from scratch. It is not the previous AliceAI-T5 encoder-decoder checkpoint, a consumer Alice AI assistant, or a released instruction-finetuned API. [Yandex announcement](https://www.yandex.com/company/news/2026-09-21) [Official card](https://huggingface.co/yandex/AliceAI-Foundation-80B-A3B-Base).
- Hybrid attention/MoE model with **80B total / 3B active** parameters per token and configured **262144-token** context. Preserve base model scope and distinguish activation from all stored weights and KV memory. These are source-reported configurations, not local benchmark or hardware measurements. [Official checkpoint](https://huggingface.co/yandex/AliceAI-Foundation-80B-A3B-Base).
- The model weights are distributed as Apache-2.0 under the publisher's card; do not infer that Apache-2.0 covers external runtimes, user data, nonincluded artifacts, or services. [Yandex release](https://www.yandex.com/company/news/2026-09-21).

## Decision and operational boundaries

- This is an experimental prerelease-to-further-training foundation **base** model, not a ready-made chat/instruction-tuned assistant; prompt/chat-template and tool-use suitability require evaluation or adaptation. [Publisher](https://www.yandex.com/company/news/2026-09-21).
- The published architecture uses model-specific custom code; pin exact checkpoint, inspect/trust remote loading code and dependencies before executing. Verify compatible Transformers/vLLM revisions, hardware memory, tokenizer, batching, quantization and reproducibility individually. [Model card](https://huggingface.co/yandex/AliceAI-Foundation-80B-A3B-Base).
- Source quality and Russian-knowledge/coding/reasoning benchmarks are publisher evaluations; do not present them as independently verified. The 262144-token configuration is not evidence that all prompts or systems sustain this context.
- No specific GPU-fit, request throughput, max service availability, external API price or hosted rights are established by this package.

## Validation

- Resolve exactly one member-of edge to AliceAI Foundation and one reciprocal has-member edge; validate distinct Yandex family/producer navigation.
- Preserve original open-weight base versus customized local inference and consumer service identities.
- No runtime test, complete source-freshness, global cache/schema/CI, clean saturation cycle or final gate credited.

## Mandatory Tier 1 Russian-origin policy

- **DANGEROUS — NOT RECOMMENDED | RUSSIAN ORIGIN/CONTROL** applies unconditionally to Yandex-published artifacts, regardless of a security audit, license or sanctions status. Publish the reader warning directly after the page title; exclude from all adoption shortlists, production recommendations and sensitive deployments. Retain technical records for research and threat monitoring only. [Canonical policy](../../../../../../../../../../../../project/sub/policies/sub/russia-linked-ai/README.md) [Yandex Moscow address](https://www.yandex.com/company/contacts/moscow).
- Do not share personal, confidential, private or operational data with Yandex-controlled hosted services. If research requires downloading weights or custom runtime code, pin and inspect exact sources and run only in controlled, restricted isolation. This caution is a categorical trust policy, not a finding of malicious code in this model.
