# Practical AI User Scenarios

Choose a solution from the person, tasks, hardware, budget, skills, and data boundary—not from model popularity alone.

**Verified:** 2026-07-27. These are starting routes, not permanent rankings. Recheck current limits, prices, availability, and data terms.

## Terms

| Term | Meaning |
| --- | --- |
| Managed assistant | A ready website or app operated by a provider |
| API | A paid or limited service called by another application |
| Local | The model runs on the user's own device |
| Self-hosted | The user or organization operates the model server |
| Cloud GPU | A rented GPU computer that must be stopped when no longer needed |
| Quantized model | A compressed model variant that uses less memory but must be evaluated separately |
| RAG | A workflow that retrieves documents before generating an answer; retrieval does not guarantee correctness |

## Data boundary

| Data | Default route | [OpenRouter](../../../../../../../software/sub/model-platforms/sub/openrouter/#openrouter-data-safety) |
| --- | --- | --- |
| Public | Any route that meets cost and quality needs | Usually acceptable after checking the selected provider and terms |
| Internal | Organization-approved assistant or API | Use only with approved providers, logging policy, routing controls, and ZDR where required |
| Confidential | Contracted direct provider, private deployment, or local processing | Use only when both OpenRouter and the downstream provider are explicitly approved |
| Regulated | Local processing or a specifically approved contracted architecture | Usually avoid unless compliance and legal review approve the complete provider chain |

OpenRouter is a routing service, not a model. Use it when access to several providers or controlled fallback is valuable, not as a default extra intermediary.

## Quick map

| Scenario | Start here | Upgrade when |
| --- | --- | --- |
| Student on a minimal budget | Rotate free hosted assistants | One service becomes a daily tool |
| Everyday home or office user | One managed assistant | Work data needs organization controls |
| Software engineer without a GPU | Small local coder plus hosted fallback | CPU latency blocks useful work |
| Gamer with an existing GPU | Compact local model matched to text or multimodal tasks | Quality, context, or VRAM becomes the limit |
| Mac developer or creator | Native compact local runtime plus hosted fallback | Larger unified memory is already available |
| AI enthusiast or home-lab owner | One resident generalist plus measured specialist lanes | Specialist or larger workloads appear |
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
| Offline text experiment | Run [Phi-4 Mini Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/microsoft/sub/phi/sub/phi-4/sub/models/sub/phi-4-mini-instruct/) or [Qwen3 8B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-8b/) through [LM Studio](../../../../../../../software/sub/inference/sub/lm-studio/) or another supported runtime | Existing laptop with roughly 16–32 GB system RAM; measure speed | CPU inference can be slow and quality is below stronger hosted models |
| Offline multimodal experiment | Test [Gemma 4 E2B Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e2b-instruct/) with its official QAT artifact when image, document, or short-audio input matters | Supported local runtime and enough RAM for the model, multimodal projection, context, and applications | Runtime modality support and compact-model quality require validation |

## 2. Everyday home or office user

**Typical setup:** ordinary laptop; wants writing, summaries, planning, file help, and minimal setup.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Simplest | Use one managed assistant such as ChatGPT, Claude, or Gemini | Browser, desktop, or mobile app | Consumer accounts may be unsuitable for confidential work data |
| Work use | Use an organization-approved business or enterprise workspace | Managed account and administrator | Higher price, policy, and administrator dependencies |
| Private text work | Run [Phi-4 Mini Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/microsoft/sub/phi/sub/phi-4/sub/models/sub/phi-4-mini-instruct/) or [Qwen3 8B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-8b/) in a supported local runtime | 16–32 GB system RAM as a starting range; measure the exact artifact | Local setup and lower capability may outweigh privacy benefits |
| Private files and media | Test [Gemma 4 E2B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e2b-instruct/) or [E4B Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e4b-instruct/) for bounded text, image, document, or short-audio tasks | Supported runtime plus the exact model and multimodal files | Compact quality, OCR detail, audio limits, and runtime support vary |

Self-hosting is not automatically cheaper after setup, updates, failures, and user support are counted.

## 3. Software engineer without a local GPU

**Typical setup:** business laptop with 32 GB RAM, strong Linux and server skills, but no useful discrete GPU.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Existing laptop | Use [Qwen2.5-Coder 3B Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen2-5-coder/sub/models/sub/qwen2-5-coder-3b-instruct/), [Qwen2.5-Coder 7B Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen2-5-coder/sub/models/sub/qwen2-5-coder-7b-instruct/), or [Qwen3 8B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-8b/) through LM Studio or another supported runtime | CPU and 16–32 GB RAM | Useful for private, bounded tasks; long contexts and agent loops are slow |
| Multimodal local helper | Use [Gemma 4 E2B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e2b-instruct/) or [E4B Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e4b-instruct/) for bounded screenshot, UI, document, and coding-context experiments | CPU or supported accelerator; exact runtime and artifact must be measured | Multimodal preprocessing and long context can make CPU latency impractical |
| Hourly GPU | Start an on-demand 24 GB GPU and serve [Qwen3 14B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-14b/) `Q4_K_M`; test [Qwen3 30B-A3B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-30b-a3b/) `Q4_K_M` only as a constrained sequential route | RTX 3090/4090-class rented GPU, [Ollama](../../../../../../../software/sub/inference/sub/ollama/) or another measured runtime | Storage, startup, shutdown, and forgotten idle billing |
| Hosted coding | Use [Cursor](../../../../../../../software/sub/development/sub/code-editors/sub/cursor/), [Codex](../../../../../../../software/sub/agents/sub/openai-codex/), or another approved coding service for time-sensitive work | Subscription or API access | Cost, usage limits, and source-code data path |

A generic CPU VPS can be slower than a modern laptop despite more advertised vCPUs and RAM. Benchmark the exact host, model artifact, context, and runtime before committing to it.

## 4. Gamer with an existing GPU

**Typical setup:** gaming PC with an 8–16 GB GPU and little interest in server administration.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Compact multimodal local | Run [Gemma 4 E2B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e2b-instruct/) or [E4B Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e4b-instruct/) official QAT artifacts for text, image, document, or short-audio work | 8–12 GB VRAM is a planning class, not a guarantee; measure model, projection, context, and applications | Games, displays, multimodal components, and context share GPU memory |
| Text or coding local | Run [Qwen3 8B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-8b/) or [Qwen2.5-Coder 7B Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen2-5-coder/sub/models/sub/qwen2-5-coder-7b-instruct/) with a measured quantization | 8–16 GB VRAM, depending on context and offload | A model fitting in VRAM does not prove useful quality or context headroom |
| Local API | Serve the same measured model through Ollama or another managed runtime when several applications need it | Existing gaming PC | Service security, updates, power, and availability |
| Hybrid | Keep the local model for routine work and use [GPT-5.6 Luna](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/luna/) or [Gemini 3.6 Flash](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemini/sub/models/sub/gemini-3-6-flash/) for harder tasks | Local GPU plus hosted access | Data classification must decide what may leave the device |

Do not buy another GPU until the existing card has been measured on the intended models and context sizes.

## 5. Mac developer or creator

**Typical setup:** Apple-silicon Mac used for coding, writing, design, or media work.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| 16 GB compact route | Test [Gemma 4 E2B Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e2b-instruct/), [Phi-4 Mini Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/microsoft/sub/phi/sub/phi-4/sub/models/sub/phi-4-mini-instruct/), or a measured [Qwen3 8B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-8b/) artifact in a native local runtime | Apple silicon with 16 GB unified memory | Unified memory is shared with macOS, applications, context, and multimodal components |
| 24–32 GB compact multimodal | Evaluate [Gemma 4 E4B Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e4b-instruct/) or a higher-precision smaller model | Apple silicon with sufficient measured unified-memory headroom | Model fit does not guarantee acceptable speed, modality support, or long-context behavior |
| 32 GB+ text route | Evaluate [Qwen3 14B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-14b/) `Q4_K_M` locally | Apple silicon with 32 GB or more unified memory | Larger model quality must justify latency and memory pressure |
| Hybrid | Keep private routine tasks local and escalate difficult tasks to a managed assistant or API | Local runtime plus hosted access | Requires an explicit data-routing rule |

Confirm runtime and model support before purchasing additional memory primarily for AI.

## 6. AI enthusiast or home-lab owner

**Typical setup:** owns or plans a GPU workstation or server and accepts infrastructure work.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Resident text generalist | Keep [Qwen3 14B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-14b/) `Q4_K_M` loaded behind Ollama or another managed service | One measured 24 GB GPU | Idle power, service exposure, maintenance, and context memory |
| Compact multimodal lane | Keep [Gemma 4 E2B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e2b-instruct/) or [E4B Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e4b-instruct/) available for bounded image, document, UI, and short-audio work | Measured local artifact, projection files, runtime, and memory budget | A second resident service can reduce context and concurrency headroom |
| Larger sequential route | Unload the resident model and load [Qwen3 30B-A3B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-30b-a3b/) `Q4_K_M` only for tasks where it wins | One 24 GB GPU only after peak-memory validation; 48 GB is less constrained | Model switching and failure recovery |
| Temporary specialist | Rent a cloud GPU for larger language models or media generation; retain a hosted API fallback | On-demand GPU provider | Lifecycle automation and verified billing shutdown |

Include electricity, storage, remote-access security, backups, updates, and operator time in total cost.

## 7. Small content business

**Typical setup:** a channel, community, or small team repeatedly creates posts, images, scripts, or memes.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Manual managed | Use ChatGPT, Claude, or Gemini for text and an approved hosted image tool | Managed subscriptions | Manual repetition and inconsistent brand output |
| API workflow | Use [Gemini 3.6 Flash](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemini/sub/models/sub/gemini-3-6-flash/), [GPT-5.6 Luna](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/luna/), or [GPT-5.6 Terra](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/terra/) for text and multimodal steps; add [OpenRouter](../../../../../../../software/sub/model-platforms/sub/openrouter/) only when multi-provider routing is useful | API budget and workflow engine | Retries, generated volume, moderation, and review cost |
| Local preparation and review | Use [Gemma 4 E4B Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e4b-instruct/) for private scripts, documents, images, and bounded media review | Supported local runtime and measured memory | Compact quality and review calibration can require hosted or human escalation |
| Hybrid production | Keep [Qwen3 14B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-14b/) or Gemma 4 E4B resident and use [FLUX.1-schnell](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/black-forest-labs/sub/flux/sub/flux-1/sub/models/sub/flux-1-schnell/) on a separately measured image worker or temporary GPU | A 24 GB-class GPU is a conservative starting point, not a universal minimum | Rights, disclosure, brand review, model switching, and media-worker lifecycle |

> OpenRouter is convenient, but sensitive data needs explicit privacy controls. [Details](../../../../../../../software/sub/model-platforms/sub/openrouter/#openrouter-data-safety).

## 8. Software development company

**Typical setup:** several or tens of developers use coding assistants or agents, and included usage can be exhausted unevenly.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Managed pilot | Pilot [Cursor](../../../../../../../software/sub/development/sub/code-editors/sub/cursor/), [Codex](../../../../../../../software/sub/agents/sub/openai-codex/), or [Claude Code](../../../../../../../software/sub/agents/sub/claude-code/) with representative repositories and users | Per-seat or bundled access | Included usage, client data routing, and weak cost attribution |
| Central hosted routing | Use approved enterprise APIs such as [GPT-5.6 Terra](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/terra/) or [Sol](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/sol/), [Claude Sonnet 5](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/anthropic/sub/claude/sub/sonnet/sub/models/sub/sonnet-5/), and [Gemini 3.6 Flash](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemini/sub/models/sub/gemini-3-6-flash/) through a controlled gateway | Central identity, budgets, logs, and vendor contracts | Gateway operation and provider dependency |
| Shared bounded workers | Use [Qwen2.5-Coder 7B Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen2-5-coder/sub/models/sub/qwen2-5-coder-7b-instruct/) for low-risk coding and Gemma 4 E4B for bounded multimodal developer tasks | Dedicated service with task routing, logs, and acceptance tests | Small models are not substitutes for architecture, autonomous changes, or high-risk review |
| Shared agent specialist | Evaluate [Qwen3-Coder-Next](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3-coder/sub/models/sub/qwen3-coder-next/) on a large-memory or multi-GPU server; retain hosted escalation | Dedicated AI platform and operations team | Hardware fit is unproven until exact artifacts, context, concurrency, and accepted-result quality are measured |

Coding agents can execute commands and modify files. Isolate them in VMs, containers, or other sandboxes with least privilege and approval gates.

> Cursor and Codex can send code or context to vendor infrastructure. Local execution or a self-hosted model endpoint does not prove the complete client path is local. [Cursor details](../../../../../../../software/sub/development/sub/code-editors/sub/cursor/#cursor-data-safety) · [Codex details](../../../../../../../software/sub/agents/sub/openai-codex/#codex-data-safety).

See [Agents and Automation Model Selection](../../../../../../../catalog/sub/models/sub/selection/sub/agents-and-automation/) for model-selection safeguards.

## 9. Business knowledge assistant

**Typical setup:** employees need answers from internal policies, product information, support material, or document collections.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Managed assistant | Use an approved business assistant with connected documents and organization controls | Managed workspace | Connector permissions, freshness, and vendor lock-in |
| Managed RAG | Use [Gemini 3.6 Flash](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemini/sub/models/sub/gemini-3-6-flash/) or [GPT-5.6 Terra](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/terra/) with approved embedding, retrieval, and citation stages | API, document store, access-control integration | Retrieval quality and permission mistakes |
| Self-hosted text RAG | Use [Qwen3 14B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-14b/) with separately evaluated embedding and reranking models | 24 GB GPU or measured server | Operations, evaluation, access control, and lower quality ceiling |
| Bounded multimodal knowledge route | Evaluate [Gemma 4 E4B Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e4b-instruct/) for private image, form, UI, or short-audio inputs before retrieval and answer generation | Measured local runtime, extraction, permissions, and provenance | Compact perception and reasoning cannot replace deterministic parsing or permission controls |

Require source citations, document-level permissions, freshness checks, and human escalation. Retrieval does not make an incorrect answer safe.

## 10. Sensitive-data professional

**Typical setup:** legal, accounting, healthcare, consulting, or other confidential or regulated work.

| Route | Concrete implementation | Hardware or access | Main limit |
| --- | --- | --- | --- |
| Contracted enterprise | Use an enterprise service only after retention, region, access, audit, training, and subprocessors are approved | Organization-managed account and contract | Cost and vendor dependency |
| Private managed API | Use a provider project or private deployment approved for the exact data class | Approved cloud and identity controls | Data still leaves the endpoint owner unless the architecture proves otherwise |
| Compact local multimodal | Run [Gemma 4 E2B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e2b-instruct/) or [E4B Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e4b-instruct/) for bounded text, image, document, or short-audio tasks | Exact local artifact, runtime, storage, logs, and deletion controls | Compact quality, OCR, audio duration, and domain accuracy may prohibit the task |
| Local text route | Run [Phi-4 Mini Instruct](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/microsoft/sub/phi/sub/phi-4/sub/models/sub/phi-4-mini-instruct/), [Qwen3 8B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-8b/), or [Qwen3 14B](../../../../../../../catalog/sub/models/sub/reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-14b/) according to hardware and measured quality | 16–32 GB RAM for smaller models or a measured 24 GB GPU for Qwen3 14B | The local quality ceiling may require human work or prohibit the task |

Do not choose a free consumer service, aggregator, or coding client only because it is convenient. Confirm the complete provider chain and legal basis first.

## Selection rules

- Existing hardware is a constraint, not a reason to force local inference.
- A subscription can be cheaper than self-hosting when administration time is included.
- Local inference is most defensible for privacy, stable high volume, offline use, or provider independence.
- Cloud GPUs fit temporary heavy workloads better than an always-running generic CPU VPS.
- Agents need stronger isolation and approval boundaries than chat assistants.
- A multimodal model does not replace deterministic extraction, schema validation, or qualified review.
- Compare total cost per accepted result, including retries and human correction.

For model-specific local resource-fit evidence, use [Local Resource Fit](../../../../../../../catalog/sub/models/sub/selection/sub/local-resource-fit/). For the current model-selection method, see [Model Selection](../../../../../../../catalog/sub/models/sub/selection/).

## Sources

- [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4)
- [Gemma 4 E2B Instruct](https://huggingface.co/google/gemma-4-E2B-it)
- [Gemma 4 E4B Instruct](https://huggingface.co/google/gemma-4-E4B-it)
- [ChatGPT Free Tier FAQ](https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq)
- [Claude plans and pricing](https://claude.com/pricing)
- [Gemini Apps limits and upgrades](https://support.google.com/gemini/answer/16275805)
