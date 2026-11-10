# JetBrains Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

A JetBrains-curated distribution of upstream Agent Skills, with source attribution and security filtering. JetBrains maintains the collection snapshot; individual skills retain their upstream authors and licenses.

## Collection boundary

Use each skill's `metadata.source` to reach its original project. Imported directories are collection entries, not automatically separate catalog identities. The collection is distinct from the Agent Skills format, JetBrains IDEs and their skill-management clients.

The repository supplies the current inventory and scanner behavior. Filtering is not a guarantee of safe execution: review instructions and scripts for the intended environment. Counts, compatibility and release availability can change; pin and evaluate the selected snapshot.

JetBrains documents Skill Repository discovery in its IDE tooling. Project/global installation and client compatibility must be checked against the installed client version rather than inferred from inclusion in this collection.

## Security-scanner coverage

The pinned [JetBrains scanning workflow](https://github.com/JetBrains/skills/blob/3f53782dec7b5424bf6e8efbb90a46ee26f31798/.github/workflows/skill-scanner.yml) does **not** prove every bundled upstream skill has passed a fresh blocking security audit. On ordinary pushes and pull requests the CI scanner selects changed skill directories and can fail on error-level findings for those changes; a manually dispatched full-repository scan uploads its report without using inherited upstream findings to block the workflow. Code Scanning SARIF upload is best-effort. Thus a green ordinary workflow or a completed manual scan is not a signed clean bill of health for all imported scripts and dependencies.

Before installing or executing a third-party skill from the curated snapshot, inspect its exact `metadata.source`, pinned content, path-specific license, included scripts, credential access and tool/network permissions. Read available scanner reports for that revision, not only the workflow badge; approval is still required for externally visible changes or sensitive-data access. No scanner run, skill execution or independent dependency verification was performed in this catalog review.

## Producer

- Curated and distributed by: [JetBrains](../../../../../producers/sub/j/sub/jetbrains/)

## Source interpretation

JetBrains distributes a filtered snapshot of skills from multiple upstream repositories; each skill's metadata.source identifies its original source. JetBrains curation and scanner results do not replace upstream authorship, per-path licenses or runtime permission review. No root license file was observed in the pinned tree; do not infer a blanket redistribution grant.

[Reviewed original README](https://github.com/JetBrains/skills/blob/3f53782dec7b5424bf6e8efbb90a46ee26f31798/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- <https://github.com/JetBrains/skills>
- <https://www.jetbrains.com/pages/ai-agents/architecture/agent-skills/>
