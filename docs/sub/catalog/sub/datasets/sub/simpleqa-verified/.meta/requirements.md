# Documentation Requirements

## Requirements

- Identify SimpleQA Verified as the Google DeepMind and Google Research team's separately curated and released September 2025 1,000-question benchmark derived from OpenAI's original 4,326-question SimpleQA; the publisher names are not interchangeable.
- The Google dataset card identifies exactly 1,000 items in the `simpleqa_verified` config's `eval` split, with `original_index`, `problem`, `answer`, `topic`, `answer_type`, `multi_step`, `requires_reasoning` and `urls` columns.
- Preserve original-index traceability, source URL reconciliation, de-duplication, topic/answer-type rebalancing, verification and difficulty selection; this is not a renaming of the full original data.
- The benchmark evaluates parametric **short-form factuality without external tools**. Browsing/retrieval-enabled scores are not comparable to the intended closed-book procedure.
- The publisher describes a revised GPT-4.1-based autorater prompt with direct-answer and numeric-grading adjustments. Compare only after pinning dataset revision, grading prompt/model, answer formatting, abstention treatment and sampling configuration.
- The MIT license is **declared on Google's Hugging Face dataset card**. Its declaration is not an independent item-level clearance of all previously collected or externally cited source URLs, rights in the original OpenAI data, or mirrored downstream distributions.
- Source URLs and reference answers can become stale or disagree; published original questions may have entered model training. Google's filtering improves the benchmark's intended quality but does not guarantee every example or score is correct or contamination-free.
- Attribute the jointly affiliated researchers to **Google DeepMind** as the existing canonical research producer (as in AndroidWorld), acknowledging Google Research collaboration without inventing a separately held legal entity or duplicating the parent Google producer.
- Record one `produced-by` / `produces` Google DeepMind reciprocal pair and one `derived-from` / `has-derivative` pair with OpenAI's original SimpleQA. These denote publisher and **dataset lineage**, not model training or model-score inheritance.
- Include Google DeepMind's official evaluation page, Google's Hub card, original paper, official Kaggle evaluation and original OpenAI SimpleQA announcement. Do not present leaderboards as fixed current results or infer model safety or legal compliance.

## Validation

- Exactly one canonical `catalog/datasets/simpleqa-verified` identity, distinct from `catalog/datasets/simpleqa`, mirrors, score tables and evaluator software.
- Source dataset, derivative dataset and existing Google DeepMind producer must have matching canonical inverse edges and resolving reader links.
- Verify all nine changed catalog paths at the approved branch and actual complete commit diff; full eight-root catalog saturation, full schema/cache/CI and final reader render remain separate unfinished gates.

## Scoped original-source qualification — 2026-11-08

- **SimpleQA Verified** is a **September 2025** independently curated **1,000-question** short-form factuality benchmark by researchers at **Google DeepMind and Google Research**. It is a derivative of OpenAI's October 2024 original **4,326-question SimpleQA** dataset, not an alias, an original OpenAI-authored replacement, the `simple-evals` software or an independent web-browsing test.
- The official `google/simpleqa-verified` Hub data card identifies a **tool-free parametric-knowledge** evaluation setting and declares **MIT** dataset metadata. The paper/data card report separate filtering, verification, topic balancing and a changed autorater/grading protocol. Reproducing comparable scores requires the exact dataset revision, scorer, model, prompting and abstention policy. Published author-source URLs and the inherited original questions have separate third-party rights/freshness boundaries.
- Verified first-party sources: https://huggingface.co/datasets/google/simpleqa-verified ; https://deepmind.google/research/evals/ ; https://arxiv.org/abs/2509.07968
- Bounded source credit covers the existing original derivative identity, publisher, source and evaluation boundaries only. No live model/autorater test, question-answer validation, item-level rights/legal/privacy/security clearance, root-wide schema/cache/CI/render, clean or final acceptance.
