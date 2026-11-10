# Documentation Requirements

## Requirements

- Identify Prisma as the current first-party publisher of its Agent Skills collection.
- Keep the skill collection distinct from the provider's database, application services, SDKs, hosted APIs, MCP servers and client-specific plugin packaging.
- Preserve dated upstream sources for mutable product names, supported development tooling, installed skill inventory, releases and compatibility.
- Retain original third-party attribution and version boundaries where the official collection links to an independent project.

## Validation

- The `produces` relation reciprocates the collection's `produced-by` relation.
- The producer identity is not conflated with upstream skill authors or platform integrators.

## Source-backed identity and operating scope

The reader must preserve the following boundaries and their source basis.

Prisma publishes the represented Prisma Skills collection in its official GitHub organization. The collection provides instructions for agents working with Prisma tooling and database workflows. This producer profile is distinct from the unrelated Prisma AIRS security brand and from individual Prisma software or hosted-service products. [Prisma Skills](https://github.com/prisma/skills).

The skills repository declares MIT licensing and separates guidance for existing Prisma 6/7 projects from Prisma 8 setups and package-owned Prisma 8 references. Match instructions to the application's installed version before authorizing schema migrations, package upgrades or provisioning. Installing a skill grants no database credentials and does not itself create a database deployment. [Collection and version guidance](https://github.com/prisma/skills).

## Reader projection

- Render every non-hidden current-entity relation in its semantic group, ordered by explicit order, canonical target display name and target ID. Preserve source/contributor, organizational and product distinctions.
- Include the official resources from canonical references as readable links. Navigation to a related catalog entry must resolve to its reader, not to metadata.
- Keep changing version, plan, availability and policy details qualified by the cited source; no general offline, license or privacy guarantee follows from producer attribution.
