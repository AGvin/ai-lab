# Documentation Requirements

## Requirements

- Identify GSM-Symbolic as Apple's independently published **2024 symbolic-template-derived mathematical reasoning evaluation dataset**, based on original GSM8K questions but distinct from the original OpenAI GSM8K dataset and from model training artifacts, evaluation scripts or model score reports.
- Keep exactly one canonical dataset family identity. The default `main`, `p1` (one additional clause) and `p2` (two additional clauses) are three configurations/variants of GSM-Symbolic, not independently accepted dataset entities. Original source commit `b6a1625025fc857300203bac9f617e5d8ec99f65` has 100 symbolic, 100 p1 and 50 p2 template JSON files; the publisher describes sampling 50 generated instances per template. Do not silently present derived sample counts as an independently validated whole-file census.
- Record the original published field semantics: template `id`, generated `instance`, `question`, `answer` with final `####` numeric answer, `original_id`, `original_question`, `original_answer` mapped to GSM8K test data, plus an intentional data-contamination `canary`.
- Preserve the source and revision boundary: GitHub original data commit `b6a1625`, later main `3b645c25d200bf950fb84e8cdcbfeccd91d6a8af` differs from it only by removal of CODE_OF_CONDUCT.md and CONTRIBUTING.md in the scoped Git comparison; this does not establish independent model-score reproduction. The Hub has one test split for each `main`, `p1`, `p2` config.
- Distinguish source/data licenses exactly: GitHub root `LICENSE` is an Apple software-specific grant; `generated_data/README.md` and Apple's Hub card declare **CC BY-NC-ND 4.0** for the released data; the acknowledgements separately preserve OpenAI's GSM8K MIT attribution. Do not treat repository software rights as permission for commercial use or redistributing modified generated data. Further legal suitability requires review for the actual use and source/version.
- State benchmark-protocol sensitivity: Apple describes eight-shot prompting, generally greedy decoding and numeric answer extraction from the model's response; model/API decoding limitations and altered clauses affect comparability. An original paper finding is not an independently reproduced universal score or conclusive diagnosis of every model.
- Warn that released test questions and source GSM8K prompts can leak into training, tuning or prompt selection; isolate held-out evaluation and record config, sample/revision, prompt, extraction and scoring protocol. No model evaluation, answer-correctness audit or complete license/beneficial-ownership clearance was performed.
- Preserve the reciprocal `produced-by` Apple Inc. relation using the existing `catalog/producers/a/apple-inc` entity. No separate Apple research group producer, GSM8K/OpenAI producer duplication or extra independent dataset per config.

## Validation

- Exactly one new `catalog/datasets/gsm-symbolic` entity plus one inverse Apple `produces` relation, with GSM8K and Apple nodes remaining distinct.
- New dataset-parent/Apple reader links resolve to materialized canonical children, and new citations describe the original primary sources and license scopes.
- No independent benchmark run, global render/cache/schema/CI gate, exhaustive ownership audit or clean eight-root research pass is inferred from this bounded intake.
