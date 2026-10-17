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
