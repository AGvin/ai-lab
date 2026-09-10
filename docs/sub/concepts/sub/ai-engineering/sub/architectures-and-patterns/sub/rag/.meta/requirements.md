# Documentation Requirements

## Requirements

- Use the reader-facing title `Retrieval-Augmented Generation (RAG)`.
- Define RAG as a system architecture/pattern that combines retrieval of external or explicitly stored information with a generative model so retrieved information can condition generation.
- Make clear that RAG is not a model scale/classification, a vector database, an embedding method, or retrieval alone; it is the composition of retrieval/augmentation with generation.
- Explain that modern RAG can use lexical, semantic, vector, hybrid, structured/database, search, or other retrieval mechanisms. Embeddings, vector indexes, fixed chunks, and rerankers are common components but are not universal requirements of the pattern.
- Explain that retrieval may happen before generation, repeatedly/iteratively, or at finer-grained generation stages depending on the architecture; do not define RAG only as one retrieve-once-then-prompt pipeline.
- Distinguish query-time retrieval from model-weight adaptation. RAG can supply or update external knowledge without encoding every knowledge change into generator parameters, but RAG systems may still fine-tune or jointly train retrievers, generators, adapters, or other components. `Does not change model weights` is therefore not part of the universal RAG definition.
- Distinguish RAG from direct long-context prompting, fine-tuning, tool/API use, and external search used only for human browsing. These mechanisms can coexist with RAG but have different roles and update semantics.
- Explain that retrieval quality, source quality/freshness, provenance, context construction, ranking/reranking, generator behavior, and evaluation all affect the result; a strong generator cannot recover evidence that was never made available reliably.
- Make clear that RAG does not by itself guarantee factuality, faithfulness, grounding, citation correctness, prompt-injection resistance, authorization, confidentiality, or freshness. Those properties require evidence and controls at the relevant retrieval, context, generation, security, and evaluation layers.
- Explain that source attribution is enabled only when provenance survives ingestion/retrieval/context construction and the application maps generated claims or answers back to evidence; citation-shaped output alone is not provenance.
- Keep concrete vector stores/search engines, indexing/chunking recipes, top-k values, prompt templates, code examples, model/provider configurations, benchmark results, access-control implementations, and application-specific RAG recommendations with their applicable catalog, learning, evidence, engineering, or decision owners.
- Keep the canonical `rag/graph-rag/` concept as a distinct RAG specialization. Graph-based retrieval/organization can contribute to RAG when relationships or higher-order structure add value, but it does not redefine the generic RAG contract or make graph construction a universal requirement.
- Use the canonical entity references as research inputs for foundational and modern RAG boundaries when reader-facing rendering is activated.

## Validation

- The page defines RAG as retrieval-conditioned generation/system composition rather than as retrieval, embeddings, or a vector database alone.
- Embeddings, vector search, chunking, reranking, and one-shot retrieve-then-prompt flow are not presented as universal RAG requirements.
- RAG is not defined by an absence of training or weight updates; query-time external knowledge augmentation is distinguished from optional component training.
- RAG is not presented as an automatic factuality, grounding, citation, security, or authorization guarantee.
- Retrieval failures and generation failures remain separately diagnosable/evaluable.
- `graph-rag/` is recognized as a canonical specialization without being treated as a universal RAG stage or requirement.
- Legacy product lists, implementation code, and workflow recipes are not duplicated into this canonical architecture concept.
