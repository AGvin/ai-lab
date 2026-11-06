# Agentic Misalignment Research Framework

The **Agentic Misalignment Research Framework** is an MIT-licensed research tool from the `anthropic-experimental` GitHub organization for controlled, **fictional** experiments on behavior such as agent blackmail and information leakage. Its repository is a *research framework*, not a managed model API, autonomous deployment system or benchmark-result dataset.

## Workflow

The [pinned README](https://github.com/anthropic-experimental/agentic-misalignment/blob/ea0630e1a3eaae7f9f9740fd2703229d3854ccda/README.md) describes generating experiment prompts from YAML configuration; querying explicitly selected model providers; and classifying stored response artifacts into behavioral labels. `scripts/generate_prompts.py`, `scripts/run_experiments.py` and `scripts/classify_results.py` are distinct stages. The [dependencies](https://github.com/anthropic-experimental/agentic-misalignment/blob/ea0630e1a3eaae7f9f9740fd2703229d3854ccda/requirements.txt) include provider clients and support libraries. Supported models and endpoints vary with provider availability and credentials.

## Interpretation, rights and risk

The scenarios are fictional. Their outputs do not establish actual misconduct, universal model safety or real-world incident rates. The classification stage is a project-specific measure, subject to mistakes, confounding and model/version changes. Provider keys, prompt content, generated responses and run logs require restricted handling; use model-provider terms and budgets appropriate to research. The [MIT license](https://github.com/anthropic-experimental/agentic-misalignment/blob/ea0630e1a3eaae7f9f9740fd2703229d3854ccda/LICENSE) covers the project software, not hosted APIs, externally supplied data or published conclusions.

No experiment, API invocation, classifier-accuracy audit, dependency audit or whole-catalog clean pass was run.

## Official source snapshot

- [First-party repository](https://github.com/anthropic-experimental/agentic-misalignment)
- [README.md](https://github.com/anthropic-experimental/agentic-misalignment/blob/ea0630e1a3eaae7f9f9740fd2703229d3854ccda/README.md)
- [requirements.txt](https://github.com/anthropic-experimental/agentic-misalignment/blob/ea0630e1a3eaae7f9f9740fd2703229d3854ccda/requirements.txt)
- [LICENSE](https://github.com/anthropic-experimental/agentic-misalignment/blob/ea0630e1a3eaae7f9f9740fd2703229d3854ccda/LICENSE)
