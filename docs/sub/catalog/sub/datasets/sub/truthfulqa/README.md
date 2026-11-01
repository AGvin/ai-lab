# TruthfulQA

TruthfulQA is a research question-and-reference-answer dataset developed by Stephanie Lin, Jacob Hilton and Owain Evans to test whether language models repeat common human misconceptions. The [original paper](https://arxiv.org/abs/2109.07958) described a historical release of 817 questions across 38 categories. Those original counts are not a claim about the current revised CSV.

## Dataset and revisions

The [research authors' repository](https://github.com/sylinrl/TruthfulQA) publishes questions and reference answers as [TruthfulQA.csv](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv). Its January 2025 update revised or removed some questions, removed the time-sensitive *Indexical Error: Time* category and introduced a preferred binary multiple-choice protocol. The authors explicitly report that they have not completed revalidation of all remaining questions and source references. Pin a specific CSV commit for reproducibility.

The revised binary protocol uses a *Best Answer* and *Best Incorrect Answer*, randomized into the two displayed positions. Historical MC1/MC2, revised binary choice and free-form generation all use the source dataset but have different evaluation contracts; they are not independent datasets.

## Evaluation limits

Generation scores distinguish truthfulness from informativeness. The authors' fine-tuned GPT-3 judge models are not publicly available for arbitrary external use, and their intended validity does not extend to unrelated questions. Compare measurements only with matching CSV revision, prompt, answer order and scoring metric.

A long-public benchmark may have contaminated training data. Older questions, incomplete source revalidation and evolving factual answers limit current correctness claims. TruthfulQA performance is not proof of broad real-world truthfulness or safety. This profile does not report independent model execution or measured scores.

## License and provenance

The [original repository LICENSE](https://github.com/sylinrl/TruthfulQA/blob/main/LICENSE) is Apache-2.0, but its presence does not independently clear every cited third-party source or mirrored distribution. Authorship belongs to the named researchers; historical Oxford/OpenAI affiliations do not establish sole corporate ownership or a valid corporate produced-by edge. Complete beneficial-ownership, indirect-holdings and sanctions checks were not performed.

## Original resources

- [Research-author repository and January 2025 update](https://github.com/sylinrl/TruthfulQA)
- [Current mutable source CSV](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)
- [Original research paper](https://arxiv.org/abs/2109.07958)
- [Author-linked explanation of the new multiple-choice setting](https://www.alignmentforum.org/posts/Bunfwz6JsNd44kgLT/new-improved-multiple-choice-truthfulqa)
- [Original repository LICENSE](https://github.com/sylinrl/TruthfulQA/blob/main/LICENSE)
