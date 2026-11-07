# Documentation Requirements

## Requirements

- Identify AGENTS.md as the practical open agent-instruction file format: Markdown text in an `AGENTS.md` file located at a repository or relevant directory scope, complementary to human-facing README documentation.
- Preserve the distinction between an adopted cross-agent convention and a ratified versioned specification; the current official site does not prescribe mandatory field names, a YAML header, a parser schema, or a complete standardized conflict-resolution algorithm.
- Keep recommended content such as project purpose, setup/build/test commands, code conventions, architecture notes and safety constraints as examples, not normative mandatory sections.
- Describe nested `AGENTS.md` files and nearest-directory precedence as the reference convention, but note that actual search paths, loading order, conflicts, tool approval and instruction precedence are client-specific; do not claim identical behavior for all agents.
- Keep Agent Skills (`SKILL.md`) packaging, `llms.txt` website discovery, and product-specific `CLAUDE.md`/editor rules separate from this project-instruction format.
- Preserve the historical origin in OpenAI Codex and the December 2025 transfer of stewardship to the Agentic AI Foundation without conflating foundation maintenance with original creation.
- Re-check the official site and upstream repository for compatibility, maturity and governance changes before upgrading wording to a formal conformance standard.

## Validation

- No invented required metadata keys or universal instruction-precedence promises are presented as normative requirements.
- The format identity is distinct from Agent Skills, `llms.txt`, agent protocols and product-specific file names.
- The `maintained-by` foundation relation has a matching `maintains` inverse.
- Published origin/stewardship claims are traceable to first-party sources.

## Scoped original-source qualification — 2026-11-07

- AGENTS.md is an open Markdown project-instruction convention for coding agents, distinct from Skill packaging and `llms.txt` web indexing. The upstream site gives examples for setup, tests, code style and security; it does not impose a required YAML schema, a fixed headings inventory or a universal parser/conformance suite.
- Nested files can scope instructions to a project subtree; the upstream guidance describes nearest-file precedence, but real discovery, conflict resolution, context loading and instruction trust are controlled by each adopting agent. Foundation stewardship does not imply all listed clients have identical support or grant autonomous tool permissions.
- Verified primary source 1: https://agents.md/
- Verified primary source 2: https://github.com/agentsmd/agents.md
- The format's existing identity and foundation maintainer inverse relation are verified; its reader page is currently absent and earns no repair credit. No tool execution, cross-client compatibility test, complete foundation governance/legal assessment, clean pass or final gate.
