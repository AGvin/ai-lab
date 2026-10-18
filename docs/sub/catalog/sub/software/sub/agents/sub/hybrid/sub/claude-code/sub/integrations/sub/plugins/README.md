# Claude Code Plugins

Claude Code plugins package extension components for installation and reuse within Claude Code. A plugin may combine skills, commands, subagents, hooks, MCP servers, and other supported components; a marketplace is a discovery and distribution catalog for those packages.

## Package and installation boundary

The usual manifest is `.claude-plugin/plugin.json`. Component locations are relative to the plugin root, and manifest path fields have component-specific merge or replacement behavior. Plugin skills receive namespaced commands such as `/plugin:skill`. Use `--plugin-dir` for a local development package or a registered marketplace for managed installation.

In a Claude Code session, `/plugin install name@marketplace` opens the plugin details for review and scope selection. The shell command `claude plugin install` performs installation directly. User, project, and local scopes have different visibility; committed project enablement does not download the package to collaborators' machines.

## Trust and lifecycle

Plugins can execute code with the user's privileges. Marketplace inclusion does not remove the need to review scripts, hooks, MCP connections, credentials, and permissions. Organization policy can require or restrict plugins.

The plugin manager supports enable, disable, update, and uninstall. Reloading or starting a new session activates pending changes; cloud sessions do not inherit plugins from local settings. Supported components and compatibility depend on the installed Claude Code version. This is Claude Code's product contract; generic Agent Plugins conformance requires explicit evidence.

## Official resources

- [Plugins overview](https://code.claude.com/docs/en/plugins)
- [Plugin manifest reference](https://code.claude.com/docs/en/plugins-reference)
- [Install and manage plugins](https://code.claude.com/docs/en/discover-plugins)
- [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
