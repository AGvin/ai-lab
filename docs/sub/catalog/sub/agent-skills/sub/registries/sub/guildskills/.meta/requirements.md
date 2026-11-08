# Documentation Requirements

## Requirements

- Present GuildSkills as an independent cross-agent registry/discovery service for skills using the open Agent Skills / `SKILL.md` format.
- Keep current discovery, installation, supported-agent, publishing, validation, and registry behavior tied to current first-party evidence.
- Distinguish registry interoperability claims from the formal Agent Skills specification and from each host product's concrete support behavior.
- Do not treat registry inclusion as an endorsement or security guarantee.
- If describing the Windows desktop installer, state that the operator says it is unsigned and recommends bypassing a Microsoft Defender SmartScreen warning. Do not recommend bypassing OS protections without independent publisher, package-provenance and integrity verification.
- Distinguish currently available free catalog/search functions from paid Quality Score and advertised one-click desktop installation, and avoid implying every marketed feature has shipped.

## Freshness

- Re-verify supported agents, installation/publishing workflow, validation, and registry scope before substantive edits.

## References

- Official site: https://guildskills.com/

## Bounded installation safety reconciliation — 2026-11-08

- The [first-party GuildSkills homepage](https://guildskills.com/) explicitly identifies the Windows installer as not code-signed and advises selecting "Run anyway" in SmartScreen. The reader now carries actionable OS-warning and package-integrity guidance; catalog inclusion is not authorization to bypass SmartScreen.
- The same homepage markets paid Quality Score and desktop one-click installation, while qualifying some installation functionality as upcoming. Do not turn provider marketing into a verified current integration or installed-client test. No installation or independent binary audit was performed.

## Scoped original-source qualification — 2026-11-06

- GuildSkills presents a cross-agent SKILL.md catalog; a free unrated directory is distinct from its paid Quality Score and desktop installation layer. The official pages distinguish the registry from the open format specification and original skill publishers.
- The site's broad compatibility and quality-scoring claims are provider statements; one listed client or score cannot verify execution safety. Its Windows installer is described by the provider as unsigned, so do not instruct users to bypass OS protections without independent verification.
- Verified first-party source 1: https://guildskills.com/
- Verified first-party source 2: https://guildskills.com/about/
- This review accepts only the current registry identity and source boundaries. It does not assert a full freshness audit, vendor-independent security, tested skill execution, complete CI/cache/schema/render, copyright clearance or verified current listing totals.
