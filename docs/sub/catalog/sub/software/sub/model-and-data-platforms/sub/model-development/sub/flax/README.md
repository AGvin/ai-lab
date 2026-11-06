# Flax

An open-source Python neural-network library for building and training models with [JAX](../jax/).

## Relations

- Produced by: [Google DeepMind](../../../../../../../producers/sub/g/sub/google-deepmind/)


## Capabilities and software boundary

Flax supplies neural-network modules, model state and training abstractions. Its current documentation recommends NNX for new users while retaining Linen; both are APIs of the same Flax package. Pretrained-model examples do not change its role as model-development software.

[Optax](../optax/) supplies a separate gradient-processing and optimizer layer. [Orbax Checkpoint](../orbax-checkpoint/) supplies separate checkpoint persistence and recovery.

## Compatibility, evidence and operations

The official repository identifies a dedicated Google DeepMind maintenance team and states that Flax is not an official Google product. Collaboration with JAX does not imply governance by the JAX core team.

Check the installed Flax and JAX releases when choosing NNX or Linen APIs, handling model state and randomness, or restoring serialized state. The Flax team recommends external Orbax for checkpointing; deprecation of the old `flax.training.checkpoints` utility does not mean that Linen itself is deprecated.

## Official resources

- [Flax documentation](https://flax.readthedocs.io/en/latest/)
- [Flax repository and maintenance attribution](https://github.com/google/flax)
- [Checkpointing guide](https://flax.readthedocs.io/en/latest/guides/checkpointing.html)
- [JAX ecosystem governance boundary](https://docs.jax.dev/en/latest/about.html)
