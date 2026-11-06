# WorkOS Agent Auth

WorkOS Agent Auth is WorkOS's agent-specific identity and access service within AuthKit. The September 2026 announcement identifies it as early access; current documentation does not establish a later general-availability transition.

## Identity and authority

The service provides first-class agent identities, reusable blueprints, delegated and autonomous instances, revocable sessions and short-lived scoped credentials. Agent Registration is a related programmatic discovery and registration capability within that boundary.

Effective authority depends on blueprint and session configuration, registration identity and trust level, delegated grants and the target service's permissions. Check the current token and refresh semantics, supported modes, endpoints and limits. Generic AuthKit user login, machine-to-machine applications, WorkOS Connect and Fine-Grained Authorization retain their separate boundaries.

## Relations

- Produced by: [WorkOS](../../../../../producers/sub/w/sub/workos/)

## Official resources

- [Agent blueprints and scoped credentials](https://workos.com/docs/authkit/agent-blueprints)
- [Agent registration and trust levels](https://workos.com/docs/authkit/agent-registration)
- [Agent Auth early-access announcement](https://workos.com/changelog/agent-auth)
