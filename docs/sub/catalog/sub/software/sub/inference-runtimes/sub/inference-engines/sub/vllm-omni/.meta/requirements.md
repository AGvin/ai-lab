# Documentation Requirements

## Requirements

- Identify vLLM-Omni as a separately released open-source inference/serving runtime for any-to-any multimodal and non-autoregressive generation (text, image, audio, video, and action), distinct from original text-centric vLLM.
- Preserve primary ownership under `software/inference-runtimes/inference-engines`, reflecting an independently packaged application/runtime with its own upstream repository, documentation, releases and heterogeneous serving components.
- Distinguish autoregressive token generation, diffusion/DiT, speech/TTS, world-model and robotics/action serving and full-duplex realtime endpoints. Do not imply every model, backend, session mode or GPU class is supported by every stable release.
- Note architectural reuse and release-cadence alignment with vLLM without collapsing vLLM-Omni into the vLLM canonical entity or duplicating ordinary subpackages.
- Keep device/platform support (CUDA, ROCm, XPU, NPU), model inventory, stage pipelines, connector and KV caching protocols, API endpoint compatibility, and streaming/full-duplex behavior freshness-sensitive.
- Qualify performance claims by model, hardware, precision, version, topology, stage pipeline, batch and workload; do not generalize from specific diffusion or speech benchmarks.
- Preserve producer provenance as the vLLM Project upstream community while keeping founding authorship of original vLLM as historical context.

## Validation

- The separately released vLLM-Omni software identity remains distinct from vLLM proper and from a managed model API.
- Model/runtime support and public release claims are version-specific and source-backed.
- `produced-by` and `produces` are reciprocal.
