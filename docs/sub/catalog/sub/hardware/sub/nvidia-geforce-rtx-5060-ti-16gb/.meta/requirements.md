# Documentation Requirements

## Requirements

- Document the released **NVIDIA GeForce RTX 5060 Ti 16 GB**, distinct from its 8 GB variant and the non-Ti RTX 5060. NVIDIA announced the two Ti memory configurations on 2025-04-15, with availability from 2025-04-16.
- Source 16 GB GDDR7, a 128-bit bus, 4,608 CUDA cores, 180 W graphics power and 600 W recommended system power to the exact NVIDIA product page. Graphics power is not system power or a multi-card PSU requirement.
- NVIDIA lists CUDA compute capability 12.0, which is not a toolkit version or assurance of runtime compatibility.
- Explain actual model memory requirements, KV-cache/runtime overhead and quantization tradeoffs; separate cards do not automatically pool their VRAM, and NVLink is unsupported.
- NVIDIA's 759 AI TOPS is a vendor peak, not verified LLM throughput. Validate actual drivers, inference engine, precision, host PCIe topology, board cooling, connectors and airflow before a deployment.
- Prices, board variants, availability and support are mutable. Manufacturer identity does not prove full beneficial ownership; no measured performance or ownership clearance is claimed.
- Preserve NVIDIA's reciprocal producer relation and the original NVIDIA product, release and CUDA references.

## Validation

- One exact 16 GB hardware identity, not additional model, software or service identities.
- Both producer directions resolve; all claims remain scoped to first-party sources.
- Final renderer, complete schema/cache/CI and two clean catalog passes remain outstanding.
