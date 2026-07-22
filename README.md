# AI Lab

Practical AI lab for models, tools, local inference, benchmarks, hardware notes, and automation workflows.

## Translations

- English
- [Українська](./docs/l10n/uk_UA/)

## Status

This repository is an active public documentation lab. Content is added incrementally when a topic has real notes, references, or practical evaluation value.

## Documentation Map

### Start here

- [`overview/`](./docs/sub/overview/) — repository documentation model, current layout, asset rules, and expansion guidance.

### Software

- [`software/`](./docs/sub/software/) — AI-related software, development tooling, model platforms, inference tools, agents, automation tools, and executable workflows.
  - [`development/`](./docs/sub/software/sub/development/) — software used to create, structure, inspect, and review changes in AI-assisted development workflows.
    - [`code-editors/`](./docs/sub/software/sub/development/sub/code-editors/) — code editors and editor extension ecosystems for AI-assisted development.
    - [`development-workflows/`](./docs/sub/software/sub/development/sub/development-workflows/) — tools that structure delivery through specifications, plans, tasks, validation, and implementation stages.
    - [`code-review-tools/`](./docs/sub/software/sub/development/sub/code-review-tools/) — non-agent tools for inspecting, navigating, annotating, and reviewing code changesets.
  - [`inference/`](./docs/sub/software/sub/inference/) — tools for local or self-hosted model execution.
  - [`workflow-engines/`](./docs/sub/software/sub/workflow-engines/) — tools that build or execute AI workflows.
  - [`agents/`](./docs/sub/software/sub/agents/) — agent-like AI systems where agent behavior is the primary documented role.
  - [`agent-orchestration/`](./docs/sub/software/sub/agent-orchestration/) — systems, frameworks, runtimes, and control planes for coordinating or running AI agents.
  - [`assistants/`](./docs/sub/software/sub/assistants/) — conversational AI assistants.
  - [`automation/`](./docs/sub/software/sub/automation/) — automation tools that support AI-adjacent workflows.
  - [`model-platforms/`](./docs/sub/software/sub/model-platforms/) — platforms for model discovery, hosting, datasets, and related AI tooling.
  - [`models/`](./docs/sub/software/sub/models/) — model families and individual model artifacts.

### Notes and decision support

- [`concepts/`](./docs/sub/notes/sub/concepts/) — practical and foundational AI concepts organized by topic and reading priority.
  - [`foundations-and-architecture/`](./docs/sub/notes/sub/concepts/sub/foundations-and-architecture/) — core concepts that explain modern AI models and their main architectural families.
    - Essential
      - [`foundation-models/`](./docs/sub/notes/sub/concepts/sub/foundations-and-architecture/sub/foundation-models/) — large reusable models trained on broad data and adapted to many downstream tasks.
      - [`large-language-models/`](./docs/sub/notes/sub/concepts/sub/foundations-and-architecture/sub/large-language-models/) — language-focused foundation models that predict and generate token sequences.
      - [`multimodal-models/`](./docs/sub/notes/sub/concepts/sub/foundations-and-architecture/sub/multimodal-models/) — models that process or generate more than one modality, such as text, images, audio, or video.
    - Useful
      - [`transformers/`](./docs/sub/notes/sub/concepts/sub/foundations-and-architecture/sub/transformers/) — neural network architectures built around attention and parallel sequence processing.
      - [`attention/`](./docs/sub/notes/sub/concepts/sub/foundations-and-architecture/sub/attention/) — a mechanism that weights which input elements are most relevant for a model operation.
      - [`mixture-of-experts/`](./docs/sub/notes/sub/concepts/sub/foundations-and-architecture/sub/mixture-of-experts/) — sparse model architectures that route each input through selected expert components.
    - Specialized
      - [`artificial-intelligence/`](./docs/sub/notes/sub/concepts/sub/foundations-and-architecture/sub/artificial-intelligence/) — the broad field of systems that perform tasks associated with perception, reasoning, generation, or decision-making.
      - [`machine-learning/`](./docs/sub/notes/sub/concepts/sub/foundations-and-architecture/sub/machine-learning/) — methods that learn patterns from data instead of relying only on explicitly programmed rules.
      - [`deep-learning/`](./docs/sub/notes/sub/concepts/sub/foundations-and-architecture/sub/deep-learning/) — machine learning based on neural networks with many processing layers.
      - [`neural-networks/`](./docs/sub/notes/sub/concepts/sub/foundations-and-architecture/sub/neural-networks/) — parameterized computational structures composed of connected layers or processing units.
      - [`self-attention/`](./docs/sub/notes/sub/concepts/sub/foundations-and-architecture/sub/self-attention/) — attention computed between positions within the same input sequence.
      - [`encoder-decoder/`](./docs/sub/notes/sub/concepts/sub/foundations-and-architecture/sub/encoder-decoder/) — model structures that encode inputs, generate outputs, or combine both roles.
      - [`dense-and-sparse-models/`](./docs/sub/notes/sub/concepts/sub/foundations-and-architecture/sub/dense-and-sparse-models/) — dense models activate most parameters for each input, while sparse models activate selected subsets.
  - [`model-usage-and-generation/`](./docs/sub/notes/sub/concepts/sub/model-usage-and-generation/) — concepts for using trained models through chats, APIs, applications, and local runtimes.
    - Essential
      - [`tokens-and-tokenization/`](./docs/sub/notes/sub/concepts/sub/model-usage-and-generation/sub/tokens-and-tokenization/) — splitting input and output into the units a model reads and generates.
      - [`context-window/`](./docs/sub/notes/sub/concepts/sub/model-usage-and-generation/sub/context-window/) — the bounded amount of tokenized information a model can consider during one request.
      - [`prompting/`](./docs/sub/notes/sub/concepts/sub/model-usage-and-generation/sub/prompting/) — supplying instructions, context, examples, and constraints to guide a model.
      - [`system-prompts/`](./docs/sub/notes/sub/concepts/sub/model-usage-and-generation/sub/system-prompts/) — high-priority instructions that define an assistant's role, behavior, and boundaries.
      - [`structured-output/`](./docs/sub/notes/sub/concepts/sub/model-usage-and-generation/sub/structured-output/) — model output constrained to a machine-readable structure such as JSON or a schema.
      - [`hallucinations/`](./docs/sub/notes/sub/concepts/sub/model-usage-and-generation/sub/hallucinations/) — unsupported or incorrect model output presented in a plausible form.
    - Useful
      - [`few-shot-prompting/`](./docs/sub/notes/sub/concepts/sub/model-usage-and-generation/sub/few-shot-prompting/) — prompting that includes a small number of examples to demonstrate desired behavior.
      - [`sampling-parameters/`](./docs/sub/notes/sub/concepts/sub/model-usage-and-generation/sub/sampling-parameters/) — controls such as temperature, top-p, top-k, and seed that influence token selection.
      - [`reasoning-models/`](./docs/sub/notes/sub/concepts/sub/model-usage-and-generation/sub/reasoning-models/) — models optimized to spend additional computation on multi-step problem solving.
      - [`model-capabilities-and-limitations/`](./docs/sub/notes/sub/concepts/sub/model-usage-and-generation/sub/model-capabilities-and-limitations/) — practical strengths, boundaries, and failure modes of a model or deployment.
    - Specialized
      - [`constrained-generation/`](./docs/sub/notes/sub/concepts/sub/model-usage-and-generation/sub/constrained-generation/) — generation restricted by a grammar, schema, token set, or another formal constraint.
      - [`chain-of-thought/`](./docs/sub/notes/sub/concepts/sub/model-usage-and-generation/sub/chain-of-thought/) — intermediate reasoning text or internal computation used to support multi-step answers.
  - [`retrieval-and-knowledge/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/) — concepts for connecting models to external information, searchable documents, and evidence-backed context.
    - Essential
      - [`rag/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/rag/) — Retrieval-Augmented Generation combines external retrieval with model generation.
      - [`embeddings/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/embeddings/) — numerical representations that place semantically related items near each other in vector space.
      - [`chunking/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/chunking/) — dividing source material into retrievable units while preserving enough context.
      - [`semantic-search/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/semantic-search/) — retrieval based on meaning rather than only exact word matches.
      - [`hybrid-search/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/hybrid-search/) — retrieval that combines semantic and lexical search signals.
      - [`grounding/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/grounding/) — constraining generated claims to supplied evidence, tools, or authoritative sources.
    - Useful
      - [`vector-search/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/vector-search/) — nearest-neighbor retrieval over embedding vectors.
      - [`vector-databases/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/vector-databases/) — storage and indexing systems optimized for vectors and similarity search.
      - [`keyword-search/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/keyword-search/) — lexical retrieval based on terms that appear in source text.
      - [`reranking/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/reranking/) — a second-stage relevance model that reorders retrieved candidates.
      - [`citations/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/citations/) — links or references connecting generated statements to supporting sources.
      - [`metadata-filtering/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/metadata-filtering/) — restricting retrieval by source, date, version, tenant, access policy, or other attributes.
    - Specialized
      - [`bm25/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/bm25/) — a probabilistic lexical ranking method widely used in document retrieval.
      - [`graph-rag/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/graph-rag/) — Retrieval-Augmented Generation using graph structures and relationships to assemble context.
      - [`knowledge-graphs/`](./docs/sub/notes/sub/concepts/sub/retrieval-and-knowledge/sub/knowledge-graphs/) — structured representations of entities and their relationships.
  - [`agents-and-automation/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/) — concepts for AI systems that plan, use tools, maintain state, and perform controlled actions.
    - Essential
      - [`ai-agents/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/ai-agents/) — AI systems that pursue goals through model decisions, tools, state, and iterative actions.
      - [`agentic-workflows/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/agentic-workflows/) — controlled multi-step processes combining model decisions with deterministic workflow logic.
      - [`tool-calling/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/tool-calling/) — a model selecting a registered external operation and producing arguments for execution.
      - [`agent-state/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/agent-state/) — explicit working data tracking progress, decisions, and intermediate results.
      - [`agent-memory/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/agent-memory/) — mechanisms preserving useful information beyond the immediate request.
      - [`planning/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/planning/) — selecting and ordering actions needed to reach a goal.
      - [`verification-and-reflection/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/verification-and-reflection/) — checking results and revising an approach when needed.
      - [`human-in-the-loop/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/human-in-the-loop/) — human review, approval, or intervention at selected points.
      - [`idempotency/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/idempotency/) — designing actions so safe repetition does not create duplicate effects.
      - [`failure-recovery/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/failure-recovery/) — restoring progress safely after model, tool, network, or workflow failures.
    - Useful
      - [`function-calling/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/function-calling/) — a structured tool interface where model output selects a function and arguments.
      - [`agent-skills/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/) — portable procedural knowledge packages discovered and loaded when a task requires them.
        - [`using/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/sub/using/) — install, invoke, update, remove, inspect, and troubleshoot skills.
        - [`creating/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/sub/creating/) — design and build a skill from a minimal `SKILL.md` through scripts, references, testing, and publication.
        - [`platform-support/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/sub/platform-support/) — compare supported clients and their installation and invocation models.
        - [`sources/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/sub/sources/) — standards, catalogs, installers, and recommended third-party collections.
      - [`task-decomposition/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/task-decomposition/) — breaking a large task into smaller, verifiable units.
      - [`retries/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/retries/) — repeating eligible failed operations under bounded rules.
      - [`autonomy-levels/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/autonomy-levels/) — the degree of independent decision-making granted to an AI system.
    - Specialized
      - [`multi-agent-systems/`](./docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/multi-agent-systems/) — systems in which multiple agents coordinate, compete, review, or specialize.
  - [`inference-and-serving/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/) — concepts for running trained models locally or as services and understanding resource and performance behavior.
    - Essential
      - [`inference/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/inference/) — running a trained model to process input and produce output.
      - [`quantization/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/quantization/) — reducing numerical precision to lower model memory and compute requirements.
      - [`numerical-precision/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/numerical-precision/) — number formats used for model weights, activations, and computation.
      - [`model-formats/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/model-formats/) — file and serialization formats used to store and load model artifacts.
      - [`gpu-offloading/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/gpu-offloading/) — placing selected model computation or layers on a GPU while other work remains elsewhere.
      - [`kv-cache/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/kv-cache/) — cached attention keys and values reused during autoregressive generation.
      - [`latency/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/latency/) — elapsed time required to produce a response or reach a defined output milestone.
      - [`throughput/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/throughput/) — the amount of model work completed per unit of time.
      - [`performance-metrics/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/performance-metrics/) — measurements such as time to first token, tokens per second, latency, and memory use.
    - Useful
      - [`model-serving/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/model-serving/) — exposing model inference through a managed process, API, queue, or runtime service.
      - [`model-loading/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/model-loading/) — moving model artifacts into RAM, VRAM, or runtime-managed memory for execution.
      - [`cpu-inference/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/cpu-inference/) — running model computation primarily on general-purpose processors.
      - [`gpu-inference/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/gpu-inference/) — running model computation primarily on graphics processors optimized for parallel workloads.
      - [`context-caching/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/context-caching/) — reusing previously processed prompt context to reduce repeated computation.
    - Specialized
      - [`flash-attention/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/flash-attention/) — attention implementations optimized to reduce memory traffic and improve GPU efficiency.
      - [`continuous-batching/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/continuous-batching/) — dynamically combining active inference requests to improve serving utilization.
      - [`speculative-decoding/`](./docs/sub/notes/sub/concepts/sub/inference-and-serving/sub/speculative-decoding/) — using a faster draft process to propose tokens for verification by a target model.
  - [`training-and-adaptation/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/) — concepts for training models or adapting them to tasks, domains, preferences, and deployment constraints.
    - Essential
      - [`fine-tuning/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/fine-tuning/) — continuing model training on targeted data to modify behavior or task performance.
      - [`parameter-efficient-fine-tuning/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/parameter-efficient-fine-tuning/) — adaptation methods that train only a small subset of model parameters or added components.
      - [`lora/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/lora/) — Low-Rank Adaptation trains compact low-rank updates instead of all base model weights.
      - [`qlora/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/qlora/) — LoRA-based adaptation with a quantized base model to reduce memory use.
    - Useful
      - [`supervised-fine-tuning/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/supervised-fine-tuning/) — fine-tuning on labeled examples that pair inputs with desired outputs.
      - [`adapters/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/adapters/) — small trainable modules attached to a base model for reusable specialization.
      - [`instruction-tuning/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/instruction-tuning/) — training a model on instruction-and-response examples to improve task following.
      - [`synthetic-data/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/synthetic-data/) — training or evaluation data generated by rules, simulations, or models.
      - [`datasets/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/datasets/) — organized collections of examples used for training, adaptation, or evaluation.
      - [`overfitting/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/overfitting/) — when a model fits training data too closely and performs poorly on new examples.
    - Specialized
      - [`pretraining/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/pretraining/) — large-scale initial training that creates a broadly capable base model.
      - [`preference-optimization/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/preference-optimization/) — training methods that favor responses judged better according to preference data.
      - [`rlhf/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/rlhf/) — Reinforcement Learning from Human Feedback uses preference signals to adjust model behavior.
      - [`dpo/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/dpo/) — Direct Preference Optimization trains directly on preferred and rejected response pairs.
      - [`distillation/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/distillation/) — training a smaller or simpler model to imitate a stronger teacher model.
      - [`pruning/`](./docs/sub/notes/sub/concepts/sub/training-and-adaptation/sub/pruning/) — removing model parameters or structures judged unnecessary for a target objective.
  - [`multimodal-and-generative-media/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/) — concepts for models and workflows involving images, audio, video, and combinations of modalities.
    - Essential
      - [`vision-language-models/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/vision-language-models/) — models that jointly process visual inputs and natural language.
      - [`image-generation/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/image-generation/) — producing images from text, images, layouts, masks, or other conditioning inputs.
      - [`diffusion-models/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/diffusion-models/) — generative models that learn to reverse a progressive noising process.
      - [`image-to-image/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/image-to-image/) — generating a transformed image while conditioning on an existing image.
      - [`inpainting/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/inpainting/) — regenerating selected masked regions of an image.
      - [`controlnet/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/controlnet/) — conditioning diffusion models with structural controls such as edges, depth, or pose.
      - [`multimodal-context/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/multimodal-context/) — combined text, image, audio, video, or document information available to a model request.
    - Useful
      - [`text-to-image/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/text-to-image/) — generating images from natural-language descriptions.
      - [`outpainting/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/outpainting/) — extending an image beyond its original boundaries.
      - [`image-embeddings/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/image-embeddings/) — vector representations used to compare, retrieve, or classify visual content.
      - [`speech-to-text/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/speech-to-text/) — converting spoken audio into written text.
      - [`text-to-speech/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/text-to-speech/) — synthesizing spoken audio from written text.
      - [`video-generation/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/video-generation/) — producing or transforming sequences of visual frames with generative models.
    - Specialized
      - [`latent-space/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/latent-space/) — a compressed learned representation in which generative models encode and manipulate information.
      - [`audio-generation/`](./docs/sub/notes/sub/concepts/sub/multimodal-and-generative-media/sub/audio-generation/) — producing music, speech, sound effects, or other audio with generative models.
  - [`safety-privacy-and-reliability/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/) — concepts for controlling model behavior, protecting data, and reducing operational risk.
    - Essential
      - [`prompt-injection/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/prompt-injection/) — input designed to override or manipulate an AI system's intended instructions.
      - [`indirect-prompt-injection/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/indirect-prompt-injection/) — malicious or conflicting instructions embedded in external content processed by an AI system.
      - [`trust-boundaries/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/trust-boundaries/) — explicit separation between trusted instructions, trusted systems, users, and untrusted data.
      - [`least-privilege/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/least-privilege/) — granting an AI system only the permissions required for its current task.
      - [`sandboxing/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/sandboxing/) — isolating execution so failures or malicious behavior have limited impact.
      - [`secret-handling/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/secret-handling/) — protecting credentials, tokens, keys, and other sensitive operational data.
      - [`data-privacy/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/data-privacy/) — controlling how personal, confidential, or sensitive data is collected, processed, retained, and shared.
      - [`retrieval-poisoning/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/retrieval-poisoning/) — manipulating indexed knowledge so retrieval supplies misleading or malicious context.
    - Useful
      - [`guardrails/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/guardrails/) — controls that validate, restrict, or monitor model inputs, outputs, and actions.
      - [`data-residency/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/data-residency/) — the geographic or jurisdictional location where data is stored or processed.
      - [`provenance/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/provenance/) — information about the origin, ownership, transformation, and custody of data or model artifacts.
      - [`content-moderation/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/content-moderation/) — detecting or restricting content according to safety, legal, or platform policies.
    - Specialized
      - [`jailbreaking/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/jailbreaking/) — attempts to bypass a model's configured safety or policy constraints.
      - [`model-alignment/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/model-alignment/) — shaping model behavior toward intended goals, values, policies, or preferences.
      - [`data-poisoning/`](./docs/sub/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/data-poisoning/) — corrupting training or adaptation data to degrade or manipulate model behavior.
  - [`evaluation-and-operations/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/) — concepts for selecting, testing, observing, and operating AI systems under quality, cost, and reliability constraints.
    - Essential
      - [`evals/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/evals/) — repeatable tests that measure whether an AI model or system meets defined requirements.
      - [`model-selection/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/model-selection/) — choosing a model based on task quality, capabilities, cost, latency, safety, and deployment constraints.
      - [`model-routing/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/model-routing/) — selecting among models dynamically according to the request or operating policy.
      - [`observability/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/observability/) — using logs, metrics, traces, and events to understand AI system behavior.
      - [`tracing/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/tracing/) — recording the sequence of model, tool, retrieval, and workflow operations for one execution.
      - [`cost-management/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/cost-management/) — measuring and controlling model, infrastructure, storage, and tool expenses.
      - [`latency-and-throughput/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/latency-and-throughput/) — balancing response time against the amount of work completed per unit of time.
      - [`quality-cost-tradeoffs/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/quality-cost-tradeoffs/) — choosing an acceptable balance between output quality and operational expense.
    - Useful
      - [`benchmarks/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/benchmarks/) — standardized tasks or datasets used to compare models or systems.
      - [`evaluation-datasets/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/evaluation-datasets/) — curated examples used to test quality, safety, retrieval, or task performance.
      - [`human-evaluation/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/human-evaluation/) — people assessing model outputs against explicit criteria.
      - [`fallback-models/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/fallback-models/) — alternative models used when the preferred model fails, is unavailable, or exceeds policy limits.
      - [`caching/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/caching/) — reusing prior results or processed data to reduce repeated work.
      - [`rate-limits/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/rate-limits/) — controls that restrict request volume over a period of time.
    - Specialized
      - [`llm-as-a-judge/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/llm-as-a-judge/) — using a language model to score, rank, or critique other model outputs.
      - [`retrieval-evaluation/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/retrieval-evaluation/) — measuring whether retrieval returns relevant, complete, and correctly ranked evidence.
      - [`reproducibility/`](./docs/sub/notes/sub/concepts/sub/evaluation-and-operations/sub/reproducibility/) — the ability to repeat an evaluation or workflow with comparable conditions and results.
- [`benchmarks/`](./docs/sub/notes/sub/benchmarks/) — benchmark and leaderboard references for evaluating models, providers, and AI systems.
- [`comparisons/`](./docs/sub/notes/sub/comparisons/) — decision-support comparisons across models, tools, workflows, platforms, and AI systems.

## License

This repository is licensed under the MIT License.

When reusing or adapting materials from this repository, please keep the original copyright notice and reference this repository as the source.
