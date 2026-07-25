# Choosing Models for AI Agents

Use this guide to shortlist models for tool-using agents, multi-step workflows, browser or computer use, and autonomous or semi-autonomous execution.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Initial shortlist verified on 2026-07-23. Provider claims and model availability can change; production adoption requires task-specific evaluation.

## What matters most

Agent quality is not the same as chat quality. Evaluate the complete loop:

- planning and task decomposition;
- tool selection and argument accuracy;
- structured-output reliability;
- recovery after tool or environment failures;
- context retention during long workflows;
- unnecessary loops, repeated actions, and token use;
- compliance with permissions and human approval boundaries;
- latency and cost across the complete run, not one response.

A model marketed as agentic may still require a strong scaffold, explicit state, bounded retries, and verification steps.

## Initial recommendations

### Frontier hosted agents

#### GPT-5.6 Sol

**Recommendation:** Preferred candidate for difficult, long-running professional agents where maximum capability is more important than lowest cost.

OpenAI describes GPT-5.6 Sol as its flagship model for complex work across coding, research, cybersecurity, science, computer use, and design. The GPT-5.6 family is available through the OpenAI API, Codex, and selected ChatGPT surfaces.

**Use when:**

- the workflow spans coding, research, documents, and computer use;
- failures are expensive enough to justify a frontier model;
- configurable reasoning depth is useful;
- hosted provider safeguards and data handling are acceptable.

**Limitations:**

- paid hosted access;
- provider moderation and operational limits apply;
- availability and product-specific access can differ between Sol, Terra, and Luna;
- verify tool-call behavior in the exact API and agent scaffold.

Source: [GPT-5.6 launch](https://openai.com/index/gpt-5-6/) and [GPT-5.6 availability](https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt/).

#### Claude Sonnet 5

**Recommendation:** Preferred balanced candidate for coding-heavy and tool-heavy agents that need strong autonomy without Opus-class cost.

Anthropic presents Sonnet 5 as its most agentic Sonnet model, with planning, browser and terminal tool use, coding, and professional-work capabilities. Anthropic states that its performance is close to Opus 4.8 at a lower price.

**Use when:**

- the agent works primarily with repositories, terminals, browsers, and knowledge-work tools;
- long-running instruction following and tool use are central;
- Claude Code or Anthropic-compatible agent infrastructure is already in use.

**Limitations:**

- hosted and provider-moderated;
- official comparative claims require independent validation on the target workflow;
- prompt-injection resistance does not remove the need for trust boundaries and least privilege.

Source: [Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5).

#### Gemini 3.6 Flash

**Recommendation:** Preferred price-performance candidate for rapid agent loops, multimodal inputs, code execution, and native Google tools.

Google documents Gemini 3.6 Flash as a stable model optimized for agentic execution, code generation, multimodal and spatial reasoning. It supports function calling, structured output, code execution, search grounding, file search, and preview computer use with a 1M-token input context.

**Use when:**

- the agent processes text, images, video, audio, PDFs, or mixed inputs;
- high-frequency tool loops need lower latency and cost than flagship models;
- Google grounding, file search, or computer-use integrations are useful.

**Limitations:**

- hosted and provider-moderated;
- computer use remains a preview capability;
- current Gemini 3.x API behavior differs from earlier generations, including deprecated sampling controls;
- stable model aliases still need release monitoring.

Source: [Gemini 3.6 Flash model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash) and [latest Gemini models](https://ai.google.dev/gemini-api/docs/latest-model).

### Cost-oriented hosted agents

#### DeepSeek V4 Flash

**Recommendation:** Alternative for high-volume tool-calling and structured-output workloads where API cost is a primary constraint.

DeepSeek documents V4 Flash with thinking and non-thinking modes, a 1M-token context, JSON output, tool calls, and high concurrency.

**Use when:**

- the workflow can tolerate additional validation around tool execution and output quality;
- cost and throughput dominate the selection;
- an OpenAI-compatible or Anthropic-compatible API is useful.

**Limitations:**

- hosted provider and jurisdictional considerations require review;
- low token price does not guarantee lower total workflow cost if retries increase;
- do not select it without evaluating instruction following, tool-call accuracy, and data-handling requirements.

Source: [DeepSeek models and pricing](https://api-docs.deepseek.com/quick_start/pricing/).

### Open-weight and self-hosted agents

#### Qwen3-Coder-Next

**Recommendation:** Preferred open-weight candidate for local or controlled coding-agent experiments when infrastructure can support the model.

Qwen describes Qwen3-Coder-Next as an open-weight coding-agent model with 80B total parameters, 3B active parameters, 256K context, long-horizon reasoning, complex tool use, and recovery from execution failures.

**Use when:**

- local deployment, customization, or provider independence matters;
- the main workload is software development;
- integration with agent CLIs or IDE scaffolds is required.

**Limitations:**

- open weights do not mean unrestricted, unaligned, or inexpensive deployment;
- practical memory use depends on format, precision, quantization, context, and runtime;
- official benchmark claims need verification on the chosen quantization and scaffold.

Source: [Qwen3-Coder-Next model card](https://huggingface.co/Qwen/Qwen3-Coder-Next).

#### Mistral Small 4

**Recommendation:** Alternative open model for organizations that need one self-hostable model for text, image understanding, reasoning, and agentic coding.

Mistral Small 4 is released under Apache 2.0 and combines reasoning, multimodal input, general chat, and agentic coding. Mistral documents 119B total parameters with 6B active parameters per token, a 256K context window, and demanding multi-GPU infrastructure recommendations.

**Use when:**

- Apache 2.0 licensing and self-hosting are important;
- one model must cover general assistance, image input, reasoning, and code;
- substantial server infrastructure is available.

**Limitations:**

- despite the name, the documented deployment requirement is not small for consumer hardware;
- local operation requires runtime, quantization, throughput, and context testing;
- self-hosting shifts moderation, security, observability, and reliability responsibilities to the operator.

Source: [Introducing Mistral Small 4](https://mistral.ai/news/mistral-small-4/).

## Selection table

| Requirement | First candidates | Why |
| --- | --- | --- |
| Maximum hosted capability | GPT-5.6 Sol, Claude Sonnet 5 | Long-running professional, coding, and tool-heavy work |
| Fast multimodal agent loops | Gemini 3.6 Flash | Multimodal input, native tools, long context, stable production model |
| Low-cost hosted execution | DeepSeek V4 Flash | Tool calls, JSON output, long context, high concurrency |
| Local coding agent | Qwen3-Coder-Next | Open-weight model designed for coding agents and IDE/CLI scaffolds |
| Self-hosted general multimodal agent | Mistral Small 4 | Apache 2.0, reasoning, images, coding, and general chat |

This table is a shortlist, not a universal ranking.

## Evaluation protocol

Run each candidate through the same workflow suite:

1. Provide the same tools, permissions, repository snapshot, and initial context.
2. Measure task completion, human corrections, tool-call errors, retries, wall-clock time, and total tokens.
3. Include failure cases: missing files, tool timeouts, conflicting instructions, stale documentation, and prompt injection.
4. Check whether the model verifies its own changes instead of only reporting success.
5. Repeat with the exact production model version and reasoning configuration.
6. Record when a cheaper model can act as a subagent while a stronger model handles planning or review.

## Safety and operations

Agents that browse, execute code, modify repositories, send messages, or operate accounts need explicit trust boundaries. Use least privilege, sandbox untrusted code, require approval for destructive or external actions, and keep auditable logs. Model safeguards are not a substitute for application-level controls.

## Related guides

- [Coding](../coding/)
- [Combined Workloads](../combined-workloads/)
- [Agentic Systems](../../../agentic-systems/)
- [Model Selection Framework](../../)
