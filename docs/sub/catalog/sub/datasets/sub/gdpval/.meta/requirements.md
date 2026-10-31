# Documentation Requirements

## Requirements

- Identify GDPval as OpenAI's released evaluation for economically valuable, real-world knowledge-work tasks across multiple occupations and industries.
- Preserve the benchmark boundary around professional work products and expert judging rather than treating it as a generic GDP/economic-impact metric.
- Keep full-set versus open benchmark subset, task/occupation inventory, reference files, gold deliverables, rubrics, grading workflow, human-expert comparison, evaluated models, scores, and leaderboard availability freshness-sensitive.
- Preserve the current shift from the retired hosted OpenAI leaderboard to open/self-run grading guidance without treating leaderboard shutdown as benchmark retirement.
- Keep benchmark tasks and model outputs separate from occupational advice, hiring/automation forecasts, and universal productivity claims.
- Attribute speed/cost/quality comparisons to the exact OpenAI evaluation setup and model revisions.
- Preserve OpenAI producer provenance.

- The first release distinguishes 1,320 full-set tasks from the 220-task public gold subset across 44 occupations and nine sectors. Treat the OpenAI Hugging Face distribution as the public subset, not the full private evaluation.
- Ground the hosted-leaderboard retirement statement in the official search-retrieved status notice. Direct text retrieval of that page exposes no body; do not represent it as a directly inspected rendered page, and do not promise an active hosted grading service from the guidance link.
- Render the complete visible current-node relation set through the standard `entity-relations` component as a provenance block; preserve relation semantics and canonical target identities.
- Render an `official-resources` block with this explicit selection from canonical references: [GDPval release and methodology](https://openai.com/index/gdpval/); [OpenAI GDPval public dataset](https://huggingface.co/datasets/openai/gdpval); [GDPval grading guidance](https://evals.openai.com/gdpval/grading); [OpenAI-hosted leaderboard status](https://evals.openai.com/gdpval/leaderboard?curius=2011).

## Validation

- GDPval remains a concrete benchmark/dataset identity rather than a broad economic-impact concept.
- Open benchmark subset and full evaluation are not conflated.
- Reported model/human comparisons remain tied to the exact evaluation configuration.
- OpenAI provenance resolves bidirectionally.
