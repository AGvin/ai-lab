# Agents and Automation Model Selection

Choose models for tool-using, multi-step, and agentic execution by evaluating the complete loop rather than chat quality alone.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Task scope

This area covers tool use and function calling, general agents, browser/desktop/mobile computer use, voice agents, planning and execution, long-running task execution, and models used as orchestrators or manager agents.

Small or inexpensive models may be useful as bounded workers, routers, extractors, or formatters without being reliable primary agents. Open weights, long context, low token price, or an `agentic` product label do not establish long-horizon reliability.

## What to evaluate

Evaluate the complete execution loop with the same tools, permissions, environment snapshot, initial context, and stopping rules:

- planning and task decomposition;
- tool selection and argument accuracy;
- structured-output reliability;
- recovery after tool or environment failures;
- context and state retention across long workflows;
- unnecessary loops, duplicate actions, and token use;
- compliance with permissions and human-approval boundaries;
- terminal acceptance, retries, corrections, wall-clock time, and total cost per accepted result.

Include adversarial and degraded cases such as missing files, timeouts, conflicting instructions, stale documentation, prompt injection, and failed verification.

Use application-level trust boundaries, least privilege, explicit stopping rules, and independent verification where risk requires it. Model safeguards are not a substitute for those controls.

## Candidate evaluation set

These candidates preserve useful hypotheses from the legacy agent guide and model-reference pages after current first-party identity/capability revalidation. They are **starting points for controlled evaluation, not a universal agent ranking**.

| Candidate | Evaluate for | Evidence state | Main boundary |
| --- | --- | --- | --- |
| [Qwen3 14B](../../../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-14b/) | Local/private routing, low-risk automation, and orchestrator experiments when one generalist is expected to draft, summarize, code, and coordinate | Provider-documented tool/agent capabilities plus explicit legacy AI Lab orchestrator hypothesis | Do not infer orchestrator reliability from general quality or model size; decomposition, state, tool use, completion, and escalation require independent tests |
| [GPT-5.6 Sol](../../../../../reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/sol/) | Complex hosted agents spanning coding, research, documents, tool use, and computer-use workflows | Current provider positioning for high-capability reasoning/coding/tool work; AI Lab loop reliability unverified here | Provider capability does not establish safe autonomy, best accepted-result cost, or reliable completion decisions |
| [Claude Sonnet 5](../../../../../reference/sub/producers/sub/anthropic/sub/claude/sub/sonnet/sub/models/sub/sonnet-5/) | Coding-heavy and tool-heavy agents using repositories, terminals, browsers, and knowledge-work tools | Current provider-documented coding and agentic strengths; AI Lab loop reliability unverified here | Exact scaffold, tool surface, correction behavior, stopping, and provider-specific constraints must be tested |
| [Gemini 3.6 Flash](../../../../../reference/sub/producers/sub/google/sub/gemini/sub/models/sub/gemini-3-6-flash/) | Rapid multimodal agent loops, structured output, function calling, code execution, files, and grounded workflows | Current provider-documented multimodal and agentic/tool capabilities; AI Lab loop reliability unverified here | Some capabilities can be preview or surface-dependent; recheck the exact API/tool surface before evaluation |
| [DeepSeek V4 Flash](../../../../../reference/sub/producers/sub/deepseek/sub/deepseek/sub/deepseek-v4/sub/models/sub/deepseek-v4-flash/) | High-volume bounded reasoning/tool workflows where economical hosted execution is a material hypothesis | Current provider-documented reasoning, JSON, tool-call, and agent-oriented API capabilities; AI Lab loop reliability unverified here | Data/privacy boundary, instruction following, retry rate, provider surface, and accepted-result economics require explicit evaluation |
| [Qwen3-Coder 30B-A3B Instruct](../../../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3-coder/sub/models/sub/qwen3-coder-30b-a3b-instruct/) | Self-hosted coding-agent and tool-use loops where a smaller MoE route than Qwen3-Coder-Next is worth controlled comparison | Provider-documented agentic-coding and tool-use positioning; AI Lab complete-loop reliability unverified here | 30.5B total / 3.3B active parameters do not establish residency, autonomy, stopping reliability, or dense-model equivalence; compare on the same scaffold and acceptance path |
| [Qwen3-Coder-Next](../../../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3-coder/sub/models/sub/qwen3-coder-next/) | Self-hosted coding-agent experiments, long-horizon code work, complex tool use, and recovery from execution failures | Provider-documented coding-agent model intended for local development; AI Lab loop reliability unverified here | Large total-weight footprint and runtime requirements can dominate deployment; active parameters are not a residency estimate |
| [Mistral Small 4](../../../../../reference/sub/producers/sub/mistral-ai/sub/mistral-small/sub/models/sub/mistral-small-4/) | Self-hosted multimodal generalist agents combining text/image understanding, reasoning, coding, and tool use | Current provider-documented multimodal, reasoning, coding, and agentic capabilities; AI Lab loop reliability unverified here | Large-model infrastructure and operator responsibility remain material; open weights do not prove economical or reliable autonomy |

Compact [Gemma 4 E2B Instruct](../../../../../reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e2b-instruct/) and [E4B Instruct](../../../../../reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e4b-instruct/) remain useful **bounded worker, router, extractor, or multimodal-preprocessor candidates**. Their provider-documented multimodal/function capabilities do not establish long-horizon planning, recovery, stopping, or primary-agent reliability.

[Qwen3 8B](../../../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-8b/) likewise remains an economical local baseline for bounded preprocessing, classification, summarization, or draft work, but the legacy documentation explicitly treated orchestrator, reviewer, and autonomous-coding suitability as **unproven until role-specific tests pass**. Preserve that negative boundary rather than promoting the model into a primary-agent shortlist from parameter count or tool-capability claims.

Candidate membership does not imply a recommendation state. Pin the exact model/version/artifact or hosted ID, freeze the tool/application surface, record the evaluation date, and recheck mutable availability, preview features, limits, and prices before a material decision.

## Orchestrator or manager model

The best worker model is not automatically the best orchestrator. When selecting a model to coordinate agents or tools, evaluate whether the exact model can reliably perform the **control role** under the intended workflow constraints.

A candidate orchestrator should be tested on its ability to:

- translate a goal into explicit deliverables and acceptance criteria;
- decompose work into bounded tasks and identify material dependencies;
- recognize shared-state, ordering, and conflict risks before recommending parallel execution;
- assign suitable workers/models/tools according to role, permissions, quality target, and evidence;
- preserve concise workflow state, decisions, unresolved risks, and evidence across steps;
- validate worker completion claims against observable artifacts or independent checks rather than trusting self-report;
- request targeted correction while preserving already valid work;
- distinguish a correctable defect from a capability gap, missing input, permission failure, or contradictory requirement;
- stop or escalate when retries, quality limits, risk, or expected accepted-result cost justify a different route;
- make a terminal completion decision only after the declared acceptance path has passed.

Evaluate dependency mistakes, unsafe/false parallelism decisions, worker/tool assignment accuracy, missed constraints, unnecessary expensive escalations, repeated correction loops, premature completion, and final criterion coverage. A model that is strong at producing work but weak at monitoring evidence or stopping can still be a poor orchestrator.

### Orchestrator stopping and escalation

Set the target quality and stop conditions before evaluation. A valid orchestrator should stop when every required criterion passes, when an authorized known limitation is accepted, when a declared retry/review budget is exhausted, when the requirement is impossible or contradictory, or when human judgment or a stronger/specialist route has higher expected value than another same-model attempt.

Attach assignment-specific reliability evidence from the [Model Selection methodology](../../../..) and use [Model Teams](../model-teams/) for portfolio/routing/escalation topology. The producing worker or orchestrator must not be the sole authority on its own completion when independent verification is material.

## Ownership boundary

This page evaluates **model capability for agent/orchestrator roles**. Designing the actual workflow engine or execution graph, choosing orchestration software, coordinating branches/workspaces, managing runtime/service lifecycle, GPU residency, provider resource startup/teardown, billing reconciliation, or infrastructure fault recovery are broader software/deployment/operations concerns and remain outside this subtree.

Those operational conditions may be recorded as frozen evaluation context when they materially affect model behavior, but they are not themselves reasons to classify an orchestration system as a model-selection page.

Link intrinsic model facts from [Model Reference](../../../../../reference/) and keep agent-workload evidence here.
