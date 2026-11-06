# Documentation Requirements

## Requirements

- Identify DeepSearchQA as Google DeepMind's published **December 11, 2025**, 900-prompt dataset for evaluating web-enabled deep-research agents, across 17 topical fields. The January 28, 2026 arXiv submission is a later public paper date, not the benchmark's initial release date.
- The paper documents multi-step "causal chain" tasks that test systematic information collation, entity resolution/deduplication and knowing when to stop searching; this is not ordinary no-tool parametric factual recall.
- Preserve the official public CSV `DSQA-full.csv` / `eval` split and the four source fields `problem`, `problem_category`, `answer`, `answer_type`. The answer type is metadata **not supplied to the agent** during inference, with roughly 65% requiring set answers.
- Evaluate agents with external web search access. Differentiate DeepSearchQA from short-answer BrowseComp, closed-book SimpleQA/Verified, a hosted Gemini Deep Research service and an evaluation runner/leaderboard.
- The official dataset card mentions "parametric knowledge" inside one field description but the same source, upstream paper and first-party Google release explicitly characterize **web-enabled** multi-step retrieval. Follow the confirmed intended benchmark protocol, not that isolated inconsistent phrase.
- Maintain original paper's outcome-based precision, recall and F1 framing, distinguishing exact complete answer sets from excessive answers, premature stopping, lucky final answers and search-step efficiency. The official dataset card names `gemini-2.5-flash` as autorater with the Kaggle starter prompt; pin dataset, evaluator model/prompt, run tools and scoring policy.
- Cite the original December 2025 Google release, official Google DeepMind benchmark hub, official Google dataset Hub card, Google-hosted technical report, arXiv report and Kaggle benchmark. Published leaderboards are mutable and not model-performance certification.
- The Google dataset card declares Apache-2.0, but this is **not** an independent item-by-item rights assessment of all underlying cited web sources; preserve producer and research-team provenance rather than claiming exclusive authorship across Google DeepMind, Google Search, Kaggle and Google Research collaborators.
- Public source publication, static dated web ground truth, link churn and real-world changes can create contamination and stale answers. Outcome-only grading cannot establish efficient or causally sound agent research behavior; no independent model runtime or legal/sanctions/beneficial ownership audit is claimed.
- Reuse the accepted canonical `catalog/producers/g/google-deepmind` producer with one exact inverse `produced-by` / `produces` relationship, without creating a second Google publisher.

## Validation

- One canonical dataset `catalog/datasets/deepsearchqa`; no duplicate full 900-question dataset identity, hosted service or software entity credit.
- Ensure dataset index, existing Google DeepMind reader and both current-node metadata files resolve to canonical paths, with the reciprocal producer graph relation and link checked.
- Verify the six changed catalog paths with exact branch readbacks and commit diff; full eight-root clean research cycles, current-HEAD repository schema/cache/CI and final reader render remain unfinished.
