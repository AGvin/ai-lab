# Petri

Petri is an open-source automated behavioral auditing framework originally released by Anthropic and maintained by Meridian Labs as Inspect Petri.

## Evaluation role and boundaries

It coordinates an auditor, target model and judge through simulated scenarios and multi-turn interactions. Dish realism extensions and Bloom integration broaden scenarios but do not make Petri a fixed benchmark dataset or a replacement for the Inspect AI runtime.

## Reproducibility and operational safeguards

Audit results vary with seed scenarios, auditor/judge models, target scaffold, prompts, tools and release versions. Automated judges are not objective ground truth. Use authorized test environments, bound model/API budgets and govern retention of potentially sensitive transcripts.

## Relations

- Originally produced by: [Anthropic](../../../../../../../producers/sub/a/sub/anthropic/)
- Maintained by: [Meridian Labs](../../../../../../../producers/sub/m/sub/meridian-labs/)

## Official resources

- [Original research](https://www.anthropic.com/research/petri-open-source-auditing)
- [Maintained source](https://github.com/meridianlabs-ai/inspect_petri)
