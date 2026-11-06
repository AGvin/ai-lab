# DeepSearchQA

**DeepSearchQA** is a **900-prompt benchmark** released by Google DeepMind on **December 11, 2025** for evaluating web-enabled research agents across **17 fields**. The original tasks require multi-step web searches to retrieve *complete, objectively verifiable answer sets*, rather than only one hard-to-find fact. It is a released dataset, distinct from Google's hosted [Gemini Deep Research agent](https://blog.google/innovation-and-ai/technology/developers-tools/deep-research-agent-gemini-api/), Kaggle grading software and [BrowseComp](../browsecomp/).

## What the dataset measures

Many prompts form a **causal chain**: finding one item reveals constraints needed to find the next. The benchmark probes systematic collation of fragmented facts across sources, resolving duplicates and knowing when a search is complete. Approximately **65%** of prompts expect answer sets rather than single answers.

The [Google-published public dataset](https://huggingface.co/datasets/google/deepsearchqa) supplies **900 rows** in an `eval` CSV, with the original problem, one of 17 categories, the reference answer and an answer-type annotation. Do **not** provide the answer-type metadata to the agent as a hint when reproducing the intended task. Give evaluated agents access to the web, unlike closed-book SimpleQA Verified.

## Evaluation and limits

An outcome-based evaluation rewards both **precision** (avoiding invented or excess answers) and **recall** (finding every matching item); a final answer can be partially correct or over-inclusive. Google's published dataset card specifies a **Gemini 2.5 Flash** autorater and Kaggle grading prompt. Preserve the pinned CSV, grader, prompt, model, search tool/budget and scoring policy when comparing results. The benchmark does not reveal whether a correct list was found efficiently or by luck, and existing public tasks may contaminate model training.

Although many questions reference dated sources to reduce factual drift, web pages can move or change. The official Hub dataset card declares **Apache-2.0** for this distribution; that alone does not independently grant rights to all external cited source material. The original report credits collaborators from Google DeepMind, Google Search, Google Research and Kaggle. No independent agent evaluations, rights audit or complete legal/ownership check were performed.

## Provenance

- Produced by: [Google DeepMind](../../../producers/sub/g/sub/google-deepmind/)

## Original resources

- [Google's December 2025 release announcement](https://blog.google/innovation-and-ai/technology/developers-tools/deep-research-agent-gemini-api/)
- [Google DeepMind benchmark listing](https://deepmind.google/research/evals/)
- [Original Google dataset card and Apache-2.0 declaration](https://huggingface.co/datasets/google/deepsearchqa)
- [Original December 2025 technical report](https://storage.googleapis.com/deepmind-media/DeepSearchQA/DeepSearchQA_benchmark_paper.pdf)
- [January 2026 arXiv paper](https://arxiv.org/abs/2601.20975)
- [Official Kaggle benchmark](https://www.kaggle.com/benchmarks/google/dsqa/leaderboard)
