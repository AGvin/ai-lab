# Documentation Requirements

## Requirements

- Identify AliceAI Foundation as a separately released, Yandex-produced **pretrained foundation-model family**, currently represented by the exact `AliceAI-Foundation-80B-A3B-Base` checkpoint. Do not fold it into the existing AliceAI-T5 encoder-decoder/MoE family, the Alice assistant, or search/API products. [Official announcement](https://www.yandex.com/company/news/2026-09-21).
- Distinguish experimental released base weights from a future unified reasoning/agent model: the 2026 release describes architectural evaluation, not a released instruction-following consumer assistant or guaranteed tool-use model. [Yandex release](https://www.yandex.com/company/news/2026-09-21) [Checkpoint card](https://huggingface.co/yandex/AliceAI-Foundation-80B-A3B-Base).
- Render the `produced-by` Yandex relation, the one direct `has-member` checkpoint relation and matching inverse edges without any invented training parent.

## Operational decision boundaries

- The checkpoint's Apache-2.0 license, 80B/3B mixture-of-experts parameter counts, 262,144-token configured context and custom model-code requirements must remain specific to that release. No generic family-wide runtime, license or benchmark inference. [Official model card](https://huggingface.co/yandex/AliceAI-Foundation-80B-A3B-Base).
- Producer comparisons and Russian factual benchmark results are not independently reproduced AI Lab measurements. Treat supported engines, revision pinning, total weights/storage, effective-context quality and resource requirements as integration-specific questions.

## Validation

- Preserve one canonical Yandex producer relation and one exact reciprocal checkpoint membership relation.
- Family reader and checkpoint are separately present, linked and not mistaken for AliceAI-T5.
- No independent inference execution, whole-catalog CI/cache or final research saturation credit.

## Mandatory Tier 1 Russian-origin policy

- **DANGEROUS — NOT RECOMMENDED | RUSSIAN ORIGIN/CONTROL** applies unconditionally to Yandex-published artifacts, regardless of a security audit, license or sanctions status. Publish the reader warning directly after the page title; exclude from all adoption shortlists, production recommendations and sensitive deployments. Retain technical records for research and threat monitoring only. [Canonical policy](../../../../../../../../project/sub/policies/sub/russia-linked-ai/README.md) [Yandex Moscow address](https://www.yandex.com/company/contacts/moscow).
- Do not share personal, confidential, private or operational data with Yandex-controlled hosted services. If research requires downloading weights or custom runtime code, pin and inspect exact sources and run only in controlled, restricted isolation. This caution is a categorical trust policy, not a finding of malicious code in this model.
