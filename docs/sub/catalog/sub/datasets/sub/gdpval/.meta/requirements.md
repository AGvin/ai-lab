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

## Scoped original-source qualification — 2026-11-08

- **GDPval** is OpenAI's original released benchmark for **real-world professional knowledge-work deliverables** across **44 occupations and nine sectors**, not a gross-domestic-product forecast or proof of universal job automation. The original evaluation includes **1,320 tasks**, while the official OpenAI Hub distributes a **220-task public gold subset** with supporting reference assets, scored rubrics and model/human evaluation methodology.
- The benchmark's full/private and released/public subsets must not be merged or scored interchangeably. Hosted leaderboard retirement/status and open/self-run grading guidance are separate platform surfaces; don't infer an active hosted grading service or independent economic value from published model costs, results or judge ratings. The public dataset card discloses third-party brand references, optional media and limited sensitive-content cases with separate rights/privacy considerations.
- Original publisher sources: https://openai.com/index/gdpval/ ; https://huggingface.co/datasets/openai/gdpval ; https://evals.openai.com/gdpval/grading
- Source acceptance covers one existing benchmark identity, public/full split and documented evaluator/rubric access boundaries only. No private task access, model/paid human-expert grading, independent productivity forecast, corpus rights/security/legal audit, whole-repo schema/cache/CI/render, clean or final gate.
