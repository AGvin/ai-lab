# Orbax Checkpoint

An open-source Python checkpointing library for saving and restoring [JAX](../jax/) model and training state. Install the `orbax-checkpoint` package and use the `orbax.checkpoint` namespace.

## Relations

- Produced by: [Google](../../../../../../../producers/sub/g/sub/google/)


## Capabilities and software boundary

Orbax Checkpoint supports training-state persistence and recovery, including distributed arrays, checkpoint scheduling and asynchronous saves. Its role is part of model development; it does not track general source, dataset and experiment provenance.

The shared Orbax repository also contains the separately installed `orbax-export` package for exporting JAX models to TensorFlow SavedModel. That sibling package is outside this checkpoint profile.

## Compatibility, evidence and operations

The checkpoint package metadata identifies Beta development status. Match guidance to the installed release: legacy V0 and V1 interfaces have distinct usage and migration requirements. A published release does not make every latest-documentation API interchangeable.

Wait for asynchronous completion and handle save errors through the selected API before relying on persisted state. Match checkpoint structure and target sharding to the restore workflow. Storage backend, custom handlers, checkpoint layout and cross-topology recovery require compatible configuration; measured performance depends on the workload, hardware and storage.

The official project paper records Google and Google DeepMind contributors. The broader Google producer relation does not assert exclusive authorship or governance by the JAX core team.

## Official resources

- [Orbax documentation](https://orbax.readthedocs.io/en/latest/)
- [Orbax repository](https://github.com/google/orbax)
- [Orbax Checkpoint package](https://pypi.org/project/orbax-checkpoint/)
- [V0 to V1 migration](https://orbax.readthedocs.io/en/latest/guides/checkpoint/v1/orbax_v0_to_v1_migration.html)
- [Asynchronous checkpointing](https://orbax.readthedocs.io/en/latest/guides/checkpoint/v1/async_checkpointing.html)
- [Orbax project paper](https://arxiv.org/html/2605.23066v1)
