# Documentation Requirements

## Requirements

- Identify WinoGrande as one concrete frozen-source **dataset**, not a model, implementation library, hosted inference service or measured benchmark result.
- Pin the first-party README at `allenai/winogrande@727e837f77521ef38bcc56df3b275c8da43f45af` (blob `0a0388a24eb9890e157d1525412123cfe76ce169`) and the actual source-license record where present.
- The pinned README identifies WinoGrande v1.1 and a download script with several training sizes (xs, s, m, l, xl) plus validation and test JSONL files.
- Official test labels are not included in the distributed test.jsonl; the original leaderboard handles test-set scoring.
- Results can vary across training-size regimes, seed, preprocessing and model/weight revision. Never infer test accuracy from a local unlabeled test copy.
- The source includes an Apache-2.0 LICENSE; distinguish code distribution from any separately required dataset/provenance terms.
- Avoid leaked test labels and represent hidden-test scores only with official measurement evidence. No files downloaded, model fine-tuned, evaluation executed or full clean pass.

## Validation

- Exactly one newly materialized dataset identity, one parent index link and no invented publisher or duplicate source entity.
- This scoped source review is not complete rights, schema/render closure, repository-wide CI or a whole-catalog clean pass.
