# Documentation Requirements

## Requirements

- Identify Flax as an open-source Python neural-network library for building and training models with JAX, with its own released package and project lifecycle.
- Place Flax under Model Development because it provides model construction, state and training abstractions; pretrained-model examples do not turn it into a model-loader library.
- Keep NNX and Linen as APIs of the same Flax identity. Current upstream recommends NNX for new users while retaining Linen; do not describe Linen itself as deprecated.
- Preserve the official README's dedicated Google DeepMind maintenance-team attribution and its statement that Flax is not an official Google product. Keep collaboration with JAX distinct from JAX-core governance.
- Keep Optax and Orbax checkpointing separate. Upstream recommends external Orbax for checkpoint persistence; the deprecated legacy flax.training.checkpoints utility does not imply deprecation of Linen.
- Treat API migrations, Python/JAX versions, accelerator support, state and randomness semantics, serialization compatibility and training results as release-sensitive.
- Render the standard entity-relations block from validated current-entity relations and include the official documentation, repository and checkpointing guide.

## Validation

- Flax is neither a trained model nor the JAX core framework.
- NNX/Linen and legacy-checkpoint lifecycle statements remain distinct.
- The Google DeepMind producer relation is reciprocal and every rendered destination resolves.
