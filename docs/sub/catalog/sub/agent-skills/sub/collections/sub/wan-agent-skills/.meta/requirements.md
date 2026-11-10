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

## Complete selected-source parity and upload/region implementation audit — 2026-11-10

- Compared the **complete 13-blob Git tree** of `Wan-Video/Wan-skills@3e92371e23b8d43bae0316ae2c87e496675ceb9d` to the inspected current upstream default `HEAD`: the commits, file paths and blob SHAs are identical (no new, changed or deleted file). This supports current **selected public source-tree parity** for this revision, not live account/service behavior or paid installation security.
- Read both `SKILL.md` entrypoints, both image reference documents, all **five** Python scripts, source README, license and multilingual README inventory. Exact contents are two main skills (`wan2.7-image-skill`, `wan-pptx-generator`), five Python scripts (four image helpers and one PPT generator) and two extra image references. No repo-level `requirements.txt`, package lock, or pinned runtime dependency manifest is in this 13-file tree; active Python packages such as `requests`, `dashscope` and `python-pptx` still require an independent installation and dependency/version/supply-chain review.
- **Broken first-party launch path:** the published [presentation skill instructions](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/skills/wan-pptx-generator/SKILL.md) repeatedly invoke/link `scripts/pptx_generator.py`, but the [actual only script](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/skills/wan-pptx-generator/scripts/pptx-generator.py) is named `pptx-generator.py` (hyphen). These paths do not resolve as written; use the actual file path only after installation, dependency and transfer permissions are separately approved. Do not silently change upstream files.
- **Region/privacy mismatch:** [README](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/README.md) and image reference/config support `DASHSCOPE_BASE_URL` Beijing or Singapore. The [presentation script](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/skills/wan-pptx-generator/scripts/pptx-generator.py) hardcodes `https://dashscope.aliyuncs.com/api/v1` for its global SDK and `/uploads` credentials; the [image OSS upload helper](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/skills/wan2.7-image-skill/scripts/file_to_oss.py) also hardcodes the Beijing `/uploads` endpoint. In contrast image generation/polling uses `DASHSCOPE_BASE_URL` where implemented. **Do not infer Singapore data residency from setting the environment variable** when executing upload or presentation scripts; resolve endpoint behavior or use approved region-specific supported tooling first.
- The image upload helper sends local media or base64 bytes to provider-issued temporary OSS; the slide script uploads PDF/DOCX/text files as needed, may write content/logs/images/PPTX locally and retrieves remote URLs. The exact input content and project metadata can leave the local environment. Require explicit consent for private documents/images, verify target region, provider input retention and billing, and avoid credentials or pasted base64 in shell history.
- The root [Apache-2.0 LICENSE.txt](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/LICENSE.txt) covers the licensed source, but downstream Python library rights, upstream models, externally uploaded data and third-party content/output rights are separate. **Selected-rights clearance and independent full-profile source closure remain pending** under existing provenance/ownership review.
- All analysis was read-only on original pinned upstream; no Python script was executed, no dependency installed, API key read, OSS upload, model call, billing or local artifact generation was performed. Source-tree parity, canonical reader reconciliation, bounded static scripts review and permissions/data-flow mapping may be counted separately; they are not a successful runtime test or Clean acceptance.
