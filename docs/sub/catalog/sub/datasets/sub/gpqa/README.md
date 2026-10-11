# GPQA

GPQA, the Graduate-Level Google-Proof Q&A benchmark, is a dataset of difficult expert-authored science questions.

## Dataset boundary

GPQA remains distinct from upstream baseline code, retrieval setups, model-specific prompts, and generic question-answering evaluation concepts. Named subsets or variants are separate evaluation conditions when upstream sources define them; results from different subsets must not be treated as if they used an identical test set.

Published contamination controls such as the canary are useful evidence but do not prove that a model's training data is uncontaminated. Dataset revisions, prompt formats, evaluation setup, and benchmark results are freshness-sensitive.

## Official resources

- [GPQA repository](https://github.com/idavidrein/gpqa)
- [GPQA on Hugging Face](https://huggingface.co/datasets/idavidrein/gpqa)
- [GPQA paper](https://arxiv.org/abs/2311.12022)
