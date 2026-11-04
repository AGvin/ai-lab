# Inspect India Evals

**Inspect India Evals** (`inspect-india-evals`) packages India-specific language-model safety, bias, factual knowledge and cultural/DPI evaluations on top of the separate [Inspect AI](https://inspect.ai-safety-institute.org.uk/) framework.

## Evaluation scope

The [official README](https://github.com/MetaFazer/inspect-india-evals/blob/2f376c316d92d431414b7e490537105a6b018ac1/README.md) describes multilingual factual tasks, BharatBBQ bias categories, multilingual refusal and jailbreak checks, digital public infrastructure safety and cultural knowledge scored against specified rubrics. The proposed composite **India Fairness Index** summarizes configured dimensions, rather than proving universal fairness or safety for every Indian language or deployment domain.

The [pinned manifest](https://github.com/MetaFazer/inspect-india-evals/blob/2f376c316d92d431414b7e490537105a6b018ac1/pyproject.toml) describes an `inspect-ai`-based Python package (version 0.1.0, Python >=3.10) with task datasets and an optional visualizer. Running the suite requires model-provider credentials and, for relevant scorers, an **independent** configured judge model.

## Important validity warning

The authors explicitly warn that safety/jailbreak results in an earlier preprint used an unintended **self-judging** model configuration. Those pilot figures should be treated as invalid pending independent-judge reruns. Other caveats in the official README include English-only DPI evaluation, a cultural-knowledge dataset smaller than projected and mismatches between BharatBBQ dataset categories and the paper. Benchmark outcomes must be tied to exact data, language, model and judge revisions; merely publishing the source does not validate scores.

## License, data and operations

The README and [package metadata](https://github.com/MetaFazer/inspect-india-evals/blob/2f376c316d92d431414b7e490537105a6b018ac1/pyproject.toml) state **Apache-2.0**, but this pinned repository lacks a separate root LICENSE file; specific source, dataset and redistributed-output rights need their own checks. Guard culturally sensitive prompts, API keys and response logs and account for model-judge costs.

No evaluation, independent rerun, rights review, installation or whole-catalog clean pass was performed.

## Official source snapshot

- [Repository](https://github.com/MetaFazer/inspect-india-evals)
- [README.md](https://github.com/MetaFazer/inspect-india-evals/blob/2f376c316d92d431414b7e490537105a6b018ac1/README.md)
- [pyproject.toml](https://github.com/MetaFazer/inspect-india-evals/blob/2f376c316d92d431414b7e490537105a6b018ac1/pyproject.toml)
