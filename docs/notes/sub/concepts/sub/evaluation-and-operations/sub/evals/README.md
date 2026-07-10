# Evals

Repeatable tests that measure whether an AI model or system meets defined requirements.

## Core idea

Repeatable tests that measure whether an AI model or system meets defined requirements. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Evals define inputs, expected properties, scoring methods, and pass criteria for an AI system.
- They can test model output, retrieval, tool use, safety, latency, or complete workflows.
- A useful eval suite is versioned and rerun whenever models, prompts, data, or tools change.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Evals affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Detect regressions and compare configurations before deployment.
- Turn subjective expectations into repeatable evidence.

## Example

A coding-agent eval checks branch use, file scope, test execution, and whether the final patch satisfies the issue.

## Trade-offs and limitations

- An eval only measures what its cases and scoring capture.
- Overfitting to a fixed suite can improve scores without improving real users.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Evals expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Evaluation and Operations](../../)
- [Reproducibility](../reproducibility/)
- [Model Selection](../model-selection/)
