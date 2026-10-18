# GPT-5.6 Luna

GPT-5.6 Luna is the cost-sensitive high-volume hosted model in the GPT-5.6 series.

## Model series

- [GPT-5.6](../../../..)

## Model profile

- Model ID: `gpt-5.6-luna`
- Input: text and images
- Output: text
- Context window: 1,050,000 tokens
- Maximum output: 128,000 tokens
- Knowledge cutoff: February 16, 2026
- Reasoning-token support: documented
- Fine-tuning: not supported

OpenAI positions Luna for cost-sensitive, high-volume workloads. That positioning is provider guidance rather than independent AI Lab quality evidence.

## Hosted capabilities

Current provider documentation lists streaming, function calling, structured outputs, web search, file search, code interpreter, hosted shell, apply patch, computer use, MCP, and tool search among supported hosted capabilities. Feature state can evolve and is not an architectural property of downloadable weights.

The current model page does not publish downloadable Luna weights or a local hardware profile. No VRAM requirement is inferred from the hosted model identity.

The current model reference also lists the image-generation tool in Responses. Tool support is a hosted capability.

## Scope boundary

This page owns Luna's model identity and source-backed current model/API profile. Pricing, rate limits, regional availability, tool charges, caching rules, low-cost routing recommendations, cross-tier comparisons, and workload-specific acceptance conclusions belong to product/service, selection, deployment/workflow, or evidence documentation.

## Operating boundaries

The August 2026 ChatGPT update is distinguished from earlier releases in the system card. Its evaluation results and deployment behavior should not be assigned automatically to every use of this model name [GPT-5.6 August system card](https://deploymentsafety.openai.com/gpt-5-6-august-update).

Reasoning effort and tool availability are API configuration. Validate tool arguments and application permissions before executing a model-proposed action [Latest-model guide](https://developers.openai.com/api/docs/guides/latest-model).

## Relations

- Member of: [GPT-5.6](../../../../README.md).

## Official resources

- [GPT-5.6 Luna model page](https://developers.openai.com/api/docs/models/gpt-5.6-luna)
- [GPT-5.6 launch](https://openai.com/index/gpt-5-6/)
