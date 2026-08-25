# Documentation Requirements

## Requirements

- Use the reader-facing title `Model Evaluation`.
- Define model evaluation as the systematic measurement and characterization of a model's behavior, capabilities, limitations, and failure modes under explicitly specified model identity, configuration, tasks/scenarios, inputs, procedures, and metrics.
- Require evaluation scope to identify the exact model/version/artifact or hosted snapshot being evaluated when identity can affect behavior; a family name alone is not sufficient evidence for concrete capability claims.
- Distinguish intrinsic/model-focused evaluation from evaluation of a larger configured AI system. When prompts, retrieval, tools, system instructions, provider controls, application logic, or other scaffolding materially contribute to measured behavior, name and record that system/deployment scope instead of attributing every result to model weights alone.
- Treat capability and limitation statements as evidence-bounded conclusions under evaluated conditions rather than permanent labels. Generalization to other tasks, input distributions, contexts, languages, modalities, quantizations, runtimes, providers, or configurations requires justification or separate evidence.
- Explain that evaluation should define representative scenarios or input distributions, target properties, metrics or acceptance criteria, and relevant uncertainty/variation. Repeated measurements, confidence intervals, subgroup analysis, or error analysis are used when the evaluation question requires them rather than as universal mandatory forms.
- Require important failure signatures and boundary conditions to remain visible instead of reporting only an average score or successful demonstrations. A high aggregate result can coexist with severe failures on particular cases or dimensions.
- Distinguish capability measurement from support/specification facts. Supported modalities, published context limits, architecture facts, API availability, and other authoritative model/service facts belong to `catalog/models/reference/`; evaluation may test behavior within those conditions but does not replace the factual owner.
- Distinguish evaluation evidence from model selection. Evaluation can provide task-specific evidence, but recommendation, ranking, hardware-fit conclusions, portfolio choice, and cost-versus-acceptance decisions remain under `catalog/models/selection/` or another selected decision owner.
- Distinguish provider/model-developer claims from independent evaluation evidence. Claims can define hypotheses or documented baselines, but their provenance and evaluation conditions must remain explicit when used as evidence.
- Record behavior-affecting conditions such as prompting/instructions, context construction, tool/retrieval access, decoding controls, quantization/precision, runtime, hardware, provider endpoint/snapshot, and concurrency only when material to the evaluation; do not universalize one test harness as the definition of model evaluation.
- Re-evaluate or qualify prior conclusions when materially behavior-affecting identity, configuration, provider/runtime behavior, task distribution, or acceptance criteria change.
- Keep concrete current scores, benchmark runs, evaluation datasets/results, provider comparisons, and recommendation outputs with their applicable evidence, catalog, benchmark, or decision owners rather than embedding mutable findings in this concept.
- Use the canonical entity references as research inputs for standardized multi-metric evaluation, documented conditions, limitations, and generalizability boundaries when reader-facing rendering is activated.

## Validation

- The page does not treat a model family name, parameter count, leaderboard rank, or a few successful demos as sufficient capability evidence.
- Model-only evaluation is distinguished from evaluation of a configured system or deployment whose scaffolding materially affects behavior.
- Capability and limitation claims are scoped to explicit evaluated conditions and are not presented as permanent intrinsic labels.
- A single aggregate benchmark score is not treated as a complete characterization of model quality, reliability, safety, or task fit.
- Canonical model/service facts remain with `catalog/models/reference/`; recommendations and task-fit decisions remain with `catalog/models/selection/`.
- Provider claims are not silently represented as independent evaluation.
- Legacy evaluation guidance is preserved as reusable measurement semantics without duplicating mutable model facts or model-selection decisions.
