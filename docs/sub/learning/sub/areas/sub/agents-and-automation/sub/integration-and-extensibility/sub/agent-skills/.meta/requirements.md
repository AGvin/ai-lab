# Documentation Requirements

## Requirements

- Use the reader-facing title `Agent Skills` and make this the canonical learning entrypoint for adopting, designing, authoring, testing, packaging, and operating Agent Skills.
- Begin with a plain-language explanation of a skill as a reusable procedural/capability package that can be discovered and loaded by an AI host; link the reusable Agent Skills concept and formal package specification as separate owners.
- Distinguish skills from prompts, repository instructions, tools/function calling, MCP, Plugins, agents/personas, orchestration workflows, and memory/context while showing how they can compose.
- Explain the discovery -> activation/loading -> execution lifecycle at a durable level and state that installation/presence is separate from activation.
- Make `using-agent-skills/`, `creating-agent-skills/`, and `platform-support-and-portability/` visible as the current source-backed learning children and explain their outcomes.
- Keep exact `SKILL.md` schema/frontmatter/layout rules sourced from the formal specification; learning pages may teach current rules but must not become the independent normative contract.
- Keep concrete skills/collections/registries/installers/platform support facts catalog/platform/evidence-owned; portability learning may compare hosts only with current sources and explicit freshness boundaries.
- Keep third-party skill trust, scripts, tool permissions, credentials, side effects, approval, and update-as-behavior-change boundaries explicit.

## Validation

- A reader can choose whether to learn skill adoption, skill creation, or cross-platform portability without confusing Agent Skills with Plugins or MCP.
- The learning root does not become a catalog or formal specification.
- Only currently materialized child tutorials appear in standard navigation.
