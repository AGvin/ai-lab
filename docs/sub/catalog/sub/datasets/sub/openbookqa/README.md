# OpenBookQA

OpenBookQA is the [Ai2](../../../producers/sub/a/sub/ai2/)-published **2018 science question-answering dataset** by Todor Mihaylov, Peter Clark, Tushar Khot and Ashish Sabharwal. It tests whether a model can use a small book of elementary science facts **plus outside common knowledge** to choose an answer, rather than merely retrieve a sentence from a document.

## Data and evaluation boundary

The [official Ai2 dataset card](https://huggingface.co/datasets/allenai/openbookqa) lists **5,957 four-choice questions**, with 4,957 training, 500 validation and 500 test questions. Its `main` and `additional` configurations contain the same question set: `additional` supplies extra fact and annotation fields, rather than new evaluation questions.

The [final original 2018 research paper](https://aclanthology.org/D18-1260/) describes a core open book of **1,326** elementary science facts. The earlier arXiv abstract uses a slightly different 1,329 figure; the edition and source should be pinned instead of merging those values. A separate 5,167 crowdsourced common-knowledge fact collection is auxiliary resource material, not extra OpenBookQA questions.

OpenBookQA's fact-application task differs from the existing [Ai2 Reasoning Challenge (ARC)](../ai2-reasoning-challenge/), and neither represents ARC-AGI. Published numbers depend on the exact original release, supplemental `main` versus `additional` fields, model access to the relevant science fact (including oracle setups), question order and evaluator. No model score was independently reproduced.

## License and reuse boundary

The publisher's [Hugging Face card](https://huggingface.co/datasets/allenai/openbookqa) currently reports the **dataset license as unknown**. Its [original Ai2 baseline code repository](https://github.com/allenai/OpenBookQA) has an [Apache-2.0 LICENSE](https://github.com/allenai/OpenBookQA/blob/main/LICENSE) for its software, which is **not** independently verified as an unrestricted rights grant for all question and supporting fact text. Obtain appropriate data/source licensing confirmation before copying, redistribution or production training use.

Open publication creates contamination concerns, and evaluation performance does not establish broad reasoning, factual reliability or safety. No data were redistributed and no complete third-party rights, beneficial ownership or sanctions audit was performed.

## Provenance

- Produced by: [Ai2](../../../producers/sub/a/sub/ai2/).

## Primary resources

- [Original published Ai2 dataset and split metadata](https://huggingface.co/datasets/allenai/openbookqa)
- [Original final EMNLP paper](https://aclanthology.org/D18-1260/)
- [Ai2 reference model code and data-preparation documentation](https://github.com/allenai/OpenBookQA)
- [Original source-code LICENSE](https://github.com/allenai/OpenBookQA/blob/main/LICENSE)
- [TensorFlow Datasets profile](https://www.tensorflow.org/datasets/catalog/openbookqa)
