# Documentation Requirements

## Requirements

- Identify NVIDIA Personal AI Router (PAIR) as installable open-source local model-gateway/routing software for distributing independent inference requests across compatible computers on the same trusted local network.
- Preserve its routing boundary: PAIR exposes Ollama-compatible and OpenAI-compatible proxy endpoints and routes each request to one eligible node based on engine/model availability and workload.
- Explicitly distinguish routing from distributed model execution: PAIR does not pool GPU memory, form a larger logical GPU, shard one model across machines, or split one in-flight request between nodes.
- Keep Ollama and LM Studio as separate inference-runtime identities; PAIR coordinates compatible engines but does not become those engines or own their model catalogs.
- Treat supported operating systems, architectures, engines, pairing/security behavior, installers, release versions, proxy compatibility, scheduling logic, and supported hardware as freshness-sensitive release state.
- Preserve current NVIDIA provenance and Apache-2.0 release identity from first-party repository/releases.
- Keep benchmark/demo timing from NVIDIA launch material as vendor evidence rather than independent AI Lab performance evaluation.

## Validation

- PAIR remains self-managed gateway/routing software rather than a hosted model API or distributed inference runtime.
- NVIDIA provenance resolves bidirectionally.
- The page does not imply memory pooling or model sharding.
- Mutable engine/hardware compatibility remains source-scoped.
