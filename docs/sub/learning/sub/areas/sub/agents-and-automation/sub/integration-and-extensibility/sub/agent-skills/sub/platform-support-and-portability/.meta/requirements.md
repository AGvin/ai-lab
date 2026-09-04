# Documentation Requirements

## Requirements

- Use the reader-facing title `Agent Skills Platform Support and Portability` and teach how to keep one Agent Skill usable across multiple compatible AI hosts without turning this page into a mutable product support matrix.
- Explain that the portable `SKILL.md` package is the shared core while hosts may differ in discovery roots, installation surfaces, explicit and automatic invocation, permissions, optional metadata, plugin packaging, and available tools.
- Teach a portability workflow: choose one canonical skill source, keep portable behavior in the standard package, isolate host-specific adapters or metadata, distribute from that source rather than maintaining independent manual copies, and record or pin source revisions when reproducibility matters.
- Compare portability strategies such as neutral project roots, reviewed symlinks, installers/copy workflows, client-specific plugin packaging, and generated adapters; explain the synchronization, trust, and maintenance trade-offs of each strategy.
- Teach readers to verify support on every actual target surface rather than assuming parity across desktop, web, CLI, IDE, remote, SDK, or managed-workspace variants of the same product.
- Include a reusable cross-platform verification method covering discovery, positive and negative activation, explicit invocation, supporting-resource resolution, required tools/scripts, denied-permission behavior, approval gates for consequential actions, and disable/removal behavior.
- Keep exact current filesystem paths, commands, plan availability, UI locations, plugin behavior, and host-by-host support facts with their catalog/platform/evidence owners; examples may be used only when current sources and freshness boundaries are explicit.
- Keep exact package-schema and normative compatibility requirements sourced from the formal Agent Skills specification rather than restating them as independent learning truth.
- Preserve the security boundary that portable instructions do not grant equivalent tools, credentials, filesystem/network access, or permissions across hosts.

## Validation

- A reader can design a maintenance and verification strategy for one skill used by several hosts without copying mutable platform facts into the learning corpus.
- The page clearly separates portable skill semantics from host-specific installation, invocation, permission, and plugin behavior.
- The verification guidance tests both expected activation and expected non-activation and covers failure/permission behavior, not only successful discovery.
