# Documentation Requirements

## Requirements

- Use the reader-facing title `AI Engineering`.
- Present AI engineering as the domain concerned with designing, building, integrating, operating, evaluating, and evolving AI-enabled systems under real software, data, infrastructure, reliability, performance, cost, and governance constraints.
- Distinguish AI engineering from model architecture/training, generic software engineering, data science, and concrete product/tool ownership; it applies engineering methods to systems that include AI components without re-owning those underlying subjects.
- Explain that an AI system can combine learned models with retrieval, deterministic software, tools, workflows, data stores, human controls, monitoring, and infrastructure; model capability alone is not the complete engineering system.
- Keep system architectures/patterns, methodologies, system design, extensibility/packaging, integration/interoperability, deployment/serving, observability, reliability/resilience, performance/scalability, and cost/capacity as distinct selected subdomains rather than collapsing them into one deployment guide.
- Treat `extensibility-and-packaging/` as the reusable AI-system owner for concepts whose primary identity is packaging reusable capabilities/instructions/components for discovery, activation/loading, distribution, composition, update/removal, or host extension. Keep concrete packages/products with their applicable catalog owners and formal package/specification contracts under `catalog/specifications/`.
- Treat `integration-and-interoperability/` as the reusable AI-system owner for concepts whose primary identity is standardized/interoperable connection across AI applications and external capabilities/systems. Keep formal normative protocol/specification contracts under `catalog/specifications/` and concrete implementations/products with their applicable catalog owners.
- Distinguish extensibility/packaging from integration/interoperability. A package can distribute reusable behavior or integration configuration without itself defining a runtime cross-component protocol; conversely, an interoperability protocol can operate independently of any plugin/skill packaging system.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Keep concrete software/services, packages/plugins/skills, provider capabilities, infrastructure inventories, benchmark/evidence results, procurement, and project-specific implementation decisions with their applicable catalog, evidence, or project/decision owners.

## Validation

- The page does not equate AI engineering with model training, prompt engineering, MLOps, or deployment alone.
- System-level concerns are distinguished from intrinsic model properties.
- Extensibility/packaging concept semantics are distinguished from concrete packages/products, formal package/specification contracts, and tutorials.
- Integration/interoperability concept semantics are distinguished from formal protocol specifications and concrete implementations/products.
- Extensibility/packaging and integration/interoperability remain distinct ownership domains rather than catch-all synonyms.
- Concrete products and mutable provider/runtime/package-support facts are not owned by this abstract domain.
- Direct-child navigation contains only currently materialized direct children.
