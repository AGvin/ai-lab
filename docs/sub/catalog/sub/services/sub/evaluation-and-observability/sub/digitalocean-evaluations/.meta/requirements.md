# Documentation Requirements

## Requirements

- Identify DigitalOcean Evaluations as a managed evaluation service covering supported models, Inference Router configurations and agents, distinct from DigitalOcean Inference hosting, standalone open-source test tools, and reusable benchmark datasets.
- Explain two main tested workflows: dataset evaluation of a candidate model/router/agent with repeatable single-turn prompts or imported multi-turn conversations; and simulation of supported agent behavior through generated multi-turn interactions. Scoring, metric/judge selection and comparisons depend on task and configuration.
- Document the provider-operated DigitalOcean Control Panel and published API/doctl interfaces, not an imaginary installable local evaluator. Evaluate only resources and data authorized for the account; do not claim local-only processing or unauthenticated service access.
- Preserve the advisory nature of evaluation output. Review generated responses and relevant error modes manually before production use; metrics, judge models, dataset split, test quality, agent context, simulations, model versions and thresholds all affect results. Avoid safety certification or generalized benchmark ranking from a single run.
- Keep model API service and evaluation service identities separate, with exactly one `produced-by` / `produces` relationship to DigitalOcean. The service's use of hosted models or dataset data does not assign those models' original authorship or content rights to DigitalOcean.
- Warn that submitted evaluation inputs, transcripts, rubrics, expected outputs and logs may contain sensitive or proprietary data. Require permission for uploaded datasets, strong key access, retention and location review, cost/usage controls, and awareness of model-judge/provider data paths.
- Keep availability, agent support, metrics, CLI/API interface names, prices, evaluation storage and retention as mutable first-party facts; if version-sensitive behavior is added, cite the exact published release or last-verified documentation.
- Cite vendor first-party docs; do not claim an actual authenticated evaluation, independent safety audit, full pricing/region verification, repo-wide CI or whole-catalog clean pass.

## Validation

- [Features](https://docs.digitalocean.com/products/evaluations/details/features/) and [Quickstart](https://docs.digitalocean.com/products/evaluations/getting-started/quickstart/) support dataset and simulation scope; [Reference](https://docs.digitalocean.com/products/evaluations/reference/) supports API/doctl access.
- Both the evaluation-and-observability category and producer reader link this canonical service once, with reciprocal entity relations.
- Separate managed evaluation and managed model inference service; third-party datasets/models keep their own provenance and access conditions.
