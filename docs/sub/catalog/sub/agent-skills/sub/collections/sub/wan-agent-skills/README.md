# Wan Agent Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Wan Agent Skills is Wan Team's official repository-backed collection of Agent Skills for Wan and Alibaba Cloud Model Studio generation workflows.

## Collection and remote processing

Current repository examples include Wan image generation/editing and Wan-assisted presentation generation. These workflows remain collection inventory; model bindings, scripts, installation steps and supported agent hosts can change.

The skills call remote Model Studio APIs using configured account credentials and region-specific endpoints, and can upload local input files. Review the selected skill's scripts, repository license, model terms and data-transfer scope. Installing a skill does not keep its inputs local or turn models, presentation libraries and agent hosts into the same product.

## Input upload and result-retention cautions

The pinned [Wan 2.7 image skill](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/skills/wan2.7-image-skill/SKILL.md) explicitly passes reference images either as local file paths or base64 to `file_to_oss.py`, which uploads the content to temporary object storage before the model API uses it. Its [upload helper](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/skills/wan2.7-image-skill/scripts/file_to_oss.py) requests temporary upload credentials from `dashscope.aliyuncs.com` and then POSTs the bytes to the returned OSS host. The documented generated result URLs expire after roughly **24 hours**; this does not establish the server-side retention of uploaded originals. Obtain explicit permission to transmit private/confidential images or documents, confirm the region and service terms, and store needed outputs in an approved location before URLs expire.

The pinned [presentation skill](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/skills/wan-pptx-generator/SKILL.md) similarly sends document or text content to the remote service and depends on `DASHSCOPE_API_KEY`. Do not put live keys or sensitive base64 payloads in shared command histories, logs or prompts. Its promotional free/discounted terms are time-limited claims; check current billing before a generation run. This review did not upload files, generate presentations or validate remote retention.

## Relations

- Produced by: [Wan Team](../../../../../producers/sub/w/sub/wan-team/)

## Source interpretation

Wan Team publishes Apache-2.0 instruction and script packages for Model Studio image generation/editing and slide workflows. These use remote APIs and may upload local media through OSS helpers; install does not imply local-only processing. Model licenses, account eligibility, API billing and rights in input/output content are separate.

[Reviewed original README](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Wan Agent Skills source and remote API use](https://github.com/Wan-Video/Wan-skills)

## Source parity and regional API limitations

The pinned original [Wan Skills repository](https://github.com/Wan-Video/Wan-skills/tree/3e92371e23b8d43bae0316ae2c87e496675ceb9d) has **13 tracked files**, and its inspected upstream default HEAD matches that exact revision. It contains two `SKILL.md` entrypoints, five Python scripts and two image reference files; no pinned Python dependency manifest was found. The repository's Apache-2.0 source license does not guarantee cloud model/content/asset rights or runtime safety.

**Broken presentation command:** the [Wan PPTX skill](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/skills/wan-pptx-generator/SKILL.md) points to `scripts/pptx_generator.py`, but its [only script is `scripts/pptx-generator.py`](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/skills/wan-pptx-generator/scripts/pptx-generator.py). The documented command is not runnable as-is. This is an upstream mismatch, not a locally tested fix.

**Region/data-transfer warning:** although the [README](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/README.md) lists `DASHSCOPE_BASE_URL` choices for Beijing and Singapore, the [PPT generator](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/skills/wan-pptx-generator/scripts/pptx-generator.py) forces a Beijing SDK endpoint and obtains file upload policies there. The [image OSS uploader](https://github.com/Wan-Video/Wan-skills/blob/3e92371e23b8d43bae0316ae2c87e496675ceb9d/skills/wan2.7-image-skill/scripts/file_to_oss.py) likewise obtains upload credentials from a hardcoded Beijing URL. Setting the Singapore environment variable alone therefore **does not guarantee the upload/slide route uses Singapore**; do not transfer regulated/confidential media before checking the actual endpoint and retention policy.

The OSS image helper and PPT script can send original media/documents to a remote service, and the slide script writes generated assets, logs and presentations locally. Python libraries and model APIs require separate current dependency, account billing, input/output rights and security review. No scripts were run, files uploaded or paid model calls made for this static source assessment; producer ownership/provenance remains pending.
