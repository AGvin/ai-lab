# Documentation Requirements

## Requirements

- Present this scenario for organization-wide employee question answering/search over internal policies, products, support material, procedures, or document collections where permissions, freshness, citations, and shared operation materially affect the model route.
- Preserve an approved managed business assistant with connected documents as the lowest-operations route when connector permissions, data terms, freshness, and vendor dependence are acceptable.
- Preserve a managed RAG route using a capable hosted generation model such as Gemini 3.6 Flash or GPT-5.6 Terra plus separately evaluated embedding, retrieval, and reranking stages; do not imply that the generator alone determines retrieval quality.
- Preserve a self-hosted text RAG route with a model such as Qwen3 14B when privacy/control justifies the operational burden; bind fit to exact model/runtime/context/concurrency and separately evaluate embeddings, retrieval, reranking, and infrastructure.
- Preserve Gemma 4 E4B Instruct as a bounded multimodal candidate for private image, form, UI, or short-audio inputs before retrieval/answer generation when the exact runtime and perception quality are adequate.
- Require source citations/provenance, document-level permissions, freshness/version checks, access-control enforcement, and human escalation when answers are uncertain, high consequence, or permission-sensitive.
- State explicitly that retrieval does not make an incorrect answer safe and that multimodal reasoning does not replace deterministic parsing, schema validation, or permission controls where those are required.
- Evaluate permission leakage, retrieval misses, stale sources, conflicting documents, citation correctness, grounded-answer quality, latency/concurrency, review/escalation rate, and accepted-result cost rather than chat fluency alone.
- Keep canonical knowledge-workspace services, retrieval software, vector stores, data platforms, and complete RAG architecture in their own catalog/solution owners; link them only where they constrain the model route.
- Escalate from a managed route when volume, permissions, privacy, data boundary, integration, audit, or quality requirements justify greater control or a multi-model pipeline.

## Validation

- The scenario is organization-scale internal knowledge access rather than a personal knowledge base or generic research task.
- Citations, source permissions, freshness, and escalation are required controls rather than optional polish.
- RAG is not presented as a guarantee of correctness or permission safety.
- Embedding/retrieval/reranking/perception components are evaluated separately where they materially affect the route.
