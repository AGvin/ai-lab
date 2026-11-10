# Documentation Requirements

## Requirements

- Identify CommonsenseQA as one concrete frozen-source **dataset**, not a model, implementation library, hosted inference service or measured benchmark result.
- Pin the first-party README at `jonathanherzig/commonsenseqa@6f5690bd539b67a4f965d8572aae3ed9195fd4a1` (blob `9aa8885d1d7a60c74ce264e53a3c4b7250a6c25a`) and the actual source-license record where present.
- The upstream README points to an official dataset website for data downloads and an evaluation script; the repository itself includes ESIM/BERT baseline implementations.
- The author explains leaderboard scoring for the random split; changing splits, preprocessing or baseline scripts invalidates direct comparisons.
- The pinned GitHub repository does not contain a root LICENSE file; public access to its code or dataset download is not itself a grant of rights.
- Report selected test split, task format, prompt and model revision; do not train on held-out evaluation examples.
- Dataset and baseline code rights require confirmation from the original publisher; no blanket commercial license is inferred. No dataset download, model execution or clean pass.

## Validation

- Exactly one newly materialized dataset identity, one parent index link and no invented publisher or duplicate source entity.
- This scoped source review is not complete rights, schema/render closure, repository-wide CI or a whole-catalog clean pass.
