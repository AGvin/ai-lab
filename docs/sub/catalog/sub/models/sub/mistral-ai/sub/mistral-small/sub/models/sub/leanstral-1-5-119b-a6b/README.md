# Leanstral 1.5 119B A6B

Leanstral 1.5 119B A6B is Mistral AI’s Lean 4 proof-engineering checkpoint built as part of the Mistral Small 4 family.

## Translations

- English

## Relations

- Family: [Mistral Small](../../../../)

## Model profile

The Apache 2.0 model has 119B total and 6.5B active parameters. It accepts text and images, with a 256K context; its model card recommends at most 200K tokens. [Leanstral 1.5 weights and family lineage](https://huggingface.co/mistralai/Leanstral-1.5-119B-A6B)

The experimental hosted `labs-leanstral-1-5` release is retired according to Mistral’s September 30, 2026 retirement schedule. The open checkpoint remains a distinct distribution. [Mistral model changelog](https://docs.mistral.ai/resources/changelogs)

## Operational boundaries

The checkpoint produces Lean code and proposed proofs; correctness is established by checking them in the intended Lean environment, including their assumptions. Model-generated reasoning is not the checker.

Keep the upstream `none`/`high` reasoning contract and model-specific serving configuration. A tool harness controls edits and execution; historical Labs setup instructions do not establish present API availability. [Leanstral 1.5 weights and family lineage](https://huggingface.co/mistralai/Leanstral-1.5-119B-A6B)

## Official resources

- [Leanstral 1.5 weights and family lineage](https://huggingface.co/mistralai/Leanstral-1.5-119B-A6B)
- [Leanstral 1.5 model card](https://docs.mistral.ai/models/leanstral-1-5)
- [Mistral model changelog](https://docs.mistral.ai/resources/changelogs)
