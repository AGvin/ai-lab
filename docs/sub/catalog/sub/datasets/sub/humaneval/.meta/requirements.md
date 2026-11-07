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

## Scoped original-source qualification — 2026-11-08

- **HumanEval** is OpenAI's released **2021 handwritten function-completion problem set**, originally presented with **Evaluating Large Language Models Trained on Code**. The official `openai/human-eval` repository is now explicitly labeled **deprecated and unmaintained**; it distributes an evaluation harness but does not imply future maintenance or provider support.
- The dataset of code-completion tasks is separate from the `human-eval` Python evaluator, model-generated completions, `pass@k` sampling estimator, code execution runtime and independently reported model scores. The upstream strongly warns that evaluated **model-generated code is untrusted** and must run in a robust sandbox, not on an ordinary host.
- Verified original sources: https://github.com/openai/human-eval and https://arxiv.org/abs/2107.03374
- Accepted only the existing original dataset identity, 2021 publication provenance, repository lifecycle and public evaluation/safety boundaries. No execution of generated code, model scoring, content rights/legal audit, operational exploit assessment, full-repository schema/cache/CI/render, clean or final credit.
