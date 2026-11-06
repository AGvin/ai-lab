# Cursor Plugins

Cursor supports the portable [Agent Plugins standard](../../../../../../../../../../../specifications/sub/formats/sub/agent-plugins/) and its own richer plugin format.

## Package and compatibility

Portable plugins use a root `plugin.json` and package skills and MCP servers. Cursor Plugins use `.cursor-plugin/plugin.json` and can also contain rules, agents, commands, hooks and variables. Cursor currently does not expand the standard's `${PLUGIN_ROOT}` or `${PLUGIN_DATA}` variables in `mcp.json`; its documented plugin-root variable is `${CURSOR_PLUGIN_ROOT}`.

## Install and manage

Install either format from a marketplace through Customize, choosing project or user scope. Manage installed components in Customize; team marketplace access and admin controls can constrain installation. Use the documented local-plugin testing flow before publishing.

Review plugin provenance, scripts, hooks, MCP credentials and the runtime permissions available to installed components. Marketplace availability does not give a plugin authority over project data or commands. Shared concepts and portability teaching remain with the AI Plugins concept and its learning owners.

## Official resources

- [Cursor Plugins](https://cursor.com/docs/plugins)
