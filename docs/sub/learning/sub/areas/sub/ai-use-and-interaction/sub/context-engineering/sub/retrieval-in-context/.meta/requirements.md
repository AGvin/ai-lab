# Documentation Requirements

## Requirements

- Teach Retrieval in Context as selecting and inserting external evidence into the current model-visible working set for a specific request or task.
- Retrieve only evidence that is relevant to the current question and acceptance criteria rather than appending every available document or chunk.
- Keep full retrieval, indexing, ranking, vector-search, RAG, and knowledge architecture with Data and Knowledge; this topic owns only how retrieved material is used as context from the practitioner perspective.
- Preserve source/provenance cues when retrieved evidence may need verification, citation, or conflict resolution.
- Size retrieved material against the concrete model/service context and tokenizer/accounting rules when capacity matters; do not assume unrelated tokenizers produce the same sequence length.
- Test retrieval-in-context behavior with representative documents and workloads, including cases where relevant evidence competes with instructions, conversation history, tool results, or generation capacity.

## Validation

- Retrieval in Context does not duplicate the full retrieval/RAG system architecture.
- More retrieved material is not presented as automatically better evidence.
- Provider/tokenizer-specific limits remain external mutable facts rather than universal learning truth.
