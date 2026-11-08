# Documentation Requirements

## Requirements

- Document **Hyperbolic Flux Inference** as the active hosted/serverless inference API within Hyperbolic's platform. The October 21, 2026 launch represents the next generation of the older Hyperbolic inference service, not a second simultaneously accepted legacy API identity.
- Separate **Flux** remote inference from the proprietary **Forge** GPU orchestration platform, rental/private cloud and Managed Kubernetes services, self-managed model inference engines, and third-party trained-model weights. Do not automatically materialize related feature, deployment, endpoint or model identities.
- Attribute the first-party OpenAI-compatible Chat Completions and streaming interface to the exact published base `https://api.hyperbolic.ai/inference/v1`; note the old API endpoint and key format are not the current integration target. The launch blog requires current `sk_live_` keys for Flux, and the vendor recommends testing compatibility, streaming and each supported model ID.
- Confirm that the published account path requires Pro or Organization access and prepaid credits; requests may be declined when balance is exhausted. Token prices, model IDs, support matrices, quotas, feature/preview lifecycle, routing and regions are mutable vendor data, not universal service guarantees.
- Distinguish Hyperbolic-hosted inference from externally routed models: the company's launch description explicitly says requests may be routed to external model-serving providers under Hyperbolic authentication/billing. The claim of mTLS GPU ingress applies to Hyperbolic-hosted capacity, not all third-party routes. Never claim universal zero retention, model safety, privacy, data residency, uptime or endpoint latency.
- Safety and provenance: protect live API keys, verify the actual current customer terms including any supplemental API agreement, data retention, processing location, downstream providers, original model publishers, licensing/rights, ownership and sanctions exposure before using confidential or regulated data.
- Model exactly one producing company, **Hyperbolic Labs, Inc.**, based on the website's March 2025 legal Terms of Service. Current 2026 corporate news uses the Hyperbolic brand; do not infer complete 2026 beneficial control or claim the older legal terms override service-specific current terms.
- Provide the exact `produced-by` / `produces` pair and current first-party product/launch/terms sources. No authenticated API execution, independent benchmark, exhaustive UBO or whole-catalog schema/cache/CI verification is represented by this authoring package.

## Validation

- Unique Flux hosted model API entity; one inverse producer relation; no legacy duplicate, self-managed Forge/NIM or trained-model authorship.
- Key format, endpoint, data routing and preview/production boundaries accurately sourced to current official vendor material.
- Bounded metadata, reader, source and link checks distinct from production verification or clean saturation cycles.

## Scoped original-source qualification — 2026-11-08

- **Hyperbolic Flux Inference** is Hyperbolic's original **October 21, 2026** hosted OpenAI-compatible inference offering. The publisher explicitly treats **Flux as the API service** on top of its distinct Forge multi-cloud GPU orchestration control plane; neither product is a new trained model nor an automatic duplicate of the deprecated Hyperbolic inference endpoint.
- The officially documented `https://api.hyperbolic.ai/inference/v1` API supports Chat Completions and streaming, Pro/Organization prepaid billing, and current `sk_live_` credentials; model IDs, provider routes and supported sampling settings vary. Models may run either on Hyperbolic-owned serving infrastructure or via **external model providers**, so Hyperbolic data-routing/security statements cannot be extrapolated to every upstream route. No account, API credentials, model inference or billing were tested.
- First-party current product and original launch sources: https://www.hyperbolic.ai/inference ; https://www.hyperbolic.ai/blog/flux-inference-api .
- Source acceptance qualifies this existing hosted-service identity and current launch/migration/contract boundaries. No new entity or metadata credit, full provider-rights/privacy/legal/security audit, latency/performance certification, whole-catalog schema/cache/CI/render, clean or final gate.
