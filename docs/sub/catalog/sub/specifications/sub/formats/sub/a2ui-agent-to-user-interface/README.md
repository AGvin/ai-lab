# A2UI — Agent-to-User Interface

A2UI (Agent-to-User Interface) is a declarative JSON format and evolving protocol for expressing UI structures and updates generated or populated by agents. The receiving application maps abstract component descriptions to its own trusted renderer and approved components; payloads are **not intended as executable UI code**.
## Versions, transport and trust
The [first-party project README](https://github.com/a2ui-project/a2ui) reviewed **5 November 2026** identifies an **early-stage public preview**, **v0.9.1** as the current production release of the stable v0.9 protocol family, and **v1.0** as a release candidate. These are evolving versions, not universal framework guarantees.
A2UI describes *UI data*, while agents can transmit it through A2A, AG-UI or host-defined transports. Renderer libraries, supported host frameworks and component assets are separate products. Validate untrusted payloads, restrict components and permissions, and sandbox consequential actions. Declarative format alone is not a safety guarantee.
## Official resources
- [A2UI upstream repository and specification](https://github.com/a2ui-project/a2ui)
- [Project documentation](https://a2ui.org/)
