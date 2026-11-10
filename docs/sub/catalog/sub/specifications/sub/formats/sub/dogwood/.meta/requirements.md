# Documentation Requirements

## Requirements

- Present Dogwood as AWS's released open-source governance/policy language for constraining AI-agent actions, including temporal conditions over prior actions and outcomes.
- Preserve the language/specification boundary separately from agent sandboxes, harnesses, MCP servers, gateways, IAM systems, and generic policy/governance concepts.
- Treat syntax, schema vocabulary, temporal operators, rule semantics, versioning, validation behavior, and implementation details as freshness-sensitive to the current Dogwood language definition.
- Treat Dogwood Local Engine as the current first-party local/reference evaluation implementation of Dogwood policies rather than a separate peer specification: it evaluates request/response event streams and maintains durable temporal history, but another enforcement layer must apply its allow/deny verdicts.
- Keep Strands Box separate and excluded from current stable intake while first-party Strands documentation marks it pre-release/developer preview; Box may embed Dogwood Local Engine without becoming the language itself.
- Preserve the enforcement-boundary caveat: policy evaluation is not equivalent to complete OS isolation, event integrity, credential isolation, or universal AI safety.
- Preserve AWS provenance without implying that downstream Dogwood-compatible implementations are AWS-operated services.

## Validation

- Dogwood remains a policy-language/specification identity rather than a sandbox or hosted governance service.
- Dogwood Local Engine is described as an implementation surface, not a duplicate canonical specification.
- Preview-only Strands Box is not promoted to stable catalog status.

## Scoped original-source qualification — 2026-11-07

- Dogwood is AWS's Apache-2.0 open-source policy language for AI agent tool-action governance, compatible with Cedar-style point-in-time policy and adding temporal conditions over prior action requests and responses. It is a policy/specification identity, not an AI model, an execution sandbox, a hosted AgentCore service or a general compliance certification.
- The first-party Dogwood Local Engine implements policy evaluation using durable ordered event history and returns allow/deny verdicts; it does **not** enforce them. A trusted harness must intercept all tool calls, apply verdicts, and protect event integrity and credentials. Preview Strands Box is not thereby a stable independent service.
- Verified first-party source 1: https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/
- Verified first-party source 2: https://aws.amazon.com/blogs/opensource/introducing-the-dogwood-local-engine-temporal-governance-for-agent-actions/
- Source qualification covers only the existing Dogwood language and its upstream provenance. No policy compiled, engine run, harness tested, safety/authorization certification completed, whole-repository schema/cache/CI/render, clean pass or final gate. Existing reader is absent, uncredited.
