# Documentation Requirements

## Requirements

- Use the reader-facing title `Human Evaluation`.
- Define human evaluation as an evaluation method in which people observe specified model/system behavior, outputs, interactions, references, or outcomes and produce structured judgments such as ratings, rankings, pairwise preferences, labels, critiques, task-success assessments, or qualitative observations under a defined protocol.
- Do not treat human evaluation as automatic ground truth. Human judgments reflect the rubric, information shown, evaluator expertise, population, incentives, culture, preferences, fatigue, uncertainty, and task ambiguity; they require validity evidence for the property being measured.
- Distinguish evaluator population from target user/affected population. General crowdworkers, internal staff, domain experts, end users, and affected stakeholders can answer different questions, and a convenient rater pool is not automatically representative of the deployment context.
- Match expertise to the criterion. Factual, legal, medical, security, linguistic, accessibility, or other specialist judgments can require qualified domain evaluators, while usability/preference questions can require representative users rather than specialists.
- Define the rubric and judgment unit explicitly. Criteria such as factuality, relevance, completeness, usability, style, safety, or preference should not be collapsed into a vague `better` judgment unless the evaluation question intentionally measures holistic preference.
- Explain common elicitation forms such as pointwise rating, pairwise comparison, ranking, categorical labeling, error marking, critique, task execution, and interview/qualitative observation. No one format is universally more valid or reliable.
- Define what context evaluators receive: prompts/inputs, candidate outputs, references/evidence, conversation history, tool traces, source documents, model identity, and other information. Missing or asymmetric evidence can materially change judgments.
- Use randomization, counterbalancing, and blinding where relevant to measure or reduce presentation-order, model-identity, anchoring, or expectation effects. Blindness is not always possible or desirable, but visibility of identity/context must be part of the protocol.
- Explain evaluator instructions, examples, training/calibration, qualification checks, and pilot studies as tools for improving consistency and identifying ambiguous rubrics; they do not guarantee validity or erase legitimate evaluator disagreement.
- Measure agreement/reliability when repeated judgments are intended to be interchangeable, while distinguishing agreement from validity. Low agreement can reveal poor instructions, insufficient expertise, heterogeneous preferences, or genuinely subjective/underspecified criteria rather than simply `bad annotators`.
- Preserve disagreement and uncertainty when they are substantively meaningful. Majority vote or mean scores can hide polarized preferences, subgroup effects, uncertainty, or multiple acceptable interpretations.
- Define aggregation/adjudication rules before interpreting results where possible. Majority vote, pairwise win rates, weighted expert judgments, consensus meetings, adjudication, and statistical models encode different assumptions and are not universal substitutes for one another.
- Explain sampling and workload effects. Evaluator fatigue, long contexts, repetitive tasks, time pressure, compensation/incentives, and interface design can affect attention and judgment quality; evaluation design should monitor the conditions relevant to the conclusion.
- Where human subjects or sensitive data are involved, follow applicable consent, welfare, compensation, privacy, data-protection, institutional, legal, and ethical requirements; detailed governance obligations remain with their applicable governance/trustworthy-AI owners.
- Distinguish human preference from factual correctness or safety. People can prefer fluent, confident, familiar, shorter/longer, or stylistically appealing outputs that are incorrect or unsafe, so preference judgments should not silently stand in for properties they were not designed to measure.
- Keep concrete evaluator identities/pools, demographics, annotation tasks/interfaces, compensation rates, rubrics, qualification tests, calibration sets, raw judgments, adjudications, result statistics, and study-specific approvals with their applicable project/evidence/governance owners.
- Use the canonical entity references as research inputs for human-subject relevance/protection and standardized/reproducible human-evaluation boundaries when reader-facing rendering is activated.

## Validation

- Human judgments are not described as objective ground truth by definition.
- Evaluator population/expertise is matched to the evaluation question rather than assumed representative from convenience sampling.
- Rubric, judgment unit, context shown, ordering/blinding, and aggregation assumptions are explicit where material.
- Inter-rater agreement is distinguished from measurement validity and legitimate disagreement is not automatically discarded.
- Human preference is not silently substituted for factuality, safety, or another property without a matching protocol.
- Concrete annotator pools, compensation, interfaces, approvals, raw judgments, and evaluation results remain outside the reusable human-evaluation owner.
