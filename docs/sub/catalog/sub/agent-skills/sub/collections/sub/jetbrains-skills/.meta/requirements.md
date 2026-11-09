# Documentation Requirements

## Requirements

- Identify JetBrains Skills as an official first-party-curated and security-filtered distribution/catalog of third-party Agent Skills, not a set of packages all originally authored by JetBrains.
- Preserve the independent collection identity because JetBrains maintains the verified snapshot, source-attribution metadata, curated inventory and its IDE-integrated Skill Repository distribution role.
- Keep source author/project provenance in upstream `SKILL.md` metadata (including `metadata.source`) rather than rewriting upstream collections or all selected skills under JetBrains authorship.
- Distinguish JetBrains's curated skill repository from its AI Assistant/Skill Manager product, IntelliJ IDEA and other IDE clients, project/global installation, and the generic Agent Skills package specification.
- Treat skill count, scanned source set, security-scanner CI rules, release/version availability, compatibility, and downstream client install options as time-sensitive. Security filtering reduces but cannot eliminate risks in untrusted scripts/instructions.
- Do not add peer records for each imported upstream skill solely because the JetBrains snapshot packages them; keep independent producer collections with their existing canonical identities where represented.

## Security-scanning evidence limits

- Explain that ordinary JetBrains Skill Scanner CI evaluates changed skill directories and can block changed-skill error-level findings, whereas manual full-repository workflow dispatch uploads a report without treating inherited findings as blocking. A passing check is not exhaustive current coverage of every imported third-party skill.
- Preserve that SARIF publication to GitHub Code Scanning is best-effort; absence of a security alert or upload is not evidence of absence of risk. Review the actual report and source commit when available.
- Require selected skill's `metadata.source`, original author/license, scripts, permissions, network/data flow and pinned revision to be inspected before execution. JetBrains curation is not upstream authorship or a blanket redistribution/runtime guarantee.
- Cite the pinned [scanner workflow](https://github.com/JetBrains/skills/blob/3f53782dec7b5424bf6e8efbb90a46ee26f31798/.github/workflows/skill-scanner.yml) and [source inventory](https://github.com/JetBrains/skills/blob/3f53782dec7b5424bf6e8efbb90a46ee26f31798/README.md); no actual scanner rerun or independent security attestation was performed.

## Validation

- The first-party curated/produced collection resolves through the named producer without erasing upstream authorship.
- The current collection/release inventory and install compatibility are source-backed rather than assumed permanent.
- Bundled skill directories are not duplicated as canonical peers merely for enumeration.
- The inverse `produces` relation matches the collection's `produced-by` relation.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
