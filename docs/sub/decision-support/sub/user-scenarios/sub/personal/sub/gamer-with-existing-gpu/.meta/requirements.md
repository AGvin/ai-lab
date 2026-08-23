# Documentation Requirements

## Requirements

- Present this scenario for a person who already owns a gaming PC with a useful discrete GPU and wants to evaluate AI without first buying dedicated AI hardware or becoming a server operator.
- Preserve an 8–16 GB GPU only as the legacy starting class for evaluation, not as a guarantee of model fit, context headroom, useful speed, modality support, or accepted-result quality.
- Evaluate compact multimodal local candidates such as Gemma 4 E2B/E4B Instruct and text/coding candidates such as Qwen3 8B or Qwen2.5-Coder 7B Instruct only with the exact artifact, precision/quantization, runtime, context, auxiliary files, display/game/application load, and measured peak memory.
- Present a local API as an optional way to reuse one measured model across applications, while accounting for service exposure, updates, power, availability, and the fact that a desktop used for gaming is not automatically a reliable server.
- Preserve a hybrid route where routine permitted data remains local and harder work escalates to an approved hosted model; require explicit data classification before sending content off-device.
- State explicitly that a model loading in VRAM does not prove useful context, concurrency, latency, or task quality.
- Do not recommend purchasing another GPU until the existing card has been measured on the intended model artifacts, contexts, modalities, and workloads and a real capability/resource gap is demonstrated.
- Keep GPU-buying advice, hardware capacity-class design, runtime selection, and server architecture outside this scenario's ownership; link those owners only when needed as decision constraints.
- Escalate when measured quality, context, modality support, latency, or VRAM headroom is the actual limiting factor and hosted or different local routes have better accepted-result economics.
- Link named models and runtime/software products to their canonical catalog owners instead of duplicating their profiles.

## Validation

- The scenario starts from owned hardware and does not turn into a general GPU purchase guide.
- Nominal VRAM and successful load are not treated as practical fit evidence.
- Hybrid use includes an explicit data-boundary decision.
- A local desktop service is not presented as operationally equivalent to a managed hosted service without accounting for maintenance and availability.
