# Documentation Requirements

## Requirements

- Identify JAX as the open-source Python library for accelerator-oriented array computation and composable program transformations used heavily in large-scale machine learning and scientific computing.
- Preserve its core identity around NumPy-like arrays, automatic differentiation, JIT compilation, vectorization, parallel/sharded computation, and accelerator execution through the modular compiler/runtime stack.
- Keep OpenXLA/XLA, Flax, Optax, Orbax, Pallas, TPU/cloud platforms, and downstream JAX model libraries separate when independently materialized.
- Preserve current upstream wording that JAX is a research project and not an official Google product.
- Treat JAX/jaxlib versions, Python/platform support, accelerator backends, CUDA/ROCm/TPU plugin support, distributed APIs, sharding behavior, numerical semantics, release/deprecation changes, and experimental features as freshness-sensitive.
- Attribute performance/scaling claims to exact JAX release, compiler/runtime, hardware, precision, and workload.

## Validation

- JAX remains the core transformable numerical-computing framework rather than the full surrounding JAX ecosystem.
- Experimental/research status is not rewritten as a Google commercial-product lifecycle.
- Producer provenance resolves to JAX Project.
