# Kimi K3

Kimi K3 is Moonshot AI's separately released, open-weight **native multimodal agentic model**, introduced on **July 16, 2026**. The original announcement distinguished that model release from public release of the complete model weights planned for **July 27, 2026**; the publisher's repository and model card now provide released weights. Kimi K3 is a concrete Kimi-family model, not a model series, hosted service, API alias or quantization variant.

## Architecture and published weights

Moonshot AI reports a sparse mixture-of-experts architecture with **2.8 trillion total parameters** and **104 billion activated parameters** per token, a **1,048,576-token context window**, Kimi Delta Attention (KDA), Gated Multi-Head Latent Attention (Gated MLA), attention residuals and sparse expert routing. The publisher documents native vision/image understanding and describes video and long-horizon agentic workflows. The released distribution uses quantization-aware training with **MXFP4 weight** and **MXFP8 activation** formats. Total-versus-active counts and format names do **not** determine storage footprint, memory residency, serving compatibility, throughput or suitability for local hardware.

## License, deployment and evidence boundaries

Published weights use the **custom Kimi K3 License**, not MIT, Apache-2.0 or an unrestricted open-source license. Its exact terms are authoritative. In particular, commercial Model-as-a-Service businesses whose combined affiliate revenue exceeds **US$20 million in any consecutive 12 months** must secure a separate license before commercial use. For covered commercial products or services with **over 100 million monthly active users** or **over US$20 million in monthly revenue**, prominent Kimi K3 branding is required. The license states exceptions for internal use and access through official Moonshot products or certified inference partners. Verify how those provisions apply to the specific use case against the current license, rather than assuming general redistribution or hosting rights.

Moonshot AI's coding, reasoning, agentic, multimodal and tool-use benchmarks are **producer-reported**, not independently reproduced here. Kimi.com, Kimi Work, Kimi Code, Kimi API and third-party inference providers are separate access and execution surfaces; their pricing, quotas, capacity, availability, inference controls and data-handling terms are mutable. Do not infer hardware fit or permanent access from benchmark scores, active parameters, or a particular provider's hosted deployment.

## Translations

- English

## Relations

- Member of: [`catalog/models/moonshot-ai/kimi`](../../../../)

## Official resources

- [Official Kimi K3 repository](https://github.com/MoonshotAI/Kimi-K3)
- [Official Kimi K3 License](https://github.com/MoonshotAI/Kimi-K3/blob/main/LICENSE)
- <https://huggingface.co/moonshotai/Kimi-K3>
- <https://www.kimi.com/blog/kimi-k3>
- <https://www.kimi.com/help/kimi-api/api-model-selection>
