# Agent Runtime on Gemini Enterprise Agent Platform

**Agent Runtime on Gemini Enterprise Agent Platform**, formerly **Vertex AI Agent Engine**, is Google Cloud's managed infrastructure for deploying, scaling, running and monitoring production AI agents. Google's official name-change table maps the prior Agent Engine name to the current Agent Runtime name; it is the same canonical service identity. [Official name changes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes).

## Runtime and deployment boundary

Agent Runtime provides a managed agent execution boundary and integrates with production facilities such as sessions, memory, code execution, monitoring, evaluation and frameworks. Some related features have independent preview or availability states. The original Agent Engine service became generally available on **March 4, 2025**; this does not mean all its optional subfeatures are generally available.

The broader Gemini Enterprise Agent Platform, Google ADK and Agents CLI, Agent Registry, Gemini model families and third-party frameworks remain separate products or building blocks. A framework integrated into the runtime does not become Google-owned model or software identity.

## Operational and security boundaries

Check current agent deployment configuration, project/service-account/IAM access, VPC/network policies, data residency, CMEK feature restrictions, quota, supported frameworks/models, sessions, memory persistence, logging, pricing and lifecycle before using production data. A managed runtime alone does not establish complete independent isolation or governance certification. [Agent Platform scaling documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale).

## Relations

- Produced by [Google Cloud](../../../../../producers/sub/g/sub/google-cloud/).

## Official resources

- [Agent Runtime / platform scale](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale)
- [Current/previous Vertex AI product names](https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes)
- [Vertex AI release notes](https://cloud.google.com/vertex-ai/generative-ai/docs/release-notes)
