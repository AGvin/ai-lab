# Documentation Requirements

## Requirements

- Identify Wan Agent Skills as Wan Team's official repository-backed collection of Agent Skills for invoking Wan/Alibaba Cloud Model Studio AIGC workflows from compatible agent harnesses.
- Preserve the collection boundary rather than creating one canonical entity per contained skill unless later intake establishes independent durable identity and material catalog value.
- Keep the exact skill inventory, scripts, reference files, installation steps, required environment variables, Model Studio endpoints, supported models, and repository structure freshness-sensitive.
- Preserve current contained workflows such as Wan image generation/editing and Wan-assisted presentation generation only as repository inventory, not as permanent exhaustive scope.
- Keep Alibaba Cloud Model Studio, Wan models, Qwen models, PowerPoint generation libraries, and supported agent hosts with their own canonical identities.
- Preserve credential and data-transfer boundaries: skills call remote Model Studio APIs and can upload local inputs, so installation does not imply that source material remains local.
- Preserve repository licensing and first-party status without treating publication as a blanket quality, security, or rights endorsement.

## Source-specific remote media handling

- Explain that pinned [Wan image skill](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/skills/wan2.7-image-skill/SKILL.md) forwards local-file or base64 image inputs via an OSS uploader; the [Python helper](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/skills/wan2.7-image-skill/scripts/file_to_oss.py) obtains a policy from DashScope and posts image bytes to temporary OSS. This is external media transmission, not local-only inference.
- Preserve source-reported roughly 24-hour result-link expiry separately from unknown upstream input retention; suggest privately saving outputs if continued access is needed. Avoid disclosing `DASHSCOPE_API_KEY`, pasted base64 or sensitive filenames in agent-visible logs/history.
- The pinned [Wan presentation skill](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/skills/wan-pptx-generator/SKILL.md) supports PDF/DOCX/text upload and advertises time-limited pricing; require explicit content-transfer authorization and current model region/price review before executing it.
- Documentation inspection is not installation, account access, runtime security validation or provider privacy/retention assurance.

## Validation

- The entity remains a skill collection rather than the Wan model family or Model Studio service.
- Producer provenance resolves to Wan Team.
- Mutable skill counts and model bindings are not frozen from one repository snapshot.
- Individual skill directories are not automatically duplicated as standalone catalog entities.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
