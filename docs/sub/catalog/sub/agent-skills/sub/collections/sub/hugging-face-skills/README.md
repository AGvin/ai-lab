# Hugging Face Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Hugging Face Skills is Hugging Face's official Agent Skills collection for Hub operations and AI and ML workflows such as dataset creation, model training, evaluation, and related ecosystem tasks.

## Hosted MCP and cloud deployment boundaries

The pinned [Hugging Face MCP configuration](https://github.com/huggingface/skills/blob/25910b3d0ba31a2ba102f901cdc9e008c278a69c/.mcp.json) points to the hosted `https://huggingface.co/mcp?login` endpoint. Enabling that integration involves external requests and account authorization; it is not an offline-only consequence of copying individual `SKILL.md` files or installing the `hf-cli` instructions. Review the chosen client and which prompts, model/dataset details or account context may be sent externally. Do not print access tokens or assume that installing a skill grants Hub account access.

The original [SageMaker IAM preflight](https://github.com/huggingface/skills/blob/25910b3d0ba31a2ba102f901cdc9e008c278a69c/skills/hf-cloud-sagemaker-iam-preflight/SKILL.md) checks for an existing execution role before any `iam:CreateRole`; a usable trust policy alone does not prove least-privilege permissions. The [endpoint deployment skill](https://github.com/huggingface/skills/blob/25910b3d0ba31a2ba102f901cdc9e008c278a69c/skills/hf-cloud-sagemaker-production-defaults/SKILL.md) can create billable models, endpoints, autoscaling policies and CloudWatch alarms. Request explicit approval of the AWS account, region, role, intended spend and deployment/teardown scope. Its optional request/response capture to S3 is disabled by default and requires a separate data-handling decision. An `InService` endpoint still needs a successful inference smoke test and log review. No hosted MCP session, AWS change or model execution was performed in this review.

## Producer

- [Hugging Face, Inc.](../../../../../producers/sub/h/sub/hugging-face-inc/)

## Collection boundary

Individual skills, including the recommended `hf-cli` bootstrap skill, remain part of the collection unless later selected as independently durable identities. Hugging Face Hub, `huggingface_hub`, CLI software, Spaces, Inference Providers, and model or dataset assets remain separate even when collection skills operate those surfaces.

Exact skill inventory, generated CLI guidance, installation and plugin mechanisms, client compatibility, and CLI or MCP integration are freshness-sensitive.

## Source interpretation

Hugging Face's Apache-2.0 collection covers Hub and ML workflows; hf-cli is the documented bootstrap route and extra workflow skills can be installed on demand. Instructions, CLI/MCP integration, model/dataset assets and cloud jobs are separate. Repository licensing does not clear model/data rights or authorize training, uploads or billable deployments.

[Reviewed original README](https://github.com/huggingface/skills/blob/25910b3d0ba31a2ba102f901cdc9e008c278a69c/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Hugging Face Skills repository](https://github.com/huggingface/skills)
