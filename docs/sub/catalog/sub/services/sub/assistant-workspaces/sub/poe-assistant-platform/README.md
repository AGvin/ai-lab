# Poe Assistant Platform

**Poe** is a hosted multiprovider conversational-assistant platform where users interact with bots and creators publish AI-powered experiences. The [official Poe Creator Guide](https://creator.poe.com/docs) distinguishes prompt-configured bots, separately hosted server bots, script bots, API bots, interactive apps and external application integrations.

## Bot and API boundaries

Poe does not itself own all models reachable through the platform. The [API Bot architecture](https://creator.poe.com/docs/api-bots/overview) describes Poe receiving chat requests, proxying them to a creator-controlled compatible endpoint and streaming results to users. [Server Bots](https://creator.poe.com/docs/server-bots/poe-protocol-specification) follow a separately specified protocol. External clients can authenticate with account-scoped [Poe API keys](https://creator.poe.com/docs/external-applications/external-application-guide) and spend the relevant account's points.

These are hosted distribution and orchestration surfaces, not proof that the creator's model, prompts, server code or connected data is Poe-owned.

## Operations, cost and privacy

Connected bots may relay messages and uploaded content to other providers or independent bot operators. Check bot provenance, access rights, account credentials, privacy policies, data retention and moderation before disclosing protected content. Usage costs, token/point accounting, model availability and creator monetization are mutable.

No bot was created, model invoked, private data sent, billing charge simulated or whole-catalog clean pass performed.

## Official resources

- [Poe platform](https://poe.com/)
- [Poe Creator documentation](https://creator.poe.com/docs)
- [API Bot overview](https://creator.poe.com/docs/api-bots/overview)
- [Server Bot protocol](https://creator.poe.com/docs/server-bots/poe-protocol-specification)
- [External application access](https://creator.poe.com/docs/external-applications/external-application-guide)
