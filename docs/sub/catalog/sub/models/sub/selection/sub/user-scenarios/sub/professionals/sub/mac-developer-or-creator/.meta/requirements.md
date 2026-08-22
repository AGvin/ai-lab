# Documentation Requirements

## Requirements

- Present this scenario for an Apple-silicon Mac professional using AI for development, writing, design, or media work where unified-memory architecture and native runtime/model support materially affect the route.
- Preserve the legacy compact 16 GB evaluation route with Gemma 4 E2B Instruct, Phi-4 Mini Instruct, or a measured Qwen3 8B artifact; state that unified memory is shared with macOS, applications, context, and multimodal components.
- Preserve the 24–32 GB compact multimodal route with Gemma 4 E4B Instruct or another measured smaller/higher-precision model when multimodal capability is useful.
- Preserve a 32 GB+ Qwen3 14B local text route only as a legacy evaluation hypothesis; require exact artifact, quantization/precision, runtime, context, application load, speed, and memory pressure to be measured.
- Treat all memory-size thresholds as planning examples from the legacy source rather than guaranteed fit or quality tiers. A model fitting in unified memory does not prove useful latency, modality support, context headroom, or accepted-result quality.
- Preserve a hybrid route where private routine tasks stay local and difficult permitted tasks escalate to a managed assistant or API under an explicit data-routing rule.
- Require current native runtime/model/quantization/modality support to be verified before recommending hardware or memory purchases primarily for AI.
- Keep Mac hardware buying, runtime implementation, and deployment architecture outside this scenario; record those facts only when they constrain model selection.
- Compare larger-local versus compact-local versus hosted routes by accepted-result quality, latency, memory pressure, review effort, and total cost rather than assuming more unified memory should always be consumed by a larger model.
- Link named models, runtimes, and hosted services to their canonical catalog owners rather than duplicating profiles.

## Validation

- Unified-memory values are planning context, not guarantees of model fit or performance.
- Current runtime/model support is a prerequisite for hardware-oriented recommendations.
- Hybrid escalation has an explicit data-boundary rule.
- The scenario remains an Apple-silicon professional route rather than a generic creator or generic Mac hardware guide.
