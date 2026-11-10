# Documentation Requirements

## Requirements

- Identify **Friendli Model APIs** as an active hosted serverless API for managed inference, produced by FriendliAI. It is not the separate Friendli Dedicated Endpoints deployment product, self-managed Friendli Container engine, a trained model, or the Friendli Suite umbrella.
- Preserve the official documented base URL `https://api.friendli.ai/serverless/v1`; contrast dedicated `https://api.friendli.ai/dedicated/v1`. Document OpenAI-compatible chat completions and vendor-described Responses and Anthropic Messages interfaces without promising identical support across all hosted models.
- The provider-curated serverless model set differs from the larger dedicated/custom model deployment catalog. A hosted DeepSeek, Qwen, Llama, GLM, Kimi or other model retains its original developer and model-license provenance; FriendliAI produces the inference service, not those original trained models.
- Source all availability and usage claims to current first-party product, help-center and pricing pages. Model IDs, token rates, quotas, regions, SLA eligibility, billing and API features vary with plan/model and may change; do not hardcode a model inventory or a universal latency/cost ranking.
- Keep provider and model risks explicit. Require verification of data processing, retention, training use, geographic location, contract, sanctions/ownership of the exact upstream model/provider and applicable rights before sending confidential or production data. Keep API keys secret; no tokens or live authenticated requests are included.
- Model the original corporate/brand producer as one **FriendliAI** organization, backed by current official brand, company and contact material, not a second model or deployment identity. Historic FriendliAI Inc. and current FriendliAI Corp. labels do not establish a complete corporate legal succession or beneficial ownership audit.
- Include exactly one inverse `produced-by` / `produces` pair and official source links. The producer's San Francisco and Seoul locations are first-party public office/hub descriptions, not proof of every subsidiary or current control holder.

## Validation

- Exactly one canonical Friendli Model APIs hosted service and FriendliAI producer, no duplicate dedicated endpoint, self-managed runtime or model.
- Original third-party model producers and licenses not reassigned; cloud terms/security claims remain scoped to exact account and contract.
- A bounded entity/reader/link/provenance check is not full schema/cache/CI, model inference execution, beneficial ownership certification, or a clean whole-catalog research pass.

## Scoped original-source qualification — 2026-11-06

- Friendli Model APIs offers provider-operated managed serverless access to selected third-party/open models. FriendliAI describes OpenAI-compatible APIs and a separate migration path to Dedicated Endpoints with isolated capacity. Hosted curated model inventory is not the full catalog of models available through dedicated endpoints or self-managed Friendli Container.
- Do not infer full API parameter compatibility, exact support for every Responses/Messages model, universal deployment SLA, unrestricted capacity, storage/retention controls or upstream model licenses from general marketing or a base URL.
- Verified first-party source 1: https://friendli.ai/product/model-apis
- Verified first-party source 2: https://learn.friendli.ai/articles/4213111023-q10-1-how-do-i-connect-friendliai-with-litellm-or-other-openai-compatible-client
- This source qualification accepts only the existing hosted-service identity and bounded claims. It does not establish full freshness, legal/ownership/license clearance, independent security or performance, authenticated endpoints, complete schema/cache/CI/render, clean pass or final delivery.
