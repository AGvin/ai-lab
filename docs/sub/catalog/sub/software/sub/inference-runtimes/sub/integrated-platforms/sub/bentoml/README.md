# BentoML

BentoML is an Apache-2.0 Python library and self-managed platform for packaging, serving, and deploying AI models and applications.

## Deployment and data boundaries

BentoML combines model and service packaging, dependency configuration, API serving, and inference orchestration. Services can run on your own infrastructure, including as Docker containers. BentoCloud provides a separate hosted deployment and management surface; its account, infrastructure, and service terms do not define every self-managed BentoML deployment.

Upstream documents anonymous usage reporting of internal API calls, excluding user code, model data, model names, and stack traces. Disable it with `BENTOML_DO_NOT_TRACK=True` or the `--do-not-track` CLI option. Self-managed inference and usage reporting are separate data paths.

## Producer and project continuity

BentoML joined Modular through a strategic product acquisition announced in February 2026. The originating BentoML publishing identity remains distinct from that corporate affiliation, and the open-source project continues under Apache 2.0.

## Relations

- Produced by: [BentoML](../../../../../../../producers/sub/b/sub/bentoml/)

## Official resources

- [BentoML documentation](https://docs.bentoml.com/en/latest/)
- [BentoML repository and usage-tracking guidance](https://github.com/bentoml/BentoML)
- [BentoML acquisition announcement](https://www.bentoml.com/blog/bentoml-is-joining-modular)
- [Modular acquisition announcement](https://www.modular.com/blog/bentoml-joins-modular)
