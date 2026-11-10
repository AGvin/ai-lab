# Language Model Evaluation Harness

EleutherAI's Language Model Evaluation Harness (`lm-eval`) is an open-source tool for running standardized language-model benchmark tasks across local and API-backed models.

## Evaluation role and boundaries

It provides task definitions, few-shot and prompt configuration, scoring/aggregation and model backends such as Hugging Face and vLLM. The harness is separate from datasets, leaderboards and independently developed multimodal evaluation frameworks.

## Reproducibility and operational safeguards

The canonical record cites release v0.4.13 (2026-08-31); CLI commands, plugin interfaces and supported tasks vary by version. Preserve harness commit, dataset revision/split, chat template, tokenizer, sampling, seed, model/quantization and backend before comparing scores. Consider evaluation contamination, API cost and data sharing.

## Relations

- Produced by: [EleutherAI](../../../../../../../producers/sub/e/sub/eleutherai/)

## Official resources

- [Source](https://github.com/EleutherAI/lm-evaluation-harness)
