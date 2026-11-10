# Documentation Requirements

## Requirements

- Identify Q2D-Web (Query2Doc-Web) as Perplexity AI's released large-scale benchmark and public leaderboard for evaluating first-stage embedding retrieval in agentic RAG/web-search settings.
- Preserve the current benchmark boundary: the evaluation corpus contains roughly 190 million web documents and about 69.7 thousand agent-reformulated queries across ten languages, with multiple relevance-judgement sources.
- Preserve the access boundary explicitly: first-party material describes the benchmark itself as private while publishing a public leaderboard and evaluation methodology; do not imply that the full corpus/query set is publicly downloadable.
- Keep leaderboard entries, model rankings, submission mechanics, corpus snapshots, judgement sets, indexing/scoring pipeline, and reported metrics freshness-sensitive.
- Attribute comparative retrieval claims to Perplexity/current leaderboard evidence rather than converting them into independent AI Lab model rankings.
- Keep Q2D-Web distinct from the original Q2D benchmark and from Perplexity Search/API product identities.

## Validation

- Q2D-Web remains a benchmark/dataset identity even though its full evaluation data is not public.
- Public leaderboard availability is not described as public dataset availability.
- Producer provenance resolves bidirectionally to Perplexity AI.

## Source-backed reader scope — 2026-10-20

- Identity and provenance: Q2D-Web is Perplexity's private evaluation benchmark for first-stage retrieval in agentic RAG, with a public methodology and leaderboard. The reported corpus has about 190 million documents and 69,721 agent-reformulated queries across ten languages.
- Decision and deployment boundary: Public rankings do not provide a downloadable corpus or redistribution rights. Compare the exact corpus/subcorpus and relevance-judgment set; full-corpus and sampled Recall@1000 results have different evaluation conditions, and production-query distribution can favor in-distribution systems.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://www.perplexity.ai/uk/hub/blog/q2d-web>, <https://arxiv.org/abs/2609.08887>.

## Scoped original-source qualification — 2026-11-08

- **Q2D-Web (Query2Doc-Web)** is Perplexity's original **September 2026** research benchmark for first-stage embedding and retrieval evaluation within web-search and agentic RAG workloads, not the standalone Perplexity search service or its earlier Q2D benchmark.
- The private benchmark describes approximately **190 million deduplicated web documents**, **69,721 agent-reformulated production queries** across **ten languages**, sampled over nine months from publisher traffic with PII filtering, and multiple separate relevance-label pipelines (agent citations, production search rankings and additional LLM judgements). Corpus/query distribution, label sparsity, retrieval-index setup and subset/full-corpus ranking metrics must be pinned before comparing published scores.
- Public *methodology and a leaderboard* do not mean the query-document benchmark is available for unrestricted download or reuse. The original production-derived sampling and external web documents demand independent data-collection/privacy/copyright and security review; no actual embedding or retrieval run, judge-label reproduction, leaderboard trust assurance or cross-provider ranking is claimed.
- First-party sources: https://www.perplexity.ai/en-GB/hub/blog/q2d-web ; https://research.perplexity.ai/ ; https://arxiv.org/abs/2609.08887 .
- Source gate accepts only this already materialized private research benchmark identity, dated publisher methodology, 190M/69,721/10 task size and rights/access boundaries; no new metadata, production-query access, complete legal/security/freshness, global schema/cache/CI/render, clean or final gate.
