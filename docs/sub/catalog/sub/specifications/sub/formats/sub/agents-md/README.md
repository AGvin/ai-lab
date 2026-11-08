# AGENTS.md

**AGENTS.md** is an open, Markdown-based project-instruction file convention for coding agents. It supplements human-facing `README.md` documentation with practical guidance such as environment setup, build/test commands, coding conventions, architecture notes and security considerations. The file name and repository/directory placement are the essential convention; those example sections are not a mandatory document schema. [Official AGENTS.md site](https://agents.md/).

## Format and interoperability boundary

A root-level or nested `AGENTS.md` file can describe instructions applicable to an entire repository or a particular subtree. The reference convention describes nearest-directory precedence, but actual discovery, loading and conflict handling depend on each coding-agent client. There is no universal required YAML frontmatter, fixed heading schema, parser or guaranteed instruction-override behavior shared by all tools.

This format is separate from portable [Agent Skills](../agent-skills/) packages with a `SKILL.md` entrypoint, the [llms.txt](../llms-txt/) website-discovery proposal, and tool-specific project instructions such as `CLAUDE.md`. An instruction file does not automatically authorize tool execution or override system, organization and security controls.

## Stewardship and maturity

The convention originated in OpenAI Codex and its stewardship moved to the Agentic AI Foundation in December 2025. Adoption as an open convention is not equivalent to certification under a ratified versioned standard. Check the current upstream site and client documentation for support and scope before assuming portability. [Reference repository](https://github.com/agentsmd/agents.md).

## Relations

- Maintained by [Agentic AI Foundation](../../../../../producers/sub/a/sub/agentic-ai-foundation/).

## Official resources

- [AGENTS.md convention](https://agents.md/)
- [Official repository](https://github.com/agentsmd/agents.md)
- [Agentic AI Foundation announcement](https://openai.com/index/agentic-ai-foundation/)
