# Documentation Requirements

## Requirements

- Use the reader-facing title `AI Extensibility and Packaging`.
- Define the domain as reusable ways to package, discover, load/activate, compose, distribute, update, disable/remove, and govern AI-system extensions or capability bundles without making one vendor's package format universal.
- Keep the domain AI-system-specific. It owns extension/package concepts whose semantics materially involve AI instructions, agents, tools, hooks, model-facing resources, capability discovery/activation, or AI-host integration; it is not a generic package-manager, archive-format, dependency-management, or software-plugin handbook.
- Distinguish extensibility/packaging from `integration-and-interoperability/`. Packaging governs how reusable capability units are represented, installed/discovered, activated, composed, versioned, and distributed; interoperability governs runtime/shared contracts between independently implemented components. A package can contain/configure an interoperability integration without becoming the protocol itself.
- Distinguish extensibility/packaging from `agents-and-autonomy/`. A package or skill can be consumed by a conversational host, IDE assistant, code-review system, or automated agent. The extension's packaging/lifecycle identity does not depend on autonomous-agent planning or coordination.
- Distinguish extensibility/packaging from `agents-and-autonomy/tool-use/`. Tools provide executable operations; extension packages can declare, bundle, configure, or teach use of tools but do not automatically grant tool authority.
- Distinguish extensibility/packaging from workflows/orchestration. A skill/plugin can package a workflow, but the workflow's planning/decomposition/orchestration semantics remain with their applicable concept owners.
- Distinguish abstract extension/package concepts from concrete packages. Individually identifiable Agent Skills, plugins, plugin collections, marketplaces, repositories, publishers, versions, and host implementations remain with applicable catalog owners.
- Distinguish reusable concept semantics from formal package/specification contracts. Exact manifest/schema fields, required filenames/directories, validation rules, version identifiers, conformance requirements, signing/publication formats, and other normative details remain under `catalog/specifications/` when a formal standard/specification owner is selected.
- Treat portability as scoped rather than binary. A package can be portable across hosts at one layer while depending on host-specific tools, permissions, metadata, paths, UI, lifecycle hooks, or execution environments at another; portability claims must state the layer and assumptions.
- Explain discovery/registration as how a host learns which extensions/capabilities are available. Discovery may use filesystem scanning, registries, manifests, marketplaces, configuration, bundled assets, or platform APIs; no one mechanism is universal.
- Explain activation/loading separately from installation. An extension can be installed/present but inactive, disabled, filtered by policy, or loaded only when a task matches. Do not equate package presence with instructions/capabilities entering model context or execution state.
- Explain progressive or selective loading where applicable. AI extension systems can reduce context and attack surface by disclosing compact metadata first and loading full instructions/resources only when relevant; exact strategies remain package/host-specific.
- Explain composition without assuming conflict-free behavior. Multiple extensions can compete for names, activation conditions, hooks, instructions, tools, configuration, or permissions. Hosts need deterministic precedence/namespace/policy behavior appropriate to their package model.
- Treat update as a behavior-changing event, not just file replacement. Changes to instructions, scripts, dependencies, hooks, permissions, remote endpoints, or configuration can materially alter model behavior and side effects and should be reviewable/versioned according to risk.
- Explain disablement/removal separately from revocation/cleanup. Removing package files may not revoke credentials, stop external services, remove generated configuration, clear cached instructions, or undo side effects; concrete hosts/packages own exact uninstall semantics.
- Treat package provenance and source identity as important trust signals without equating them with safety. Repository/publisher/version/signature metadata can improve traceability but cannot prove that instructions/code are benign or appropriate.
- Treat third-party extension content as supply-chain input. Markdown instructions, prompts, manifests, scripts, hooks, binaries, templates, MCP configuration, and remote references can all influence behavior or data flow.
- Apply least privilege to extension capabilities. Installation or activation must not imply blanket filesystem, shell, network, credential, account, tenant-data, or side-effect authority; concrete permissions remain host/system policy.
- Distinguish package trust from runtime input trust. A reviewed extension can still consume malicious external content, and a benign package can invoke an overprivileged tool; security analysis spans both the extension source and the capabilities/data it orchestrates.
- Explain host responsibility. The host/runtime determines what files can be read, what tools execute, which permissions/credentials are available, how user approvals work, and what isolation applies. An extension package describes/requests behavior but does not itself create authority beyond the host's enforcement.
- Explain compatibility as multidimensional. Relevant dimensions can include package/spec version, host/version, supported metadata/extensions, operating system/runtime, tool names, path conventions, permissions, network availability, installed dependencies, and optional components.
- Keep mutable host support matrices, install paths, marketplace status, command syntax, current preview/GA state, plugin manifests, supported metadata fields, and compatibility bugs with concrete platform/catalog/evidence owners.
- Keep tutorials for installing, authoring, publishing, migrating, debugging, or testing extensions with `learning/` or concrete implementation owners rather than the canonical concept domain.
- Keep security advisories, malicious-package incidents, benchmark/evaluation results, trust ratings, recommendations, and package-review findings with their evidence/decision owners.
- Keep `agent-skills/` as the currently selected direct child. Do not infer a generic `plugins/` child or vendor-specific package leaf solely because a product uses the word `plugin`; exact concept identity/owner must be separately selected.
- Render direct-child navigation only from validated materialized selected descendants when reader-facing rendering is activated.
- Use canonical entity references as research inputs for portable Agent Skills and host-specific plugin packaging while preserving their distinct concept/specification/catalog boundaries.

## Validation

- The domain is not used as a catch-all for generic packages, dependency management, APIs, tools, agent workflows, or interoperability protocols.
- Installation, discovery, activation/loading, execution authority, update, and removal remain distinct lifecycle concerns.
- Portable concepts are not described using one vendor's install path, manifest, command syntax, permission model, or marketplace as universal behavior.
- Concrete packages/products and mutable support/version facts remain outside the reusable concept owner.
- Formal package/specification rules remain separate from concept semantics.
- Extension/package presence is not treated as trust, safety, permission, or execution authority by itself.
- `agent-skills/` is the only currently selected direct child; additional extension/package concepts require explicit architecture selection.
