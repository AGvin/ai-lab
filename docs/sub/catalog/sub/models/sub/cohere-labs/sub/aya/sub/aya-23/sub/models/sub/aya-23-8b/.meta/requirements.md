# Documentation Requirements

## Requirements

- Identify **Aya 23 8B** as the exact distinct model `CohereLabs/aya-23-8B` released in May 2024, not an Aya Expanse version, hosted inference route, quantization, alias or duplicate of the other Aya 23 parameter scale. [First-party model card](https://huggingface.co/CohereLabs/aya-23-8B) [Cohere release](https://cohere.com/blog/aya23).
- Preserve **8B** published parameter class, **8,192-token** context, text-to-text instruction generation and **23 supported languages**. Do not transfer later Aya Vision multimodal input or longer Expanse 32B context to this older model. [Official model card](https://huggingface.co/CohereLabs/aya-23-8B).
- Model weights are **gated**, distributed for non-commercial research under **CC-BY-NC-4.0** with an additional acceptable-use policy and license addendum. Public repo metadata and usage examples do not establish current hosted API service or commercial deployment permission. [Gated model card](https://huggingface.co/CohereLabs/aya-23-8B).
- The publisher describes a pretrained Command-family foundation and Aya data; without the exact checkpoint do not assert a `derived-from` edge or an independently replicated score. The 8B size implies lower deployment footprint relative to the 35B counterpart, but no runtime test, VRAM measurement or benchmark was performed.
- Confirm that the current official model card refers to this historical weight identity, rather than treating a newer Aya release as an identical successor. Do not infer producer nationality/control or Russian ownership from the model's Russian-language support.

## Validation

- One unique `member-of` / `has-member` reciprocal relationship with Aya 23; exact official reference URLs and sibling reader navigation.
- Full canonical entity, scoped requirements and complete English reader, with clear licensing, access, context, modality, lineage and provenance limitations.
- No full repository schema/cache/CI, freshness certification, independent inference, whole-catalog clean pass or final gate credit.
