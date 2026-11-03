# DigitalOcean Evaluations

**DigitalOcean Evaluations** is a managed evaluation service operated by [DigitalOcean](../../../../producers/sub/d/sub/digitalocean/). It measures outcomes for supported foundation models, Inference Router configurations and agents using datasets, selected metrics and simulations. The service is distinct from model hosting through **DigitalOcean Inference** and from an independently installable testing framework.

## Evaluation workflows

**Dataset evaluations** use fixed inputs to compare candidate model, router or supported agent responses. The official service supports single-turn prompts, scoring of existing multi-turn conversations, ground-truth answer comparisons and selectable evaluation metrics. Comparable results require recording the dataset, test conditions, model version, judge rubric, parameters, pass threshold and scoring configuration.

**Agent simulations** assess supported agents through generated multi-turn conversations. Their outputs can help investigate behavior across scenarios, but are not a substitute for manually reviewing outputs, identifying model-judge errors, or testing production controls with representative data.

DigitalOcean provides control-panel, API and `doctl evaluation` interfaces for creating datasets, running evaluations, comparing scores and obtaining results. Exact commands, metrics, supported agent types and account permissions are subject to the currently published [reference](https://docs.digitalocean.com/products/evaluations/reference/). Neither package installation nor access to DigitalOcean's model catalog implies free or unlimited evaluation runs.

## Safe use and interpretation

Evaluate only datasets, prompts, expected answers and conversations you may lawfully send to the provider. Evaluation logs can contain user inputs, private information and model outputs: verify the contract, data-processing region, retention, available access controls and any upstream model-judge paths. Secure credentials and monitor charges. One metric score does not establish general model quality, safety, regulatory compliance, or suitability for production.

No authenticated DigitalOcean evaluation was executed for this catalog entry; documented capabilities and their availability can change.

## Relations

- Produced by: [DigitalOcean](../../../../producers/sub/d/sub/digitalocean/)
- Related model API service: [DigitalOcean Inference](../../model-apis/sub/digitalocean-inference/)

## Official resources

- [DigitalOcean Evaluations](https://docs.digitalocean.com/products/evaluations/)
- [Supported evaluation features](https://docs.digitalocean.com/products/evaluations/details/features/)
- [Getting started and dataset assessments](https://docs.digitalocean.com/products/evaluations/getting-started/quickstart/)
- [Evaluation API and doctl reference](https://docs.digitalocean.com/products/evaluations/reference/)
