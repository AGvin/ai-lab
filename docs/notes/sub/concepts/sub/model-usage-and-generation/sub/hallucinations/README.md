# Hallucinations

Unsupported or incorrect model output presented in a plausible form.

## Core idea

Unsupported or incorrect model output presented in a plausible form. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- A hallucination occurs when generated content is unsupported, incorrect, or invented while remaining linguistically plausible.
- It can arise from missing knowledge, ambiguous context, weak retrieval, conflicting sources, sampling, or pressure to answer instead of abstaining.
- Detection requires evidence checks, tool verification, deterministic validation, or evaluation against known answers.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Hallucinations affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Design refusal and uncertainty behavior.
- Decide where citations, retrieval, calculators, code execution, or human review are required.

## Example

A model may invent an API method that follows a library naming pattern even though the method does not exist.

## Trade-offs and limitations

- Lower temperature does not eliminate hallucinations.
- A confident style or detailed explanation is not evidence of correctness.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Hallucinations expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Model Usage and Generation](../../)
- [Structured Output](../structured-output/)
- [Few-Shot Prompting](../few-shot-prompting/)
