# Documentation Requirements

## Requirements

- Present this scenario for an individual who actively experiments with models, runtimes, modalities, agents, local APIs, quantizations, and hosted alternatives and accepts frequent changes in the stack.
- Preserve the legacy idea of a routine local generalist plus measured specialist or larger routes as experiment hypotheses, not as a requirement to keep one permanent production service running.
- Include Qwen3 14B as a legacy resident-generalist experiment, Gemma 4 E2B/E4B Instruct as compact multimodal experiments, and Qwen3 30B-A3B as a larger sequential experiment only when exact artifact/runtime/resource evidence supports the test.
- Allow temporary cloud GPU or hosted specialist use when a larger model, media workload, or short-lived experiment does not justify dedicated local hardware; account for startup, storage, shutdown, idle billing, and provider/data boundaries.
- Treat experimentation breadth and easy model/runtime switching as primary route values; do not import persistent uptime, backup, remote-access, or service-hardening requirements unless the user's behavior has crossed into the separate `home-lab-owner/` scenario.
- Measure exact model artifacts, context, runtime, memory, latency, task quality, and accepted-result cost rather than selecting experiments from parameter count or popularity alone.
- Include electricity, storage, download/update burden, and operator time in comparisons when local experimentation is frequent enough for those costs to matter.
- Keep permanent infrastructure design, GPU purchasing, and home-lab operations outside this scenario except as constraints that may trigger a move to the dedicated home-lab route.
- Escalate or change route when a recurring specialist workload, persistent service need, privacy/offline requirement, or measured capability/resource gap makes experimentation-only operation inefficient.
- Link models, runtimes, cloud services, and other products to canonical catalog owners rather than duplicating their complete profiles.

## Validation

- The scenario is experimentation-first and remains distinct from persistent home-lab service operation.
- Legacy model examples remain evaluation hypotheses bound to exact artifacts/runtime conditions, not permanent recommendations.
- Temporary cloud capacity includes lifecycle/billing and data-boundary constraints.
- Hardware acquisition and infrastructure architecture are not treated as canonical ownership of this model-selection scenario.
