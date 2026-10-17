# Documentation Requirements

## Requirements

- Identify JetBrains Skills as an official first-party-curated and security-filtered distribution/catalog of third-party Agent Skills, not a set of packages all originally authored by JetBrains.
- Preserve the independent collection identity because JetBrains maintains the verified snapshot, source-attribution metadata, curated inventory and its IDE-integrated Skill Repository distribution role.
- Keep source author/project provenance in upstream `SKILL.md` metadata (including `metadata.source`) rather than rewriting upstream collections or all selected skills under JetBrains authorship.
- Distinguish JetBrains's curated skill repository from its AI Assistant/Skill Manager product, IntelliJ IDEA and other IDE clients, project/global installation, and the generic Agent Skills package specification.
- Treat skill count, scanned source set, security-scanner CI rules, release/version availability, compatibility, and downstream client install options as time-sensitive. Security filtering reduces but cannot eliminate risks in untrusted scripts/instructions.
- Do not add peer records for each imported upstream skill solely because the JetBrains snapshot packages them; keep independent producer collections with their existing canonical identities where represented.

## Validation

- The first-party curated/produced collection resolves through the named producer without erasing upstream authorship.
- The current collection/release inventory and install compatibility are source-backed rather than assumed permanent.
- Bundled skill directories are not duplicated as canonical peers merely for enumeration.
- The inverse `produces` relation matches the collection's `produced-by` relation.
