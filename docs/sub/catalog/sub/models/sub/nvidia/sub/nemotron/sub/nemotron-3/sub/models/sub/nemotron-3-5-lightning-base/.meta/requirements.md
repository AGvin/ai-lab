# Documentation Requirements

## Requirements

- Identify NVIDIA Nemotron 3.5 Lightning Base as a separately released pretrained checkpoint, not the post-trained Lightning identity.
- Preserve official NVIDIA registry identity and source-specific parameter counts.
- Maintain reciprocal Nemotron 3 series membership and inherited NVIDIA producer provenance.
- Keep quantization, deployment and serving artifacts separate from trained model identity.

## Validation

- Model entity has a first-party registry reference and a member-of relation to Nemotron 3.
- Nemotron 3 has a reciprocal has-member relation.
