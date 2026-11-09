# Documentation Requirements

## Requirements

- Identify Hugging Face Skills as Hugging Face's official Agent Skills collection for Hub operations and AI/ML workflows such as dataset creation, model training, evaluation, cloud/model deployment, and related ecosystem tasks.
- Preserve the collection boundary rather than materializing every skill as an independent catalog identity; `hf-cli` is the recommended bootstrap skill but remains part of the collection unless later selected independently.
- Keep Hugging Face Hub, `huggingface_hub`, CLI software, Spaces, Inference Providers, and model/dataset assets separate from the skill collection even when skills operate those surfaces.
- Preserve the current expansion into cloud deployment as collection-level capability: current upstream/AWS evidence includes six composable `hf-cloud-*` skills for planning and deploying Hugging Face models to Amazon SageMaker AI with AWS-context discovery, Python environment setup, IAM preflight, serving-image selection, and production defaults.
- Keep Amazon SageMaker AI, AWS IAM, ECR/DLC, CloudWatch, Bedrock Custom Model Import, serving runtimes, and model assets with their own canonical owners; the skills encode deployment procedures but do not own those services/products.
- Treat exact skill inventory, generated CLI guidance, installation/plugin mechanisms, client compatibility, cloud-provider coverage, deployment targets, pinned revisions, and CLI/MCP integration as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Source-specific hosted access and AWS execution boundaries

- Distinguish independent skill installation from the [pinned Cursor/MCP manifest](https://github.com/huggingface/skills/blob/25910b3d0ba31a2ba102f901cdc9e008c278a69c/.mcp.json), which configures the remotely hosted `https://huggingface.co/mcp?login` service. Authentication and queries cross a network/data boundary; do not imply that the whole collection is offline or installed with Hub credentials.
- For `hf-cloud-sagemaker-iam-preflight`, prefer inspecting and validating existing AWS execution roles, verify scoped policies, and require authorization before creating IAM roles or changing permissions. SSO failures do not justify bypassing authorization.
- For `hf-cloud-sagemaker-production-defaults`, preserve account, region, role, ongoing cost and teardown boundaries for SageMaker models/endpoints/autoscaling/alarms. Optional S3 request/response capture is off by default, not implicit consent for collecting input data; an `InService` status alone is not a successful inference check.
- Use pinned [IAM source](https://github.com/huggingface/skills/blob/25910b3d0ba31a2ba102f901cdc9e008c278a69c/skills/hf-cloud-sagemaker-iam-preflight/SKILL.md) and [deployment source](https://github.com/huggingface/skills/blob/25910b3d0ba31a2ba102f901cdc9e008c278a69c/skills/hf-cloud-sagemaker-production-defaults/SKILL.md); these are scoped source assertions, not live billing, permission, retention or runtime verification.

## Validation

- Producer provenance resolves to Hugging Face, Inc.
- The collection is not conflated with the Hub service or CLI itself.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
