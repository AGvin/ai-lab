# Documentation Requirements

## Requirements

- Use the reader-facing title `Eval-Driven Development` and define it as a software-development methodology in which explicit evaluations operationalize expected AI behavior and are created early enough to shape requirements, implementation, iteration, and regression decisions rather than being added only after a feature appears complete.
- Treat an eval as executable evidence for a defined capability, quality, safety, or task outcome. Evals complement rather than replace deterministic unit/integration tests for ordinary code paths.
- Explain the core loop as: define representative tasks and success criteria -> establish a baseline -> change the system -> re-run the controlled evaluation -> inspect failures and trade-offs -> iterate. Do not prescribe one framework, grader, metric, or numerical threshold as universal.
- Explain that useful eval-driven development can intentionally begin with low pass rates when the evaluation specifies a future target capability; the evaluation then makes progress and regressions visible as models, prompts, tools, retrieval, or orchestration change.
- Require evaluation tasks and datasets to represent real product requirements and failure modes rather than only examples the current implementation already handles. Include adversarial/edge cases when risk warrants them.
- Distinguish capability evaluation, regression evaluation, and release/quality gates. The same suite can serve several roles, but a benchmark optimized during development can become less informative if it is repeatedly tuned against without independent validation.
- Preserve evaluation configuration and relevant system identity for comparison: model, prompt/template, tools, retrieval/data state, environment, evaluator/grader, and dataset/version where material.
- Explain human calibration and review where automated graders are subjective or consequential. LLM-as-a-judge and other automated scoring are measurement techniques, not unquestionable ground truth.
- Treat production feedback and newly discovered failures as inputs that can expand the evaluation set, then re-run the broader suite so local fixes do not silently create regressions elsewhere.
- Keep concrete evaluation frameworks, CI products, datasets, prompts, thresholds, model choices, release policies, and project-specific test cases with their applicable catalog/project/evidence owners.
- Use the canonical entity references as research inputs for the methodology's current terminology and operational boundaries when reader-facing rendering is activated.

## Validation

- Eval-driven development is presented as a development methodology, not a synonym for generic benchmarking or one evaluation product.
- Evaluation is introduced before or during implementation rather than only as post-hoc QA.
- Deterministic software tests remain distinct and necessary where applicable.
- Automated graders are not treated as perfect ground truth.
- The methodology does not prescribe one framework, metric, threshold, or vendor.
- Regression coverage includes newly discovered real-world failures without narrowing the suite only to the latest fix.
