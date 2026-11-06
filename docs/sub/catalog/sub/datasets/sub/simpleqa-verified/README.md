# SimpleQA Verified

**SimpleQA Verified** is a **1,000-question** benchmark released by researchers from **Google DeepMind and Google Research** in September 2025 to evaluate a language model's *parametric* (closed-book) short-form factual knowledge. It was curated from OpenAI's **4,326-question** [original SimpleQA](../simpleqa/) and has its own dataset revision, filtering and grading protocol. [Google DeepMind's evaluation catalog](https://deepmind.google/research/evals/); [original paper](https://arxiv.org/abs/2509.07968).

## Dataset identity and evaluation

The authors filtered original questions to remove redundant sources, similar questions and conflicting references, balance topics and answer formats, and retain a difficult 1,000-question selection. Google's official dataset card publishes an `eval` split with `original_index` linking each selection back to OpenAI's original corpus, plus question, answer, topic, answer type, reasoning flags and supporting URLs.

Use this dataset **without browsing or retrieval tools** when assessing memory-based factual knowledge. The authors describe a revised **GPT-4.1** autorater prompt intended to encourage direct answers and improve numeric grading. Pin the dataset commit, grader and rubric, model snapshot, prompt, abstention policy and sampling settings before interpreting results; published scores or rankings are not directly interchangeable with original SimpleQA results.

## Limitations, licensing and provenance

Some answers or source URLs may become stale or conflict; the data is public and may be contaminated in training. A curated question set and automated grading do not certify correctness of every gold answer, long-form factuality, tool use, operational reliability or general model safety. No independent model execution or dataset item-level verification was performed for this profile.

The official Google Hugging Face card declares **MIT** licensing for its distributed dataset. That alone does not constitute an independent clearance of every original question or third-party source behind its reference URLs. The paper credits researchers from both Google DeepMind and Google Research; the catalog uses the existing Google DeepMind research producer rather than creating a second corporate identity for a collaborating team.

## Relations

- Produced by: [Google DeepMind](../../../producers/sub/g/sub/google-deepmind/)
- Derived from: [OpenAI's original SimpleQA](../simpleqa/)

## Official resources

- [Google DeepMind evaluation catalog](https://deepmind.google/research/evals/)
- [Google-published SimpleQA Verified dataset and license card](https://huggingface.co/datasets/google/simpleqa-verified)
- [Original research paper](https://arxiv.org/abs/2509.07968)
- [Official Kaggle evaluation and leaderboard](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified)
- [Source SimpleQA publication](https://openai.com/index/introducing-simpleqa/)
