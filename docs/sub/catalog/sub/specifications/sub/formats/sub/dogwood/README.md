# Dogwood

**Dogwood** is an AWS-released open-source governance and policy language for specifying which actions an AI agent may take, including constraints based on preceding requests, responses and the order or timing of events. It extends Cedar-compatible point-in-time authorization with temporal conditions over a history of tool actions. AWS introduced the language on **August 6, 2026**. [Dogwood language announcement](https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/).

## Policy-language boundary

Dogwood specifies agent-action policies; it is **not** an agent sandbox, a model, a hosted service, or a substitute for a trusted enforcement layer. Its Cedar-compatible authorization rules can express point-in-time conditions, while temporal clauses can capture requirements such as prior approval, request ordering and running limits on actions. Syntax, operators, schema bindings, validation and conformance depend on the current language release and upstream specification.

The Dogwood Local Engine is AWS's local/reference implementation for evaluating policies against an ordered event history and returning permit/deny decisions. **The engine evaluates; a trusted harness must actually intercept and enforce the decision.** Tool-call integrity, credentials, isolation and trusted event recording remain separate security obligations. The preview-only Strands Box product is not itself the Dogwood language or a stable independently released specification. [Dogwood Local Engine description](https://aws.amazon.com/blogs/opensource/introducing-the-dogwood-local-engine-temporal-governance-for-agent-actions/).

## Maturity and scope

AWS released Dogwood as Apache-2.0 open source. Support, runtime complexity, policy language extensions and interoperability must be checked against the specific upstream implementation and language definition; the existence of evaluation logic is not a complete AI-safety, IAM or production-security certification.

## Relations

- Produced by [Amazon Web Services](../../../../../producers/sub/a/sub/amazon-web-services/).

## Official resources

- [Dogwood runtime verification introduction](https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/)
- [Dogwood Local Engine and enforcement boundary](https://aws.amazon.com/blogs/opensource/introducing-the-dogwood-local-engine-temporal-governance-for-agent-actions/)
