# Neon Agent Skills

## Relations

- Produced by: [Neon](../../../../../producers/sub/n/sub/neon/)

## Collection purpose

Neon Agent Skills is Neon's published collection of portable agent instructions, scripts, and supporting resources for Neon and Lakebase Postgres workflows. The upstream collection covers database use and branches, authentication, object storage, gateways, and related developer-agent work. [Upstream collection](https://github.com/neondatabase/agent-skills).

## Organization and access

The repository's `skills/` directories and their `SKILL.md` entry points hold the collection's skill content. The upstream README provides the current inventory and installation choices. Optional Agent Plugins v1 packaging and client-specific manifests for Claude, Cursor, Kimi, Pi, and other clients distribute or expose that same collection; they do not create separate skill-collection identities.

The Neon MCP server is an integration that can accompany the skills. A separately linked Neon-for-agent-platforms repository contains companion material with its own distribution boundary; a link from this collection does not establish common ownership of every companion workflow.

## Runtime and permission boundaries

Installing instructions does not authenticate a database session or grant authority to change data, provision infrastructure, deploy code, or use credentials. Actual operations depend on the agent client, configured tools, account permissions, and runtime behavior. Review the underlying service's data and access conditions for the chosen workflow.

Skill names, client support, plugin declarations, Neon/Databricks product branding, and service features change. Follow the current upstream inventory and [Neon documentation](https://neon.com/docs/ai/agent-skills) for supported installation and usage; collection publication alone does not validate a specific client or deployment.

## Official resources

- [Agent Skills repository and current inventory](https://github.com/neondatabase/agent-skills)
- [Neon Agent Skills documentation](https://neon.com/docs/ai/agent-skills)
