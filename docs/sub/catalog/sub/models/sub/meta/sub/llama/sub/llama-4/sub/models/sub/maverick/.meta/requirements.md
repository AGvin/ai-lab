# Documentation Requirements

## Requirements

- Identify Llama 4 Maverick as a released concrete Llama 4 model and preserve its natively multimodal identity.
- Preserve Meta-documented 17B active parameters and 128-expert MoE structure only with explicit source support.
- Keep benchmark comparisons, provider hosting, pricing, runtime throughput, quantization behavior, and workload recommendations outside intrinsic model identity.

## Validation

- Maverick remains distinct from Scout and Behemoth.
- Mutable provider and benchmark state is not generalized into permanent model facts.

## Verified card scope (2026-10-30)

- Meta's official card reports 400B total and 17B active parameters, 1M-token context, text/image input and text/code output. The release uses the custom Llama 4 Community License; access and use remain subject to its terms.
- Source: https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct
- Keep total and active counts separate; neither context capacity nor active count establishes runtime memory or throughput.
