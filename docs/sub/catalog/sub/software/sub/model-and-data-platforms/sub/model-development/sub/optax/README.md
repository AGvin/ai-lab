# Optax

An independently released, open-source Python library for gradient processing and numerical optimization in [JAX](../jax/).

## Relations

- Produced by: [Google DeepMind](../../../../../../../producers/sub/g/sub/google-deepmind/)


## Capabilities and software boundary

Optax provides composable optimizer transformations, schedules and losses for training parametric models. It operates on training gradients and updates; it is separate from model libraries and tools that quantize or compile model artifacts after training.

The current package developed from the historical `jax.experimental.optix` prototype. The official repository places Optax in the DeepMind JAX Ecosystem. JAX compatibility does not make Optax part of JAX-core governance.

## Compatibility, evidence and operations

A transformation chain runs its transformations in sequence and carries optimizer state. Callers apply the resulting updates to parameters; changing transformation order can change behavior. Individual optimizers are included algorithms, not separate software identities.

Check the installed JAX and Optax releases for supported transformations, state structure, numeric types and experimental APIs. [Flax](../flax/) model construction and [Orbax Checkpoint](../orbax-checkpoint/) persistence remain separate software roles. Training outcomes depend on the model, data and optimizer configuration.

## Official resources

- [Optax documentation](https://optax.readthedocs.io/en/latest/)
- [Optax repository and project provenance](https://github.com/google-deepmind/optax)
- [Getting started and parameter updates](https://optax.readthedocs.io/en/latest/getting_started.html)
- [Combining optimizers](https://optax.readthedocs.io/en/latest/api/combining_optimizers.html)
