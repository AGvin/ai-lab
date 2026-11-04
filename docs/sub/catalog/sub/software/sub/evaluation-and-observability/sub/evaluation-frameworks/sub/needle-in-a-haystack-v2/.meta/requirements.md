# Documentation Requirements

## Requirements

- Identify Needle In A Haystack v2 as an installable Python evaluation runner for LLM long-context retrieval and multi-hop information access, not as a hosted inference service, model, dataset, or separately materialized v1 product.
- Pin first-party source commit `021385d68d3202e37893e9d3cd29011c569abe30` and [README](https://github.com/gkamradt/needle-in-a-haystack/blob/021385d68d3202e37893e9d3cd29011c569abe30/README.md), [pyproject.toml](https://github.com/gkamradt/needle-in-a-haystack/blob/021385d68d3202e37893e9d3cd29011c569abe30/pyproject.toml) and [MIT LICENSE](https://github.com/gkamradt/needle-in-a-haystack/blob/021385d68d3202e37893e9d3cd29011c569abe30/LICENSE.txt). The manifest declares `needlehaystack` version `2.0.0` and Python >=3.12; version is a pinned source observation, not proof of latest published package.
- Document the `niah` CLI, a local `niah demo --fake` mode, two-file YAML configuration for real runs, configurable provider adapters, context-length × needle-depth sweeps, JSONL output, reconstruction and incremental/resumable runs.
- Describe built-in single fact, multiple fact, UUID, and UUID-chain tasks. A successfully returned needle or identifier measures only that defined evaluation and does not establish general reasoning quality.
- Separate the runner's MIT license from third-party model provider pricing/terms, bundled or user-supplied texts, prompts/results, model access keys and redistribution rights. The fake demo exercises an in-process fake model and is not a live LLM benchmark.
- Disclose cost and reproducibility: fix exact benchmark configuration, seeds, depth sampling, model/provider/revision, context length, date, sampling parameters, input text rights and prompt privacy before comparing results.
- Do not claim an installed Python environment, actual `niah` execution, paid API calls, model evaluation, verified benchmark outcomes, whole-repository CI or a whole-catalog clean pass.

## Validation

- Official repository, pinned manifest/README and MIT license prove identity, shipped interface and rights.
- Indexed exactly once under Evaluation Frameworks without creating a duplicate long-context benchmark dataset entity.
