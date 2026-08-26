# Documentation Requirements

## Requirements

- Use the reader-facing title `Model Routing`.
- Define model routing as a system-level architecture/policy that selects among two or more eligible model, endpoint, configuration, execution, or escalation paths for a request or workflow step using explicit request/context signals, capabilities, policy constraints, availability, risk, quality expectations, latency, cost, or other decision criteria.
- Distinguish routing from static model selection. Model selection chooses a model/path for a deployment or use case; routing makes a runtime or per-request/per-step choice among already governed candidate paths, though both can share evidence and eligibility criteria.
- Distinguish model routing from intrinsic mixture-of-experts/expert routing. MoE routers select internal neural experts/parameters during model execution; model routing selects system-level model/execution paths and remains an AI-engineering architecture concern.
- Distinguish model routing from speculative decoding. Speculative decoding uses a proposal path plus target verification to accelerate one target model's generation; model routing chooses which system/model path owns the request/step according to policy.
- Explain router implementations as families rather than requirements: deterministic rules, user choice, request classifiers, learned preference/quality routers, confidence/uncertainty gates, cost/latency optimizers, policy engines, cascades/escalation, contextual bandits, or combinations.
- Separate hard eligibility/policy constraints from optimization preferences. Modality support, required context/tool/schema capabilities, data residency, trust boundary, authorization, safety policy, contractual restrictions, and mandatory quality requirements should exclude ineligible routes before cost/latency optimization when the system depends on those constraints.
- Treat routing inputs as potentially untrusted. Prompt/request text can inform task classification but must not directly grant access to privileged tools, restricted data regions, higher-trust execution environments, or other capabilities without independent authorization/policy enforcement.
- Explain routing error as a first-class failure mode. A router can misclassify difficulty/capability/risk, route an eligible request to a lower-quality path, or unnecessarily escalate easy work; evaluate the complete policy against relevant fixed-path baselines and target acceptance criteria.
- Explain that router quality depends on the distribution of requests and candidate models/endpoints. A threshold or classifier calibrated for one model pair, workload, price schedule, or version can become invalid after model/provider updates or workload drift.
- Distinguish route selection from fallback/recovery. A router can choose among healthy eligible paths during normal operation; `fallback-architectures/` owns controlled alternative behavior triggered by failure, unavailability, rejection, or inability to satisfy the preferred path. Systems can combine both.
- Explain cascades/escalation as a routing family in which one path runs first and another is invoked after a confidence, validation, quality, policy, or failure condition. Escalation criteria require evaluation because the first path's self-confidence or self-judgment can be poorly calibrated.
- Address state/session consistency where relevant. Changing models mid-conversation or workflow can alter tokenization, system-prompt interpretation, tool schemas, structured-output behavior, safety/refusal policy, style, context limits, and hidden assumptions; shared application state must not assume model equivalence.
- Explain that routing across providers or deployment locations can change privacy, residency, retention, licensing, observability, rate-limit, and incident boundaries. Availability/cost optimization must not silently relax a stronger data/security policy.
- Require route decisions and materially relevant decision inputs/outcomes to be observable enough for debugging/evaluation without logging prohibited sensitive content. Compare routed-system quality, failures, latency, cost, policy violations, and route distribution rather than only aggregate spend.
- Keep concrete candidate model/provider lists, current capability matrices, route thresholds, classifier checkpoints, pricing tables, provider availability, incident data, prompt-specific rules, and deployment recommendations with their applicable catalog, evidence, project, or decision owners.
- Use the canonical entity references as research inputs for learned/cascade routing and quality-cost policy boundaries when reader-facing rendering is activated.

## Validation

- Model routing is not confused with MoE expert routing, speculative decoding, or static model selection.
- Hard capability/trust/authorization constraints are not silently traded away for lower cost or latency.
- Untrusted request content cannot directly select privileged routes without independent policy enforcement.
- Router thresholds/classifiers are not presented as workload/model-version-independent constants.
- Route-policy evaluation includes misrouting/regression and complete-system outcomes rather than cost reduction alone.
- Cross-provider/model routing does not assume equivalent context, tool, schema, safety, privacy, or licensing behavior.
- Concrete models/providers, thresholds, prices, and routing tables remain outside the reusable model-routing owner.
