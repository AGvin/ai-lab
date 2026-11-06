# Documentation Requirements

## Requirements

- Present Perplexity Search API as Perplexity AI's released hosted web-data API for real-time ranked web search results, filtering, multi-query search, and content extraction.
- Preserve the raw-results boundary: Search API returns structured retrieval results for application-side processing, while Perplexity Agent API owns LLM-generated web-grounded answers and multi-provider agent requests.
- Keep Search SDK, Perplexity CLI, agent-installable search skills, MCP surfaces, official language SDKs, crawlers, and playground interfaces as access/integration surfaces rather than separate web-data service identities.
- Treat index freshness/coverage, ranking, result limits, extracted-content behavior, filters, regional/language support, pricing, endpoint schemas, and quotas as freshness-sensitive.
- Do not treat search citations/results as guaranteed complete, current, or correct without application-level verification.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Search API remains web-data-first rather than a generic model gateway.
- Search SDK/CLI/skills are not duplicated as hosted service peers.
- Producer provenance resolves bidirectionally to Perplexity AI.

## Source-backed reader scope — 2026-10-20

- Identity and provenance: Perplexity Search API returns ranked web retrieval results and extracted content for application processing. It is separate from the generated-answer behavior of Agent API.
- Decision and deployment boundary: Choose domain, language, regional and result-budget controls for the task. Treat returned pages as external source material whose relevance and claims require checking. Review current API data terms and limits before submitting sensitive queries.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://docs.perplexity.ai/docs/search/quickstart>, <https://docs.perplexity.ai/docs/resources/privacy-security>.

## Scoped original-source qualification — 2026-11-06

- Perplexity Search API is the publisher-hosted raw ranked web result/retrieval product. Search returns structured source URLs and content snippets for application-side analysis, whereas Perplexity Agent API and Gateway API serve agent/model-generated answers and routing respectively; keep these as separate service identities where independently cataloged.
- Search filters, multi-query support, ranked-result count, language/region control, content retrieval, SDKs, CLI and MCP integration are API/tool surfaces rather than new Perplexity-owned hosted web-data products. Users must verify current index freshness, result completeness and source ownership, especially before handling regulated/personal data.
- Current provider privacy/security guidance, region/model processing, account billing, rate quotas and consent must be checked for exact endpoint; a source citation in results is not itself proof of accuracy or right to republish.
- Verified first-party source 1: https://docs.perplexity.ai/docs/search/quickstart
- Verified first-party source 2: https://docs.perplexity.ai/docs/resources/privacy-security
- Qualification is existing original-provider identity and bounded API/data/license/version claims, not live authenticated tests, full terms/privacy/legal review, independent benchmark, new entity/metadata, reader repair, global schema/cache/CI/render, clean pass, final-delivery gate or merge.
