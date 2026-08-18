# Model Classification

Model classification describes independent dimensions of a model, such as scope, relative scale, capability position, and ecosystem maturity.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Classification dimensions

| Dimension | Examples | What it describes |
| --- | --- | --- |
| Model scope or modality | Foundation model, language model, multimodal model | The broad kind of inputs, outputs, and downstream uses the model supports. |
| [Language-model scale](./sub/language-model-scale/) | SLM, LLM | Relative model scale and operational footprint. |
| [Capability-frontier position](./sub/frontier-models/) | Frontier, non-frontier | Whether current evidence places the model near the leading capability boundary at a stated time. |
| Ecosystem maturity | Experimental, emerging, mainstream, legacy | Adoption, tooling support, documentation maturity, and operational familiarity. |
| [Parameter activation architecture](../model-architectures/) | Dense, sparse, MoE | How model computation and parameter activation are organized. |
| Deployment mode | Local, self-hosted, provider-hosted | Where and by whom inference is operated. |
| Access and licensing | Free, paid, open-weight, open-source, proprietary | How the model or service can be accessed, modified, and redistributed. |

These dimensions are related but not interchangeable. A model can simultaneously be an LLM, dense, provider-hosted, proprietary, mainstream, and non-frontier. Another model can be an LLM, MoE, open-weight, self-hosted, emerging, and frontier.

## Current pages

- [`language-model-scale/`](./sub/language-model-scale/) — Small Language Models and Large Language Models as relative scale classes.
- [`frontier-models/`](./sub/frontier-models/) — time-sensitive capability-frontier status.

## Related existing concepts

The broader documentation structure is being migrated incrementally. These existing pages remain under the earlier mixed foundations node until their placement is reviewed:

- [Foundation Models](../foundations-and-architecture/sub/foundation-models/)
- [Large Language Models](../foundations-and-architecture/sub/large-language-models/)
- [Multimodal Models](../foundations-and-architecture/sub/multimodal-models/)
- [Model Architectures](../model-architectures/)

## Usage rules

- Do not use SLM and LLM as synonyms for local and hosted deployment.
- Do not classify a quantized LLM as an SLM merely because the artifact is smaller.
- Keep dense, sparse, and MoE architecture separate from scale and hardware fit.
- Treat frontier status and ecosystem maturity as mutable, evidence-backed labels.
- Treat mainstream as adoption and ecosystem maturity, not as a synonym for best, largest, safest, or frontier.
