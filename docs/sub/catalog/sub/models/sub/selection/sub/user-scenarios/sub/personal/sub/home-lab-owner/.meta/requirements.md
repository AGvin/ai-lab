# Documentation Requirements

## Requirements

- Present this scenario for an individual who operates or plans persistent AI services on a workstation, server, NAS-adjacent host, SBC, or other home-lab infrastructure and accepts ongoing systems administration.
- Preserve the legacy resident-generalist Qwen3 14B route as an evaluation hypothesis; require exact artifact, quantization/precision, runtime, context, concurrency, auxiliary components, and peak-memory evidence before treating it as resident-fit.
- Preserve a compact multimodal lane with Gemma 4 E2B/E4B Instruct when bounded image/document/UI/short-audio tasks justify a separate service; account for the memory and operational cost of multiple resident services.
- Preserve Qwen3 30B-A3B as a larger sequential route only when measured switching/unloading/reloading provides accepted-result value that justifies recovery overhead.
- Preserve temporary cloud GPU or hosted specialist escalation for workloads too large, occasional, or operationally unsuitable for permanent local residency.
- Treat uptime, remote access, service exposure, authentication, updates, storage, backups, observability, power, heat/noise, failure recovery, and operator time as material route constraints.
- Distinguish this scenario from `ai-enthusiast/`: persistent reliable service operation is primary here; experimentation breadth/frequent stack switching is primary there.
- State that self-hosting is not automatically cheaper than managed access after electricity, storage, administration, failures, upgrades, and operator time.
- Keep detailed network/security architecture, hardware purchasing, orchestration, and service scheduling in their canonical owners; record them here only as constraints that materially affect model selection.
- Include a **Hardware-specific model selection** continuation that links the complete `../../../hardware/` journey, `../../../hardware/sub/servers/` for dedicated inference hosts, and `../../../hardware/sub/single-board/` when SBCs are part of the lab. Do not duplicate platform-specific runtime/model-fit analysis here.
- Escalate/change the portfolio when specialist workloads, concurrency, context, quality ceiling, privacy boundary, power/maintenance cost, or service reliability make the current resident route inefficient.
- Link named models, runtimes, infrastructure software, and hosted services to canonical catalog owners instead of duplicating profiles.

## Validation

- Persistent operational concerns distinguish this from experimentation-first AI enthusiast use.
- Resident-fit claims are bound to exact artifact/runtime/context/concurrency evidence rather than nominal memory or active-parameter counts.
- Total cost includes operator/infrastructure costs.
- Hardware-specific fit is delegated to sibling hardware selection.
- Cloud specialist escalation includes lifecycle, billing, and data-boundary considerations.
