# Documentation Requirements

## Requirements

- Identify AbstentionBench as a published abstention-evaluation benchmark family with benchmark questions and evaluation scripts, distinct from its separate upstream component datasets, human judges and model API providers.
- Pinned first-party README describes 20 component datasets (including three new underspecified reasoning challenges), six abstention scenarios and human-validated judges. Record whether a reported score covers all scenarios or a selected subset.
- Preserve abstention-vs-answer correctness and judge settings separately; scoring a refusal as correct or incorrect depends on the original task, available evidence and annotator criteria. Never infer that every refusal is desirable or that any model is universally safe.
- The pinned root LICENSE is Creative Commons Attribution-NonCommercial 4.0. Commercial uses are not automatically allowed. README explicitly warns that incorporated third-party content may have its own licenses and legal obligations.
- Document withheld/out-of-date facts, ambiguous question semantics, model version, judge version, prompt, inference costs and data leakage as reproducibility and privacy limitations.
- No model run, human annotation audit, score validation, comprehensive individual dataset-license clearance or whole-catalog clean pass was performed.

## Validation

- Exactly one canonical dataset identity, pinned publisher sources, and a resolvable dataset index link.
- Distinguish repository and benchmark data rights; do not award runtime, complete source audit or whole-catalog clean-pass credit.
