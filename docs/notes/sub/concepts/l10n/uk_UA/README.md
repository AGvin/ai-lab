<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:5d49d927c17a0a1b06a82b85e2f94930371e1c46
  mode: copy-through
-->

# Concepts



Practical and foundational AI concepts organized by topic and reading priority.

Priority indicates the recommended learning order for a user who primarily consumes models, configures local inference, and builds or operates agent workflows.

## Переклади

- [English](../../)
- Українська — поточна

## [Foundations and Architecture](../../sub/foundations-and-architecture/l10n/uk_UA/)

Core concepts that explain what modern AI models are and how their main architectural families relate.

### Essential

- [`foundation-models/`](../../sub/foundations-and-architecture/sub/foundation-models/l10n/uk_UA/) — Large reusable models trained on broad data and adapted to many downstream tasks.
- [`large-language-models/`](../../sub/foundations-and-architecture/sub/large-language-models/l10n/uk_UA/) — Language-focused foundation models that predict and generate token sequences.
- [`multimodal-models/`](../../sub/foundations-and-architecture/sub/multimodal-models/l10n/uk_UA/) — Models that process or generate more than one modality, such as text, images, audio, or video.

### Useful

- [`transformers/`](../../sub/foundations-and-architecture/sub/transformers/l10n/uk_UA/) — Neural network architectures built around attention and parallel sequence processing.
- [`attention/`](../../sub/foundations-and-architecture/sub/attention/l10n/uk_UA/) — A mechanism that weights which input elements are most relevant for a model operation.
- [`mixture-of-experts/`](../../sub/foundations-and-architecture/sub/mixture-of-experts/l10n/uk_UA/) — Sparse model architectures that route each input through selected expert components.

### Specialized

- [`artificial-intelligence/`](../../sub/foundations-and-architecture/sub/artificial-intelligence/l10n/uk_UA/) — The broad field of building systems that perform tasks associated with perception, reasoning, generation, or decision-making.
- [`machine-learning/`](../../sub/foundations-and-architecture/sub/machine-learning/l10n/uk_UA/) — Methods that learn patterns from data instead of relying only on explicitly programmed rules.
- [`deep-learning/`](../../sub/foundations-and-architecture/sub/deep-learning/l10n/uk_UA/) — Machine learning based on neural networks with many processing layers.
- [`neural-networks/`](../../sub/foundations-and-architecture/sub/neural-networks/l10n/uk_UA/) — Parameterized computational structures composed of connected layers or processing units.
- [`self-attention/`](../../sub/foundations-and-architecture/sub/self-attention/l10n/uk_UA/) — Attention computed between positions within the same input sequence.
- [`encoder-decoder/`](../../sub/foundations-and-architecture/sub/encoder-decoder/l10n/uk_UA/) — Model structures that encode inputs, generate outputs, or combine both roles.
- [`dense-and-sparse-models/`](../../sub/foundations-and-architecture/sub/dense-and-sparse-models/l10n/uk_UA/) — Dense models activate most parameters for each input, while sparse models activate selected subsets.

## [Model Usage and Generation](../../sub/model-usage-and-generation/l10n/uk_UA/)

Concepts for using trained models effectively through chats, APIs, applications, and local runtimes.

### Essential

- [`tokens-and-tokenization/`](../../sub/model-usage-and-generation/sub/tokens-and-tokenization/l10n/uk_UA/) — The process of splitting input and output into the units a model reads and generates.
- [`context-window/`](../../sub/model-usage-and-generation/sub/context-window/l10n/uk_UA/) — The bounded amount of tokenized information a model can consider during one request.
- [`prompting/`](../../sub/model-usage-and-generation/sub/prompting/l10n/uk_UA/) — The practice of supplying instructions, context, examples, and constraints to guide a model.
- [`system-prompts/`](../../sub/model-usage-and-generation/sub/system-prompts/l10n/uk_UA/) — High-priority instructions that define an assistant's role, behavior, and operational boundaries.
- [`structured-output/`](../../sub/model-usage-and-generation/sub/structured-output/l10n/uk_UA/) — Model output constrained to a machine-readable structure such as JSON or a schema.
- [`hallucinations/`](../../sub/model-usage-and-generation/sub/hallucinations/l10n/uk_UA/) — Unsupported or incorrect model output presented in a plausible form.

### Useful

- [`few-shot-prompting/`](../../sub/model-usage-and-generation/sub/few-shot-prompting/l10n/uk_UA/) — Prompting that includes a small number of examples to demonstrate desired behavior.
- [`sampling-parameters/`](../../sub/model-usage-and-generation/sub/sampling-parameters/l10n/uk_UA/) — Controls such as temperature, top-p, top-k, and seed that influence token selection.
- [`reasoning-models/`](../../sub/model-usage-and-generation/sub/reasoning-models/l10n/uk_UA/) — Models optimized to spend additional computation on multi-step problem solving.
- [`model-capabilities-and-limitations/`](../../sub/model-usage-and-generation/sub/model-capabilities-and-limitations/l10n/uk_UA/) — The practical strengths, boundaries, and failure modes of a specific model or deployment.

### Specialized

- [`constrained-generation/`](../../sub/model-usage-and-generation/sub/constrained-generation/l10n/uk_UA/) — Generation restricted by a grammar, schema, token set, or other formal constraint.
- [`chain-of-thought/`](../../sub/model-usage-and-generation/sub/chain-of-thought/l10n/uk_UA/) — Intermediate reasoning text or internal computation used to support multi-step answers.

## [Retrieval and Knowledge](../../sub/retrieval-and-knowledge/l10n/uk_UA/)

Concepts for connecting models to external information, searchable documents, and evidence-backed context.

### Essential

- [`rag/`](../../sub/retrieval-and-knowledge/sub/rag/l10n/uk_UA/) — Retrieval-Augmented Generation combines external retrieval with model generation.
- [`embeddings/`](../../sub/retrieval-and-knowledge/sub/embeddings/l10n/uk_UA/) — Numerical representations that place semantically related items near each other in vector space.
- [`chunking/`](../../sub/retrieval-and-knowledge/sub/chunking/l10n/uk_UA/) — Dividing source material into retrievable units while preserving enough context for use.
- [`semantic-search/`](../../sub/retrieval-and-knowledge/sub/semantic-search/l10n/uk_UA/) — Retrieval based on meaning rather than only exact word matches.
- [`hybrid-search/`](../../sub/retrieval-and-knowledge/sub/hybrid-search/l10n/uk_UA/) — Retrieval that combines semantic and lexical search signals.
- [`grounding/`](../../sub/retrieval-and-knowledge/sub/grounding/l10n/uk_UA/) — Constraining generated claims to supplied evidence, tools, or authoritative sources.

### Useful

- [`vector-search/`](../../sub/retrieval-and-knowledge/sub/vector-search/l10n/uk_UA/) — Nearest-neighbor retrieval over embedding vectors.
- [`vector-databases/`](../../sub/retrieval-and-knowledge/sub/vector-databases/l10n/uk_UA/) — Storage and indexing systems optimized for vectors and similarity search.
- [`keyword-search/`](../../sub/retrieval-and-knowledge/sub/keyword-search/l10n/uk_UA/) — Lexical retrieval based on terms that appear in the source text.
- [`reranking/`](../../sub/retrieval-and-knowledge/sub/reranking/l10n/uk_UA/) — A second-stage relevance model that reorders retrieved candidates.
- [`citations/`](../../sub/retrieval-and-knowledge/sub/citations/l10n/uk_UA/) — Links or references that connect generated statements to supporting sources.
- [`metadata-filtering/`](../../sub/retrieval-and-knowledge/sub/metadata-filtering/l10n/uk_UA/) — Restricting retrieval by attributes such as source, date, version, tenant, or access policy.

### Specialized

- [`bm25/`](../../sub/retrieval-and-knowledge/sub/bm25/l10n/uk_UA/) — A probabilistic lexical ranking method widely used in document retrieval.
- [`graph-rag/`](../../sub/retrieval-and-knowledge/sub/graph-rag/l10n/uk_UA/) — Retrieval-Augmented Generation that uses graph structures and relationships to assemble context.
- [`knowledge-graphs/`](../../sub/retrieval-and-knowledge/sub/knowledge-graphs/l10n/uk_UA/) — Structured representations of entities and their relationships.

## [Agents and Automation](../../sub/agents-and-automation/l10n/uk_UA/)

Concepts for configuring AI systems that plan, use tools, maintain state, and perform controlled actions.

### Essential

- [`ai-agents/`](../../sub/agents-and-automation/sub/ai-agents/l10n/uk_UA/) — AI systems that pursue goals through model decisions, tools, state, and iterative actions.
- [`agentic-workflows/`](../../sub/agents-and-automation/sub/agentic-workflows/l10n/uk_UA/) — Controlled multi-step processes that combine model decisions with deterministic workflow logic.
- [`tool-calling/`](../../sub/agents-and-automation/sub/tool-calling/l10n/uk_UA/) — A model selecting a registered external operation and producing arguments for its execution.
- [`agent-state/`](../../sub/agents-and-automation/sub/agent-state/l10n/uk_UA/) — The explicit working data that tracks progress, decisions, and intermediate results.
- [`agent-memory/`](../../sub/agents-and-automation/sub/agent-memory/l10n/uk_UA/) — Mechanisms that preserve useful information beyond the immediate model request.
- [`planning/`](../../sub/agents-and-automation/sub/planning/l10n/uk_UA/) — Selecting and ordering actions needed to reach a goal.
- [`verification-and-reflection/`](../../sub/agents-and-automation/sub/verification-and-reflection/l10n/uk_UA/) — Checking results, identifying errors, and revising an approach when needed.
- [`human-in-the-loop/`](../../sub/agents-and-automation/sub/human-in-the-loop/l10n/uk_UA/) — Requiring human review, approval, or intervention at selected workflow points.
- [`idempotency/`](../../sub/agents-and-automation/sub/idempotency/l10n/uk_UA/) — Designing actions so safe repetition does not create unintended duplicate effects.
- [`failure-recovery/`](../../sub/agents-and-automation/sub/failure-recovery/l10n/uk_UA/) — Restoring progress safely after tool, model, network, or workflow failures.

### Useful

- [`function-calling/`](../../sub/agents-and-automation/sub/function-calling/l10n/uk_UA/) — A structured tool-calling interface where model output selects a function and arguments.
- [`task-decomposition/`](../../sub/agents-and-automation/sub/task-decomposition/l10n/uk_UA/) — Breaking a large task into smaller, verifiable units of work.
- [`retries/`](../../sub/agents-and-automation/sub/retries/l10n/uk_UA/) — Repeating eligible failed operations under bounded and observable rules.
- [`autonomy-levels/`](../../sub/agents-and-automation/sub/autonomy-levels/l10n/uk_UA/) — The degree of independent decision-making and action granted to an AI system.

### Specialized

- [`multi-agent-systems/`](../../sub/agents-and-automation/sub/multi-agent-systems/l10n/uk_UA/) — Systems in which multiple agents coordinate, compete, review, or specialize.

## [Inference and Serving](../../sub/inference-and-serving/l10n/uk_UA/)

Concepts for running trained models locally or as services and understanding their resource and performance behavior.

### Essential

- [`inference/`](../../sub/inference-and-serving/sub/inference/l10n/uk_UA/) — Running a trained model to process input and produce output.
- [`quantization/`](../../sub/inference-and-serving/sub/quantization/l10n/uk_UA/) — Reducing numerical precision to lower model memory and compute requirements.
- [`numerical-precision/`](../../sub/inference-and-serving/sub/numerical-precision/l10n/uk_UA/) — The number format used for model weights, activations, and computation.
- [`model-formats/`](../../sub/inference-and-serving/sub/model-formats/l10n/uk_UA/) — File and serialization formats used to store and load model artifacts.
- [`gpu-offloading/`](../../sub/inference-and-serving/sub/gpu-offloading/l10n/uk_UA/) — Placing selected model computation or layers on a GPU while other work remains elsewhere.
- [`kv-cache/`](../../sub/inference-and-serving/sub/kv-cache/l10n/uk_UA/) — Cached attention keys and values reused during autoregressive generation.
- [`latency/`](../../sub/inference-and-serving/sub/latency/l10n/uk_UA/) — The elapsed time required to produce a response or reach a defined output milestone.
- [`throughput/`](../../sub/inference-and-serving/sub/throughput/l10n/uk_UA/) — The amount of model work completed per unit of time.
- [`performance-metrics/`](../../sub/inference-and-serving/sub/performance-metrics/l10n/uk_UA/) — Measurements such as time to first token, tokens per second, latency, and memory use.

### Useful

- [`model-serving/`](../../sub/inference-and-serving/sub/model-serving/l10n/uk_UA/) — Exposing model inference through a managed process, API, queue, or runtime service.
- [`model-loading/`](../../sub/inference-and-serving/sub/model-loading/l10n/uk_UA/) — Moving model artifacts into RAM, VRAM, or runtime-managed memory for execution.
- [`cpu-inference/`](../../sub/inference-and-serving/sub/cpu-inference/l10n/uk_UA/) — Running model computation primarily on general-purpose processors.
- [`gpu-inference/`](../../sub/inference-and-serving/sub/gpu-inference/l10n/uk_UA/) — Running model computation primarily on graphics processors optimized for parallel workloads.
- [`context-caching/`](../../sub/inference-and-serving/sub/context-caching/l10n/uk_UA/) — Reusing previously processed prompt context to reduce repeated computation.

### Specialized

- [`flash-attention/`](../../sub/inference-and-serving/sub/flash-attention/l10n/uk_UA/) — Attention implementations optimized to reduce memory traffic and improve GPU efficiency.
- [`continuous-batching/`](../../sub/inference-and-serving/sub/continuous-batching/l10n/uk_UA/) — Dynamically combining active inference requests to improve serving utilization.
- [`speculative-decoding/`](../../sub/inference-and-serving/sub/speculative-decoding/l10n/uk_UA/) — Using a faster draft model or process to propose tokens for verification by a target model.

## [Training and Adaptation](../../sub/training-and-adaptation/l10n/uk_UA/)

Concepts for training models or adapting existing models to tasks, domains, preferences, and deployment constraints.

### Essential

- [`fine-tuning/`](../../sub/training-and-adaptation/sub/fine-tuning/l10n/uk_UA/) — Continuing model training on targeted data to modify behavior or task performance.
- [`parameter-efficient-fine-tuning/`](../../sub/training-and-adaptation/sub/parameter-efficient-fine-tuning/l10n/uk_UA/) — Adaptation methods that train only a small subset of model parameters or added components.
- [`lora/`](../../sub/training-and-adaptation/sub/lora/l10n/uk_UA/) — Low-Rank Adaptation trains compact low-rank updates instead of all base model weights.
- [`qlora/`](../../sub/training-and-adaptation/sub/qlora/l10n/uk_UA/) — LoRA-based adaptation performed with a quantized base model to reduce memory use.

### Useful

- [`supervised-fine-tuning/`](../../sub/training-and-adaptation/sub/supervised-fine-tuning/l10n/uk_UA/) — Fine-tuning on labeled examples that pair inputs with desired outputs.
- [`adapters/`](../../sub/training-and-adaptation/sub/adapters/l10n/uk_UA/) — Small trainable modules attached to a base model for reusable specialization.
- [`instruction-tuning/`](../../sub/training-and-adaptation/sub/instruction-tuning/l10n/uk_UA/) — Training a model on instruction-and-response examples to improve task following.
- [`synthetic-data/`](../../sub/training-and-adaptation/sub/synthetic-data/l10n/uk_UA/) — Training or evaluation data generated by rules, simulations, or models.
- [`datasets/`](../../sub/training-and-adaptation/sub/datasets/l10n/uk_UA/) — Organized collections of examples used for training, adaptation, or evaluation.
- [`overfitting/`](../../sub/training-and-adaptation/sub/overfitting/l10n/uk_UA/) — When a model fits training data too closely and performs poorly on new examples.

### Specialized

- [`pretraining/`](../../sub/training-and-adaptation/sub/pretraining/l10n/uk_UA/) — Large-scale initial training that creates a broadly capable base model.
- [`preference-optimization/`](../../sub/training-and-adaptation/sub/preference-optimization/l10n/uk_UA/) — Training methods that favor responses judged better according to preference data.
- [`rlhf/`](../../sub/training-and-adaptation/sub/rlhf/l10n/uk_UA/) — Reinforcement Learning from Human Feedback uses human preference signals to adjust model behavior.
- [`dpo/`](../../sub/training-and-adaptation/sub/dpo/l10n/uk_UA/) — Direct Preference Optimization trains directly on preferred and rejected response pairs.
- [`distillation/`](../../sub/training-and-adaptation/sub/distillation/l10n/uk_UA/) — Training a smaller or simpler model to imitate a stronger teacher model.
- [`pruning/`](../../sub/training-and-adaptation/sub/pruning/l10n/uk_UA/) — Removing model parameters or structures judged unnecessary for a target objective.

## [Multimodal and Generative Media](../../sub/multimodal-and-generative-media/l10n/uk_UA/)

Concepts for models and workflows involving images, audio, video, and combinations of modalities.

### Essential

- [`vision-language-models/`](../../sub/multimodal-and-generative-media/sub/vision-language-models/l10n/uk_UA/) — Models that jointly process visual inputs and natural language.
- [`image-generation/`](../../sub/multimodal-and-generative-media/sub/image-generation/l10n/uk_UA/) — Producing images from text, images, layouts, masks, or other conditioning inputs.
- [`diffusion-models/`](../../sub/multimodal-and-generative-media/sub/diffusion-models/l10n/uk_UA/) — Generative models that learn to reverse a progressive noising process.
- [`image-to-image/`](../../sub/multimodal-and-generative-media/sub/image-to-image/l10n/uk_UA/) — Generating a transformed image while conditioning on an existing image.
- [`inpainting/`](../../sub/multimodal-and-generative-media/sub/inpainting/l10n/uk_UA/) — Regenerating selected masked regions of an image.
- [`controlnet/`](../../sub/multimodal-and-generative-media/sub/controlnet/l10n/uk_UA/) — Conditioning diffusion models with structural controls such as edges, depth, or pose.
- [`multimodal-context/`](../../sub/multimodal-and-generative-media/sub/multimodal-context/l10n/uk_UA/) — The combined text, image, audio, video, or document information available to a model request.

### Useful

- [`text-to-image/`](../../sub/multimodal-and-generative-media/sub/text-to-image/l10n/uk_UA/) — Generating images from natural-language descriptions.
- [`outpainting/`](../../sub/multimodal-and-generative-media/sub/outpainting/l10n/uk_UA/) — Extending an image beyond its original boundaries.
- [`image-embeddings/`](../../sub/multimodal-and-generative-media/sub/image-embeddings/l10n/uk_UA/) — Vector representations used to compare, retrieve, or classify visual content.
- [`speech-to-text/`](../../sub/multimodal-and-generative-media/sub/speech-to-text/l10n/uk_UA/) — Converting spoken audio into written text.
- [`text-to-speech/`](../../sub/multimodal-and-generative-media/sub/text-to-speech/l10n/uk_UA/) — Synthesizing spoken audio from written text.
- [`video-generation/`](../../sub/multimodal-and-generative-media/sub/video-generation/l10n/uk_UA/) — Producing or transforming sequences of visual frames with generative models.

### Specialized

- [`latent-space/`](../../sub/multimodal-and-generative-media/sub/latent-space/l10n/uk_UA/) — A compressed learned representation in which generative models encode and manipulate information.
- [`audio-generation/`](../../sub/multimodal-and-generative-media/sub/audio-generation/l10n/uk_UA/) — Producing music, speech, sound effects, or other audio with generative models.

## [Safety, Privacy, and Reliability](../../sub/safety-privacy-and-reliability/l10n/uk_UA/)

Concepts for controlling model behavior, protecting data, and reducing operational risk in AI systems.

### Essential

- [`prompt-injection/`](../../sub/safety-privacy-and-reliability/sub/prompt-injection/l10n/uk_UA/) — Input designed to override or manipulate an AI system's intended instructions.
- [`indirect-prompt-injection/`](../../sub/safety-privacy-and-reliability/sub/indirect-prompt-injection/l10n/uk_UA/) — Malicious or conflicting instructions embedded in external content processed by an AI system.
- [`trust-boundaries/`](../../sub/safety-privacy-and-reliability/sub/trust-boundaries/l10n/uk_UA/) — Explicit separation between trusted instructions, trusted systems, users, and untrusted data.
- [`least-privilege/`](../../sub/safety-privacy-and-reliability/sub/least-privilege/l10n/uk_UA/) — Granting an AI system only the permissions required for its current task.
- [`sandboxing/`](../../sub/safety-privacy-and-reliability/sub/sandboxing/l10n/uk_UA/) — Isolating execution so failures or malicious behavior have limited impact.
- [`secret-handling/`](../../sub/safety-privacy-and-reliability/sub/secret-handling/l10n/uk_UA/) — Protecting credentials, tokens, keys, and other sensitive operational data.
- [`data-privacy/`](../../sub/safety-privacy-and-reliability/sub/data-privacy/l10n/uk_UA/) — Controlling how personal, confidential, or sensitive data is collected, processed, retained, and shared.
- [`retrieval-poisoning/`](../../sub/safety-privacy-and-reliability/sub/retrieval-poisoning/l10n/uk_UA/) — Manipulating indexed knowledge so retrieval supplies misleading or malicious context.

### Useful

- [`guardrails/`](../../sub/safety-privacy-and-reliability/sub/guardrails/l10n/uk_UA/) — Controls that validate, restrict, or monitor model inputs, outputs, and actions.
- [`data-residency/`](../../sub/safety-privacy-and-reliability/sub/data-residency/l10n/uk_UA/) — The geographic or jurisdictional location where data is stored or processed.
- [`provenance/`](../../sub/safety-privacy-and-reliability/sub/provenance/l10n/uk_UA/) — Information about the origin, ownership, transformation, and custody of data or model artifacts.
- [`content-moderation/`](../../sub/safety-privacy-and-reliability/sub/content-moderation/l10n/uk_UA/) — Detecting or restricting content according to safety, legal, or platform policies.

### Specialized

- [`jailbreaking/`](../../sub/safety-privacy-and-reliability/sub/jailbreaking/l10n/uk_UA/) — Attempts to bypass a model's configured safety or policy constraints.
- [`model-alignment/`](../../sub/safety-privacy-and-reliability/sub/model-alignment/l10n/uk_UA/) — Shaping model behavior toward intended goals, values, policies, or preferences.
- [`data-poisoning/`](../../sub/safety-privacy-and-reliability/sub/data-poisoning/l10n/uk_UA/) — Corrupting training or adaptation data to degrade or manipulate model behavior.

## [Evaluation and Operations](../../sub/evaluation-and-operations/l10n/uk_UA/)

Concepts for selecting, testing, observing, and operating AI systems under real quality, cost, and reliability constraints.

### Essential

- [`evals/`](../../sub/evaluation-and-operations/sub/evals/l10n/uk_UA/) — Repeatable tests that measure whether an AI model or system meets defined requirements.
- [`model-selection/`](../../sub/evaluation-and-operations/sub/model-selection/l10n/uk_UA/) — Choosing a model based on task quality, capabilities, cost, latency, safety, and deployment constraints.
- [`model-routing/`](../../sub/evaluation-and-operations/sub/model-routing/l10n/uk_UA/) — Selecting among models dynamically according to the request or operating policy.
- [`observability/`](../../sub/evaluation-and-operations/sub/observability/l10n/uk_UA/) — Using logs, metrics, traces, and events to understand AI system behavior.
- [`tracing/`](../../sub/evaluation-and-operations/sub/tracing/l10n/uk_UA/) — Recording the sequence of model, tool, retrieval, and workflow operations for one execution.
- [`cost-management/`](../../sub/evaluation-and-operations/sub/cost-management/l10n/uk_UA/) — Measuring and controlling model, infrastructure, storage, and tool expenses.
- [`latency-and-throughput/`](../../sub/evaluation-and-operations/sub/latency-and-throughput/l10n/uk_UA/) — Balancing response time against the amount of work completed per unit of time.
- [`quality-cost-tradeoffs/`](../../sub/evaluation-and-operations/sub/quality-cost-tradeoffs/l10n/uk_UA/) — Choosing an acceptable balance between output quality and operational expense.

### Useful

- [`benchmarks/`](../../sub/evaluation-and-operations/sub/benchmarks/l10n/uk_UA/) — Standardized tasks or datasets used to compare models or systems.
- [`evaluation-datasets/`](../../sub/evaluation-and-operations/sub/evaluation-datasets/l10n/uk_UA/) — Curated examples used to test quality, safety, retrieval, or task performance.
- [`human-evaluation/`](../../sub/evaluation-and-operations/sub/human-evaluation/l10n/uk_UA/) — People assessing model outputs against explicit criteria.
- [`fallback-models/`](../../sub/evaluation-and-operations/sub/fallback-models/l10n/uk_UA/) — Alternative models used when the preferred model fails, is unavailable, or exceeds policy limits.
- [`caching/`](../../sub/evaluation-and-operations/sub/caching/l10n/uk_UA/) — Reusing prior results or processed data to reduce repeated work.
- [`rate-limits/`](../../sub/evaluation-and-operations/sub/rate-limits/l10n/uk_UA/) — Controls that restrict request volume over a period of time.

### Specialized

- [`llm-as-a-judge/`](../../sub/evaluation-and-operations/sub/llm-as-a-judge/l10n/uk_UA/) — Using a language model to score, rank, or critique other model outputs.
- [`retrieval-evaluation/`](../../sub/evaluation-and-operations/sub/retrieval-evaluation/l10n/uk_UA/) — Measuring whether retrieval returns relevant, complete, and correctly ranked evidence.
- [`reproducibility/`](../../sub/evaluation-and-operations/sub/reproducibility/l10n/uk_UA/) — The ability to repeat an evaluation or workflow with comparable conditions and results.
