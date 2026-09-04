# Documentation Requirements

## Requirements

- Use the reader-facing title `LLM as a Judge` and introduce `LLM-as-a-Judge` / `model-based evaluation` as common related names.
- Define LLM-as-a-judge as an evaluation method in which a language model receives specified evaluation context and produces structured judgments about candidate outputs, system behavior, interactions, or evidence, such as ratings, rankings, pairwise preferences, labels, critiques, error analyses, or rubric-based assessments.
- Distinguish the judge model from the system/candidate being evaluated and from the evaluation design. A judge is one measurement instrument/method component; its score is not the evaluation design, benchmark, metric definition, or final acceptance decision.
- Do not treat judge output as objective ground truth. A language-model judge has model-specific capabilities, training priors, biases, blind spots, prompt sensitivity, stochastic/numerical variation, and context limitations that require external validation for the property being measured.
- Define the judging protocol explicitly: judge model/version, system/developer/judge instructions, rubric/criteria, pointwise versus pairwise/ranking format, candidate ordering, references/evidence shown, sampling/decoding settings, output parser/schema, abstention/tie policy, and aggregation/repetition where relevant.
- Explain pointwise scoring, pairwise comparison, ranking, classification, critique, and reference-based judging as different elicitation forms. Pairwise comparison can reduce some scale-calibration problems but is not universally more valid and can remain sensitive to order, verbosity, and candidate quality gaps.
- Require calibration/meta-evaluation against an appropriate external reference process such as expert/human judgments, known-answer cases, executable checks, controlled perturbations, or another validated measurement. Agreement with another judge model alone is not sufficient evidence of correctness when judges can share correlated biases.
- Distinguish judge reliability/stability from validity. Repeated judgments, lower temperature, deterministic settings, self-consistency, or judge ensembles can reduce variance or expose instability but do not prove that the judge measures the intended property correctly.
- Explicitly account for known bias families where relevant, including position/order bias, verbosity/length preference, style/tone preference, self-enhancement or same-family preference, name/identity effects, reference-answer anchoring, and prompt/rubric sensitivity. Measure or counterbalance them rather than assuming neutrality.
- Treat candidate outputs and retrieved/source content as untrusted judge input. Text being evaluated can contain instructions, quoted prompts, markup, role-like tokens, or adversarial content that attempts to alter the judge's behavior; separate evaluation instructions from candidate content and test injection robustness when the application is exposed to such inputs.
- Distinguish factuality/source-grounded judging from plausibility judging. If the judge lacks authoritative evidence or tools needed to verify a factual claim, a high score can reflect fluency or internal model belief rather than factual correctness; provide references/evidence or use deterministic/external verification where the property requires it.
- Prefer deterministic executable checks for properties that can be verified exactly, such as schema validity, test-suite success, arithmetic constraints, file existence, or policy/rule conformance. Use model judging when semantic or open-ended judgment is actually required, or combine it with exact checks.
- Explain that chain-of-thought/rationale-style judge text is not proof of the causal basis or correctness of the judgment. Rationales can be useful for audit/debugging but can themselves be plausible, inconsistent, or unsupported.
- Explain that judge model/provider updates can change scores, preferences, refusal behavior, context handling, and cost/latency. Pin/version the judge and protocol for reproducible comparisons and revalidate when materially changed.
- Explain that using the same or closely related model family as both generator and judge can introduce correlated preferences or self-enhancement effects. It is not forbidden by definition, but requires calibration suited to the intended conclusion.
- Explain that multiple judges, repeated order swaps, reference checks, or adjudication can strengthen evidence only when their aggregation and independence assumptions are explicit. Majority vote among highly correlated judges is not automatically equivalent to independent human agreement.
- Keep concrete judge model identities/versions, judge prompts/rubrics, reference sets, order-randomization scripts, calibration results, judge scores, provider prices, retry settings, and evaluation runs with their applicable catalog/project/evidence owners.
- Use the canonical entity references as research inputs for judge calibration, position/verbosity/self-enhancement biases, and current prompt-sensitivity/meta-judging limitations when reader-facing rendering is activated.

## Validation

- Judge-model output is not described as self-validating ground truth or an objective score by definition.
- Judge reliability/stability is distinguished from validity against the intended evaluation property.
- Position, verbosity/style, same-family/self-enhancement, prompt sensitivity, and untrusted-content effects are recognized where relevant.
- Exact deterministic properties are not delegated exclusively to an LLM judge without a documented reason.
- Factuality judgments do not assume access to evidence the judge was never provided.
- Judge rationales are not treated as proof of correctness or faithful internal reasoning.
- Concrete judge models, prompts, calibration runs, provider behavior, and result values remain outside the reusable LLM-as-a-judge owner.
