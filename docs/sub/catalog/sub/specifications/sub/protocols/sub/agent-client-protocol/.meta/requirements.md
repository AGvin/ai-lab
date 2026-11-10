# Documentation Requirements

## Requirements

- Identify Agent Client Protocol (ACP) as the JSON-RPC-based interoperability protocol between code editors or other clients and coding agents.
- Preserve the lifecycle boundary between the stable version-1 wire protocol and explicitly experimental later protocol work when current sources distinguish them.
- Keep ACP distinct from Model Context Protocol, Agent2Agent Protocol, AG-UI, and unrelated commerce protocols that also use the acronym ACP.
- Describe project governance from current upstream evidence without attributing protocol production or ownership solely to Zed, JetBrains, or another participant unless governance changes establish that fact.
- Keep implementation-specific client or agent capabilities with their product owners rather than treating them as protocol guarantees.

## Validation

- The page documents protocol semantics rather than one editor or coding-agent implementation.
- Experimental protocol work is not presented as stable wire-protocol behavior.
- The ACP acronym is disambiguated from unrelated protocols.

## Scoped original-source qualification — 2026-11-07

- Agent Client Protocol is the official editor/IDE-to-coding-agent interoperability contract. The first-party website currently identifies v1 as latest stable and v2 as Draft; local agents may use JSON-RPC over stdio, while remote agents can use supported remote transports.
- The protocol does not make editor privileges, filesystem writes, approvals, prompts, agent model performance, or remote hosting equivalent across clients. Do not conflate this ACP with the unrelated Agentic Commerce Protocol, MCP, A2A, or a specific IDE/agent vendor's implementation.
- Verified primary source 1: https://agentclientprotocol.com/get-started/introduction
- Verified primary source 2: https://agentclientprotocol.com/governance/
- Verified primary source 3: https://github.com/agentclientprotocol/agent-client-protocol
- Existing protocol/source identity accepted only; no editor compatibility, agent session, permission or protocol-v2 runtime test, independent security/legal audit, root-wide schema/cache/CI/render, clean pass or final gate.
