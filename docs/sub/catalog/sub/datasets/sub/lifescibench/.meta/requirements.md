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

## Scoped original-source qualification — 2026-11-08

- **LifeSciBench** is OpenAI's original **July 2026** expert-curated evaluation for realistic applied life-science research work: **750 tasks** across **seven workflow categories and seven biological domains**, with **1,062 attached task artifacts**, **19,020 scored rubric criteria**, and documented contributions from **173 scientists and 453 expert reviewers**. Scientific prompts, expert rubrics, attachments, response graders and evaluated models form different surfaces of one benchmark identity.
- The seven workflow categories span evidence handling, analysis, design/optimization, scientific reasoning, validation/operations, translation and scientific communication. Supporting images, papers, tables, structure files and web sources may carry separate copyright, privacy, model-output and publication limits. Expert-authored tasks do not prove models can carry out independent wet-lab research, drug discovery, or clinical intervention safely.
- First-party publisher source: https://openai.com/index/introducing-life-sci-bench/ .
- Source gate qualifies one existing task-based benchmark identity, released 750/7/7 scope and artifact/rubric construction boundaries only. No benchmark/model execution, complete attached-resource rights/security/legal/freshness audit, reader repair, whole-repository schema/cache/CI/render, clean or final credit.
