# Documentation Requirements

## Requirements

- Identify A2A CLI as the official open-source command-line client maintained by the A2A project for discovering, messaging, streaming with, and managing Agent2Agent-compatible agents.
- Preserve its primary software-tool identity under agentic development tooling: the CLI bridges shells, scripts, CI, tests, coding harnesses, and non-A2A programs to A2A agents rather than defining the A2A protocol itself.
- Preserve the current released v0.3.0 boundary only while supported by current upstream release evidence; treat command grammar, transports, server modes, plugin interfaces, configuration, packaging, and supported protocol revision as freshness-sensitive.
- Keep the bundled A2A Agent Skill and Agent Plugin as distribution/integration surfaces of the CLI unless their lifecycle becomes independently useful enough to justify separate canonical identities.
- Keep A2A SDKs, A2A Inspector, the A2A TCK, protocol specification, remote agents, transport plugins, and community CLIs separate from the canonical A2A CLI identity.
- Preserve security boundaries around credentials, custom headers, remote agent endpoints, executed local programs, files saved from remote FileParts, and third-party transport/command plugins.
- Preserve current AAIF stewardship through the canonical maintainer relation without implying that AAIF authored every historical A2A implementation detail.

## Validation

- The node represents the official A2A CLI software product, not the A2A protocol or one language SDK.
- Version-specific commands and transports remain tied to current released documentation.
- Maintainer provenance resolves bidirectionally.
- Bundled skill/plugin packaging is not duplicated as a peer software identity by default.
