# Magistral Small 2509

Magistral Small 2509 is the open reasoning checkpoint named Magistral Small 1.2 in Mistral’s September 2025 API documentation.

## Translations

- English

## Relations

- Family: [Magistral](../../../../)

## Model profile

The Apache 2.0 checkpoint accepts text and images and supports 128K tokens; Mistral warns that performance may degrade beyond 40K. [Magistral Small 2509 weights and prompting](https://huggingface.co/mistralai/Magistral-Small-2509)

The hosted `magistral-small-2509` release is deprecated from April 30, 2026, with Mistral Small 4 identified for new integrations. [Magistral Small 1.2 lifecycle and model card](https://docs.mistral.ai/models/magistral-small-1-2-25-09)

## Operational boundaries

Use the release’s reasoning system prompt and tokenizer support for the special `[THINK]` / `[/THINK]` tokens. Plain text that resembles these tokens is not equivalent to their encoded control tokens. [Magistral Small 2509 weights and prompting](https://huggingface.co/mistralai/Magistral-Small-2509)

Reasoning traces are generated content, not proof that an answer is correct; downstream verification remains separate from the model’s reasoning format.

## Official resources

- [Magistral Small 2509 weights and prompting](https://huggingface.co/mistralai/Magistral-Small-2509)
- [Magistral Small 1.2 lifecycle and model card](https://docs.mistral.ai/models/magistral-small-1-2-25-09)
