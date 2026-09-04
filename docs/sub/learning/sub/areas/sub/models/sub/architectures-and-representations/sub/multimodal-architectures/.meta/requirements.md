# Documentation Requirements

## Requirements

- Teach Multimodal Architectures as model structures that jointly encode, align, fuse, route, or generate across multiple modalities.
- Keep concrete multimodal tasks with `modalities-and-tasks/multimodal/` and practical assistant interaction with AI Use and Interaction rather than duplicating them here.
- Explain common architectural patterns such as separate modality encoders, projectors/adapters, shared token spaces, cross-attention, early/late fusion, and modality-specific decoders at a mechanism level without tying them to one product/model family.
- Distinguish model capability from provider/interface support: a multimodal architecture may support inputs or outputs that a concrete hosted interface does not expose.
- Keep visual preprocessing, resolution/token budgets, runtime compatibility, exact model architecture facts, and dated capability evidence with catalog/evidence owners when they are model/version specific.

## Validation

- Architecture-level fusion/alignment is not conflated with a particular VQA/captioning task.
- Provider UI support is not inferred from model architecture alone.
- Current navigation exposes only source-backed selected children.
