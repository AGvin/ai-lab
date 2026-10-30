# GLM-5.3

**GLM-5.3** is a separately published, post-trained Z.AI text Mixture-of-Experts model. Z.AI states that it reuses the **GLM-5.2 base model** and that its improvements come from post-training; it is not the same trained release as GLM-5.2 or the separately pretrained, multimodal GLM-5.3-Flash.

## Checkpoint and source scope

- **Architecture:** text-oriented sparse MoE model with DeepSeek-style sparse attention, intended by its producer for complex coding and long-horizon agentic tasks.
- **Parameters:** the official GLM-5 project describes **744B total / 40B active** (744B-A40B), while the exact Hugging Face repository reports **approximately 753B total** in registry metadata. These source-specific accounting figures must not be silently substituted for one another.
- **Weights:** Z.AI publishes the GLM-5.3 checkpoint as FP8 and a separately named BF16 weight artifact. Precision formats are distribution or serving variants, not independent trained identities.
- **License:** the GLM-5.3 model card uses a **model-specific GLM-5.3 license**, not GLM-5.3-Flash's MIT license. Review the exact upstream terms before use or redistribution.
- **Context and runtime:** the producer documents long-context support, but supported context, memory, batch behavior, precision and tool configuration must be verified with the pinned weights and serving framework.

## Evaluation and access boundaries

Coding, cybersecurity and agent benchmark improvements in producer materials are **Z.AI claims**, not independently reproduced AI Lab results. In particular, cybersecurity capabilities should not be treated as verified vulnerability-discovery performance or authorization for unreviewed security use.

Z.AI's API plans, pricing, quotas, hosted aliases, provider data handling and throughput are separate, mutable service concerns. Published checkpoint metadata does not establish local GPU fit or an operational service-level guarantee.

## Translations

- English

## Relations

- Member of: [GLM family](../../../../)

## Official resources

- [GLM-5.3 published checkpoint](https://huggingface.co/zai-org/GLM-5.3)
- [Z.AI GLM-5 project and checkpoint table](https://github.com/zai-org/GLM-5)
- [Z.AI model documentation](https://docs.z.ai/guides/overview/overview)
