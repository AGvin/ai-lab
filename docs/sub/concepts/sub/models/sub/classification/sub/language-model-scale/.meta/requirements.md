# Documentation Requirements

## Requirements

- Use the reader-facing title `Small and Large Language Models (SLMs and LLMs)`.
- Define SLM and LLM as practical relative scale descriptors for language models, not as universal permanent parameter-count classes.
- Explain that published and operational usages apply materially different numerical ranges; when a parameter threshold or range is mentioned, attribute it to its source and comparison context instead of presenting it as universal.
- Treat parameter count as useful scale metadata but not as a complete predictor of model capability, runtime memory, throughput, latency, cost, or deployment feasibility.
- Explain that smaller models commonly reduce compute and memory demand and can improve deployment flexibility, while larger models commonly offer greater capacity; present these as tendencies whose practical consequences still require measurement for the actual model and workload.
- Keep scale independent from deployment location, quantization or numerical precision, dense versus sparse/MoE architecture, modality, frontier status, ecosystem maturity, access/licensing, and hardware fit.
- Explain that quantization changes numerical representation and resource requirements but does not by itself reclassify the underlying model from LLM to SLM.
- When MoE scale is discussed, distinguish total parameters from active parameters where relevant and avoid comparing one number naively with dense-model parameter counts.
- Keep detailed model-selection procedures, escalation/cascade strategies, portfolios, and scenario recommendations with their decision or learning owners rather than treating them as scale-concept facts.
- Use the canonical entity references as research inputs for numerical-range and comparative claims when reader-facing rendering is activated.

## Validation

- The page does not define one universal SLM/LLM parameter threshold.
- The page does not equate `SLM` with local execution or `LLM` with provider-hosted execution.
- The page does not equate a quantized LLM with an SLM solely because its artifact or runtime footprint is smaller.
- The page does not present scale label or parameter count alone as proof of task quality, safety, cost efficiency, or practical hardware fit.
- Comparative resource or capability statements are qualified as tendencies or supported by an explicitly stated evidence context.
- Model-selection workflow and pedagogical escalation guidance from the legacy source are not duplicated into this canonical concept owner.
