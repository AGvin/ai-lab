# Documentation Requirements

## Requirements

- Use the reader-facing title `Evaluation Design`.
- Define evaluation design as the process of turning an evaluation question or decision need into a specified test/measurement plan: define the unit under evaluation, target behavior/property, operating conditions, examples/tasks, baselines/controls, measurement methods, metrics/judges, aggregation, uncertainty, acceptance criteria, and analysis/reporting plan.
- Start from a concrete evaluation question and intended use. Do not treat `evaluate the model` or `measure quality` as sufficiently specified without identifying the behavior, users/workload, conditions, and decision the evidence must support.
- Distinguish the unit under evaluation: base model, adapted model, prompt/configuration, retrieval component, agent/tool workflow, complete application/system, or human-AI process. Evaluate the complete system when surrounding components materially determine outcomes.
- Distinguish evaluation design from an evaluation dataset, benchmark, metric, judge, or result. Those are inputs/method components or outputs of a design, not synonyms for the design itself.
- Define representative conditions and sampling strategy explicitly. Include realistic task distributions and, where relevant, difficult, negative, boundary, adversarial, rare, subgroup, multilingual, long-context, failure-recovery, or other cases that materially affect the intended use.
- Explain train/development/evaluation separation and leakage/contamination risks where generalization is being estimated. Repeatedly optimizing against a fixed evaluation set can turn it into development data and reduce the credibility of subsequent estimates.
- Define success/failure criteria before interpreting results where practical. Acceptance thresholds, release gates, tolerances, and escalation rules are decision artifacts and must be connected to the actual risk/quality requirement rather than selected after seeing outcomes.
- Use multiple measurements when one aggregate score would hide material trade-offs or failure classes. Accuracy/quality, robustness, calibration, safety, latency, throughput, cost, human preference, and other dimensions are not interchangeable.
- Distinguish deterministic checks, executable/task-based scoring, reference-based metrics, human evaluation, model/LLM judges, simulations, and mixed methods. The choice of method must match the property being evaluated and its known failure modes.
- When using human or model judges, define the rubric, comparison/scale, context shown to judges, randomization/blinding where applicable, disagreement/reliability handling, and judge validation/calibration needed for the decision; a judge score is not self-validating.
- Record enough configuration/provenance to interpret and reproduce the test: model/system versions, prompts/instructions, tools/retrieval state, data version, decoding/runtime settings, dependencies, hardware/service conditions when relevant, and evaluation code/method version.
- Report distributions, uncertainty, sample counts, missing/failed cases, and meaningful failure categories rather than only a mean/aggregate score where variability matters. Statistical confidence is not a substitute for external validity or representative test design.
- Distinguish offline evaluation from production monitoring. Predeployment tests provide bounded evidence under sampled conditions; real operating behavior can shift through data, users, dependencies, models, attacks, policies, or environment and may require ongoing monitoring/re-evaluation.
- Keep concrete benchmark suites, evaluation datasets, test cases, model scores, leaderboards, acceptance decisions, experiment runs, and product-specific release gates with their applicable benchmark/dataset/evidence/project/decision owners.
- Use the canonical entity references as research inputs for representative-condition, multi-metric, uncertainty, and documented-evaluation boundaries when reader-facing rendering is activated.

## Validation

- Evaluation design is not equated with running a benchmark, selecting one metric, or collecting a score.
- The evaluated unit, intended use, operating conditions, and decision criteria are explicit rather than assumed.
- One average/aggregate metric does not hide material failure categories or trade-offs.
- Human/LLM judges are not treated as ground truth without rubric and method validation.
- Repeated test-set tuning, leakage, and distribution representativeness are acknowledged where applicable.
- Concrete evaluation cases/results, benchmark rankings, and release decisions remain outside the abstract design owner.
