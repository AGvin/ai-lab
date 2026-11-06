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

## Scoped original-source qualification — 2026-11-06

- DigitalOcean's current Inference docs operate one managed model catalog and inference surface with serverless APIs, dedicated GPU inference and Inference Router variants. The serverless endpoint uses https://inference.do-ai.run, separate from the DigitalOcean control-plane API; model access keys are distinct from agent endpoint keys.
- The official API endpoint list includes model listings, Chat Completions/Responses, embeddings and modality-specific media workflows, including asynchronous video generation. APIs, model coverage, regional deployment, output retention and hosted third-party authorship differ by endpoint; do not transfer general compatibility claims into guarantees for every model.
- Verified first-party source 1: https://docs.digitalocean.com/products/inference/
- Verified first-party source 2: https://docs.digitalocean.com/reference/api/reference/serverless-inference/
- Verified first-party source 3: https://docs.digitalocean.com/products/inference/how-to/manage-model-access-keys/
- Scope: only current provider-documented hosted service identity and endpoint/version boundaries. No new metadata or entity, reader-repair credit, independent run, complete freshness/legal/security clearance, root-wide schema/cache/CI/render, clean pass or final delivery.
