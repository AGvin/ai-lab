# Small and Large Language Models

Small Language Models (SLMs) and Large Language Models (LLMs) are relative language-model scale classes. They describe model scale and operational footprint, not a universal parameter-count threshold or deployment mode.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core distinction

An SLM is relatively compact within the relevant model generation or comparison context. It is commonly selected when latency, memory use, cost, offline operation, device deployment, or high request volume matters.

An LLM is relatively large within that context. It commonly provides greater capacity and broader capability, but usually requires more memory, computation, serving infrastructure, or provider cost.

There is no universal parameter boundary that permanently separates SLMs from LLMs. Model generations, architectures, modalities, and deployment techniques change what counts as small or large in practice.

## Typical operational patterns

| Dimension | SLM tendency | LLM tendency |
| --- | --- | --- |
| Relative scale | Smaller within the relevant comparison set | Larger within the relevant comparison set |
| Resource demand | Lower memory and compute requirements | Higher memory and compute requirements |
| Deployment fit | Edge devices, laptops, workstations, constrained services, high-volume routes | Powerful workstations, multi-GPU systems, data centers, or provider-hosted services |
| Latency and throughput | Often easier to optimize for low latency or high volume | Often trades more resources for capability |
| Task fit | Bounded, repetitive, specialized, privacy-sensitive, or cost-sensitive work | Complex, broad, ambiguous, or high-capability work |

These are tendencies, not definitions. An SLM can be provider-hosted, and an LLM can run locally when hardware, quantization, and runtime support make that practical.

## Independent dimensions

Scale must be recorded separately from other model properties:

- **Deployment:** local, self-hosted, and provider-hosted describe where inference runs.
- **Representation:** quantization reduces numerical precision and deployment cost but does not convert the underlying LLM into an SLM.
- **Architecture:** dense and Mixture of Experts describe parameter activation, not scale class.
- **Capability position:** an SLM or LLM may or may not be a frontier model.
- **Ecosystem maturity:** either class may be experimental, emerging, mainstream, or legacy.
- **Modality:** text-only and multimodal models may exist in either relative scale class.

## Selection guidance

Prefer the smallest model that consistently satisfies the required acceptance criteria in the real environment.

A practical workflow is:

1. define the task, quality threshold, failure cost, privacy boundary, latency target, and budget;
2. test an appropriate SLM against representative inputs;
3. retain it when measured quality is sufficient;
4. escalate difficult or uncertain cases to a stronger LLM when that improves accepted-result quality enough to justify the added cost;
5. validate the complete route rather than assuming parameter count predicts success.

Common portfolio patterns include one generalist LLM, one specialized SLM, or a cascade in which an SLM handles routine work and an LLM handles exceptions.

## Classification guidance

When a comparison uses `SLM` or `LLM`:

- classify the exact model version or artifact, not only the provider;
- explain the comparison context when the label could be ambiguous;
- use `Unclear` rather than inventing a precise threshold;
- record parameter counts separately when they are known and useful;
- for MoE models, record total and active parameters separately;
- do not infer local feasibility from the scale label alone.

## Common mistakes

- Defining one permanent parameter threshold for every model generation and modality.
- Calling every locally runnable model an SLM.
- Calling a quantized LLM an SLM because its file fits on one device.
- Assuming every LLM requires a cluster or provider API.
- Selecting a larger model without measuring whether it improves accepted results.
- Comparing an MoE model's total parameters directly with a dense model's active parameters.

## Related concepts

- [Model Classification](../../)
- [Model Architectures](../../../model-architectures/)
- [Dense and Sparse Architectures](../../../model-architectures/sub/dense-and-sparse-architectures/)
- [Mixture of Experts](../../../model-architectures/sub/mixture-of-experts/)
- [Quantization](../../../inference-and-serving/sub/quantization/)
- [Model Selection](../../../evaluation-and-operations/sub/model-selection/)
