# Documentation Requirements

## Requirements

- Identify ARC-AGI-2 as the ARC Prize Foundation's static visual abstract-reasoning grid tasks, intended to measure adaptation to novel reasoning problems.
- Preserve this benchmark's independent identity from ARC-AGI-1 predecessor and ARC-AGI-3 interactive agent benchmark.
- Preserve the public/private evaluation split, task updates, scoring protocol, and the release-specific data version when claiming reproducible scores. ARC Prize competitions and leaderboards should not be confused with the canonical dataset itself.
- Ground dataset/environment counts, access paths, official rules, results, scores, model/harness versions, contamination controls, and revision history in dated official first-party sources.
- Keep generated reasoning strategies, model-specific submissions, benchmark analysis, and application code outside the canonical dataset identity unless they have independently useful released software identities.
- Preserve the ARC Prize Foundation producer provenance with reciprocal `produces` linkage.

## Validation

- The dataset represents an official released benchmark identity, not a single model score or a competition leaderboard.
- The release-specific evaluation protocol and public/private access boundaries are not confused.
- Official sources match the entity metadata and producer relation.
- Comparisons across versions, tasks and harnesses are qualified rather than treated as directly equivalent.

## Scoped original-source qualification — 2026-11-08

- **ARC-AGI-2** is a distinct **2025 static abstract-reasoning benchmark** released by the ARC Prize Foundation. The official publisher's current version page lists **1,000 public training tasks**, **120 public evaluation tasks**, **120 semi-private evaluation tasks**, and **120 private evaluation tasks**. Public calibration, human trials, and `pass@2` competition rules are publisher claims about the released evaluation protocol, not independent validation of every model score.
- ARC-AGI-2 is not the 2019 ARC-AGI-1 dataset, an interactive ARC-AGI-3 environment or an unrestricted license to the held-out evaluation tasks. The official ARC Prize page and GitHub organization are authoritative on edition and access; do not infer access to semi-private/private task content from public repository metadata.
- Verified first-party sources: https://arcprize.org/arc-agi/2 and https://arcprize.org/guide/1 and https://github.com/arcprize/ARC-AGI-2
- Source acceptance covers existing identity, publisher, public source/split boundaries and published evaluation protocol; no licensed private tasks, independent human calibration replay, live model testing, full rights/legal/security audit, repository-wide schema/cache/CI/render, reader repair, clean or final credit.
