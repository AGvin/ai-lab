# Documentation Requirements

## Requirements

- Use the reader-facing title `AI System Cost and Capacity`.
- Define this node as the reusable engineering owner for measuring, forecasting, allocating, and constraining the financial/resource capacity required to deliver AI-system work under explicit quality, reliability, latency, safety, and policy requirements.
- Distinguish cost from price. Provider token prices, GPU-hour rates, storage tariffs, and API fees are input prices; total system cost can also include retrieval, embeddings/reranking, tools/external APIs, networking/egress, storage, caches, observability, idle/provisioned infrastructure, retries/fallbacks, human review, engineering/operations, and consequential failure/rework where relevant.
- Prefer unit economics tied to an explicit accepted unit of value or work, such as cost per accepted task, successful workflow, evaluated document, generated asset, active user, transaction, or another defined business/mission unit. Raw `cost per token` or `cost per request` is insufficient when success rates, retries, output lengths, or downstream correction differ.
- Define the acceptance/quality boundary before comparing cost where practical. A cheaper path that produces more invalid outputs, failures, human correction, policy violations, or retries can have higher cost per accepted result than a higher-priced path.
- Distinguish variable/marginal consumption costs from fixed, reserved, idle, capital, and operational costs. Hosted usage, self-hosted infrastructure, rented accelerators, and hybrid systems distribute these cost classes differently and should not be compared through one marginal request price alone.
- Define capacity as the sustainable amount of workload/resource demand a system can serve while meeting the required performance/reliability/policy targets. Capacity can be constrained by compute, accelerator memory, CPU/RAM, storage, network, request/token/tool quotas, concurrency, queue depth/age, human-review throughput, provider limits, or other bottlenecks.
- Distinguish nominal installed/provisioned resources from usable capacity. Hardware specifications, purchased quota, maximum concurrency, or memory size do not prove sustained capacity for the target workload after overhead, headroom, failures, context/cache state, and acceptance criteria are included.
- Explain capacity planning as matching expected and peak demand to sufficient supply/headroom while avoiding unnecessary overprovisioning. Forecasts should include workload mix, growth/seasonality/bursts, scaling/recovery delay, dependency limits, and uncertainty rather than only average demand.
- Distinguish capacity planning from scalability. Capacity planning estimates and provisions/allocates resources for expected demand; `performance-and-scalability/` owns how architecture/runtime behavior adapts as demand changes and where saturation/queueing/backpressure emerge.
- Treat budgets and quotas as explicit controls rather than descriptive metrics alone. Budgets can cap spend or trigger alerts/escalation; quotas/rate limits can constrain requests, tokens, generated output, concurrency, tool actions, compute time, storage, or monetary consumption at user, tenant, workflow, service, or provider boundaries.
- Do not define rate limiting only as HTTP 429. HTTP 429 is one protocol response for a rate-limited request; generic rate/quota enforcement can reject, delay, queue, shed, degrade, or otherwise govern work and can use fixed/sliding/token-bucket/leaky-bucket/concurrency or provider-specific mechanisms.
- When a service exposes retry/reset information, use it as concrete protocol/provider behavior rather than a universal rate-limit contract. Retrying without budget/deadline/backoff controls can amplify overload and cost; retry semantics remain linked to reliability-and-resilience.
- Treat rate limits as both capacity and governance controls where relevant. They can protect dependencies, isolate tenants, bound runaway agents/tool loops, enforce commercial tiers, or reserve capacity for priority workloads; one shared request-count limit is not sufficient for every resource dimension.
- Explain caching as a possible unit-cost/capacity lever: reusing compatible responses, retrievals, embeddings, tool results, compiled artifacts, or processed context can avoid repeated work, but cache storage, lookup, invalidation, staleness, low hit rates, privacy/isolation, and correctness risks can outweigh savings.
- Distinguish generic cost-oriented caching from selected `models/inference/memory-and-context/context-caching/`, which owns reuse of processed model context/prefix state. Do not duplicate that mechanism's canonical semantics here.
- Explain attribution/showback/chargeback dimensions as implementation families: costs and capacity consumption can be tagged/allocated to users, tenants, teams, products, workflows, models, providers, or business units so optimization does not hide cross-subsidies or abnormal loops.
- Treat forecasts and budgets as uncertain models. Changes in provider pricing, workload distribution, model versions, output length, hit rates, utilization, hardware availability, staffing, or failure rate can materially alter unit economics; record the assumptions and effective date of mutable inputs.
- Distinguish cost optimization from indiscriminate cost reduction. Security, privacy/residency, reliability, correctness, human oversight, verification, latency, or accepted quality constraints may set non-negotiable floors; cost optimization searches within eligible solutions rather than trading those constraints away silently.
- Keep model-choice consequences linked to the canonical `catalog/models/selection/` decision owner. This concept can explain cost/capacity variables and trade-offs but must not become a duplicate model recommendation tree.
- Keep concrete provider prices, current quota values, hardware purchase/rental prices, budgets, forecasts, unit-cost measurements, tenant allocations, billing exports, current rate-limit headers, and project/model-selection decisions with their applicable catalog/evidence/project/decision owners.
- Use the canonical entity references as research inputs for unit-economics, capacity-planning, and generic rate-limit boundaries when reader-facing rendering is activated.

## Validation

- Cost is not equated with provider/API price or token price alone.
- Cost comparisons use a defined work/value/accepted-result denominator when raw request/token units would hide quality or retry differences.
- Capacity is not inferred from nominal hardware specifications, purchased quotas, or maximum theoretical concurrency alone.
- Capacity planning is distinguished from scalability/performance engineering.
- Rate limits can govern multiple resource dimensions and are not defined only as HTTP 429 or requests-per-minute.
- Caching is treated as a trade-off with correctness, storage, invalidation, isolation, and hit-rate costs rather than automatic savings.
- Cost optimization cannot silently weaken mandatory trust, privacy, safety, reliability, or acceptance constraints.
- Concrete prices, quotas, budgets, measurements, and model/provider recommendations remain outside the reusable concept owner.
