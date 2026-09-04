# Discovery Resources Component

## Description

Reusable block for presenting specialized catalogs, registries, directories, marketplaces, or comparable resources that materially help readers discover entities in the current canonical domain or class.

## Purpose

Expose validated `has-discovery-resource` relations as a focused reader-facing discovery section without turning the generic relation block into a catalog-of-catalogs UI and without materializing volatile edges to every item listed by an external resource.

## Inputs

The caller supplies the resolved visible projection of the current entity's validated `has-discovery-resource` relations and the resolved canonical target identity needed to link each resource.

When the approved resolved target context exposes a concise reader-facing summary suitable for this block, the caller may supply that summary with the target entry. A summary is optional and must come from the target's canonical content/context; it must not be copied into the relation record or invented by the component.

## Rendering Rules

- include every visible validated `has-discovery-resource` relation supplied to the block and no other relation type;
- preserve canonical endpoint-local `hidden` and `order` semantics, including the normal alphabetical fallback and canonical target ID tie-breaker;
- render the canonical target name as the primary link to the target documentation node;
- when an approved concise target summary is available, render it as secondary orientation without duplicating a longer target profile;
- do not imply that a listed resource has complete coverage, is endorsed by AI Lab, or is authoritative merely because it is a discovery resource;
- do not expand a domain-level relation into links for every skill, model, service, software item, dataset, or other entity the target resource currently lists;
- omit the block when the page contract does not authorize discovery-resource presentation or when no visible qualifying relation remains;
- keep the heading and compact presentation oriented to discovery rather than generic semantic relationships.

## Does Not Own

- relation discovery, factual validation, target resolution, inverse materialization, or relation membership;
- whether a page requires this block;
- the target entity's canonical description or authoritative resources;
- generic relation presentation for relation types other than `has-discovery-resource`;
- creation of per-item membership edges from an external catalog's volatile contents.

The component consumes only the validated current-entity discovery-resource projection supplied through the approved render context. It must not scan unrelated nodes or external resources to infer additional edges.
