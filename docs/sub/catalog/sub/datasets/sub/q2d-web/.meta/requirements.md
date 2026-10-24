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
