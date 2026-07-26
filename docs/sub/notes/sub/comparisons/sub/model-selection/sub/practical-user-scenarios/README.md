# Practical AI User Scenarios

Choose a solution from the person, tasks, hardware, budget, skills, and data boundary—not from model popularity alone.

**Verified:** 2026-07-26. These are starting routes, not permanent rankings. Recheck current limits, prices, availability, and data terms.

## Quick map

| Scenario | Start here | Upgrade when |
| --- | --- | --- |
| Student on a minimal budget | Rotate free hosted assistants | One service becomes a daily tool |
| Everyday home or office user | One managed assistant | Work data needs organization controls |
| Software engineer without a GPU | Small local coder plus hosted fallback | CPU latency blocks useful work |
| Gamer with an existing GPU | Local 7B–8B quantized model | Quality or VRAM becomes the limit |
| Mac developer or creator | Native local runtime plus hosted fallback | Larger unified memory is already available |
| AI enthusiast or home-lab owner | One resident local model | Specialist or larger workloads appear |
| Small content business | Managed tools first | Repeated work justifies API automation |
| Software development company | Managed coding-agent pilot | Sustained usage justifies central routing or hosting |
| Business knowledge assistant | Managed business assistant or bounded RAG | Volume, permissions, or privacy require control |
| Sensitive-data professional | Approved enterprise or local route | External processing is contractually permitted |

## 1. Student on a minimal budget

**Typical setup:** basic laptop, little spare money, and limited administration experience.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Free rotation | Use free [ChatGPT](../../../../../../../software/sub/assistants/sub/chatgpt/), Claude, and Gemini accounts; move to another service after a current limit is reached | Browser or mobile device | Limits and available models change; do not upload private university, employer, or third-party data |
| One subscription | Pay for the assistant that performs best on the student's actual writing, study, coding, and file tasks | No local AI hardware | Subscription access still has usage and product limits |
| Offline experiment | Run [Phi-4 Mini Instruct](../../../../../../../software/sub/models/sub/microsoft/sub/phi/sub/phi-4/sub/mini-instruct/) or [Qwen3 8B](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3/sub/8b/) `Q4_K_M` through [LM Studio](../../../../../../../software/sub/inference/sub/lm-studio/) | Existing laptop with roughly 16–32 GB system RAM; measure speed | CPU inference can be slow and quality is below stronger hosted models |

## 2. Everyday home or office user

**Typical setup:** ordinary laptop; wants writing, summaries, planning, file help, and minimal setup.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Simplest | Use one managed assistant such as ChatGPT, Claude, or Gemini | Browser, desktop, or mobile app | Consumer accounts may be unsuitable for confidential work data |
| Work use | Use an organization-approved business or enterprise workspace | Managed account and administrator | Higher price, policy, and administrator dependencies |
| Private routine work | Run Phi-4 Mini Instruct or Qwen3 8B `Q4_K_M` through LM Studio | 16–32 GB system RAM | Local setup and lower capability may outweigh privacy benefits |

Self-hosting is not automatically cheaper after setup, updates, failures, and user support are counted.

## 3. Software engineer without a local GPU

**Typical setup:** business laptop with 32 GB RAM, strong Linux and server skills, but no useful discrete GPU.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Existing laptop | Use [Qwen2.5-Coder 3B Instruct](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen2-5-coder/sub/3b-instruct/), [Qwen2.5-Coder 7B Instruct](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen2-5-coder/sub/7b-instruct/), or Qwen3 8B `Q4_K_M` through LM Studio | CPU and 16–32 GB RAM | Useful for private, bounded tasks; long contexts and agent loops are slow |
| Hourly GPU | Start an on-demand 24 GB GPU and serve [Qwen3 14B](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3/sub/14b/) `Q4_K_M`; test [Qwen3 30B-A3B](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3/sub/30b-a3b/) `Q4_K_M` only as a constrained sequential route | RTX 3090/4090-class rented GPU, [Ollama](../../../../../../../software/sub/inference/sub/ollama/) or another measured runtime | Storage, startup, shutdown, and forgotten idle billing |
| Hosted coding | Use [Cursor](../../../../../../../software/sub/development/sub/code-editors/sub/cursor/), [Codex](../../../../../../../software/sub/agents/sub/openai-codex/), or another approved coding service for time-sensitive work | Subscription or API access | Cost, usage limits, and source-code data path |

A generic CPU VPS can be slower than a modern laptop despite more advertised vCPUs and RAM. Benchmark the exact host, model artifact, context, and runtime before committing to it.

## 4. Gamer with an existing GPU

**Typical setup:** gaming PC with an 8–16 GB GPU and little interest in server administration.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Desktop local | Run Qwen3 8B or Qwen2.5-Coder 7B `Q4_K_M` through LM Studio | 8–16 GB VRAM, depending on context and offload | Games, displays, context cache, and other applications share GPU memory |
| Local API | Serve the same measured model through Ollama when several applications need it | Existing gaming PC | Service security, updates, power, and availability |
| Hybrid | Keep the local model for routine work and use [GPT-5.6 Luna](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/luna/) or [Gemini 3.6 Flash](../../../../../../../software/sub/models/sub/google/sub/gemini/sub/gemini-3-6-flash/) for harder tasks | Local GPU plus hosted access | Data classification must decide what may leave the device |

Do not buy another GPU until the existing card has been measured on the intended models and context sizes.

## 5. Mac developer or creator

**Typical setup:** Apple-silicon Mac used for coding, writing, design, or media work.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| 16 GB class | Run Phi-4 Mini Instruct or Qwen3 8B `Q4_K_M` in a native local runtime | Apple silicon with 16 GB unified memory | Unified memory is shared with macOS and applications |
| 32 GB+ class | Evaluate Qwen3 14B `Q4_K_M` locally | Apple silicon with 32 GB or more unified memory | Model fit does not guarantee acceptable speed or long-context behavior |
| Hybrid | Keep private routine tasks local and escalate difficult tasks to a managed assistant or API | Local runtime plus hosted access | Requires an explicit data-routing rule |

Confirm runtime and model support before purchasing additional memory primarily for AI.

## 6. AI enthusiast or home-lab owner

**Typical setup:** owns or plans a GPU workstation or server and accepts infrastructure work.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Resident generalist | Keep Qwen3 14B `Q4_K_M` loaded behind Ollama or another managed service | One measured 24 GB GPU | Idle power, service exposure, maintenance, and context memory |
| Larger sequential route | Unload the resident model and load Qwen3 30B-A3B `Q4_K_M` only for tasks where it wins | One 24 GB GPU only after peak-memory validation; 48 GB is less constrained | Model switching and failure recovery |
| Temporary specialist | Rent a cloud GPU for larger language models or media generation; retain a hosted API fallback | On-demand GPU provider | Lifecycle automation and verified billing shutdown |

Include electricity, storage, remote-access security, backups, updates, and operator time in total cost.

## 7. Small content business

**Typical setup:** a channel, community, or small team repeatedly creates posts, images, scripts, or memes.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Manual managed | Use ChatGPT, Claude, or Gemini for text and an approved hosted image tool | Managed subscriptions | Manual repetition and inconsistent brand output |
| API workflow | Use Gemini 3.6 Flash, GPT-5.6 Luna or [GPT-5.6 Terra](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/terra/) for text and multimodal steps; add OpenRouter only when multi-provider routing is useful | API budget and workflow engine | Retries, generated volume, moderation, and review cost |
| Hybrid production | Keep Qwen3 14B resident and use [FLUX.1-schnell](../../../../../../../software/sub/models/sub/black-forest-labs/sub/flux/sub/flux-1-schnell/) on a separately measured 24 GB+ worker or temporary GPU | Local or rented GPU operations | Rights, disclosure, brand review, and media-worker lifecycle |

> OpenRouter is convenient, but sensitive data needs explicit privacy controls. [Details](../../../../../../../software/sub/model-platforms/sub/openrouter/#openrouter-data-safety).

## 8. Software development company

**Typical setup:** several or tens of developers use coding assistants or agents, and included usage can be exhausted unevenly.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Managed pilot | Pilot Cursor, Codex, or Claude Code with representative repositories and users | Per-seat or bundled access | Included usage, client data routing, and weak cost attribution |
| Central hosted routing | Use approved enterprise APIs such as GPT-5.6 Terra or Sol, [Claude Sonnet 5](../../../../../../../software/sub/models/sub/anthropic/sub/claude/sub/sonnet-5/), and Gemini 3.6 Flash through a controlled gateway | Central identity, budgets, logs, and vendor contracts | Gateway operation and provider dependency |
| Shared self-hosted | Use Qwen2.5-Coder 7B for low-risk bounded work and evaluate [Qwen3-Coder-Next](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3-coder/sub/qwen3-coder-next/) on a large-memory or multi-GPU server; retain hosted escalation | Dedicated AI platform and operations team | Hardware fit is unproven until exact artifacts, context, concurrency, and accepted-result quality are measured |

Coding agents can execute commands and modify files. Isolate them in VMs, containers, or other sandboxes with least privilege and approval gates.

> Cursor and Codex can send code or context to vendor infrastructure. Local execution or a self-hosted model endpoint does not prove the complete client path is local. [Cursor details](../../../../../../../software/sub/development/sub/code-editors/sub/cursor/#cursor-data-safety) · [Codex details](../../../../../../../software/sub/agents/sub/openai-codex/#codex-data-safety).

See [Choosing Models for AI Agents](../agents/) for execution safeguards.

## 9. Business knowledge assistant

**Typical setup:** employees need answers from internal policies, product information, support material, or document collections.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Managed assistant | Use an approved business assistant with connected documents and organization controls | Managed workspace | Connector permissions, freshness, and vendor lock-in |
| Managed RAG | Use Gemini 3.6 Flash or GPT-5.6 Terra with approved embedding, retrieval, and citation stages | API, document store, access-control integration | Retrieval quality and permission mistakes |
| Self-hosted RAG | Use Qwen3 14B with separately evaluated embedding and reranking models | 24 GB GPU or measured server | Operations, evaluation, access control, and lower quality ceiling |

Require source citations, document-level permissions, freshness checks, and human escalation. Retrieval does not make an incorrect answer safe.

## 10. Sensitive-data professional

**Typical setup:** legal, accounting, healthcare, consulting, or other confidential or regulated work.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Contracted enterprise | Use an enterprise service only after retention, region, access, audit, training, and subprocessors are approved | Organization-managed account and contract | Cost and vendor dependency |
| Private managed API | Use a provider project or private deployment approved for the exact data class | Approved cloud and identity controls | Data still leaves the endpoint owner unless the architecture proves otherwise |
| Local-only | Run Phi-4 Mini, Qwen3 8B, or Qwen3 14B locally according to hardware and quality needs | 16–32 GB RAM for smaller models or a measured 24 GB GPU for Qwen3 14B | The local quality ceiling may require human work or prohibit the task |

Do not choose a free consumer service, aggregator, or coding client only because it is convenient. Confirm the complete provider chain and legal basis first.

## Selection rules

- Existing hardware is a constraint, not a reason to force local inference.
- A subscription can be cheaper than self-hosting when administration time is included.
- Local inference is most defensible for privacy, stable high volume, offline use, or provider independence.
- Cloud GPUs fit temporary heavy workloads better than an always-running generic CPU VPS.
- Agents need stronger isolation and approval boundaries than chat assistants.
- Compare total cost per accepted result, including retries and human correction.

For detailed hardware portfolios, continue to [Concrete Model Portfolio Profiles](../combined-workloads/sub/environment-profiles/). For evaluation rules, see [Model Selection Methodology](../methodology/).

## Sources

- [ChatGPT Free Tier FAQ](https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq)
- [Claude plans and pricing](https://claude.com/pricing)
- [Gemini Apps limits and upgrades](https://support.google.com/gemini/answer/16275805)
