# Documentation Requirements

## Requirements

- Identify Kilo Code as the open-source AI coding product represented by its current local editor/CLI surfaces and hosted Cloud Agent surface.
- Preserve the execution-boundary distinction documented by Kilo: local coding runs in the Kilo CLI runtime on the developer machine, while Cloud Agent runs repository work in hosted cloud execution environments.
- Distinguish hosted Cloud Agent execution from Remote Connections, where the cloud UI controls a local CLI session and the user's machine still performs the compute.
- Preserve the product's editor, CLI, MCP, model/provider, gateway, SDK, automation, and cloud coding surfaces at a stable high level without turning the profile into setup or billing guidance.
- Preserve useful legacy operational boundaries around provider/gateway credentials, repository/filesystem permissions, custom rules/agents/skills, MCP server scopes, browser/terminal execution, remote-control account security, hosted-agent execution, generated diffs, and human review before commit/push/merge.
- Keep model-provider, credit, beta, retention, organization-policy, cloud-trigger, source-availability, acquisition, and other mutable product/service claims source-backed and time-scoped when expanded.
- Include current official Kilo site, CLI/Cloud Agent documentation, and repository references.
- Preserve Kilo Code Inc. as the canonical producer through the `produced-by` relation.

## Validation

- The page does not describe Cloud Agent as merely a remote UI for a local process; hosted Cloud Agent execution is distinguished from Remote Connections to local CLI sessions.
- The page does not imply that local editor or CLI coding runs inside Kilo Cloud.
- Remote Connections explicitly preserve the local-compute trust boundary and account-access risk.
- Official resource links match canonical entity metadata.
