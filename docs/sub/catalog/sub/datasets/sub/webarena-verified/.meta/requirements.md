# Documentation Requirements

## Requirements

- Present WebArena-Verified as ServiceNow's separately released, independently audited and version-controlled WebArena-derived web-agent **evaluation dataset and scoring contract**, not the same current benchmark identity as the original WebArena's annotation v0.2.0 or a generic browser-automation framework.
- Preserve the verified-task and reference-answer correction process, deterministic type-aware and network-event/HAR trace scoring, and offline replay/evaluation support as distinct evaluation semantics. Unlike the original WebArena's historical DOM/substring/LLM-judged checks, results require the specific audited task corpus and evaluator version.
- Distinguish the full version-controlled verified task corpus from the separately prioritized **258-task WebArena-Verified Hard subset**; the subset is not a complete replacement benchmark or a separately governed producer.
- Describe **2025-12-04** as the scheduled public-release date in the repository announcement and later official **2026-01/02** PyPI, uvx/Docker and optimized environment availability as dated distribution/methodology changes, not a new trained model, LLM provider, or separate evaluation service.
- Preserve the difference between original WebArena research stewardship (WebArena-x academic team), this ServiceNow-maintained verified derivation, and the independently published VisualWebArena multimodal tasks. Do not treat task IDs, success rates, validators or runtime trace fields across these as inherently comparable.
- Record dataset license, environment versions, authorization, benchmark inputs, network trace capture, task accessibility, and model/agent evaluator setup as version-sensitive and source-backed; do not present the verification claim as a blanket absence of measurement errors.

- Render the identity, provenance and operational context recorded in canonical `entity.identity_note`; keep version-sensitive claims and official resources aligned with the cited first-party sources.

- Render the standard `entity-relations` block from validated current-entity relations, ordered by explicit numeric order, target canonical name and target ID; resolve every visible target to its reader.

## Validation

- The published official ServiceNow repository and documentation substantiate the verified benchmark's independent maintained identity and evaluator.
- Original WebArena, VisualWebArena and WebArena-Verified remain distinct and their scores are not compared without matching versioned evaluation conditions.
- A reciprocal ServiceNow `produces` relation exists for this exact benchmark identity.

## Scoped original-source qualification — 2026-11-08

- **WebArena-Verified** is ServiceNow's independently maintained **2025–2026** audited derivative of the original WebArena browser-agent benchmark, with **812 version-controlled tasks** and a separately selected **258-task Hard subset**. Its checked/corrected task instructions, expected outputs and deterministic evaluators remain independent from the original WebArena, VisualWebArena, other WebArena-x benchmarks and the agent frameworks used to run them.
- Publisher evaluation replaces fragile substring and model-judged checks with type-aware JSON normalization, structural matching and captured **HAR/network-event** trace analysis, enabling offline result replay at a specified task/environment snapshot. The repository documents a planned December 2025 public release, January 2026 PyPI release and February 2026 `uvx`/Docker images. The root Apache-2.0 code grant does not prove that every replayed website, user account, webpage or captured network field is unrestricted or safe to publish.
- First-party sources: https://github.com/ServiceNow/webarena-verified ; https://servicenow.github.io/webarena-verified/ ; https://servicenow.github.io/webarena-verified/latest/ .
- One existing original corrected benchmark dataset/protocol is scoped as source-qualified; verified labels do not certify all remaining tasks as bug-free or authorize access to live third-party websites. No container/browser runs, protected trace viewing, model score reproduction, comprehensive rights/security/legal audit, complete schema/cache/CI/render, clean or final gate.
