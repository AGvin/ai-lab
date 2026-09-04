# Product Integration Page

## Description

Canonical child page for one substantial product- or service-specific integration surface.

## Purpose

Help readers understand how a concrete parent product or hosted service supports one shared or external technology, what host-specific behavior and constraints apply, and where generic concept, specification, or learning guidance belongs.

## Use When

Use for materialized children under a concrete product or service `integrations/` node when the page owns substantive host-specific support, discovery, setup, invocation, permissions, configuration, compatibility, lifecycle, or operational behavior.

## Do Not Use When

Do not use for the parent software/service profile, a generic integrations category, the generic concept or specification of the integrated technology, reusable learning guidance, a standalone third-party product, or a thin link-only child without substantive host-specific content.

## Owns

- integration identity and scope in the context of the parent product or service;
- current host-specific availability, supported surfaces, and behavior;
- host-specific discovery, setup or placement, invocation, permissions, configuration, lifecycle, and compatibility facts when applicable and source-backed;
- distinctions from adjacent extension, instruction, plugin, or protocol surfaces in the same host;
- mutable version, client, workspace, plan, path, command, limit, or configuration boundaries with explicit freshness requirements;
- relation-block placement and reader wording when applicable requirements authorize relation presentation;
- authoritative host-specific integration resources.

## Does Not Own

- generic semantics or the formal specification of the integrated technology;
- cross-product portability teaching or a universal support matrix;
- the parent product's general identity and capabilities;
- a duplicated standalone profile of the integrated technology;
- timeless claims about mutable support, paths, commands, configuration, limits, or availability without current evidence;
- long procedural tutorials better owned by learning or workflow documentation;
- per-relation membership, visibility, or ordering, which come from the validated current entity projection.

## Expected Inputs

Requirement-approved integration title/orientation, parent product or service context, host-specific integration behavior, current mutable boundaries, distinctions from nearby host surfaces, authoritative resources, links to canonical concept/specification/learning owners, and the validated current-entity relation projection when the page requirements call for the relation block.

## Composition

1. default header;
2. concise integration identity in the parent-product context;
3. `entity-relations` when applicable requirements call for relation presentation;
4. availability, scope, and current support boundary;
5. setup/discovery/invocation/configuration/permissions or lifecycle sections required by the node;
6. distinctions from adjacent host mechanisms plus relevant compatibility or limitations;
7. links to canonical concept, specification, or learning owners instead of duplicating reusable guidance;
8. freshness caveats for mutable behavior when required;
9. `official-resources`.

## Variants

Agent Skills, MCP, plugin, protocol, provider, or other integration children reuse this family while the reader job remains host-specific integration behavior. Software and hosted-service parents may emphasize different mutable constraints without requiring separate integration templates by default.

## Representative Examples

- Claude Code Agent Skills;
- OpenAI Codex Agent Skills;
- OpenCode Agent Skills;
- Cursor Agent Skills;
- ChatGPT Agent Skills.

## Anti-patterns

- using the parent software or service profile template for a product-local integration child;
- copying generic authoring, portability, or specification guidance into every host integration page;
- treating nominal support as proof that behavior is identical across products, clients, versions, workspaces, or plans;
- presenting mutable paths, commands, permissions, limits, or availability as timeless facts;
- materializing empty integration children solely for taxonomy symmetry.
