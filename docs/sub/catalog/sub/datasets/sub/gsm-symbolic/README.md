# GSM-Symbolic

**GSM-Symbolic** is Apple's released 2024 mathematical-reasoning evaluation dataset built by transforming original [GSM8K](../gsm8k/) questions into reusable symbolic templates and sampled numerical or textual variations. The [original Apple research](https://machinelearning.apple.com/research/gsm-symbolic) tests whether a model's answers are stable across equivalent arithmetic problems and when extra clauses are introduced. It is **one independently identified dataset family**, not a replacement for GSM8K or a new trained model.

## Data, versions and benchmark use

The [official Apple dataset distribution](https://huggingface.co/datasets/apple/GSM-Symbolic) exposes one test split for each of three configurations: `main` (baseline symbolic variants), `p1` (one additional clause) and `p2` (two additional clauses). The [original source snapshot](https://github.com/apple-aiml-research/ml-gsm-symbolic/commit/b6a1625025fc857300203bac9f617e5d8ec99f65) contains 100 baseline, 100 P1 and 50 P2 template JSON files; Apple describes sampling 50 examples per template. These are **configurations of the same original release**, not three separately accepted catalog datasets.

Generated records contain a template `id`, instance number, generated `question` and worked `answer` ending in a `####` final value, references to the corresponding original GSM8K test question/answer and an anti-contamination `canary`. Apple publishes the templates and sample JSONL data; its [source README](https://github.com/apple-aiml-research/ml-gsm-symbolic) says the underlying parser/generator was not released with that snapshot. Do not assume template edits can be reproduced through a published generator.

The original [research paper](https://arxiv.org/abs/2410.05229) reports sensitivity to numerical substitutions and added clauses for the models and protocols it evaluated. Its setup generally uses eight-shot prompts, greedy or API-equivalent decoding, and extraction of a final numeric answer. Scores across different datasets, `main/p1/p2` configs, prompts, model revisions, answer extractors or external API sampling settings are not directly interchangeable. No evaluation or independent accuracy validation was performed for this catalog entry.

## Licensing and responsible use

**The generated dataset is marked [CC BY-NC-ND 4.0](https://github.com/apple-aiml-research/ml-gsm-symbolic/blob/main/generated_data/README.md)** by the source authors and the [Apple Hub card](https://huggingface.co/datasets/apple/GSM-Symbolic). The repository root separately contains an [Apple-specific software license](https://github.com/apple-aiml-research/ml-gsm-symbolic/blob/main/LICENSE), while [ACKNOWLEDGEMENTS](https://github.com/apple-aiml-research/ml-gsm-symbolic/blob/main/ACKNOWLEDGEMENTS) recognizes OpenAI's original GSM8K MIT-covered material. These grants **are not interchangeable**. Commercial reuse and distribution of adapted data require separate rights review; repository source-code reuse does not override the dataset restrictions.

As the questions and GSM8K source examples are public, avoid mixing test prompts into training or tuning data. Record the source revision, configuration, generation sample, prompting, decoding and answer extraction for any evaluation. No complete legal rights, beneficial-ownership or test-set contamination audit was performed.

## Provenance

- Produced by: [Apple Inc.](../../../producers/sub/a/sub/apple-inc/).
- Derived from the separate source [GSM8K](../gsm8k/) dataset originally published by OpenAI; GSM8K is **not** another Apple-produced dataset.

## Official resources

- [Apple GSM-Symbolic research](https://machinelearning.apple.com/research/gsm-symbolic)
- [Original Apple source, templates and generated data](https://github.com/apple-aiml-research/ml-gsm-symbolic)
- [Official Apple Hugging Face dataset](https://huggingface.co/datasets/apple/GSM-Symbolic)
- [Research paper](https://arxiv.org/abs/2410.05229)
- [Original software and generated-data licensing](https://github.com/apple-aiml-research/ml-gsm-symbolic/blob/main/LICENSE)
