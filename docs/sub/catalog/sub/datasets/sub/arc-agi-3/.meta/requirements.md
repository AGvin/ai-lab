# Documentation Requirements

## Requirements

- Identify ARC-AGI-3 as the ARC Prize Foundation's released interactive, turn-based environments for evaluating an agent's exploration, goal inference, planning, and learning efficiency.
- Preserve this benchmark's independent identity from ARC-AGI-2 static grid-task benchmark and the ARC-AGI-3 benchmarking harness/toolkit implementation.
- Track Relative Human Action Efficiency and benchmark scoring by the applicable official revision. Separate interactive environment datasets, public/private game sets, agent runtime/harness configurations, retries, state retention, and provider-native conversation adapters so results remain comparable only under equivalent protocols.
- Ground dataset/environment counts, access paths, official rules, results, scores, model/harness versions, contamination controls, and revision history in dated official first-party sources.
- Keep generated reasoning strategies, model-specific submissions, benchmark analysis, and application code outside the canonical dataset identity unless they have independently useful released software identities.
- Preserve the ARC Prize Foundation producer provenance with reciprocal `produces` linkage.

## Validation

- The dataset represents an official released benchmark identity, not a single model score or a competition leaderboard.
- The release-specific evaluation protocol and public/private access boundaries are not confused.
- Official sources match the entity metadata and producer relation.
- Comparisons across versions, tasks and harnesses are qualified rather than treated as directly equivalent.

## Scoped original-source qualification — 2026-11-08

- **ARC-AGI-3** is the ARC Prize Foundation's interactive adaptive-reasoning benchmark, launched **2026-03-25**. Unlike ARC-AGI-1/2 static grid transformations, it evaluates agents exploring turn-based environments without explicit task instructions, inferring goals and dynamics, and planning action sequences relative to human action-efficiency baselines.
- Public benchmark environments, optional private competition material, current rules and leaderboards are different release/access surfaces. The `arcprize/arc-agi-3-benchmarking` repository is a **benchmark runner/agent harness**, not the canonical game-set dataset; its standard and provider-native conversation adapters use different context management, so scores must identify the exact harness and environment protocol.
- First-party publisher sources: https://arcprize.org/arc-agi/3 ; https://arcprize.org/blog/arc-agi-3-launch ; https://github.com/arcprize/arc-agi-3-benchmarking
- Bounded source acceptance covers original release, identity, publicly documented interactive task and scoring boundaries. No restricted games, reproduced model score, independent data-rights/security/legal audit, repository-wide schema/cache/CI/render, clean or final credit.
