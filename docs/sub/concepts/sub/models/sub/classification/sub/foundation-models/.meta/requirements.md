# Documentation Requirements

## Requirements

- Use the reader-facing title `Foundation Models`.
- Define a foundation model through its reusable role: a model trained on broad data at substantial scope and intended or able to serve as a basis that can be adapted to a wide range of downstream tasks.
- Explain that large-scale self-supervised pretraining is a characteristic and historically central foundation-model training pattern, while avoiding turning one training objective or modality into a timeless universal definition.
- Distinguish foundation-model status from language-model scale. A foundation model need not be a language model or an LLM, and a language model's scale label alone does not establish that it functions as a foundation model.
- Distinguish foundation-model status from multimodal status, architecture, deployment mode, access/licensing, frontier status, and concrete model capability; these dimensions can intersect but are not synonyms.
- Explain adaptation as downstream reuse or specialization of the pretrained model. Fine-tuning, parameter-efficient adaptation, or prompting can be examples when appropriate, but do not classify retrieval, tool execution, orchestration, or an agent workflow itself as model adaptation merely because a system uses the foundation model.
- Make clear that a foundation model is a model component rather than a complete AI application or system; downstream systems may add retrieval, tools, permissions, deterministic logic, validation, state, and human controls.
- Explain that broad pretraining and reuse do not guarantee domain accuracy, freshness, attribution, robustness, safety, fairness, legal suitability, or task acceptance; downstream evaluation remains separate.
- Keep concrete model facts, adaptation procedures, system-integration recipes, current benchmark results, licensing analysis, and model-selection recommendations with their applicable catalog, learning, evidence, or decision owners.
- Use the canonical entity references as research inputs for definition and terminology when reader-facing rendering is activated.

## Validation

- The page does not equate `foundation model` with `LLM`, `frontier model`, or `multimodal model`.
- Self-supervision is described with appropriate scope rather than asserted as the only possible future training mechanism by definition.
- Retrieval, tool calling, RAG, and agent orchestration are not mislabeled as intrinsic model-adaptation methods.
- The page does not imply that broad reuse makes a foundation model a complete application or guarantees downstream quality or safety.
- Legacy model-selection and workflow advice is not duplicated into this canonical classification concept.
