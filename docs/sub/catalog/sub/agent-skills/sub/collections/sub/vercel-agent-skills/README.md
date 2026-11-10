# Vercel Agent Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Vercel Agent Skills is Vercel's official repository-backed collection of Agent Skills for compatible AI coding agents.

## Collection and execution boundary

The collection contains repository-defined guidance and workflows for development, design, writing, optimization and deployment. Its skill inventory, discovery index, installation process and immutable release artifacts follow the selected upstream revision. Individual skill directories remain collection contents.

Skills can inspect project data, modify code, transmit project contents or deploy a project. Review the selected skill and scripts, pin the intended revision and authorize each relevant external action. Installation and first-party publication do not grant that authority or guarantee safe execution. The separate skills registry, AI SDK, AI Gateway and Vercel Connect retain their own identities.

## Deployment and credential safety

The pinned [`deploy-to-vercel` skill](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/deploy-to-vercel/SKILL.md) can push a linked Git repository, link a Vercel team/project, and upload code as a preview or a no-login `vercel deploy --temporary` deployment. A push to the production branch may trigger a production deployment despite the skill's general preview preference. Verify the exact project, team, branch, uploaded files and secret exposure, and obtain explicit authorization before linking, pushing or deploying. Temporary deployments create remotely reachable artifacts and a sensitive claim URL; do not disclose the claim URL.

The pinned [`vercel-cli-with-tokens` skill](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/vercel-cli-with-tokens/SKILL.md) shows diagnostic commands that print `VERCEL_TOKEN` or read raw `.env` values. Do not run these verbatim with live secrets in agent-visible terminals or logs. Check only credential presence, keep tokens out of command-line arguments, history and version control, and use scoped credentials with rotation if exposed. Neither first-party publication nor skill installation overrides these controls.

## Relations

- Produced by: [Vercel Inc.](../../../../../producers/sub/v/sub/vercel-inc/)

## Source interpretation

Vercel's collection contains development, optimization and deployment instructions, distinct from skills.sh, its CLI and the hosting platform. The README declares MIT but no root LICENSE file was observed in the pinned tree; verify selected-path terms before redistribution. Deployment can create remote artifacts, including temporary claimable previews, and needs task-specific authorization.

[Reviewed original README](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Agent Skills source and workflows](https://github.com/vercel-labs/agent-skills)
