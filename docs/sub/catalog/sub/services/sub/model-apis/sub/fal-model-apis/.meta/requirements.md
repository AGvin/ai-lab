# Documentation Requirements

## Requirements

- Identify **fal Model APIs** as the managed generative-model endpoint service operated by fal (Features & Labels, Inc.), not a standalone open-source model, the serverless self-deployment offering, or a second legal producer.
- Official [Model APIs docs](https://fal.ai/docs/documentation/model-apis/overview) distinguish synchronous `run`, queue-backed `subscribe` and asynchronous `submit` workflows, plus model-specific streaming and real-time WebSocket interfaces. Do not imply that every model supports every transport.
- Document example queue endpoint shape `https://queue.fal.run/<model-path>` using `Authorization: Key` from [first-party documentation](https://fal.ai/docs/documentation); direct execution and queue have different failure, polling and webhook semantics.
- Preserve third-party authorship and model-specific output/data rights: API access is not a blanket license to copy weights, redistribute training inputs or impersonate content owners. Models, endpoints, usage credits, API concurrency, security controls, region and retention are mutable.
- Connect this service's `produced-by` to **existing** `catalog/producers/f/features-and-labels-inc` and add the reciprocal `produces` relation there. Do **not** materialize `catalog/producers/f/fal-ai` as a second entity; frozen candidate `v1:fal-ai` is an unresolved alias/duplicate case needing explicit versioned scope reconciliation, not an additional accepted identity/gate.
- Honor [fal's published legal terms](https://fal.ai/legal/terms-of-service), including current API supplemental agreements and user-input controls; protect keys, user media and confidential prompts, and obtain appropriate rights for uploaded media and generated output.
- No API call, account authentication, image/video generation, price or latency benchmark, complete rights/privacy freshness audit, full CI or whole-catalog clean pass is claimed.

## Validation

- The existing Features & Labels producer and this new service reciprocally link; only the new Model APIs entry counts as frozen-candidate acceptance.
- The fal.ai brand versus legal entity duplicate remains explicit in operational work-state, with no new duplicate producer node.

## Scoped original-source qualification — 2026-11-06

- fal Model APIs are provider-hosted model invocation interfaces. The documented synchronous fal.run route returns results directly and does not automatically retry transient failures, whereas queue.fal.run accepts jobs and exposes request/status/result/cancel semantics. Endpoint-specific streaming, real-time and synchronous fallback chains are not available uniformly.
- Official fal requests use an API key with the Authorization: Key scheme for authenticated endpoints. Request/response storage can follow account defaults or supported request headers; model-owner identity, content rights, pricing, model schema, concurrency and output retention remain per-model and per-account.
- Verified first-party source 1: https://fal.ai/docs/api-reference/inference-api/sync/run
- Verified first-party source 2: https://fal.ai/docs/api-reference/inference-api/queue/submit
- Verified first-party source 3: https://fal.ai/docs/documentation/model-apis/inference/fallback-chains
- Scope: only current provider-documented hosted service identity and endpoint/version boundaries. No new metadata or entity, reader-repair credit, independent run, complete freshness/legal/security clearance, root-wide schema/cache/CI/render, clean pass or final delivery.
