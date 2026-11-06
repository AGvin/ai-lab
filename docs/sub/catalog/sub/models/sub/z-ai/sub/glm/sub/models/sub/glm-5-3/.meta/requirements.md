# Documentation Requirements

## Requirements

- Identify GLM-5.3 as a distinct concrete GLM model published by Z.AI and preserve its exact official model-card identity.
- Keep parameter accounting, context, reasoning behavior, licensing, and artifact facts source-backed to the current upstream model card.
- Preserve the shared GLM-5.2 base versus distinct GLM-5.3 post-training; the model-specific GLM-5.3 weight license is not GLM-5.3-Flash's MIT license.
- State source-specific parameter accounting: the official GLM-5 project lists 744B total / 40B active, while Hugging Face repository metadata reports approximately 753B total; do not conflate these measurement scopes or infer tested context capacity.
- Keep provider pricing, hosted aliases, throughput, and leaderboard state outside intrinsic model identity.

## Validation

- GLM-5.3 is not conflated with GLM-5.3-Flash or earlier GLM 5.x releases.
- Distribution artifacts and quantized checkpoints are not silently treated as separate trained models.
