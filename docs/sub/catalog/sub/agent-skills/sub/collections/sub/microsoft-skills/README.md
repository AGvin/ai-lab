# Microsoft Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Microsoft Skills is Microsoft's official `microsoft/skills` repository-backed collection of Agent Skills, plugins, custom-agent assets, templates, and MCP configurations for Azure SDK and Microsoft Foundry development workflows.

## Azure operations, capture and data boundaries

Microsoft's pinned [AKS network-capture skill](https://github.com/microsoft/skills/blob/4f831bbbf54e004507758d8ef2ab420c77bb81b6/.github/plugins/aks-skills/skills/aks-network-capture/SKILL.md) is an **operator-run packet-capture workflow**, not a passive documentation lookup or a capability provided automatically by an Azure MCP connection. It requires an explicitly approved, correctly bound AKS cluster and Kubernetes context, an execution host with `kubectl`, Azure CLI and approved artifact storage, plus a scoped node/pod, duration and BPF filter. Packet captures may include credentials and customer data. Its [authorization instructions](https://github.com/microsoft/skills/blob/4f831bbbf54e004507758d8ef2ab420c77bb81b6/.github/plugins/aks-skills/skills/aks-network-capture/references/capture-authorization.md) require separately reviewing generated traffic, ConfigMaps, capture Jobs, retrieval pods, cleanup and any ephemeral debug-container fallback; a successful Azure MCP metadata query does not authorize these actions. Nothing in this catalog review ran packet captures or accessed an AKS cluster.

Other Microsoft skills can access or change Azure resources and may invoke hosted MCP tools. The pinned [Azure cost-optimization skill](https://github.com/microsoft/skills/blob/4f831bbbf54e004507758d8ef2ab420c77bb81b6/.github/plugins/azure-cost/skills/cost-optimization/SKILL.md) explicitly limits itself to recommendations and forbids deleting, resizing, purchasing or deploying resources as an automatic consequence of an optimization request. For any selected skill, inspect its own instructions, permissions and third-party data flow before execution; first-party provenance, a root MIT license and a repository test badge do not establish tenant authorization, data minimization or runtime safety.

## Producer

- [Microsoft](../../../../../producers/sub/m/sub/microsoft/)

## Collection boundary

The collection keeps its plugin-contained skills and duplicated `.github/skills/` installation surface as implementation details of one identity. MicrosoftDocs Azure Agent Skills remains a separate collection because it has a different repository, docs-derived catalog, ownership workflow, and release/update pipeline. Microsoft Agent Framework, Copilot Studio, Foundry, and VS Code remain separate product identities.

Skill counts, language breakdown, installer commands, plugin manifests, supported agents, repository structure, and work-in-progress or testing status are freshness-sensitive.

## Source interpretation

Microsoft's MIT repository contains Azure SDK/Foundry skill guidance plus plugins, templates and MCP configurations. The README explicitly marks development and testing as work in progress. Keep the distinct MicrosoftDocs Azure collection, hosted Foundry services and language SDKs separate; verify versions and permissions for the selected workflow.

[Reviewed original README](https://github.com/microsoft/skills/blob/4f831bbbf54e004507758d8ef2ab420c77bb81b6/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Microsoft Skills repository](https://github.com/microsoft/skills)
