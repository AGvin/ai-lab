# Documentation Requirements

## Requirements

- Identify LifeSciBench as OpenAI's expert-authored and expert-reviewed benchmark for evaluating AI systems on realistic life-science research tasks.
- Preserve the current first-party benchmark boundary: 750 tasks across seven workflows and seven biological domains, with attached scientific artifacts and rubric-based expert evaluation, only while supported by current OpenAI material.
- Keep benchmark identity distinct from model results, evaluator implementations, individual task artifacts, generic scientific-reasoning concepts, and downstream product recommendations.
- Treat task counts, artifact counts, workflow/domain taxonomy, scoring thresholds, reported model performance, public-access/distribution details, and future benchmark revisions as freshness-sensitive.
- Preserve OpenAI producer provenance through the canonical relation rather than duplicating organization details in benchmark prose.
- Do not generalize benchmark performance into claims about end-to-end autonomous scientific reliability or real-world experimental validity.

- Render the complete visible current-node relation set through the standard `entity-relations` component as a provenance block; preserve relation semantics and canonical target identities.
- Render an `official-resources` block with this explicit selection from canonical references: [LifeSciBench publication and evaluation scope](https://openai.com/index/introducing-life-sci-bench/).

## Validation

- LifeSciBench is represented as a concrete benchmark/dataset identity, not as a generic life-science evaluation concept.
- OpenAI provenance resolves bidirectionally.
- Benchmark-specific quantitative claims remain scoped to the documented revision and evaluation setup.
