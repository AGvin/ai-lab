# Cursor Agent Skills

Cursor discovers skills from project `.agents/skills/` and `.cursor/skills/` directories and their user-level equivalents. Each skill is a folder containing `SKILL.md`.

## Discovery and use

Agent selects relevant skills from their descriptions. Typing `/` in chat invokes a skill for one message; `disable-model-invocation: true` makes invocation manual. Create a skill folder or use Cursor's `/create-skill`. Repository imports arrive through marketplace plugins.

## Execution and sharing

Skills can include executable scripts, so review their source and the permissions of the Agent runtime that uses them. Personal `~/.cursor/skills/` content stays local until explicitly synced for Cloud Agents or published to a team. Unsynced local skills and `~/.agents/skills/` are not automatically copied to remote workers.

Shared concepts and cross-host guidance belong to Agent Skills and Agent Skills Platform Support and Portability. The [Agent Skills specification](../../../../../../../../../../../specifications/sub/formats/sub/agent-skills/) owns the portable format.

## Official resources

- [Cursor Agent Skills](https://cursor.com/docs/context/skills)
