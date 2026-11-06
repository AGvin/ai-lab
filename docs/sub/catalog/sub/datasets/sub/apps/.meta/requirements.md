# Documentation Requirements

## Requirements

- Identify APPS Coding Challenge Dataset as one concrete frozen-source **dataset**, not a model, implementation library, hosted inference service or measured benchmark result.
- Pin the first-party README at `hendrycks/apps@362aedc3c71cd7d9bd2fc96a6c80e11dbc38c7a5` (blob `087eaf8dfec02a6f83a7415e5a06b5a15ba3c4bd`) and the actual source-license record where present.
- The pinned README links the original APPS archive and separately mirrored Hugging Face dataset; the repo includes training and evaluation code but is not itself the complete downloaded archive.
- Benchmark outcomes are sensitive to task split, tests, runtime timeouts, language and generation parameters.
- Evaluation commonly runs generated programs; isolate untrusted code with strict filesystem, network, memory, CPU and time limits.
- The source MIT license does not automatically license every separately sourced competitive-programming problem or repack.
- Never execute model-generated programs without isolation. No dataset download, local execution, test corpus copyright review, benchmark score or full clean pass is claimed.

## Validation

- Exactly one newly materialized dataset identity, one parent index link and no invented publisher or duplicate source entity.
- This scoped source review is not complete rights, schema/render closure, repository-wide CI or a whole-catalog clean pass.
