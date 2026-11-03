# Documentation Requirements

## Requirements

- Identify DigitalOcean Inference as the producer-operated hosted model catalog, model-routing and inference interface offering serverless and dedicated deployment options. Do not treat it as standalone self-managed OSS inference software, a new trained model, the entire Agent Platform, or the separately documented Evaluations service.
- Preserve source-backed serverless API base `https://inference.do-ai.run`, distinct from the `https://api.digitalocean.com` control-plane API. The documented serverless API supports OpenAI-compatible text inference and additional modality-specific endpoints with distinct capability support; never imply uniform model/endpoint capabilities.
- Describe serverless inference, dedicated hosted instances, Inference Router and the vendor's managed model catalog as product/workflow variants of the same canonical service candidate. Do not multiply identities or count upstream model publishers as DigitalOcean-authored models.
- Serverless access uses permitted DigitalOcean/model access credentials; secure keys, scope privilege and spending, and check actual account availability and feature support before use. Client examples are reference workflows only, not executed requests.
- Treat available model IDs, pricing, routing policy, APIs, context limits, quotas, region/data-residency coverage, logging, data-retention and upstream provider behavior as mutable vendor/customer-contract facts, not stable promises. Distinguish DigitalOcean-hosted and third-party routed models.
- Note risks around confidential data, third-party provider access, terms of service, training-data/model rights, paid usage, and potential model output errors. Require privacy, source provenance, contract and sanctioned-provider checks appropriate to the actual service context.
- Preserve exactly one `produced-by` / `produces` relation to the canonical DigitalOcean producer, with official up-to-date vendor references.

## Validation

- API base and vendor product boundaries are substantiated by [Inference](https://docs.digitalocean.com/products/inference/), [Supported Models](https://docs.digitalocean.com/products/inference/details/models/), [Serverless API](https://docs.digitalocean.com/products/inference/reference/api/serverless-inference/), and [Availability](https://docs.digitalocean.com/products/inference/details/availability/).
- The Model APIs index lists the one materialized DigitalOcean Inference service exactly once; producer inverse resolves to an existing canonical entity.
- No authenticated API execution, legal/security certification, performance benchmark, full model availability/freshness audit, full repository CI, or clean whole-catalog pass.
