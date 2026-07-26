# AI Glossary

Short definitions for AI terms used across model, comparison, deployment, and workflow documentation.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Model ecosystem status

Ecosystem status describes adoption, tooling support, documentation maturity, integration availability, and operational familiarity. It is independent from model architecture, relative scale, capability-frontier position, access model, and quality for a specific task.

### Experimental

A model, artifact, or integration with limited validation, immature tooling, unstable interfaces, narrow availability, or substantial operational uncertainty.

Experimental does not necessarily mean weak. A newly released high-capability model can be experimental while its runtimes and deployment practices mature.

### Emerging

A model or ecosystem gaining meaningful adoption and support but not yet broadly established across common tools, providers, documentation, and production workflows.

Emerging indicates growing practical relevance, not guaranteed long-term adoption.

### Mainstream

Widely adopted and broadly supported within the current industry or relevant community.

`Mainstream` describes ecosystem adoption and maturity. It does **not** mean:

- best or highest quality;
- newest or frontier;
- largest or an LLM;
- dense, sparse, or MoE;
- open-source, open-weight, or proprietary;
- free or inexpensive;
- safe, unbiased, or suitable for every task.

A model can be mainstream but no longer frontier. A frontier model can be emerging or experimental rather than mainstream.

### Legacy

A model, artifact, interface, or ecosystem retained for compatibility or historical use after newer alternatives have become the primary path.

Legacy does not automatically mean unusable. It may remain appropriate when compatibility, reproducibility, hardware limits, validated behavior, or migration cost matters.

## Applying ecosystem status

Use ecosystem status only when it helps model selection or maintenance. Base it on observable signals such as:

- support in major inference runtimes and model-serving tools;
- availability through established providers or official distributions;
- active integrations and compatible tooling;
- documentation quality and operational knowledge;
- community or organizational adoption;
- maintenance activity and release support;
- known production use where evidence is available.

Record a verification date when the status is decision-relevant because ecosystem maturity changes over time.

Recommended compact field:

```text
Ecosystem status: Experimental | Emerging | Mainstream | Legacy | Unclear
Verified: YYYY-MM-DD
```

Do not infer ecosystem status from download count, one leaderboard, social attention, or model age alone.

## Related concepts

- [Model Classification](../concepts/sub/model-classification/)
- [Small and Large Language Models](../concepts/sub/model-classification/sub/language-model-scale/)
- [Frontier Models](../concepts/sub/model-classification/sub/frontier-models/)
- [Model Architectures](../concepts/sub/model-architectures/)
