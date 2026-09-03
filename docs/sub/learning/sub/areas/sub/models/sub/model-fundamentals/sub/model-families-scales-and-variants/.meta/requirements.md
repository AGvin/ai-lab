# Documentation Requirements

## Requirements

- Teach model family, scale, and variant labels as descriptors that help organize related models but do not by themselves establish quality, runtime fit, context usability, deployment location, or safety.
- Explain `foundation model` as a broad-pretrained reusable role/classification and `LLM` as a relative language-model scale descriptor rather than a universal parameter threshold.
- Keep scale distinct from numerical representation and deployment: quantization can change storage/runtime representation without changing the underlying model scale label, and an LLM can be hosted or local.
- Select models using demonstrated task quality, representative evaluation, usable context, latency, cost, resource requirements, license/provenance, privacy constraints, deployment options, and provider dependence where relevant.
- Before adapting a model, compare prompting, retrieval, tools, structured outputs, or other application techniques when they can satisfy the same acceptance criteria with lower lifecycle cost.
- Treat broad pretraining as neither a guarantee of domain accuracy nor a mechanism for fresh attributable knowledge.
- Keep concrete model names, versions, parameter counts, licenses, runtime compatibility, prices, and benchmark evidence with catalog/evidence owners.

## Validation

- Parameter count or family labels are not treated as sufficient practical-fit evidence.
- Quantization and deployment location are not inferred from an `LLM` label.
- Selection guidance remains evidence- and workload-driven.
