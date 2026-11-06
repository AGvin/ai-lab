# PaperBench

**PaperBench** is OpenAI's original 2025 AI research-replication benchmark dataset. It evaluates agents tasked with implementing and reproducing **20 ICML 2024 Spotlight and Oral research papers** from scratch. The [original OpenAI release](https://openai.com/index/paperbench/) describes **8,316 individually gradable rubric criteria** across these papers. These criteria are grading sub-tasks—not 8,316 independently released datasets or completed replications.

## Dataset and evaluation boundary

The original [PaperBench source and dataset](https://github.com/openai/frontier-evals/tree/main/project/paperbench) live within the OpenAI Frontier Evals repository. Each paper's data includes a PDF/Markdown version, author-supplied addenda, related paper assets, an evaluation `rubric.json`, a `blacklist.txt` of forbidden original code/resources, `config.yaml` and sometimes additional judging guidance. The paper data are stored in **Git-LFS**, and the default install does not hydrate them. The catalog review did not download or hash all third-party paper files.

An agent attempts the research reproduction in a container; its submitted implementation is then executed in a separate GPU-capable container and assessed against paper-specific weighted rubrics with a configured LLM judge. Run time, model/scaffold, allowed tools and websites, GPU/data access, exact dataset and grader revision, and judge behavior materially affect score comparisons. Historic [publisher leaderboard entries](https://github.com/openai/frontier-evals/blob/main/project/paperbench/README.md) are not AI Lab reproduced performance results.

**Variants are not additional accepted datasets.** PaperBench Code-Dev skips the reproduction/execution stage and grades only coding requirements; auxiliary JudgeEval measures grader accuracy. The 10-paper subset used in later evaluation reports has a narrower scope. PaperBench also differs from OpenAI's separate [MLE-bench](../mle-bench/), which evaluates machine-learning engineering over Kaggle competitions rather than replication of scientific papers.

## Versioning, permissions and safe execution

The [original research announcement](https://openai.com/index/paperbench/) was published **2025-04-02**. The inspected source revision [`b78dab1`](https://github.com/openai/frontier-evals/commit/b78dab1da774a6456b1ed9c48c9ff194ee3ff36d) contains an installable Python package identifying itself as `1.0.0`; this is **not evidence of a separately tagged PaperBench dataset release** or byte-identical grading compared with the 2025 launch. Pin data, rubric, code, execution image, model and judge versions for reproduction.

The repository's [MIT `LICENSE.md`](https://github.com/openai/frontier-evals/blob/main/LICENSE.md) applies to repository software and associated documentation. It **does not independently establish redistribution rights** in third-party scientific papers, figures, datasets, linked artifacts or external services. Upstream explicitly states that some JudgeEval tarballs cannot be redistributed automatically. Consult the rights and terms of every paper/asset and downstream dependency before commercial or redistributed use.

**Untrusted code execution is a central risk.** PaperBench runs agent-written programs in isolated compute environments and can expose access to GPU, files, network services and external OpenAI/Hugging Face tokens. Use isolated disposable hosts, pinned dependencies, constrained Docker permissions/network/volumes, protected credentials and cost quotas; never run unreviewed benchmark submissions with production secrets or privileged host access. No benchmark runs, payload execution, full third-party rights review, independent score reproduction or complete ownership/security audit occurred in this documentation review.

## Provenance

- Produced by: [OpenAI](../../../producers/sub/o/sub/openai/).
- Original selected ICML papers and coauthored rubrics have their own authorship and third-party rights.

## Official resources

- [OpenAI PaperBench publication](https://openai.com/index/paperbench/)
- [Original PaperBench code and dataset](https://github.com/openai/frontier-evals/tree/main/project/paperbench)
- [Original PaperBench README and reproducibility requirements](https://github.com/openai/frontier-evals/blob/main/project/paperbench/README.md)
- [PaperBench research paper](https://arxiv.org/abs/2504.01848)
- [Original Frontier Evals MIT code license](https://github.com/openai/frontier-evals/blob/main/LICENSE.md)
