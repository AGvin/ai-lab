# Documentation Requirements

## Requirements

- Identify FrontierScience as OpenAI's expert-level scientific-reasoning benchmark spanning physics, chemistry, and biology.
- Preserve the two benchmark tracks, Olympiad and Research, and the current gold-set/public-release boundary only while supported by current first-party OpenAI material.
- Keep the benchmark identity distinct from model scores, model-based graders, sample questions, external scientific benchmarks, and general AI-for-science concepts.
- Treat question counts, gold-set composition, grading details, evaluated models, reported scores, contamination controls, and future benchmark revisions as freshness-sensitive.
- Preserve OpenAI producer provenance through the canonical relation.
- Do not generalize performance on constrained benchmark problems into a claim that a model can independently perform complete scientific research.

- The published full evaluation has more than 700 questions; the public gold release contains 100 Olympiad and 60 Research questions, with the remainder held out for contamination tracking. Preserve these release boundaries when stating counts.
- Explain short-answer grading for Olympiad and the Research 10-point rubric with a published 7/10 correctness threshold as release-specific methods; distinguish expert task authorship from model-based response grading.
- Render the complete visible current-node relation set through the standard `entity-relations` component as a provenance block; preserve relation semantics and canonical target identities.
- Render an `official-resources` block with this explicit selection from canonical references: [FrontierScience release, gold sets, and grading method](https://openai.com/index/frontierscience/).

## Validation

- FrontierScience remains a concrete benchmark/dataset identity rather than a generic scientific-reasoning concept.
- Olympiad and Research are represented as benchmark tracks rather than separate canonical datasets unless a later upstream lifecycle establishes independent identities.
- OpenAI provenance resolves bidirectionally.
- Reported scores remain scoped to the exact evaluation setup and model revisions.

## Scoped original-source qualification — 2026-11-08

- **FrontierScience** is OpenAI's original **January 2026** expert-written benchmark for scientific reasoning in **physics, chemistry and biology**, with distinct **Olympiad** (constrained short-answer science problems) and **Research** (open-ended self-contained scientific subtasks) tracks. The publisher's complete evaluation contains **more than 700 original questions**, while its released public gold sets contain **100 Olympiad and 60 Research** questions; the rest are withheld for contamination monitoring and are not publicly distributable.
- Olympiad answers can be checked against constrained references, while the original Research evaluation uses expert-reviewed task-specific **10-point rubrics**, with the published **at least 7/10** threshold counted as correct. Research expert task-writing, automatic rubric grading, model evaluation and result leaderboards are distinct sources and procedures; model scores reflect selected prompt/harness/grader versions, not an independently demonstrated scientific discovery capability.
- Original publisher source: https://openai.com/index/frontierscience/ .
- Scoped acceptance covers the existing benchmark identity, dated original release, two tracks, gold/full split and score-protocol limitations only; no private task access, model run, third-party scientific dataset rights/security/legal audit, reader or metadata rewrite, complete schema/cache/CI/render, clean or final gate.
