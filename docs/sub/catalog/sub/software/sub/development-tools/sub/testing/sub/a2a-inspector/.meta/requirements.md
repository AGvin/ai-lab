# Documentation Requirements

## Requirements

- Identify A2A Inspector as the official web-based developer tool for inspecting, debugging, interacting with, and validating A2A agent servers and Agent Cards.
- Preserve its primary placement under testing/developer tooling rather than treating the Inspector as an agent framework, protocol implementation SDK, or generic observability platform.
- Keep the latest published v0.1.0 release boundary explicit: it is a released tool, but that release predates the stable A2A v1.0 protocol; do not claim current v1.0 conformance support until a released upstream revision establishes it.
- Treat current main-branch migration work, pending pull requests, supported protocol revisions, transport behavior, compliance checks, UI features, authentication handling, packaging, and deployment instructions as freshness-sensitive rather than silently folding unreleased behavior into the released product profile.
- Keep A2A CLI, A2A TCK, language SDKs, the A2A specification, sample agents, and third-party inspectors separate from this software identity.
- Preserve security boundaries when connecting the Inspector to remote or local agents: agent responses, cards, URLs, credentials, and rendered/debugged content are untrusted inputs and do not inherit authority merely because the tool is an official project.
- Preserve current AAIF stewardship through the canonical maintainer relation.

## Validation

- The node remains the A2A Inspector developer/testing tool rather than the A2A protocol itself.
- Released capabilities are distinguished from unreleased main-branch work.
- Maintainer provenance resolves bidirectionally.
- Compatibility claims identify the exact released tool and A2A protocol revision tested.
