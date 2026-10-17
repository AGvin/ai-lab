# Documentation Requirements

## Requirements

- Identify Google Agent Development Kit (ADK) as the canonical software profile for Google's open-source agent-development framework represented at this path.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Describe ADK as a framework for building tool-using and multi-agent applications; keep evaluation, deployment, language support, protocol support, and Google Cloud integration details source-backed when expanded.
- Include the official ADK documentation reference.
- Preserve ADK as one Google framework-family identity across separately maintained Python (`google/adk-python`), TypeScript (`google/adk-js`), Go (`google/adk-go`), and Java (`google/adk-java`) upstreams; verify each language's package versions and feature parity separately rather than treating them as interchangeable APIs.
- Distinguish open-source self-managed framework/runtime usage from separately operated Google Cloud Run and Vertex AI Agent Engine deployment services; cloud integration is optional and does not make all ADK use a hosted service.
- Keep the current ADK entry point (`https://adk.dev/`) synchronized with metadata and the reader page. Explain that ADK Web/dev UI is for local development and must not be exposed as a production-facing UI without separately supported deployment/authentication/security controls.

## Validation

- The official resource link matches canonical entity metadata.
- The page does not conflate ADK with the separate Google Agents CLI or a hosted agent service.
- The page contains no temporary-placeholder wording.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
