# Documentation Requirements

## Requirements

- Identify Alibaba Cloud Skills as Alibaba Cloud's official repository-backed Agent Skills collection for Alibaba Cloud products and related general-purpose workflows.
- Preserve stable versus preview release channels and do not generalize preview skill state to the stable collection.
- Keep Alibaba Cloud services, Qwen models, MCP servers, CLI tools, and individual skill contents separate from the collection identity unless independently materialized.
- Treat exact skill inventory, stable/preview versions, installation commands, supported agents, repository layout, and product coverage as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The collection remains a first-party skill collection rather than a duplicate identity for Alibaba Cloud itself.
- Producer provenance resolves to Alibaba Cloud.

## Scoped original-source qualification — 2026-11-08

- **Alibaba Cloud Skills** is the official `aliyun/alibabacloud-aiops-skills` collection of reusable Agent Skills for Alibaba Cloud product workflows, separate from Alibaba Cloud as producer, the underlying paid cloud services, Qwen models, any MCP servers and individual bundled instructions. Source identity is established by the publisher-operated repository, not by executing or importing its scripts.
- First-party `master` release/install guidance is distinct from the independent `preview` channel. At the pinned review, `master` points to `4a4e9c62d4690949af094d29546ed852309f7ca9`, `preview` to `ab4f573fa248dceab37dde388d7466765616aa1d`. The current README describes `npx skills add aliyun/alibabacloud-aiops-skills`, a preview branch and version-specific tag patterns; actual available skill names, published branches, host support and exact versions may change, and the README's own skills list remains a placeholder.
- **Licensing unresolved — do not copy or redistribute solely on this evidence.** The same first-party `master` README calls the repository **Apache-2.0** in its *License* section but says all skills are governed by **MIT** in its *Legal* section. The reviewed repository root contains `README.md`, `README-CN.md`, and `skills/`, with **no root `LICENSE` file**. Neither conflicting declaration is adopted as a verified universal permission. Require authoritative publisher clarification and per-skill/dependency review before redistribution, reuse in commercial software, or other license-sensitive deployment.
- The official documentation describes local AccessKey/CLI-profile credentials as a **local personal testing** path and recommends ECS RAM role credentials for cloud deployment. Installation and catalog qualification do not grant cloud IAM privileges, authorize infrastructure changes, or certify any workflow. Do not run untrusted skills with broad secret, filesystem, network, billing or production access; pin the inspected source and inspect the exact selected skill.
- Evidence: https://github.com/aliyun/alibabacloud-aiops-skills/tree/4a4e9c62d4690949af094d29546ed852309f7ca9 ; https://github.com/aliyun/alibabacloud-aiops-skills/blob/4a4e9c62d4690949af094d29546ed852309f7ca9/README.md (publisher master and README inspected 2026-11-08). This accepts **one existing collection identity's bounded original-source gate only**, with licensing **explicitly held for legal review**. No new metadata/identity gate, runtime installation, authenticated cloud operation, dependency/license clearance, full security/privacy audit, renderer/schema/cache/CI validation, clean pass or final-delivery acceptance.
