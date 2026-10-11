# Documentation Requirements

## Requirements

- Present WebArena-Verified as ServiceNow's separately released, independently audited and version-controlled WebArena-derived web-agent **evaluation dataset and scoring contract**, not the same current benchmark identity as the original WebArena's annotation v0.2.0 or a generic browser-automation framework.
- Preserve the verified-task and reference-answer correction process, deterministic type-aware and network-event/HAR trace scoring, and offline replay/evaluation support as distinct evaluation semantics. Unlike the original WebArena's historical DOM/substring/LLM-judged checks, results require the specific audited task corpus and evaluator version.
- Distinguish the full version-controlled verified task corpus from the separately prioritized **258-task WebArena-Verified Hard subset**; the subset is not a complete replacement benchmark or a separately governed producer.
- Note the public WebArena-Verified release announced **2025-12-04** and later official **2026-01/02** PyPI, uvx/Docker and optimized environment availability as dated distribution/methodology changes, not a new trained model, LLM provider, or separate evaluation service.
- Preserve the difference between original WebArena research stewardship (WebArena-x academic team), this ServiceNow-maintained verified derivation, and the independently published VisualWebArena multimodal tasks. Do not treat task IDs, success rates, validators or runtime trace fields across these as inherently comparable.
- Record dataset license, environment versions, authorization, benchmark inputs, network trace capture, task accessibility, and model/agent evaluator setup as version-sensitive and source-backed; do not present the verification claim as a blanket absence of measurement errors.

## Validation

- The published official ServiceNow repository and documentation substantiate the verified benchmark's independent maintained identity and evaluator.
- Original WebArena, VisualWebArena and WebArena-Verified remain distinct and their scores are not compared without matching versioned evaluation conditions.
- A reciprocal ServiceNow `produces` relation exists for this exact benchmark identity.
