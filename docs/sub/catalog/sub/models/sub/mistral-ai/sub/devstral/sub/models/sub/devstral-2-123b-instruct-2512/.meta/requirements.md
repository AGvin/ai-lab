# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify this checkpoint as the 123B Devstral 2 code-agent model released in December 2025.
- Preserve the upstream modified-MIT license boundary and do not inherit the Apache-2.0 license of Devstral Small 2.
- Keep coding-agent benchmarks, API availability, context, deployment, and Vibe defaults freshness-sensitive.

## Validation

- Membership resolves to Devstral.

## Source-backed profile

- Required reader orientation: Devstral 2 123B Instruct 2512 is Mistral AI’s December 2025 code-agent checkpoint for repository exploration, multi-file editing and software-engineering tools.
- Preserve this model-scoped fact: The released instruct weights are FP8, with 123B parameters and a 256K-token context. [Devstral 2 released weights](https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512)
- Preserve this model-scoped fact: Mistral marks the API release `devstral-2512` deprecated from May 22, 2026 and names Mistral Medium 3.5 as its replacement for new integrations. The released weights remain a separate artifact. [Devstral 2 lifecycle and API model card](https://docs.mistral.ai/models/devstral-2-25-12)

## Operational and interpretation boundaries

- Explain this boundary: The Modified MIT license has an additional commercial boundary: it withholds rights where the company’s or employer’s preceding-month global consolidated revenue exceeds US$20 million. Consult the exact license for its full conditions. [Devstral 2 Modified MIT license](https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512/blob/main/LICENSE)
- Explain this boundary: The model produces tool requests; its agent harness controls filesystem access, command execution and approval. A coding benchmark does not establish that a proposed patch is correct. [Function-calling contract](https://docs.mistral.ai/studio/conversations/function-calling)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
