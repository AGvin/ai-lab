# Documentation Requirements

## Requirements

- Identify Strands Decider as the AWS/Strands Agents project's released open-source/local decision-model line for fast typed routing, tool selection, classification and scoring, distinct from Amazon Nova models and the Strands Agents software SDK.
- Preserve the difference between the decision-model weights and the `strands-decider` Python CLI/server/training harness. Software APIs and runtimes are not new trained-model variants.
- Distinguish typed choice, noul and score outputs with calibrated confidence from free-form text generation and model-level reasoning capabilities.
- Represent exact public checkpoint revisions only when they have independently released artifacts and meaningful version boundaries; do not create one catalog entity per training run or config alias.
- Treat vendor latency, local hardware comparisons and calibration/accuracy measurements as first-party workload-specific evidence, not general AI Lab performance rankings.
- Retain AWS Strands project attribution while citing current `strands-labs` code stewardship and StrandsAgents official model distribution.

## Validation

- Family and member checkpoint relations resolve bidirectionally.
- AWS/Strands provenance is evidence-backed and distinct from model hosting/runtime tools.
- Decision model cannot be assumed to make perfectly correct or risk-free automated choices.

## Decision and operational boundaries

- Preserve this canonical boundary: AWS Strands model lineage with published adapters and option-scoring heads, separate from the Strands SDK and inference package. noul, choice and score select or rate supplied alternatives rather than generating free-form answers. Public checkpoints define trained identities; mirrors, seeds and code releases do not. Confidence calibration needs target-traffic evaluation. Qwen vision is optional and not image-trained; the released Gemma deciders are text-only and require the repository runtime with Gemma support. Runtime state is truncated by default; strict-window mode rejects oversize input.
- A question uses `noul` for a yes/no probability, `choice` for alternatives or `score` for an ordered scale. The reported choice confidence is transformed from the option distribution and must not be confused with its raw top probability. [Strands Decider inference and runtime contract](https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md)
- Published names distinguish the base model and recipe release. The Amazon and StrandsAgents copies mirror one identity, and Hobson V21 is a different recipe from v1 rather than an alias. [Strands Decider upstream repository](https://github.com/strands-labs/strands-decider) [Strands Decider model release naming](https://github.com/strands-labs/strands-decider/blob/main/docs/naming.md)
- Thresholds require evaluation on the intended traffic and question wording. The runtime truncates over-window state by default; `--strict-window` rejects it instead. The bundled HTTP server has no authentication and is documented for local experiments. [Strands Decider 2B Hobson V21 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v21) [Strands Decider inference and runtime contract](https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md)
- Gemma releases require the repository code with Gemma support and use only the text decoder. Qwen optional vision retains the base tower without image training; these are different modality boundaries. [Strands Decider upstream repository](https://github.com/strands-labs/strands-decider) [Strands Decider inference and runtime contract](https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md)
