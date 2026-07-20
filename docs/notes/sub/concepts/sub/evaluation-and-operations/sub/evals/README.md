# Evals

Evals are repeatable tests that measure whether a model or AI system meets defined quality, safety, reliability, and operational requirements.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

An evaluation starts with a concrete task and success criteria. It supplies representative inputs, runs a fixed configuration, and scores outputs through deterministic checks, human review, model judges, or a combination. Evals should measure the complete system when prompts, retrieval, tools, and post-processing materially affect results.

## Practical use

- Compare candidate models for a workflow.
- Detect regressions after prompt or model changes.
- Measure tool-calling and structured-output reliability.
- Test hallucination, safety, and prompt-injection behavior.
- Establish release gates for production changes.

## Good evaluation design

Use realistic examples, include difficult and negative cases, preserve a held-out set, and record model and configuration versions. Report both aggregate metrics and important failure categories.

## Trade-offs and limitations

Evals approximate real use and can become stale. A model may overfit public benchmarks or a repeatedly used internal set. Automated scores can miss subtle factual, stylistic, or safety problems.

## Common mistakes

- Testing only easy happy-path prompts.
- Changing the dataset while comparing model versions.
- Using one average score without failure analysis.
- Evaluating the model but not retrieval and tool execution.

## Related concepts

- [Evaluation and Operations](../../)
- [Evaluation Datasets](../evaluation-datasets/)
- [Human Evaluation](../human-evaluation/)
- [Reproducibility](../reproducibility/)
