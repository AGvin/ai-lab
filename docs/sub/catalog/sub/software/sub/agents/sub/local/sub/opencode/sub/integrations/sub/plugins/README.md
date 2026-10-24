# OpenCode Plugins

OpenCode plugins are JavaScript or TypeScript modules that extend the host with hooks and custom behavior. This is OpenCode's executable plugin mechanism; current documentation does not establish conformance with the vendor-neutral Agent Plugins package standard.

## Loading and execution

Local modules load from project `.opencode/plugins` and user `~/.config/opencode/plugins` directories. npm packages are listed in the configuration's `plugin` array; OpenCode installs package dependencies with Bun at startup and caches them.

The documented order is global configuration, project configuration, global plugin directory, then project plugin directory. Identical package/version entries are deduplicated; a local plugin and an npm plugin can both load.

A plugin exports a function that returns hooks and receives host facilities such as the SDK client, project information, and Bun's shell helper. Local dependencies can be declared in the configuration directory's `package.json`. Hook and permission events describe host behavior, not an isolation boundary for arbitrary plugin code. Review the module, dependencies, credentials, and filesystem access before loading it. Skills, MCP servers, commands, and agent configuration remain distinct extension mechanisms.

## Related

- [Agent Plugins specification](../../../../../../../../../../../specifications/sub/formats/sub/agent-plugins/)

## Official resources

- [OpenCode plugin documentation](https://opencode.ai/docs/plugins/)
