# Bloom

Bloom is an open-source framework for generating targeted behavioral evaluation suites for AI models from seed definitions.

## Evaluation role and boundaries

Its workflow develops behavior specifications, scenarios, model rollouts and judgments to form a configurable evaluation suite. Anthropic originally released Bloom; the former standalone repository is frozen, and Meridian Labs maintains the ongoing Petri Bloom implementation.

## Reproducibility and operational safeguards

Generated suites vary with behavior seeds, prompts, target model, judge configuration, scenario generation and implementation version. Treat scores from differently generated suites as incomparable without full configuration provenance. Isolate tool-using target agents and handle judged transcripts with appropriate privacy controls.

## Relations

- Originally produced by: [Anthropic](../../../../../../../producers/sub/a/sub/anthropic/)
- Maintained by: [Meridian Labs](../../../../../../../producers/sub/m/sub/meridian-labs/)

## Official resources

- [Anthropic research](https://www.anthropic.com/research/bloom)
- [Maintained source](https://github.com/meridianlabs-ai/petri_bloom)
- [Historical source](https://github.com/safety-research/bloom)
