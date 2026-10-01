# Agent Skills

Agent Skills is an open package format and specification for portable skill packages.

## Specification boundary

The core package is a skill directory with a required `SKILL.md` entrypoint containing YAML frontmatter followed by Markdown instructions. The current upstream specification defines required metadata such as `name` and `description`, while other fields and supporting files may be optional or experimental according to the active specification.

Client-specific discovery paths, precedence, invocation, permissions, enable or disable controls, metadata extensions, and compatibility behavior remain product-integration concerns rather than universal Agent Skills requirements.

## Official resources

- [Agent Skills specification](https://agentskills.io/specification)
- [Agent Skills repository](https://github.com/agentskills/agentskills)
