# Hindsight Cloud

Hindsight Cloud is [Vectorize](../../../../../../../producers/sub/v/sub/vectorize-ai-inc/)'s operated, self-service agent-memory platform. It exposes persistent retain, recall and reflect memory over hosted APIs, SDK integrations and MCP without users managing the Hindsight storage or model infrastructure. This **managed multi-tenant service** is distinct from the [MIT-licensed self-hosted Hindsight software](../../../../../../../software/sub/data-infrastructure/sub/memory-and-context/sub/hindsight/).

## Managed service and billing

The [Cloud introduction](https://docs.hindsight.vectorize.io/cloud/) documents managed infrastructure, included model processing, organizational team administration, dashboard/usage analytics and API access. The [official integration guide](https://docs.hindsight.vectorize.io/cloud/api-integration/) identifies `https://api.hindsight.vectorize.io` as the API base and describes issuance and revocation of API keys.

[Official pricing](https://vectorize.io/pricing) uses pay-as-you-go metering, with token-based retain/recall/file-conversion usage, call-based reflect/model-refresh charges, and older stored-memory charges. Prices, included credits, backup frequency, support, regions and the advertised uptime guarantee are mutable and contract-dependent: verify them against the actual account and agreement. The vendor describes daily backups and 99.9% uptime for its standard Cloud offering, **not** an independently tested AI Lab service level or recovery outcome.

**Hindsight Enterprise** is described as a different dedicated/BYOC/on-premises deployment and contractual option. Do not assume its single-tenant isolation, SSO, private networking or higher support SLAs are included in standard Hindsight Cloud.

## Privacy, security and operational boundaries

Memory data can include personal, sensitive and confidential context across sessions. Before real workloads, verify bank-level and tenant-level authorization, model/data processor routing, retention and deletion, DPA and residency, credential and network controls, data-export and tested restore procedures. An opaque memory bank identifier does not by itself grant authorization. Treat retrieved memories as potentially stale or prompt-injected data rather than agent instructions.

Vendor security, benchmark, availability and SOC/certification statements require edition-specific independent documentation and appropriate contractual assurance; AI Lab did **not** audit provider infrastructure or run the hosted API.

## Relations

- Produced by: [Vectorize AI, Inc.](../../../../../../../producers/sub/v/sub/vectorize-ai-inc/)

## Official resources

- [Hindsight Cloud overview](https://docs.hindsight.vectorize.io/cloud/)
- [API endpoint and keys](https://docs.hindsight.vectorize.io/cloud/api-integration/)
- [Pricing](https://vectorize.io/pricing)
- [Billing and metering](https://docs.hindsight.vectorize.io/cloud/billing/)
- [Self-hosted vs Cloud vs Enterprise](https://hindsight.vectorize.io/cloud-enterprise/overview)
