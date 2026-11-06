# Bias in Open-ended Language Generation (BOLD)

**BOLD** (Bias in Open-ended Language Generation Dataset) is an English-language set of prompts for studying representational and topical biases in model-generated text.

## Scope and interpretation

The [official source README](https://github.com/amazon-science/bold/blob/3ad652c773f5d1e30d5f6f61657ed934d768ecad/README.md) reports **23,679 text-generation prompts** across five categories: profession, gender, race, religious ideologies and political ideologies. Many prompts were drawn from Wikipedia. Subgroup and category compositions, decoding, model revisions and metric selection materially affect published bias measures.

These prompts are a **dataset**, not an independently verified statement about any demographic group or a universal fairness test. Models can respond to identity-linked prompts with harmful stereotypes or offensive language; evaluation requires appropriate safeguards, context, and careful reporting.

## Data licensing and limits

The publisher README states **CC BY-SA 4.0**, but this checkout has no separate root LICENSE file. Publication of the repository does not certify ownership or full reuse rights for every Wikipedia-derived passage or unrelated third-party asset. Follow attribution/share-alike requirements where applicable, and review exact original content permissions.

No model generations, bias metrics, copyright audit or whole-catalog clean pass were run.

## Official source snapshot

- [Upstream publisher repository](https://github.com/amazon-science/bold)
- [Pinned first-party README](https://github.com/amazon-science/bold/blob/3ad652c773f5d1e30d5f6f61657ed934d768ecad/README.md)
