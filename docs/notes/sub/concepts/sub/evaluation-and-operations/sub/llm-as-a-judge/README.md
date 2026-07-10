# LLM as a Judge

Using a language model to score, rank, or critique other model outputs.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Using a language model to score, rank, or critique other model outputs. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- An LLM judge receives candidate output, criteria, and sometimes reference material, then assigns scores or preferences.
- Pairwise comparison can be more stable than absolute scoring.
- Calibration uses human-reviewed examples and checks for position, verbosity, and self-preference bias.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

LLM as a Judge affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Scale evaluation of open-ended text when exact matching is unsuitable.
- Rank several candidate responses for further review.

## Example

A judge model scores whether a summary is faithful to supplied source text, while a sample is audited by humans.

## Trade-offs and limitations

- The judge can make factual errors and inherit model biases.
- Using the same model family as generator and judge can reduce independence.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is LLM as a Judge expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Evaluation and Operations](../../)
- [Rate Limits](../rate-limits/)
- [Retrieval Evaluation](../retrieval-evaluation/)
