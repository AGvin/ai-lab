# BrowseSafe

BrowseSafe is Perplexity AI's released **browser-agent prompt-injection detector**, fine-tuned from **Qwen3-30B-A3B-Instruct-2507**. The first-party model card describes a causal mixture-of-experts classifier that analyzes **raw web-page HTML** and emits a **yes/no** injection decision.

## Security and identity boundaries

The checkpoint is published under **MIT** terms. A classifier decision supports a browser-agent security workflow but is not a guarantee against all prompt injections or a replacement for tool isolation and authorization checks. Benchmark F1, latency, attack coverage and deployment architecture are Perplexity-reported claims until independently reproduced.

**BrowseSafe++** is later benchmark/guard work; its described unreleased guard weights are **not** this trained model. Do not count the BrowseSafe dataset or an unreleased guard as a released BrowseSafe checkpoint.

## Producer and official sources

- [Perplexity AI model catalog](../../)
- [Perplexity BrowseSafe announcement](https://www.perplexity.ai/hub/blog/browsesafe)
- [Official BrowseSafe checkpoint](https://huggingface.co/perplexity-ai/browsesafe)
