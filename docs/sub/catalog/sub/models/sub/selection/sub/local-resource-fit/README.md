# Local Model Resource Fit

Use local memory capacity as a constraint on an exact model artifact, not as a model-quality ranking or a hardware-selection shortcut.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Decision boundary

This page preserves the model-selection portion of the legacy `local-models-by-vram` guide. It answers whether an exact local model artifact is a credible candidate under a stated VRAM constraint.

Canonical model identities, artifact names, and published artifact sizes belong to [Model Reference](../../../reference/). Task quality, role suitability, and recommendation state belong to the applicable task-selection page. GPU purchasing, hardware capacity taxonomy, sharding topology, runtime choice, resident-service scheduling, and broader deployment architecture remain outside this subtree.

Published model-file size is not peak runtime VRAM. Runtime buffers, KV cache, context length, batching, graph capture, GPU offload, multimodal projectors or encoders, and concurrent services can materially change memory use. A successful load does not prove useful context headroom, target latency, concurrency, or accepted task quality.

## Current planning matrix

The fit labels below preserve bounded planning judgments from the legacy guide. They are not AI Lab measurements and must be replaced or narrowed by exact workload measurements before a material deployment decision.

| VRAM constraint | Exact candidate artifact | Published artifact footprint | Planning fit | Main boundary |
| ---: | --- | ---: | --- | --- |
| 8 GB | [Gemma 4 E2B Instruct](../../../reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e2b-instruct/) official QAT Q4_0 GGUF | 3.35 GB model + 987 MB multimodal projector | Constrained | Long context, multimodal processing, runtime buffers, and other GPU consumers can remove the nominal headroom |
| 12 GB | [Gemma 4 E4B Instruct](../../../reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e4b-instruct/) official QAT Q4_0 GGUF | 5.15 GB model + 992 MB multimodal projector | Comfortable | Exact modality workload and runtime memory still require measurement |
| 12 GB | [Qwen3 8B](../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-8b/) official `Q4_K_M` GGUF | 5.03 GB | Comfortable | Context, batch size, offload, and concurrent services remain unmeasured here |
| 16 GB | [Qwen3 14B](../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-14b/) official `Q4_K_M` GGUF | approximately 9 GB | Comfortable | Fit does not establish coding, reasoning, or other task quality |
| 24 GB | Qwen3 14B official `Q4_K_M` GGUF | approximately 9 GB | Comfortable | Additional headroom may be required for long context or other GPU consumers |
| 24 GB | [Qwen3 30B-A3B](../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-30b-a3b/) official `Q4_K_M` GGUF | approximately 18.6 GB | Constrained | Nominal file-size headroom is limited; do not assume useful context or concurrent residency |
| 32 GB | Qwen3 30B-A3B official `Q4_K_M` GGUF | approximately 18.6 GB | Comfortable | Runtime and workload conditions still determine practical fit |
| 48 GB | Qwen3 30B-A3B official `Q4_K_M` GGUF | approximately 18.6 GB | Comfortable | Extra memory may be used for context or other services, but concurrency is not implied |
| 96 GB | Exact larger or higher-precision artifact selected from workload evidence | Varies | Unknown | Do not promote a model merely because the nominal capacity permits a larger artifact |

## Fit vocabulary

Use deployment-fit labels only for the exact recorded model artifact and conditions:

- **Comfortable** — measured or bounded evidence supports practical memory headroom under the stated assumptions.
- **Constrained** — the candidate may meet the minimum only with explicit compromises or limited nominal headroom.
- **Sequential only** — the candidate is credible only when a conflicting resident model or service is unloaded first; this label does not choose the scheduling architecture.
- **Impractical** — the represented artifact does not fit or misses a material operating threshold under the stated conditions.
- **Unknown** — evidence is insufficient; do not infer fit from parameter count, active MoE parameters, nominal artifact size, or available VRAM alone.

A planning label based only on published artifact footprint is weaker than a measured deployment-fit label and must say so. None of these labels proves a safe context size, production concurrency, throughput, latency, or task acceptance.

## Required evidence for a material fit conclusion

Record the exact conditions that can change the result:

```text
Model, version, and artifact:
Artifact revision and quantization or precision:
Required projectors, encoders, or auxiliary files:
Runtime and version:
Context and KV-cache configuration:
Batch size and concurrency:
GPU offload policy:
Target GPU and available VRAM:
Measured peak per-GPU VRAM:
Measured peak host RAM when relevant:
Load and warm-up behavior:
Latency or throughput requirement when relevant:
Task acceptance result:
Failure or out-of-memory boundary:
Verified:
```

The target GPU may be recorded as an evidence condition, but choosing which GPU to buy or how to design the host belongs to hardware or deployment guidance rather than model selection.

## Selection rules

- Do not select a model solely because its weights appear to fit.
- Include required auxiliary components when estimating a represented multimodal artifact route.
- Prefer measured peak memory under the intended context, batch, offload, and concurrency conditions over nominal artifact size.
- Do not infer multi-GPU fit by summing device VRAM without validating the actual serving strategy.
- Re-evaluate after a material model revision, quantization, runtime, context, batch, offload, modality, or concurrency change.
- Keep task-quality evidence on the relevant task-selection page and compare total accepted-result value rather than treating greater memory use as greater quality.

## Legacy residual outside this node

The legacy `local-models-by-vram` page also contains concrete GPU examples, VRAM capacity-class taxonomy, multi-GPU topology choices, runtime/service-residency implications, and broader deployment planning. Those sections are intentionally not migrated into model selection. The mixed legacy page must remain available during the staged migration until every still-valid non-model residual has another verified canonical owner or an explicitly approved disposition.

## Related pages

- [Model Selection](../..)
- [Model Reference](../../../reference/)
- [Software Development Model Selection](../software-development/)
- [Language and Research Model Selection](../language-and-research/)
- [Agents and Automation Model Selection](../agents-and-automation/)
- [Model Teams](../model-teams/)
