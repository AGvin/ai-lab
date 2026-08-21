# Model Teams

Choose a model portfolio only when role separation, routing, specialization, or independent evaluation produces a measurable benefit over one model.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Team-design boundary

Model-team selection covers role-based portfolios, model routing, and ensembles or consensus. Start with the smallest portfolio that can meet the complete workflow acceptance criteria.

The same model may cover several compatible roles when doing so does not create unacceptable conflicts, correlated failure, quality loss, latency, or cost. Add a specialist or independent model only when the measured gain justifies the additional model calls, context transfer, routing, review, and maintenance complexity.

This subtree selects **models and their roles**. GPU placement, concurrent/sequential loading, runtime lifecycle, cloud resource startup/shutdown, service topology, hardware purchasing, and environment-profile design are broader deployment/operations decisions and remain outside model-selection ownership.

## Portfolio topologies

Treat the simplest valid topology as the baseline and add complexity only when evidence requires it.

### Single generalist

One model covers all validated roles or compatible tasks. Prefer this baseline when it meets every required acceptance threshold and role-independence requirement. Reject it when a material task exceeds its verified quality ceiling or when independent review cannot credibly be performed by the same model/configuration.

### Generalist with specialist fallback

A generalist handles routine assignments while an exact specialist handles declared gaps. Use this only when the fallback trigger can be defined and tested. The worker's self-assessment alone is not a reliable escalation policy; deterministic evidence, an independent verifier, or explicit task rules may be required.

### Router with quality tiers

A router assigns work among lower-cost, standard, or stronger models according to explicit task/risk/quality conditions. Evaluate routing accuracy independently because misrouting and excessive escalation can erase the expected quality or cost benefit.

### Specialist team

Use distinct models for materially different tasks or roles when specialist quality or independence exceeds the simpler baseline by enough to justify the additional coordination cost. Do not create a specialist role merely because a specialized model exists.

### Ensemble or consensus

Use multiple independent candidates or judges only when disagreement handling or reduced correlated error materially improves the target decision. Diversity of model names is not sufficient evidence of independence; shared training lineage, provider stack, prompt context, or evaluation bias can still correlate failures.

## Current materialized guidance

- [`role-based-portfolios/`](./sub/role-based-portfolios/) — choose models by planner, worker, reviewer, verifier, evaluator, advisor, memory/context, and related role contracts.

Routing and ensemble branches are materialized only when reviewed task content requires them; the selected navigation is not created as an empty skeleton.

## Candidate portfolio hypotheses

The legacy environment profiles contained useful **model-role combinations** mixed together with hardware, residency, cloud, and resource-lifecycle design. The combinations below preserve only the model-selection part after current identity/capability revalidation. They are evaluation hypotheses, not current environment recommendations.

| Portfolio hypothesis | Candidate relationship to evaluate | Why retain it | Main boundary |
| --- | --- | --- | --- |
| Local text generalist with higher-capacity fallback | [Qwen3 14B](../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-14b/) as a routine local text/generalist baseline; [Qwen3 30B-A3B](../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-30b-a3b/) as a higher-capacity fallback candidate | Preserves the legacy hypothesis that a smaller routine core plus a larger bounded escalation can beat keeping the larger route universal | No VRAM class, quantization, residency, or quality superiority is implied; exact artifacts and escalation gain must be measured |
| Text core plus compact multimodal specialist | A validated text core plus [Gemma 4 E2B Instruct](../../../reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e2b-instruct/) or [E4B Instruct](../../../reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e4b-instruct/) for bounded image/document/UI/short-audio work | Preserves the legacy role-separation hypothesis without turning compact multimodality into a claim that Gemma should own every reasoning task | Specialist benefit, handoff quality, modality accuracy, and complete-workflow cost must beat one validated generalist; deployment placement stays outside this page |
| Economical hosted route with stronger bounded escalation | [DeepSeek V4 Flash](../../../reference/sub/producers/sub/deepseek/sub/deepseek/sub/deepseek-v4/sub/models/sub/deepseek-v4-flash/) or [GPT-5.6 Luna](../../../reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/luna/) for eligible lower-cost work; [GPT-5.6 Terra](../../../reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/terra/), [GPT-5.6 Sol](../../../reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/sol/), or [Claude Sonnet 5](../../../reference/sub/producers/sub/anthropic/sub/claude/sub/sonnet/sub/models/sub/sonnet-5/) as stronger/different escalation candidates | Preserves the legacy quality-tier routing hypothesis while separating model roles from old point-in-time price tables | Exact routing triggers, provider/data boundaries, independence, retry rate, accepted-result cost, aliases, availability, and current prices require fresh evidence |
| Generalist plus modality specialist | Add [Gemini 3.6 Flash](../../../reference/sub/producers/sub/google/sub/gemini/sub/models/sub/gemini-3-6-flash/) for a hosted multimodal route, [FLUX.1-schnell](../../../reference/sub/producers/sub/black-forest-labs/sub/flux/sub/flux-1/sub/models/sub/flux-1-schnell/) for text-to-image generation, or an exact [Whisper](../../../reference/sub/producers/sub/openai/sub/whisper/) checkpoint/model for ASR only when that specialist closes a measured task gap | Preserves the legacy specialist-augmentation hypothesis across perception, generation, and speech without pretending one model should cover all modalities | Pin exact specialist identity where the reference is family-level; prove task gain, handoff quality, rights/data boundary, review need, and coordination cost before adoption |

The legacy `pyannote/speaker-diarization-community-1` pipeline also appeared in these portfolios. It is not a model-team identity; use the canonical [`pyannote.audio`](../../../../../../sub/software/sub/model-and-data-platforms/sub/model-libraries/sub/pyannote-audio/) software/library owner when that pipeline is part of a broader workflow.

For task-specific candidate evidence, use [Software Development](../software-development/), [Agents and Automation](../agents-and-automation/), [Translation and Localization](../language-and-research/sub/translation-and-localization/), [Media Creation](../media-creation/), and [Content Understanding](../content-understanding/). Do not duplicate their complete shortlists here.

## Escalation and verification

Define bounded retries, escalation conditions, and terminal acceptance before execution. Escalate when repeated failures indicate a capability gap, an important requirement is repeatedly omitted, the expected retry/review cost exceeds a stronger route, or the task risk exceeds the current model's verified reliability.

Do not let the producing model be the only approver of its own output when independent verification is material. Depending on the assignment, verification may use deterministic tests, a separate reviewer/verifier model, a specialist evaluator, explicit acceptance criteria, artifact diffs/regression checks, or human approval.

A fallback model must satisfy the same relevant acceptance and data-boundary requirements as the primary route; being stronger or more expensive does not automatically make it a valid fallback.

## Portfolio evidence

Evaluate terminal workflow acceptance, role coverage, correlated errors, role independence, handoff quality, retries, escalation frequency, routing mistakes, model-call latency, review effort, and total cost per accepted result. Compare the proposed team against a single-generalist baseline rather than assuming more models improve quality.

Record exact participating model identities and evaluated roles. Link canonical facts for every participating model from [Model Reference](../../../reference/) rather than copying technical profiles here.

Operational residency and infrastructure metrics may be recorded as **evidence conditions** when they materially affect a model-team comparison, but selecting runtimes, GPU schedules, provider resources, or lifecycle automation belongs outside this subtree.
