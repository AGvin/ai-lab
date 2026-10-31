# Documentation Requirements

## Requirements

- Identify HumanEval as OpenAI's hand-written programming evaluation dataset introduced with the Codex evaluation work.
- Keep the dataset/problem-set identity distinct from the `human-eval` evaluation harness, pass@k metric/reporting procedure, model results, and generic code-evaluation concepts.
- Preserve the intended task boundary: generated function completions are checked for functional correctness against tests; do not generalize HumanEval results into broad software-engineering or repository-level agent capability.
- Treat dataset files, harness behavior, execution environment, pass@k settings, mirrors, preprocessing, and reported scores as version/protocol-sensitive facts requiring source-backed conditions when expanded.
- Preserve the upstream safety boundary when the harness is discussed: evaluating arbitrary model-generated code executes untrusted code and requires robust isolation/sandboxing rather than ordinary host execution.
- Preserve contamination/exposure caveats for a long-public test set and do not assume current models were never exposed to related benchmark material.
- Render the standard `entity-relations` block from validated current-entity relations and preserve OpenAI as the producer.
- Include the official repository and original paper as research references.

## Validation

- The page profiles the HumanEval dataset, not a current leaderboard or a generic coding benchmark category.
- HumanEval scores are not treated as evidence of repository-scale software-engineering performance without separate evidence.
- Harness execution risk is not hidden if practical evaluation guidance references executable model output.
- The `produces` / `produced-by` relation pair resolves consistently to OpenAI.
