# Documentation Requirements

## Requirements

- Identify the operated **Jina Reader API** as hosted URL-to-LLM-friendly-text retrieval (`r.jina.ai`) and search-to-text (`s.jina.ai`). Keep these web-data endpoints distinct from the separate `api.jina.ai` embeddings/reranking service already materialized as Jina Search Foundation API.
- Source-pin the public `jina-ai/reader` README and Apache-2.0 source license at `1574bfd380d249c86c82db4dace0d9c8fe17e2b1`, and consult the live Jina API reference for currently operated endpoints.
- Note that the open-source repository README explicitly distinguishes **self-hostable stateless/bucket-cache code** from the vendor's MongoDB-backed SaaS storage layer; source code distribution is **not** a license for hosted service infrastructure or third-party content.
- Reader can fetch and render web pages, PDFs and supported documents; Search returns web results converted to text. Search requires a Jina API key, while Reader may work at lower unauthenticated rate limits. Exact rate limits and file support must be checked per endpoint and plan.
- Document URL SSRF/unsafe-content handling, request payload/URL privacy, API key exposure, copyright/robots policies and usage costs. A fetched page being accessible does not imply permission to republish it.
- Do not claim successful live extraction, automated browsing, search quality, end-to-end agent test or whole-catalog clean pass.

## Validation

- Verify the provider-owned API/product boundary and current documentation sources.
- Maintain a single catalog identity with the correct category link; never equate hosted terms with unrelated SDK or model licenses.
- Do not credit unperformed runtime, whole-site or clean-pass checks.
