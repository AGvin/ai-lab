# Practical AI User Scenarios

Start with the person, available hardware, budget, skills, data, and workload before choosing a model.

These scenarios are short decision examples, not fixed product bundles. Use the simplest option that meets the real requirement.

## Quick map

| Scenario | Typical starting point | First option to try |
| --- | --- | --- |
| Student on a minimal budget | Basic laptop, little setup experience | Free hosted assistants |
| Everyday home or office user | Typical laptop, wants convenience | One managed assistant subscription |
| Software engineer without a GPU | Business laptop, strong technical skills | Hybrid local and hosted workflow |
| Gamer with an existing GPU | Gaming PC, limited AI experience | Simple local desktop runtime |
| Mac developer or creator | Apple silicon with unified memory | Native local app plus hosted fallback |
| AI enthusiast or home-lab owner | GPU workstation or server | Self-hosted inference service |
| Small content business | Repeated text and media production | Managed tools, then API automation |
| Software development company | Many coding-agent users | Managed pilot, then shared inference if justified |
| Business knowledge assistant | Internal documents and repeat questions | Managed or self-hosted RAG |
| Sensitive-data professional | Confidential or regulated material | Contracted private service or local deployment |

## 1. Student on a minimal budget

**Situation:** little spare money, a basic laptop, and no desire to administer servers.

**Options:**

1. Use the free tiers of several assistants, such as ChatGPT, Claude, and Gemini, and switch when a current limit is reached.
2. Pay for one subscription only when daily use justifies it.
3. Use a small local model through a simple desktop app only when offline access or privacy matters.

**Watch:** free limits and available models change. Do not upload private university, employer, or third-party data without permission.

## 2. Everyday home or office user

**Situation:** needs help with writing, summaries, planning, files, or routine questions and does not want technical setup.

**Options:**

1. Use one managed assistant.
2. Choose a business-managed account when work data is involved.
3. Use a simple local app only when privacy is more important than maximum quality.

**Watch:** self-hosting is rarely cheaper after setup and maintenance time are counted.

## 3. Software engineer without a local GPU

**Situation:** a capable business laptop with 32 GB RAM, strong Linux and server skills, but no useful discrete GPU.

**Options:**

1. Run a small or quantized model locally for private, low-urgency tasks.
2. Rent a GPU only for larger coding models or experiments.
3. Use hosted assistants or APIs for the highest-quality and time-sensitive work.

**Watch:** vCPU and RAM numbers do not guarantee fast inference on a generic VPS. Benchmark the exact host, runtime, model artifact, and context.

## 4. Gamer with an existing GPU

**Situation:** a gaming PC already has an 8–16 GB GPU, but the owner may have limited AI or server experience.

**Options:**

1. Start with a desktop runtime such as LM Studio.
2. Use Ollama or another service only when API access or several clients are needed.
3. Keep a hosted fallback for tasks beyond the local quality or memory limit.

**Watch:** VRAM, cooling, power use, context size, and other running applications limit practical performance.

## 5. Mac developer or creator

**Situation:** an Apple-silicon Mac with 16–64 GB of unified memory used for coding, design, writing, or media work.

**Options:**

1. Use a native local runtime for private and routine work.
2. Use a managed assistant for convenience and stronger models.
3. Combine local processing with selective hosted escalation.

**Watch:** unified memory is shared with the operating system and applications. Confirm runtime and model support before buying more memory only for AI.

## 6. AI enthusiast or home-lab owner

**Situation:** owns or plans a GPU workstation or server and accepts infrastructure work.

**Options:**

1. Run an always-on local service with Ollama, vLLM, or another measured runtime.
2. Rent temporary cloud GPUs for larger models or media generation.
3. Keep a hosted API as a reliability or quality fallback.

**Watch:** include electricity, storage, remote-access security, updates, idle time, and maintenance in total cost.

## 7. Small content business

**Situation:** a channel, community, or small team repeatedly creates posts, images, scripts, or memes.

**Options:**

1. Use managed assistants while work is mostly manual.
2. Use direct APIs or OpenRouter when a repeatable workflow needs automation.
3. Rent or self-host a GPU only when stable volume makes it cheaper and someone can operate it.

**Watch:** keep human brand review and check rights, disclosure, platform rules, and moderation requirements.

> OpenRouter is convenient, but sensitive data needs explicit privacy controls. [Details](../../../../../../../software/sub/model-platforms/sub/openrouter/#openrouter-data-safety).

## 8. Software development company

**Situation:** several developers use coding assistants or agents, and seat or token limits can become expensive at scale.

**Options:**

1. Start with managed coding-agent seats for a bounded pilot.
2. Use approved enterprise APIs for stronger central controls and measured usage.
3. Operate shared coding models and agents when sustained volume justifies GPU and platform costs.

**Watch:** isolate coding agents in virtual machines, containers, or other sandboxes with least privilege. A self-hosted model does not prove that the IDE or agent client keeps code local; verify the complete data path.

> Cursor and Codex can send code or context to vendor infrastructure. Local execution or a self-hosted model endpoint does not prove the complete client path is local. [Cursor details](../../../../../../../software/sub/development/sub/code-editors/sub/cursor/#cursor-data-safety) · [Codex details](../../../../../../../software/sub/agents/sub/openai-codex/#codex-data-safety).

See [Choosing Models for AI Agents](../agents/) for execution safeguards.

## 9. Business knowledge assistant

**Situation:** employees need answers from internal documents, policies, product information, or support material.

**Options:**

1. Buy a managed business assistant when its access and data terms are acceptable.
2. Build managed retrieval-augmented generation with an approved API.
3. Self-host retrieval and inference for sensitive, frequent, or predictable workloads.

**Watch:** enforce source permissions, citations, document freshness, and human escalation. Retrieval does not make an incorrect answer safe.

## 10. Sensitive-data professional

**Situation:** a lawyer, accountant, healthcare professional, consultant, or other user works with confidential or regulated information.

**Options:**

1. Use a contracted enterprise service with acceptable retention, region, access, and audit controls.
2. Use a private managed deployment under explicit organizational approval.
3. Keep data and inference local when external transfer is prohibited.

**Watch:** do not choose a free service, aggregator, or consumer account only because it is convenient. Confirm the full provider chain and legal basis first.

## Selection rules

- Existing hardware is a constraint, not a reason to force local inference.
- A subscription can be cheaper than self-hosting when administration time is included.
- Local inference can be preferable for privacy, stable high volume, offline use, or provider independence.
- Cloud GPUs fit temporary heavy workloads better than an always-running generic CPU VPS.
- Agents need stronger isolation and approval boundaries than chat assistants.
- Recheck current prices, limits, availability, and data terms before adoption.

For hardware-oriented model portfolios, continue to [Concrete Model Portfolio Profiles](../combined-workloads/sub/environment-profiles/). For evaluation rules, see [Model Selection Methodology](../methodology/).

## Sources

- [ChatGPT Free Tier FAQ](https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq)
- [Claude plans and pricing](https://claude.com/pricing)
- [Gemini Apps limits and upgrades](https://support.google.com/gemini/answer/16275805)
