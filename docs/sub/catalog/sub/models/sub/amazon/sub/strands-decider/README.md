# Strands Decider

Strands Decider is an AWS-published family of trained decision models that answer typed questions over an application state.

## Scope and boundaries

AWS Strands model lineage with published adapters and option-scoring heads, separate from the Strands SDK and inference package. noul, choice and score select or rate supplied alternatives rather than generating free-form answers. Public checkpoints define trained identities; mirrors, seeds and code releases do not. Confidence calibration needs target-traffic evaluation. Qwen vision is optional and not image-trained; the released Gemma deciders are text-only and require the repository runtime with Gemma support. Runtime state is truncated by default; strict-window mode rejects oversize input.

## Decision and operational boundaries

- A question uses `noul` for a yes/no probability, `choice` for alternatives or `score` for an ordered scale. The reported choice confidence is transformed from the option distribution and must not be confused with its raw top probability. [Strands Decider inference and runtime contract](https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md)
- Published names distinguish the base model and recipe release. The Amazon and StrandsAgents copies mirror one identity, and Hobson V21 is a different recipe from v1 rather than an alias. [Strands Decider upstream repository](https://github.com/strands-labs/strands-decider) [Strands Decider model release naming](https://github.com/strands-labs/strands-decider/blob/main/docs/naming.md)
- Thresholds require evaluation on the intended traffic and question wording. The runtime truncates over-window state by default; `--strict-window` rejects it instead. The bundled HTTP server has no authentication and is documented for local experiments. [Strands Decider 2B Hobson V21 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v21) [Strands Decider inference and runtime contract](https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md)
- Gemma releases require the repository code with Gemma support and use only the text decoder. Qwen optional vision retains the base tower without image training; these are different modality boundaries. [Strands Decider upstream repository](https://github.com/strands-labs/strands-decider) [Strands Decider inference and runtime contract](https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md)

## Relations

- Produced by: [`catalog/producers/a/amazon-web-services`](../../../../../producers/sub/a/sub/amazon-web-services/)
- has-member: [`catalog/models/amazon/strands-decider/models/strands-decider-12b-gemma4-v1-2610`](sub/models/sub/strands-decider-12b-gemma4-v1-2610/)
- has-member: [`catalog/models/amazon/strands-decider/models/strands-decider-26b-a4b-gemma4-v1-2610`](sub/models/sub/strands-decider-26b-a4b-gemma4-v1-2610/)
- has-member: [`catalog/models/amazon/strands-decider/models/strands-decider-2b-hobson-v21`](sub/models/sub/strands-decider-2b-hobson-v21/)
- has-member: [`catalog/models/amazon/strands-decider/models/strands-decider-2b-qwen3-5-v1-2610`](sub/models/sub/strands-decider-2b-qwen3-5-v1-2610/)
- has-member: [`catalog/models/amazon/strands-decider/models/strands-decider-e2b-gemma4-v1-2610`](sub/models/sub/strands-decider-e2b-gemma4-v1-2610/)
- has-member: [`catalog/models/amazon/strands-decider/models/strands-decider-e4b-gemma4-v1-2610`](sub/models/sub/strands-decider-e4b-gemma4-v1-2610/)

## Official resources

- <https://github.com/strands-labs/strands-decider>
- <https://aws.amazon.com/blogs/machine-learning/icymi-what-landed-for-ai-builders-in-september-2026/>
- <https://github.com/strands-labs/strands-decider/blob/main/docs/naming.md>
- <https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md>
- <https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v21>

## Child pages

- [Models](./sub/models/)
