# Documentation Requirements

## Requirements

- Identify NVIDIA Nemotron 3 Ultra Base as a released pretrained checkpoint for further model development, distinct from post-trained Ultra.
- Preserve the official 550B total / 55B active architecture description and source-specific OpenMDW-1.1 terms.
- Distinguish its teacher role in Super VL distillation from Super Base backbone initialization; do not infer shared weights or substitute post-trained Ultra.
- Keep published benchmark results scoped to the base checkpoint and its evaluation configuration; do not transfer post-trained reasoning results.

## Validation

- Series membership resolves reciprocally through Nemotron 3 and producer provenance follows the existing NVIDIA family chain.
- BF16 weights and the NVFP4 pretraining recipe are not separate model identities or runtime validation claims.
