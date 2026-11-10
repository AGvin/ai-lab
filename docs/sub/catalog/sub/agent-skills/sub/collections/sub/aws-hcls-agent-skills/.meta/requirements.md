# Documentation Requirements

## Requirements

- Identify AWS HCLS Agent Skills as the AWS Labs open-source collection of healthcare and life-sciences Agent Skills covering domain reasoning and executable/pipeline procedures.
- Preserve the collection boundary rather than materializing every individual skill as a canonical peer unless a later intake review establishes independent catalog value for selected skills.
- Treat the exact number of skills, domain count, skill inventory, categories, supported harnesses, installation commands, agent configurations, and evaluation results as freshness-sensitive: the AWS launch article described 38 skills across 11 HCLS domains, while the current upstream repository has already expanded beyond that launch snapshot.
- Preserve compatibility with the Agent Skills format/open standard as source-backed implementation metadata without turning cross-tool compatibility into ownership by any one assistant or platform.
- Keep Kiro, Strands Agents, AgentCore, Amazon Quick, Claude Code, Codex, and other supported harnesses/services with their own canonical owners.
- Keep medical/scientific framework content source-attributed and preserve the upstream disclaimer that the collection is demonstrative and not a substitute for professional medical advice or clinical use.
- Treat AWS-reported evaluation results as producer evidence rather than independent AI Lab validation.
- Explain reasoning skills (domain methodologies and decision frameworks) separately from pipeline skills (tool commands, parameters and runnable workflows). Collection inventory, domain counts and host support remain mutable.
- Scope the publisher's evaluation correctly: 410 test prompts (380 single-skill plus 30 cross-skill), Claude Opus 4.7 as judge, and different agentic CLI (69.5%) versus clean SDK (85.9%) comparison outcomes. These are publisher-run response comparisons, not clinically validated accuracy or independently reproduced AI Lab experiments.
- Surface the publisher's express demonstration-only, not-for-clinical-use and not-for-production limitations. Human scientific review, HIPAA applicability, any required AWS Business Associate Addendum (BAA), protected-health-information processing, and configuration remain separate obligations.
- Treat the MIT-0 root license as source distribution terms, not authorization to access clinical records or to execute AWS pipeline operations.

## Validation

- The entity remains a skill collection rather than a healthcare/life-science concept or a duplicate identity for its supported agent harnesses.
- Producer provenance resolves bidirectionally to Amazon Web Services.
- Mutable skill/domain counts are not frozen from either the launch article or a single repository snapshot.
- Individual skills are not eagerly materialized solely for symmetry.

## Source and safety reconciliation — 2026-11-08

- Checked pinned [upstream README](https://github.com/awslabs/hcls-agent-skills/blob/4603541c396cdd845dbae554800a65132d12bb63/README.md), [evaluation report](https://github.com/awslabs/hcls-agent-skills/blob/4603541c396cdd845dbae554800a65132d12bb63/eval/TECHNICAL_REPORT.md), and [MIT-0 LICENSE](https://github.com/awslabs/hcls-agent-skills/blob/4603541c396cdd845dbae554800a65132d12bb63/LICENSE). The report measures 38 evaluated skills plus cross-skill categories; the collection's published inventory is separately mutable.
- This bounded source correction does not validate healthcare outcomes, complete skills/dependencies/license clearance, installation or HIPAA compliance.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
