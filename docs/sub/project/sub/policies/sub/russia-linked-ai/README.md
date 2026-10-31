# Russia-linked AI: provenance and adoption restrictions

## Binding AI Lab classification

AI Lab **retains Russian-linked AI resources in the catalog for research, comparison and threat monitoring**, not endorsement. Determine the restriction from **documented origin, current ownership, effective control and upstream technology provenance**, including direct and indirect links. Russian ownership is not necessarily evident from a brand, registration country or current vendor name.

**Tier 1 — DANGEROUS — NOT RECOMMENDED | RUSSIAN ORIGIN OR CONTROL.** Apply when a product or relevant component has verified Russian development/technology origin, is produced or operated by a Russia-based entity, or is subject to verified Russian ownership **that confers control** (including through subsidiaries, voting rights, board appointment, veto or other effective control). Russian-origin model weights, code or artifacts remain in this category even after mirroring or rehosting. **Never recommend these for adoption**, regardless of audits, open-source status, licensing, favorable benchmarks, an absence of known malware, or an absence of applicable sanctions. Keep them cataloged for monitoring only. Do not automatically assign the *entire* independent host company this tier solely because it distributes one such component; identify the affected product or dependency chain.

**Tier 2 — ELEVATED RISK — DEPRIORITIZED | PARTIAL RUSSIAN OWNERSHIP.** Apply where **any nonzero, reliably verified current direct or indirect Russian ownership stake** exists but no Russian control, Russian operation or Russian-origin technology has been established. There is **no minimum ownership-percentage threshold for disclosure in AI Lab**. Mark the stake, source, as-of date and control assessment. **Prefer equally suitable alternatives without such ownership; downgrade the affected product/company in shortlists and recommendations.** This is *not* the unconditional Tier 1 exclusion if the Russian stake is verified to be noncontrolling. If control is later established, escalate to Tier 1. Binding sanctions or other legal restrictions can independently forbid adoption.

**Tier 3 — PROVENANCE/OWNERSHIP REVIEW PENDING.** Apply when an ownership chain, beneficial owner, development origin or key upstream provider cannot be substantiated. Disclose the unresolved issue **without claiming verified Russian ownership**. Do not treat absence of evidence as proof of independence. For sensitive/high-impact selection, defer a safety or vendor-eligibility conclusion until the relevant verification is complete.

**Historical connection.** Record former ownership, previous operators and divestments with **effective dates**, but do not assert that a former investor still has a current stake or control. An artifact's independently established Russian technological origin can remain Tier 1 even if its current distributor is non-Russian.

These are **owner-defined trust, procurement and recommendation policies**, not findings that every Russian-linked artifact contains malware and not a blanket declaration that every such entity is sanctioned. Keep legal sanctions results as independently verified, jurisdiction-specific facts.

## Mandatory origin and ownership due diligence

Before accepting or recommending any materially relevant producer, model, dataset, service, software package, hardware product, agent skill or upstream artifact:

1. Identify the **legal publisher, developer, service operator, and registered jurisdictions**, distinguishing the brand from the legal entity and actual infrastructure/data operator.
2. Trace **parent companies, subsidiaries, intermediaries, ultimate beneficial owners, present and past shareholders, financing/investment where publicly attributable, and acquisitions or divestments**. Check direct/indirect ownership fractions when evidence permits; where fractions are not available, say so.
3. Check **voting/board appointment/veto rights, shareholder agreements or other evidence of de facto control** separately from nominal share percentages. Minority equity can sometimes carry control; aggregate/indirect ownership should be considered where supported.
4. Trace **model training/developer provenance, original checkpoint and code ownership, licensing, dependencies, datasets, OEM/white-label products, mirrors, API gateways, and rebrands**. A foreign-facing brand or intermediary does not remove the original artifact's provenance.
5. Consult **official company registers, beneficial-owner/PSC filings, securities filings, corporate ownership statements, and primary release repositories**. For legal compliance, check the [Ukrainian State Sanctions Register](https://drs.nsdc.gov.ua/) and other *applicable* official registers separately. The [UK Companies House PSC guidance](https://www.gov.uk/guidance/people-with-significant-control-pscs) illustrates why indirect shares and control rights require separate examination; its national disclosure thresholds **are not AI Lab's ownership-disclosure threshold**.
6. Record **source URL, observation/publication date, effective date, confirmed percentage where known, identified control mechanism, affected entity/artifact, confidence and unresolved gaps** in the existing supported canonical entity/requirements/evidence owners. Do **not** invent unsupported YAML schema keys. Revisit mutable ownership, mergers and jurisdiction details when relevant to a decision.

A person's **name, ethnicity, birthplace, native language or nationality alone** does not establish an entity's Russian ownership, technology origin or control. A person/entity's **documented ownership or controlling rights**, including through intermediaries, are relevant regardless of where the company markets itself. Avoid unsupported allegations from rumor or inferred identities.

## Documentation and recommendation behavior

- Place the applicable **Tier 1, Tier 2 or review-pending warning immediately below the title** of each affected reader-facing page, with a source-backed explanation and a link to this policy.
- Keep current ownership/provenance facts and the resulting recommendation status in the appropriate canonical entity notes and local requirements; render affected pages from their canonical owners.
- **Tier 1:** no positive recommendations, rankings for adoption, or sensitive/production integrations; use only for research/threat monitoring.
- **Tier 2:** keep the entity visible but **lower its recommendation priority**, present the verified partial ownership explicitly in comparisons, and prefer comparable independent alternatives. Never describe Tier 2 as cleared merely because an audit succeeded.
- **Tier 3:** disclose the verification gap, do not speculate about Russian ownership, and avoid treating unverified provenance as an independent/safe endorsement.
- Do not equate AI Lab's precautionary classification with an official sanctions determination or an independently reproduced technical-security finding.

## Research-only safety boundary

When strictly necessary to study a Tier 1 resource, use disposable isolated environments, restricted or disabled network egress, no secrets, no personal/confidential data, reviewed and revision-pinned code/dependencies, and legal/sanctions checks. Never send sensitive material to Russia-operated endpoints. These controls **do not change Tier 1's DANGEROUS — NOT RECOMMENDED classification**. Tier 2 and Tier 3 resources still require appropriate ordinary supply-chain, data-protection and legal review.

## Example and scope

Yandex's [official corporate contacts](https://yandex.com/company/contacts/moscow) identify its Moscow office and illustrate a Russian operator subject to Tier 1. This example does **not** establish the nationality, shareholding or control of unrelated companies. Other entities must be investigated through their own contemporaneous primary sources.
