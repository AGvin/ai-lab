# Choosing Models for AI Agents

Use this guide to shortlist models for tool-using agents, multi-step workflows, browser or computer use, and autonomous or semi-autonomous execution.

## Translations

- English
- [Українська](./l10n/uk_UA/)

**Status:** Shortlist structure updated on 2026-07-26. Provider claims, model access, pricing, and behavior change; production adoption requires task-specific evaluation.

## Quick picks

| Need | First candidate | Model type | Scale | Route | Main reason |
| --- | --- | --- | --- | --- | --- |
| Maximum hosted capability | [GPT-5.6 Sol](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/sol/) | General-purpose reasoning and agent model | LLM | Hosted | Difficult, long-running professional workflows across coding, research, documents, and computer use |
| Balanced coding and tool use | [Claude Sonnet 5](../../../../../../../software/sub/models/sub/anthropic/sub/claude/sub/sonnet-5/) | General-purpose agentic model with strong coding capability | LLM | Hosted | Strong repository, terminal, browser, and professional-work fit without the highest hosted tier |
| Fast multimodal loops | [Gemini 3.6 Flash](../../../../../../../software/sub/models/sub/google/sub/gemini/sub/gemini-3-6-flash/) | Multimodal general-purpose agent model | LLM | Hosted | Multimodal inputs, native tools, long context, and lower-latency loops |
| Cost-oriented hosted execution | [DeepSeek V4 Flash](../../../../../../../software/sub/models/sub/deepseek/sub/deepseek-v4/sub/flash/) | General-purpose reasoning and tool-use model | LLM | Hosted | Low token price, tool calls, structured output, and high concurrency |
| Controlled coding-agent experiment | [Qwen3-Coder-Next](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3-coder/sub/qwen3-coder-next/) | Coding-specialized agent model | LLM | Self-hosted | Open weights, coding-agent focus, long context, and provider independence |
| Self-hosted multimodal generalist | [Mistral Small 4](../../../../../../../software/sub/models/sub/mistral-ai/sub/mistral-small/sub/mistral-small-4/) | Multimodal general-purpose agent model | LLM | Self-hosted | Apache-2.0, text, image understanding, reasoning, and coding in one model |

These are starting candidates, not a universal ranking.

## Economical SLM candidates

No SLM currently meets the evidence threshold for a general recommendation as the primary model for long-running, tool-using agent workflows on this page.

Small models can still be useful as bounded workers, classifiers, routers, extractors, or formatters. Do not promote one to the primary agent role solely because it is inexpensive or fits local hardware. Validate planning, tool selection, argument accuracy, recovery, context retention, stopping behavior, and accepted-result cost on the complete loop.

A sparse model with a low active-parameter count is not automatically an SLM. Classify scale from the canonical model definition rather than active MoE parameters, quantization size, latency, or hosted price.

## Hosted candidates

| Candidate | Model type | Scale | Best fit | Main limitation | Official evidence |
| --- | --- | --- | --- | --- | --- |
| [GPT-5.6 Sol](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/sol/) | General-purpose reasoning and agent model | LLM | Maximum-capability professional agents spanning coding, research, documents, and computer use | Paid hosted access, provider limits, and workflow-specific tool validation | [Launch](https://openai.com/index/gpt-5-6/) · [Availability](https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt/) |
| [Claude Sonnet 5](../../../../../../../software/sub/models/sub/anthropic/sub/claude/sub/sonnet-5/) | General-purpose agentic model with strong coding capability | LLM | Coding-heavy and tool-heavy agents using repositories, terminals, browsers, and knowledge-work tools | Hosted data path, provider moderation, and independent validation of comparative claims | [Announcement](https://www.anthropic.com/news/claude-sonnet-5) |
| [Gemini 3.6 Flash](../../../../../../../software/sub/models/sub/google/sub/gemini/sub/gemini-3-6-flash/) | Multimodal general-purpose agent model | LLM | Rapid multimodal loops, function calling, structured output, code execution, grounding, and Google integrations | Preview capabilities, changing API behavior, and release monitoring | [Model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash) · [Latest models](https://ai.google.dev/gemini-api/docs/latest-model) |
| [DeepSeek V4 Flash](../../../../../../../software/sub/models/sub/deepseek/sub/deepseek-v4/sub/flash/) | General-purpose reasoning and tool-use model | LLM | High-volume tool calling and structured output where API cost is a primary constraint | Jurisdiction, data handling, instruction following, and retry cost require explicit evaluation | [Models and pricing](https://api-docs.deepseek.com/quick_start/pricing/) |

## Open-weight and self-hosted candidates

| Candidate | Model type | Scale | Architecture signal | Best fit | Main limitation | Official evidence |
| --- | --- | --- | --- | --- | --- | --- |
| [Qwen3-Coder-Next](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3-coder/sub/qwen3-coder-next/) | Coding-specialized agent model | LLM | Sparse MoE; 80B total and 3B active parameters | Controlled coding-agent experiments with local deployment, customization, or provider independence | Memory use depends on artifact, precision, context, and runtime; official claims need scaffold-specific validation | [Model card](https://huggingface.co/Qwen/Qwen3-Coder-Next) |
| [Mistral Small 4](../../../../../../../software/sub/models/sub/mistral-ai/sub/mistral-small/sub/mistral-small-4/) | Multimodal general-purpose agent model | LLM | Sparse MoE; 119B total and 6B active parameters | Organizations needing one self-hostable model for text, image understanding, reasoning, and agentic coding | Demanding multi-GPU infrastructure and full operator responsibility for safety and reliability | [Announcement](https://mistral.ai/news/mistral-small-4/) |

Open weights do not imply unrestricted use, low deployment cost, or safe autonomous execution.

## Workload view

| Agent workload | Prefer | Escalate or reject when |
| --- | --- | --- |
| Repository and terminal work | Claude Sonnet 5, GPT-5.6 Sol, or Qwen3-Coder-Next under a controlled scaffold | The model repeatedly misuses tools, skips verification, or cannot recover from execution failures |
| Browser and computer use | GPT-5.6 Sol or a validated hosted route with explicit computer-use support | The capability is preview-only, the environment cannot be isolated, or approval boundaries are unclear |
| Multimodal document or media workflows | Gemini 3.6 Flash or another validated multimodal route | Required modalities, file sizes, context, grounding, or data terms are unsupported |
| High-volume bounded tool loops | Gemini 3.6 Flash or DeepSeek V4 Flash after validation | Retry rate, human correction, or failed actions erase the apparent token-price saving |
| Private or provider-independent coding agent | Qwen3-Coder-Next on measured infrastructure | Hardware, context, concurrency, or accepted-result quality cannot meet the target |
| Bounded subagent task | A validated smaller specialist may be used | The task requires long-horizon planning, broad context, destructive actions, or independent judgment |

## What to measure

Agent quality is not chat quality. Evaluate the complete loop:

1. planning and task decomposition;
2. tool selection and argument accuracy;
3. structured-output reliability;
4. recovery after tool or environment failures;
5. context retention during long workflows;
6. unnecessary loops, repeated actions, and token use;
7. compliance with permissions and human approval boundaries;
8. terminal acceptance, wall-clock time, retries, human corrections, and total cost per accepted result.

Use the same tools, permissions, repository or environment snapshot, initial context, and stopping rules for each candidate. Include missing files, timeouts, conflicting instructions, stale documentation, prompt injection, and failed verification in the evaluation suite.

## Decision and escalation rule

Use the least expensive validated route that consistently reaches the required acceptance tier. A lower token price, smaller active parameter count, local deployment, or open weights are not enough by themselves.

Escalate to a stronger model, different specialist, deterministic validator, or human reviewer when the current assignment repeatedly fails for capability reasons. Retry only failures likely to improve under the same assignment.

## Safety and operations

Agents that browse, execute code, modify repositories, send messages, or operate accounts need explicit trust boundaries. Use least privilege, sandbox untrusted code, require approval for destructive or external actions, and keep auditable logs. Model safeguards are not a substitute for application-level controls.

A model marketed as agentic still requires explicit state, bounded retries, verification, stopping rules, and resource lifecycle controls.

## Related guides

- [Coding](../coding/)
- [Combined Workloads](../combined-workloads/)
- [Agent Role Selection](../agent-role-selection/)
- [Reliability Profiles](../reliability-profiles/)
- [Orchestration](../orchestration/)
- [Agentic Systems](../../../agentic-systems/)
- [Model Selection Methodology](../methodology/)
- [AI Model Selection and Team Design](../../)
