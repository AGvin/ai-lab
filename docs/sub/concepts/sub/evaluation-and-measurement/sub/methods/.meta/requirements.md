# Documentation Requirements

## Requirements

- Use the reader-facing title `Evaluation Methods`.
- Present this node as the canonical owner for reusable procedures that turn evaluation cases, candidate outputs, system behavior, references, rubrics, and evaluator observations into structured judgments or evidence used by an evaluation design.
- Distinguish an evaluation method from the evaluation design that selects and combines methods. A design specifies the question, sample, controls, acceptance logic, and analysis plan; a method specifies how a particular class of observations or judgments is elicited and recorded.
- Distinguish methods from metrics, datasets, benchmarks, evaluator identities, rubrics, and results. A method can use a dataset, rubric, evaluator, and metric, but none of those artifacts alone is synonymous with the method.
- Keep `human-evaluation/` and `llm-as-a-judge/` as distinct selected descendants. Humans and language-model judges can apply similar rubrics or pairwise/rating procedures, but their error sources, validity evidence, operational constraints, and governance concerns differ materially.
- Explain that method choice should follow the property being measured. Exact executable checks, reference-based scoring, human judgment, model judgment, task success, simulation, observational measurement, and mixed methods are appropriate for different questions; do not substitute subjective judging for deterministic validation when exact correctness can be checked directly.
- Require the evaluator's observable context and task instructions to be defined: candidates shown, references/evidence, rubric, scoring/ranking scale, allowed tools, identity/blinding information, ordering/randomization, and abstention/uncertainty options where applicable.
- Distinguish reliability from validity. Repeated evaluators can agree consistently on the wrong criterion, while disagreement can arise from ambiguous rubrics, heterogeneous legitimate preferences, insufficient evidence, evaluator error, or genuinely subjective tasks.
- Explain that calibration/validation requires comparison against an appropriate trusted reference process, known-answer subset, expert review, controlled perturbations, or other external evidence suited to the evaluation property. An evaluator cannot validate itself merely by producing confident rationales or stable scores.
- Explain that aggregation choices such as majority vote, mean score, median, pairwise win rate, adjudication, weighting, or ensemble voting encode assumptions and can change conclusions; no aggregation rule is universally correct.
- Make clear that presentation order, formatting, verbosity, model/source identity, evaluator expectations, incentives, fatigue, prompt wording, and contextual framing can influence judgment. Design methods to measure or mitigate relevant effects rather than assuming evaluator neutrality.
- Explain that evaluator disagreement, missing judgments, abstentions, invalid responses, and failed evaluations require explicit handling and should not be silently discarded when they affect uncertainty or conclusions.
- Keep concrete evaluator pools/models, prompts/rubrics, calibration sets, annotation interfaces, compensation, judge configurations, evaluation runs, scores, and acceptance decisions with their applicable project/evidence/catalog/governance owners.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.

## Validation

- Evaluation methods are not equated with datasets, metrics, benchmarks, rubrics, evaluator identities, or result records.
- Reliability/agreement is not treated as sufficient proof of validity.
- Subjective judges are not substituted for deterministic checks where exact correctness is directly testable without a documented reason.
- Evaluator context, instructions, ordering, uncertainty, and aggregation assumptions are explicit where material.
- Concrete evaluators, prompts, rubrics, annotation runs, and result values remain outside the reusable methods owner.
- Direct-child navigation contains only currently materialized selected descendants.
