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
