# Documentation Requirements

## Requirements

- Identify Bias Benchmark for QA (BBQ) as one concrete frozen-source **dataset**, not a model, implementation library, hosted inference service or measured benchmark result.
- Pin the first-party README at `nyu-mll/BBQ@bea11bd97d79217245b5871acd247b9d6eb24598` (blob `6ca1792e1f39e56770c1f0eed36cfd716f956a51`) and the actual source-license record where present.
- The pinned README describes bias assessment across nine social dimensions, with separate under-informative and adequately-informative contexts.
- Dataset files are JSONL by category; the README describes 11 JSONL category files. Counts are repository-version-specific.
- Ambiguous and disambiguated evaluations have different interpretations; bias and accuracy should be reported separately.
- The pinned root LICENSE is Creative Commons Attribution 4.0 International (CC BY 4.0), rather than MIT or unrestricted public domain.
- Handle protected-group stereotype content as sensitive evaluation material, not training instructions or endorsements. No fairness certification, complete demographic validity audit, test run or clean pass.

## Validation

- Exactly one newly materialized dataset identity, one parent index link and no invented publisher or duplicate source entity.
- This scoped source review is not complete rights, schema/render closure, repository-wide CI or a whole-catalog clean pass.
