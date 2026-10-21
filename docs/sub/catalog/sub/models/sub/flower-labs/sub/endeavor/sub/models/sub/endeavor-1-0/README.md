# Endeavor 1.0

Endeavor 1.0 is Flower Labs' generalist model release for reasoning, coding assistance and long-horizon agent work, described in the official documentation as a production-ready preview. [Primary source](https://flower.ai/docs/model/endeavor.html)

## Release status and access

The public documentation separates two meanings: production-ready describes the supported Flower-managed and private-deployment paths; preview describes limited access by request. Private deployment is a supported arrangement with Flower, and the reviewed public pages do not provide an open-weight checkpoint for unrestricted download. The model remains the same catalog identity across these operating choices. [Official lifecycle and access contract](https://flower.ai/docs/model/endeavor.html)

## Deployment contract

Before building against an approved deployment, confirm its endpoint and credentials, exact model identifier, request/response formats, tool and streaming support, usage limits, artifact formats, support and applicable terms. Flower states that the complete technical contract is supplied during onboarding and may differ between managed service and private deployment. A public product description of familiar APIs does not specify those details. [Preview interface and support](https://flower.ai/docs/model/endeavor.html) · [Managed and private operation](https://flower.ai/models/endeavor)

## Context and request budget

The supplied Codex client configuration uses 128,000 tokens for context and automatic compaction at 96,000. These are client settings, not universal API caps. Flower separately advertises support up to one million context tokens and asks participants to confirm the supported limit for their deployment. Effective request capacity depends on the route, requested output budget and processing overhead; use the agreed deployment contract when sizing a workflow. [Context window and limits](https://flower.ai/docs/model/endeavor.html)

## Training and evaluation evidence

Flower describes mature capabilities from unnamed leading open-weight models, contributions from its own model program including Lizzy's UK-specialist knowledge, and continual pretraining, posttraining and model integration. The public description does not identify exact learned-weight parents. The dedicated documentation also explains that comparison scores come from different sources and harnesses; the marketing table is not a controlled common-harness evaluation. Assess the intended workflow and deployment instead of inferring a guaranteed ranking. [Training and evaluation methodology](https://flower.ai/docs/model/endeavor.html) · [System-level positioning](https://flower.ai/models/endeavor)

## Operating choice

A managed deployment places model operations with Flower. Private operation places the model in the participant's environment with Flower support and control over upgrade adoption. For agent workflows, confirm the actual tool interfaces and action-authorization boundaries, and evaluate recovery and correctness on the intended tasks before relying on the integration. These operating choices do not establish an unlisted public checkpoint or a universal runtime configuration. [Operation and support](https://flower.ai/docs/model/endeavor.html)

## Relations

- Member of: [Endeavor](../../../../README.md)

## Official resources

- <https://flower.ai/docs/model/endeavor.html>
- <https://flower.ai/models/endeavor>
