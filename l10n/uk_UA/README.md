<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:84cc0060b305385645f5f402776606d945425335
  mode: translated
-->

# AI Lab

Практична AI lab для моделей, інструментів, локального inference, benchmarks, hardware notes та automation workflows.

## Переклади

- [English](../../)
- Українська — поточна

## Статус

Цей репозиторій є активною публічною documentation lab. Вміст додається поступово, коли тема має реальні нотатки, references або практичну цінність для оцінювання.

## Мапа документації

### Почати звідси

- [`overview/`](../../docs/overview/l10n/uk_UA/) — модель документації репозиторію, поточна структура, правила assets та настанови щодо розширення.

### Підтримка рішень

- [`agentic-systems/`](../../docs/notes/sub/comparisons/sub/agentic-systems/l10n/uk_UA/) — міжкатегорійне порівняння агентів, orchestration systems, coding-agent control centers та суміжних agentic AI tools.
- [`comparisons/`](../../docs/notes/sub/comparisons/l10n/uk_UA/) — порівняння для прийняття рішень щодо моделей, інструментів, workflows, platforms та AI systems.
- [`benchmarks/`](../../docs/notes/sub/benchmarks/l10n/uk_UA/) — benchmark і leaderboard references для оцінювання моделей, providers та AI systems.

### Software

- [`software/`](../../docs/software/l10n/uk_UA/) — AI-related software, model platforms, inference tools, workflow engines, code editors, agents, assistants, automation tools та models.
  - [`inference/`](../../docs/software/sub/inference/l10n/uk_UA/) — інструменти для локального або self-hosted model execution.
    - [`ollama/`](../../docs/software/sub/inference/sub/ollama/l10n/uk_UA/) — local та self-hosted model runtime.
    - [`lm-studio/`](../../docs/software/sub/inference/sub/lm-studio/l10n/uk_UA/) — desktop model runner та local model server.
  - [`workflow-engines/`](../../docs/software/sub/workflow-engines/l10n/uk_UA/) — інструменти, що будують, компонують або виконують AI workflows.
    - [`comfy-ui/`](../../docs/software/sub/workflow-engines/sub/comfy-ui/l10n/uk_UA/) — node-based AI image generation workflow UI.
  - [`code-editors/`](../../docs/software/sub/code-editors/l10n/uk_UA/) — code editors та editor extension ecosystems для AI-assisted development.
    - [`cursor/`](../../docs/software/sub/code-editors/sub/cursor/l10n/uk_UA/) — AI-enabled code editor.
    - [`vs-code/`](../../docs/software/sub/code-editors/sub/vs-code/l10n/uk_UA/) — extensible code editor для AI-assisted workflows.
      - [`extensions/`](../../docs/software/sub/code-editors/sub/vs-code/sub/extensions/l10n/uk_UA/) — AI-related Visual Studio Code extensions.
        - [`continue/`](../../docs/software/sub/code-editors/sub/vs-code/sub/extensions/sub/continue/l10n/uk_UA/) — AI coding assistant extension.
  - [`agents/`](../../docs/software/sub/agents/l10n/uk_UA/) — standalone agent-like AI systems, де agent behavior є primary documented role.
    - [`hermes-agent/`](../../docs/software/sub/agents/sub/hermes-agent/l10n/uk_UA/) — AI agent entry requiring source confirmation.
    - [`openclaw/`](../../docs/software/sub/agents/sub/openclaw/l10n/uk_UA/) — browser-use AI agent project.
    - [`pi/`](../../docs/software/sub/agents/sub/pi/l10n/uk_UA/) — terminal coding-agent harness, documented at pi.dev.
  - [`agent-orchestration/`](../../docs/software/sub/agent-orchestration/l10n/uk_UA/) — systems, frameworks, runtimes та control planes для coordinating або running AI agents.
    - [`autogen/`](../../docs/software/sub/agent-orchestration/sub/autogen/l10n/uk_UA/) — multi-agent conversation framework.
    - [`crewai/`](../../docs/software/sub/agent-orchestration/sub/crewai/l10n/uk_UA/) — collaborative multi-agent orchestration framework.
    - [`langgraph/`](../../docs/software/sub/agent-orchestration/sub/langgraph/l10n/uk_UA/) — stateful agent orchestration framework and runtime.
    - [`openhands/`](../../docs/software/sub/agent-orchestration/sub/openhands/l10n/uk_UA/) — developer control center for coding agents and automations.
  - [`assistants/`](../../docs/software/sub/assistants/l10n/uk_UA/) — conversational AI assistants.
  - [`automation/`](../../docs/software/sub/automation/l10n/uk_UA/) — automation tools, що можуть підтримувати AI-adjacent workflows.
    - [`playwright/`](../../docs/software/sub/automation/sub/playwright/l10n/uk_UA/) — browser automation and end-to-end web testing framework.
  - [`model-platforms/`](../../docs/software/sub/model-platforms/l10n/uk_UA/) — platforms для model discovery, hosting, datasets, Spaces або related tooling.
    - [`hugging-face/`](../../docs/software/sub/model-platforms/sub/hugging-face/l10n/uk_UA/) — model, dataset, Spaces та AI tooling platform.
  - [`models/`](../../docs/software/sub/models/l10n/uk_UA/) — model families та individual models.
    - [`image-generation/`](../../docs/software/sub/models/sub/image-generation/l10n/uk_UA/) — image generation models.
      - [`z-image/`](../../docs/software/sub/models/sub/image-generation/sub/z-image/l10n/uk_UA/) — Alibaba image generation model.
    - [`multimodal/`](../../docs/software/sub/models/sub/multimodal/l10n/uk_UA/) — multimodal models.
      - [`glm-5v-turbo/`](../../docs/software/sub/models/sub/multimodal/sub/glm-5v-turbo/l10n/uk_UA/) — multimodal foundation model для agentic workflows.

### Notes

- [`notes/`](../../docs/notes/l10n/uk_UA/) — concepts, benchmarks, comparisons та practical AI notes, які не є окремою software або hardware documentation.
  - [`concepts/`](../../docs/notes/sub/concepts/l10n/uk_UA/) — практичні та фундаментальні AI concepts, організовані за темою і пріоритетом.
    - [`foundations-and-architecture/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/l10n/uk_UA/) — Core concepts that explain what modern AI models are and how their main architectural families relate.
      - Essential
        - [`foundation-models/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/foundation-models/l10n/uk_UA/)
        - [`large-language-models/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/large-language-models/l10n/uk_UA/)
        - [`multimodal-models/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/multimodal-models/l10n/uk_UA/)
      - Useful
        - [`transformers/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/transformers/l10n/uk_UA/)
        - [`attention/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/attention/l10n/uk_UA/)
        - [`mixture-of-experts/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/mixture-of-experts/l10n/uk_UA/)
      - Specialized
        - [`artificial-intelligence/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/artificial-intelligence/l10n/uk_UA/)
        - [`machine-learning/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/machine-learning/l10n/uk_UA/)
        - [`deep-learning/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/deep-learning/l10n/uk_UA/)
        - [`neural-networks/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/neural-networks/l10n/uk_UA/)
        - [`self-attention/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/self-attention/l10n/uk_UA/)
        - [`encoder-decoder/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/encoder-decoder/l10n/uk_UA/)
        - [`dense-and-sparse-models/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/dense-and-sparse-models/l10n/uk_UA/)
    - [`model-usage-and-generation/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/l10n/uk_UA/) — Concepts for using trained models effectively through chats, APIs, applications, and local runtimes.
      - Essential
        - [`tokens-and-tokenization/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/tokens-and-tokenization/l10n/uk_UA/)
        - [`context-window/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/context-window/l10n/uk_UA/)
        - [`prompting/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/prompting/l10n/uk_UA/)
        - [`system-prompts/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/system-prompts/l10n/uk_UA/)
        - [`structured-output/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/structured-output/l10n/uk_UA/)
        - [`hallucinations/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/hallucinations/l10n/uk_UA/)
      - Useful
        - [`few-shot-prompting/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/few-shot-prompting/l10n/uk_UA/)
        - [`sampling-parameters/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/sampling-parameters/l10n/uk_UA/)
        - [`reasoning-models/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/reasoning-models/l10n/uk_UA/)
        - [`model-capabilities-and-limitations/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/model-capabilities-and-limitations/l10n/uk_UA/)
      - Specialized
        - [`constrained-generation/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/constrained-generation/l10n/uk_UA/)
        - [`chain-of-thought/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/chain-of-thought/l10n/uk_UA/)
    - [`retrieval-and-knowledge/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/l10n/uk_UA/) — Concepts for connecting models to external information, searchable documents, and evidence-backed context.
      - Essential
        - [`rag/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/rag/l10n/uk_UA/)
        - [`embeddings/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/embeddings/l10n/uk_UA/)
        - [`chunking/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/chunking/l10n/uk_UA/)
        - [`semantic-search/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/semantic-search/l10n/uk_UA/)
        - [`hybrid-search/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/hybrid-search/l10n/uk_UA/)
        - [`grounding/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/grounding/l10n/uk_UA/)
      - Useful
        - [`vector-search/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/vector-search/l10n/uk_UA/)
        - [`vector-databases/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/vector-databases/l10n/uk_UA/)
        - [`keyword-search/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/keyword-search/l10n/uk_UA/)
        - [`reranking/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/reranking/l10n/uk_UA/)
        - [`citations/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/citations/l10n/uk_UA/)
        - [`metadata-filtering/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/metadata-filtering/l10n/uk_UA/)
      - Specialized
        - [`bm25/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/bm25/l10n/uk_UA/)
        - [`graph-rag/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/graph-rag/l10n/uk_UA/)
        - [`knowledge-graphs/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/knowledge-graphs/l10n/uk_UA/)
    - [`agents-and-automation/`](../../docs/notes/sub/concepts/sub/agents-and-automation/l10n/uk_UA/) — Concepts for configuring AI systems that plan, use tools, maintain state, and perform controlled actions.
      - Essential
        - [`ai-agents/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/ai-agents/l10n/uk_UA/)
        - [`agentic-workflows/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/agentic-workflows/l10n/uk_UA/)
        - [`tool-calling/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/tool-calling/l10n/uk_UA/)
        - [`agent-state/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/agent-state/l10n/uk_UA/)
        - [`agent-memory/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/agent-memory/l10n/uk_UA/)
        - [`planning/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/planning/l10n/uk_UA/)
        - [`verification-and-reflection/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/verification-and-reflection/l10n/uk_UA/)
        - [`human-in-the-loop/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/human-in-the-loop/l10n/uk_UA/)
        - [`idempotency/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/idempotency/l10n/uk_UA/)
        - [`failure-recovery/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/failure-recovery/l10n/uk_UA/)
      - Useful
        - [`function-calling/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/function-calling/l10n/uk_UA/)
        - [`task-decomposition/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/task-decomposition/l10n/uk_UA/)
        - [`retries/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/retries/l10n/uk_UA/)
        - [`autonomy-levels/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/autonomy-levels/l10n/uk_UA/)
      - Specialized
        - [`multi-agent-systems/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/multi-agent-systems/l10n/uk_UA/)
    - [`inference-and-serving/`](../../docs/notes/sub/concepts/sub/inference-and-serving/l10n/uk_UA/) — Concepts for running trained models locally or as services and understanding their resource and performance behavior.
      - Essential
        - [`inference/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/inference/l10n/uk_UA/)
        - [`quantization/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/quantization/l10n/uk_UA/)
        - [`numerical-precision/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/numerical-precision/l10n/uk_UA/)
        - [`model-formats/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/model-formats/l10n/uk_UA/)
        - [`gpu-offloading/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/gpu-offloading/l10n/uk_UA/)
        - [`kv-cache/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/kv-cache/l10n/uk_UA/)
        - [`latency/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/latency/l10n/uk_UA/)
        - [`throughput/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/throughput/l10n/uk_UA/)
        - [`performance-metrics/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/performance-metrics/l10n/uk_UA/)
      - Useful
        - [`model-serving/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/model-serving/l10n/uk_UA/)
        - [`model-loading/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/model-loading/l10n/uk_UA/)
        - [`cpu-inference/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/cpu-inference/l10n/uk_UA/)
        - [`gpu-inference/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/gpu-inference/l10n/uk_UA/)
        - [`context-caching/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/context-caching/l10n/uk_UA/)
      - Specialized
        - [`flash-attention/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/flash-attention/l10n/uk_UA/)
        - [`continuous-batching/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/continuous-batching/l10n/uk_UA/)
        - [`speculative-decoding/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/speculative-decoding/l10n/uk_UA/)
    - [`training-and-adaptation/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/l10n/uk_UA/) — Concepts for training models or adapting existing models to tasks, domains, preferences, and deployment constraints.
      - Essential
        - [`fine-tuning/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/fine-tuning/l10n/uk_UA/)
        - [`parameter-efficient-fine-tuning/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/parameter-efficient-fine-tuning/l10n/uk_UA/)
        - [`lora/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/lora/l10n/uk_UA/)
        - [`qlora/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/qlora/l10n/uk_UA/)
      - Useful
        - [`supervised-fine-tuning/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/supervised-fine-tuning/l10n/uk_UA/)
        - [`adapters/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/adapters/l10n/uk_UA/)
        - [`instruction-tuning/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/instruction-tuning/l10n/uk_UA/)
        - [`synthetic-data/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/synthetic-data/l10n/uk_UA/)
        - [`datasets/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/datasets/l10n/uk_UA/)
        - [`overfitting/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/overfitting/l10n/uk_UA/)
      - Specialized
        - [`pretraining/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/pretraining/l10n/uk_UA/)
        - [`preference-optimization/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/preference-optimization/l10n/uk_UA/)
        - [`rlhf/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/rlhf/l10n/uk_UA/)
        - [`dpo/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/dpo/l10n/uk_UA/)
        - [`distillation/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/distillation/l10n/uk_UA/)
        - [`pruning/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/pruning/l10n/uk_UA/)
    - [`multimodal-and-generative-media/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/l10n/uk_UA/) — Concepts for models and workflows involving images, audio, video, and combinations of modalities.
      - Essential
        - [`vision-language-models/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/vision-language-models/l10n/uk_UA/)
        - [`image-generation/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/image-generation/l10n/uk_UA/)
        - [`diffusion-models/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/diffusion-models/l10n/uk_UA/)
        - [`image-to-image/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/image-to-image/l10n/uk_UA/)
        - [`inpainting/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/inpainting/l10n/uk_UA/)
        - [`controlnet/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/controlnet/l10n/uk_UA/)
        - [`multimodal-context/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/multimodal-context/l10n/uk_UA/)
      - Useful
        - [`text-to-image/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/text-to-image/l10n/uk_UA/)
        - [`outpainting/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/outpainting/l10n/uk_UA/)
        - [`image-embeddings/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/image-embeddings/l10n/uk_UA/)
        - [`speech-to-text/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/speech-to-text/l10n/uk_UA/)
        - [`text-to-speech/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/text-to-speech/l10n/uk_UA/)
        - [`video-generation/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/video-generation/l10n/uk_UA/)
      - Specialized
        - [`latent-space/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/latent-space/l10n/uk_UA/)
        - [`audio-generation/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/audio-generation/l10n/uk_UA/)
    - [`safety-privacy-and-reliability/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/l10n/uk_UA/) — Concepts for controlling model behavior, protecting data, and reducing operational risk in AI systems.
      - Essential
        - [`prompt-injection/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/prompt-injection/l10n/uk_UA/)
        - [`indirect-prompt-injection/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/indirect-prompt-injection/l10n/uk_UA/)
        - [`trust-boundaries/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/trust-boundaries/l10n/uk_UA/)
        - [`least-privilege/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/least-privilege/l10n/uk_UA/)
        - [`sandboxing/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/sandboxing/l10n/uk_UA/)
        - [`secret-handling/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/secret-handling/l10n/uk_UA/)
        - [`data-privacy/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/data-privacy/l10n/uk_UA/)
        - [`retrieval-poisoning/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/retrieval-poisoning/l10n/uk_UA/)
      - Useful
        - [`guardrails/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/guardrails/l10n/uk_UA/)
        - [`data-residency/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/data-residency/l10n/uk_UA/)
        - [`provenance/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/provenance/l10n/uk_UA/)
        - [`content-moderation/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/content-moderation/l10n/uk_UA/)
      - Specialized
        - [`jailbreaking/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/jailbreaking/l10n/uk_UA/)
        - [`model-alignment/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/model-alignment/l10n/uk_UA/)
        - [`data-poisoning/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/data-poisoning/l10n/uk_UA/)
    - [`evaluation-and-operations/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/l10n/uk_UA/) — Concepts for selecting, testing, observing, and operating AI systems under real quality, cost, and reliability constraints.
      - Essential
        - [`evals/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/evals/l10n/uk_UA/)
        - [`model-selection/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/model-selection/l10n/uk_UA/)
        - [`model-routing/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/model-routing/l10n/uk_UA/)
        - [`observability/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/observability/l10n/uk_UA/)
        - [`tracing/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/tracing/l10n/uk_UA/)
        - [`cost-management/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/cost-management/l10n/uk_UA/)
        - [`latency-and-throughput/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/latency-and-throughput/l10n/uk_UA/)
        - [`quality-cost-tradeoffs/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/quality-cost-tradeoffs/l10n/uk_UA/)
      - Useful
        - [`benchmarks/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/benchmarks/l10n/uk_UA/)
        - [`evaluation-datasets/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/evaluation-datasets/l10n/uk_UA/)
        - [`human-evaluation/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/human-evaluation/l10n/uk_UA/)
        - [`fallback-models/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/fallback-models/l10n/uk_UA/)
        - [`caching/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/caching/l10n/uk_UA/)
        - [`rate-limits/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/rate-limits/l10n/uk_UA/)
      - Specialized
        - [`llm-as-a-judge/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/llm-as-a-judge/l10n/uk_UA/)
        - [`retrieval-evaluation/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/retrieval-evaluation/l10n/uk_UA/)
        - [`reproducibility/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/reproducibility/l10n/uk_UA/)
  - [`benchmarks/`](../../docs/notes/sub/benchmarks/l10n/uk_UA/) — benchmark and leaderboard notes для AI models, providers та systems.
    - [`livebench/`](../../docs/notes/sub/benchmarks/sub/livebench/l10n/uk_UA/) — AI model benchmark.
    - [`open-llm-leaderboard/`](../../docs/notes/sub/benchmarks/sub/open-llm-leaderboard/l10n/uk_UA/) — Open LLM leaderboard view from LLM Stats.
    - [`benchlm/`](../../docs/notes/sub/benchmarks/sub/benchlm/l10n/uk_UA/) — AI benchmark resource.
    - [`arena/`](../../docs/notes/sub/benchmarks/sub/arena/l10n/uk_UA/) — AI leaderboard resource.
    - [`artificial-analysis/`](../../docs/notes/sub/benchmarks/sub/artificial-analysis/l10n/uk_UA/) — provider and model analysis leaderboard.
  - [`comparisons/`](../../docs/notes/sub/comparisons/l10n/uk_UA/) — decision-support comparisons across models, tools, workflows, platforms та AI systems.
    - [`agentic-systems/`](../../docs/notes/sub/comparisons/sub/agentic-systems/l10n/uk_UA/) — cross-category comparison agents, orchestration systems, coding-agent control centers та adjacent agentic AI tools.

## Ліцензія

Цей репозиторій ліцензовано за MIT License.

Під час повторного використання або адаптації матеріалів з цього репозиторію зберігайте оригінальний copyright notice і посилайтеся на цей репозиторій як на джерело.
