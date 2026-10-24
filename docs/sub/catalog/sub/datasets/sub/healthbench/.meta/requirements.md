# Documentation Requirements

## Requirements

- Identify HealthBench as OpenAI's released rubric-based benchmark for evaluating health-response capability and safety on realistic health conversations.
- Preserve the benchmark family boundary across the main HealthBench evaluation and named variants such as Hard, Consensus, and Professional only while current OpenAI evaluation material supports their definitions.
- Keep conversation count, theme/axis taxonomy, rubric criteria, physician validation, grader methodology, response-length adjustment, evaluated models, scores, and current variant inventory freshness-sensitive.
- Keep HealthBench distinct from MentalHealthBench, clinical-decision systems, medical-device validation, ChatGPT Health product behavior, and generic healthcare QA benchmarks.
- Preserve the safety boundary from OpenAI material: benchmark performance is not evidence that a model is approved to diagnose, treat, or replace a medical professional.
- Attribute model comparisons to the exact HealthBench revision, length-adjustment method, grader, and model configuration.
- Preserve OpenAI producer provenance.

- Use the official release to distinguish the original 5,000-conversation benchmark, 1,000-example Hard subset, and 3,671-example Consensus variant with criteria filtered through physician agreement. Preserve the difference between Consensus error-rate reporting and other score conventions.
- Use the HealthBench Professional paper for its 525 clinician tasks across care consult, writing/documentation, and medical research; it complements rather than replaces the broader HealthBench evaluation.
- Explain that the GPT-5.5 system-card methodology uses an updated implementation and empirical final-response-length adjustment around a 2,000-character baseline, with variant-specific coefficients. Require exact implementation, grader, raw/adjusted score convention and response length; do not compare these scores unqualified with earlier publications.
- Render the complete visible current-node relation set through the standard `entity-relations` component as a provenance block; preserve relation semantics and canonical target identities.
- Render an `official-resources` block with this explicit selection from canonical references: [HealthBench paper](https://cdn.openai.com/pdf/bd7a39d5-9e9f-47b3-903c-8b847ca650c7/healthbench_paper.pdf); [HealthBench release, Hard, and Consensus](https://openai.com/index/healthbench/); [HealthBench Professional paper](https://cdn.openai.com/dd128428-0184-4e25-b155-3a7686c7d744/HealthBench-Professional.pdf); [Updated HealthBench implementation and length adjustment](https://deploymentsafety.openai.com/gpt-5-5/healthbench).

## Validation

- HealthBench remains a benchmark identity rather than a clinical validation claim.
- HealthBench variants remain benchmark tracks/subsets unless independent upstream lifecycle establishes separate canonical identities.
- MentalHealthBench is not treated as an alias or subset.
- OpenAI provenance resolves bidirectionally.
