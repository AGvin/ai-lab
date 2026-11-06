# BoolQ

**BoolQ** (Boolean Questions) is Google Research's **2019 natural yes/no question-answering dataset**. It tests whether a model can interpret a real information-seeking question in the context of an accompanying passage.

## Dataset format and release

The [original README](https://github.com/google-research-datasets/boolean-questions/blob/90af34107399cc7a446b373dc4ee35b8001da7c2/README.md) describes **15,942 examples**, each with a question, evidence passage and Boolean answer, with an optional page title. It provides versioned JSONL artifacts for training, development and testing; these are splits of one dataset rather than separate products.

Questions arise from unconstrained information requests, making the task different from templated yes/no classification. Prompt design, passage truncation and answer extraction influence comparability. The official upstream repository is archived, so a pinned source release should not be taken as evidence of ongoing maintenance.

## License and provenance

The source README explicitly declares **CC BY-SA 3.0** for BoolQ. No separate repository-root LICENSE was present at this pinned revision. Original passages or pages may be covered by additional third-party terms, so check text provenance for redistribution or commercial use.

No dataset download, full rights verification, score reproduction or whole-catalog clean pass was performed.

## Official source snapshot

- [Upstream publisher repository](https://github.com/google-research-datasets/boolean-questions)
- [Pinned first-party README](https://github.com/google-research-datasets/boolean-questions/blob/90af34107399cc7a446b373dc4ee35b8001da7c2/README.md)
