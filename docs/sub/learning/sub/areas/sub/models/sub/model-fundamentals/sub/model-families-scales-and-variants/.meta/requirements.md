# Documentation Requirements

## Requirements

- Teach model family, scale, and variant labels as descriptors that help organize related models but do not by themselves establish quality, runtime fit, context usability, deployment location, or safety.
- Explain `foundation model` as a broad-pretrained reusable role/classification and `LLM` as a relative language-model scale descriptor rather than a universal parameter threshold.
- Keep classification axes independent where they answer different questions: modality/scope, model scale, dated capability-frontier position, ecosystem maturity, parameter-activation architecture, deployment mode, and access/licensing can all describe the same model simultaneously.
- Keep scale distinct from numerical representation and deployment: quantization can change storage/runtime representation without changing the underlying model scale label, and an LLM can be hosted or local.
- Do not infer quality, safety, size, frontier status, hardware fit, or deployment mode from ecosystem labels such as `mainstream`; treat named-model frontier/maturity labels as mutable evidence rather than timeless truth.
- Select models using demonstrated task quality, representative evaluation, usable context, latency, cost, resource requirements, license/provenance, privacy constraints, deployment options, and provider dependence where relevant.
- Before adapting a model, compare prompting, retrieval, tools, structured outputs, or other application techniques when they can satisfy the same acceptance criteria with lower lifecycle cost.
- Treat broad pretraining as neither a guarantee of domain accuracy nor a mechanism for fresh attributable knowledge.
- Keep concrete model names, versions, parameter counts, licenses, runtime compatibility, prices, frontier/maturity status, and benchmark evidence with catalog/evidence owners.

## Validation

- Parameter count or family labels are not treated as sufficient practical-fit evidence.
- Quantization, architecture, deployment location, access/licensing, scale, frontier status, and ecosystem maturity remain distinct axes.
- Selection guidance remains evidence- and workload-driven.
