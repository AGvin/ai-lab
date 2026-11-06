# Documentation Requirements

## Requirements

- Identify Apify as a hosted cloud platform for operating Actor-based scraping, browser automation, extraction and other data workflows, whose public API triggers serverless containerized actors and retrieves structured results for agents and applications.
- Distinguish Apify-operated Actor runtime/store/distribution infrastructure from individual community/publisher-owned Actor programs. A listed actor, scraper, integration or MCP connector does not imply that Apify authored or security-reviewed its extraction logic.
- Preserve cloud API/Actor runs, input/output schemas, schedules, dataset/key-value storage, public/private Actors, creator monetization and local Actor development as different surfaces of the same platform rather than multiple canonical hosted-service identities.
- Separate the Apify platform's web-data automation primary use from dedicated raw managed browser sessions (Browserbase, Browserless) and direct web-search indexes (Exa, Linkup, Parallel); actor programs may employ or integrate third-party providers.
- Pin actor ID, owner, version/build, configuration, permissions, destination-site access policies, rate limits, data exports, retention, plan/quota/cost and any externally supplied credentials for reproducibility and safe deployment.
- Treat the Apify maintainer as platform producer, without transferring ownership or accuracy claims for third-party marketplace Actors.

## Validation

- Official first-party product/documentation sources demonstrate a released hosted operator service.
- `produced-by` and producer `produces` links are an exact inverse pair.
- Material beta, deployment or third-party content attribution boundaries are preserved.

## Scoped original-source qualification — 2026-11-06

- Apify's first-party Actor documentation describes versioned containerized jobs run through cloud API, CLI or schedule, with input/output schemas, per-run datasets and key-value storage. Public/private Actors and published Actor Store listings are hosted execution/distribution surfaces of the platform; individual community Actor authors retain their own authorship and maintenance responsibilities.
- Actor Store publishers may select pay-per-event or pay-per-usage pricing, and storage/read operations can incur additional cost after runs. Dataset access, named/unnamed retention, export formats, tokens, actor permissions and resource link sharing require owner- and plan-specific validation, not general assumptions about every Actor.
- Target website terms, extraction rights, personal-data processing and robots/access restrictions still apply. Marketplace listing, platform integration or API/MCP access is not a security review of third-party scraping code or a license for arbitrary content republication.
- Verified first-party source 1: https://docs.apify.com/actors
- Verified first-party source 2: https://docs.apify.com/actors/running/actors-in-store
- Verified first-party source 3: https://docs.apify.com/storage/dataset
- Accept only original provider service identity and source-scoped API, maturity, content-rights and data boundaries. No new metadata/entity, reader repair, authenticated traffic execution, complete freshness/legal/security/privacy audit, whole-repository schema/cache/CI/render, clean pass, final-delivery or merge credit.
