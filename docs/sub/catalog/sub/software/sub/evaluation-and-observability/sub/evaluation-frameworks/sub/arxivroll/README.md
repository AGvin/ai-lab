# ArxivRoll

**ArxivRoll** is a rolling LLM evaluation and benchmark-construction pipeline for analyzing whether public benchmark exposure inflates evaluation results. The pinned [first-party README](https://github.com/liangzid/ArxivRoll/blob/709b0c5738b1710a4ac6988d70b32ffb1d21458b/README.md) describes crawling fresh arXiv papers, extracting content, constructing private tasks, evaluating models and publishing expired rounds after first use.

## Pipeline and identity

Task families are **Sequencing**, **Cloze** and next-fragment **Prediction** (SCP). Repository scripts cover crawling, task generation, evaluations and result aggregation. The project includes references to released ArxivRollBench rounds, but the pipeline software, the generated benchmark task sets and the separate [harness fork](https://github.com/liangzid/harness-4-arxivrollbench) are **different resources**.

The [pinned package manifest](https://github.com/liangzid/ArxivRoll/blob/709b0c5738b1710a4ac6988d70b32ffb1d21458b/pyproject.toml) sets Python >=3.13 and packages the project under the name `arxivbench`. Its README flags hardcoded 2025a file paths and explicitly describes manual round-specific updates; reproducibility requires preserving the paper window, source snapshots, exact datasets, evaluation harness revision and result mapping.

## Rights and operational limits

**No repository-root LICENSE file was found in the pinned snapshot.** The public code should therefore be treated as **source-visible, with reuse and redistribution rights unresolved**, not as MIT/Apache-licensed software. Individual arXiv papers may have different content licenses; do not publish protected article text or private test rounds without permission. Respect robots/usage policies and rate limits when crawling; publishing evaluation tasks can destroy their contamination-resistance utility.

No paper scraping, benchmark construction, model evaluation, legal review or whole-catalog clean pass was performed.

## Official source snapshot

- [First-party repository](https://github.com/liangzid/ArxivRoll)
- [README.md](https://github.com/liangzid/ArxivRoll/blob/709b0c5738b1710a4ac6988d70b32ffb1d21458b/README.md)
- [pyproject.toml](https://github.com/liangzid/ArxivRoll/blob/709b0c5738b1710a4ac6988d70b32ffb1d21458b/pyproject.toml)
