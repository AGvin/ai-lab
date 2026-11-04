# Glean Enterprise AI Workspace

**Glean Enterprise AI Workspace** is a hosted enterprise assistant and knowledge workspace that connects company documents and tools to deliver grounded answers, search, drafting and work execution. Its [official overview](https://docs.glean.com/user-guide/about/what-is-glean) identifies search as one capability of a broader AI coworker rather than a standalone generic vector search backend.

## Enterprise context and access

The [Glean Assistant](https://www.glean.com/ai-assistant) combines enterprise context with work-product generation and connected actions. Its [information access guide](https://docs.glean.com/user-guide/assistant/how-glean-accesses-info) describes personalized search governed by permissions from connected apps. [AI Answers](https://docs.glean.com/user-guide/assistant/ai-answers) includes citations to organization sources and is intended to use information the querying user may access. The underlying source documents remain owned and access-controlled by their corresponding systems.

## Security and operations

Permission-aware retrieval is not a reason to grant unrestricted connector scopes. Administrators must consider identity mapping, ACL synchronization, token security, data residency, records retention, source confidentiality, action approvals, evidence provenance and model processing terms. Answers may be stale or incomplete; source links and access boundaries should be checked before executing consequential actions.

Commercial availability, connectors, features and prices can change. This profile does not assert that a tenant was provisioned, permissions tested, live documents indexed or a whole-catalog clean pass performed.

## Official resources

- [Glean Assistant](https://www.glean.com/ai-assistant)
- [What is Glean?](https://docs.glean.com/user-guide/about/what-is-glean)
- [Information access and permissions](https://docs.glean.com/user-guide/assistant/how-glean-accesses-info)
- [AI Answers](https://docs.glean.com/user-guide/assistant/ai-answers)
