# Documentation Requirements

## Requirements

- Identify GSM8K as OpenAI's concrete released 2021 English grade-school word-problem dataset, with 8.5K approximately described examples, original train/test JSONL files and human-authored solutions that usually require 2–8 reasoning/calculation steps.
- The original README rounds train/test counts to 7.5K/1K; separate official OpenAI Hub card currently reports 7,473 train and 1,319 test records for the main config. Scope these to the exact release/split and do not silently reconcile rounded counts into exact claims.
- Distinguish the main `question` and multi-step `answer` data from Socratic subquestion variants, calculator calculation markup, example model outputs, evaluation code, and leaderboard scores. These are not individually accepted source datasets.
- The solution format embeds calculator calculation annotations and a final answer after `####`; removing annotations or changing preprocessing requires explicit version/protocol documentation.
- Preserve original OpenAI research paper and official OpenAI Hub source. The original repository is marked archived/as-is: the historical released dataset remains useful but no active maintenance or up-to-date score ranking is promised.
- The publisher's Hub card declares MIT for its dataset; the exact original repository LICENSE uses MIT for software and associated documentation. Keep those source declarations separate and do not generalize data grants to third-party repacks or all derived samples.
- Distinguish this elementary arithmetic word-problem dataset from competition-level original MATH and its 500-problem selected evaluation subset; a score on either cannot be transferred to the other.
- Public evaluation exposure, prompt/answer extraction differences, calculator/tool policies and original older sample-calculator bugs limit score comparison. Publisher-reported model results are not independently reproduced AI Lab findings.
- Preserve OpenAI produced-by / produces reciprocal relations without creating an invented new producer. No exhaustive beneficial-ownership, indirect holding or sanctions evaluation was performed.

## Validation

- Exactly one canonical GSM8K source-dataset identity; Socratic dataset view, main split, calculator software and samples receive zero duplicate entities.
- Reciprocal OpenAI producer relation resolves; all new index and producer reader links point to canonical metadata and available readers.
- No inferred cross-dataset MATH or MATH-500 derivation: they are independent data collections with different source authors and intended math difficulty levels.
