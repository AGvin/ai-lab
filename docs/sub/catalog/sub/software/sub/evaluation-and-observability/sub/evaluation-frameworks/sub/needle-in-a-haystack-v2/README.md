# Needle In A Haystack v2

**Needle In A Haystack** (`needlehaystack`, CLI `niah`) is Greg Kamradt's Python framework for testing long-context information retrieval and multi-hop lookup in large prompts. The [v2 README](https://github.com/gkamradt/needle-in-a-haystack/blob/021385d68d3202e37893e9d3cd29011c569abe30/README.md) describes model-provider-agnostic experiments as a matrix of **context length × needle depth**, with a result row per cell stored as JSONL.

## How it evaluates

V2 includes single-fact, multi-fact, UUID and UUID-chain tasks. Users define a YAML run configuration and model configuration, then use `niah validate` to resolve the config or `niah run` for an actual sweep. `niah demo --fake` uses an in-process fake model to exercise the runner without an API key; it is **not** a real-model validation. The README documents OpenAI, Anthropic and Cohere adapters as of the pinned snapshot, plus reconstruction, retries and resumable runs.

The [pinned Python package manifest](https://github.com/gkamradt/needle-in-a-haystack/blob/021385d68d3202e37893e9d3cd29011c569abe30/pyproject.toml) declares version `2.0.0`, Python >=3.12 and the `niah` CLI. These are declared requirements, not a runtime compatibility test or guarantee that a particular PyPI release remains current.

## Interpreting results and rights

Results vary with exact model revision, prompt templates, context source, needle placement, depth sampling, random seeds, provider APIs and generation settings. JSONL output and logs can contain proprietary source texts, prompts or model responses. Plan API charges, keep provider keys secure, and review rights to any haystack text independently of the code.

The [runner is MIT licensed](https://github.com/gkamradt/needle-in-a-haystack/blob/021385d68d3202e37893e9d3cd29011c569abe30/LICENSE.txt); third-party models, APIs and evaluation data have separate terms. No execution, live-provider benchmark, score verification, dependency audit or whole-catalog clean pass is claimed.

## Official sources

- [Pinned README](https://github.com/gkamradt/needle-in-a-haystack/blob/021385d68d3202e37893e9d3cd29011c569abe30/README.md)
- [Pinned Python manifest](https://github.com/gkamradt/needle-in-a-haystack/blob/021385d68d3202e37893e9d3cd29011c569abe30/pyproject.toml)
- [Pinned MIT LICENSE](https://github.com/gkamradt/needle-in-a-haystack/blob/021385d68d3202e37893e9d3cd29011c569abe30/LICENSE.txt)
- [Repository](https://github.com/gkamradt/needle-in-a-haystack)
