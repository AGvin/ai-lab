# AI Lab

<!--
ai_content:
  managed: true
  l10n: true
-->

Practical AI lab for models, tools, local inference, benchmarks, hardware notes, and automation workflows.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Status

This repository is an active public documentation lab. Content is added incrementally when a topic has real notes, references, or practical evaluation value.

## Documentation Map

### Start here

- [`overview/`](./docs/overview/) — repository documentation model, current layout, asset rules, and expansion guidance.

### Decision support

- [`agentic-systems/`](./docs/notes/sub/comparisons/sub/agentic-systems/) — cross-category comparison of agents, orchestration systems, coding-agent control centers, and adjacent agentic AI tools.
- [`comparisons/`](./docs/notes/sub/comparisons/) — decision-support comparisons across models, tools, workflows, platforms, and AI systems.
- [`benchmarks/`](./docs/notes/sub/benchmarks/) — benchmark and leaderboard references for evaluating models, providers, and AI systems.

### Software

- [`software/`](./docs/software/) — AI-related software, model platforms, inference tools, workflow engines, code editors, agents, assistants, automation tools, and models.
  - [`inference/`](./docs/software/sub/inference/) — tools for local or self-hosted model execution.
    - [`ollama/`](./docs/software/sub/inference/sub/ollama/) — local and self-hosted model runtime.
    - [`lm-studio/`](./docs/software/sub/inference/sub/lm-studio/) — desktop model runner and local model server.
  - [`workflow-engines/`](./docs/software/sub/workflow-engines/) — tools that build, arrange, or execute AI workflows.
    - [`comfy-ui/`](./docs/software/sub/workflow-engines/sub/comfy-ui/) — node-based AI image generation workflow UI.
  - [`code-editors/`](./docs/software/sub/code-editors/) — code editors and editor extension ecosystems used for AI-assisted development.
    - [`cursor/`](./docs/software/sub/code-editors/sub/cursor/) — AI-enabled code editor.
    - [`vs-code/`](./docs/software/sub/code-editors/sub/vs-code/) — extensible code editor for AI-assisted workflows.
      - [`extensions/`](./docs/software/sub/code-editors/sub/vs-code/sub/extensions/) — AI-related Visual Studio Code extensions.
        - [`continue/`](./docs/software/sub/code-editors/sub/vs-code/sub/extensions/sub/continue/) — AI coding assistant extension.
  - [`agents/`](./docs/software/sub/agents/) — standalone agent-like AI systems where agent behavior is the primary documented role.
    - [`hermes-agent/`](./docs/software/sub/agents/sub/hermes-agent/) — AI agent entry requiring source confirmation.
    - [`openclaw/`](./docs/software/sub/agents/sub/openclaw/) — browser-use AI agent project.
    - [`pi/`](./docs/software/sub/agents/sub/pi/) — terminal coding-agent harness documented at pi.dev.
  - [`agent-orchestration/`](./docs/software/sub/agent-orchestration/) — systems, frameworks, runtimes, and control planes for coordinating or running AI agents.
    - [`autogen/`](./docs/software/sub/agent-orchestration/sub/autogen/) — multi-agent conversation framework.
    - [`crewai/`](./docs/software/sub/agent-orchestration/sub/crewai/) — collaborative multi-agent orchestration framework.
    - [`langgraph/`](./docs/software/sub/agent-orchestration/sub/langgraph/) — stateful agent orchestration framework and runtime.
    - [`openhands/`](./docs/software/sub/agent-orchestration/sub/openhands/) — developer control center for coding agents and automations.
  - [`assistants/`](./docs/software/sub/assistants/) — conversational AI assistants.
  - [`automation/`](./docs/software/sub/automation/) — automation tools that can support AI-adjacent workflows.
    - [`playwright/`](./docs/software/sub/automation/sub/playwright/) — browser automation and end-to-end web testing framework.
  - [`model-platforms/`](./docs/software/sub/model-platforms/) — platforms for model discovery, hosting, datasets, Spaces, or related tooling.
    - [`hugging-face/`](./docs/software/sub/model-platforms/sub/hugging-face/) — model, dataset, Spaces, and AI tooling platform.
  - [`models/`](./docs/software/sub/models/) — model families and individual models.
    - [`image-generation/`](./docs/software/sub/models/sub/image-generation/) — image generation models.
      - [`z-image/`](./docs/software/sub/models/sub/image-generation/sub/z-image/) — Alibaba image generation model.
    - [`multimodal/`](./docs/software/sub/models/sub/multimodal/) — multimodal models.
      - [`glm-5v-turbo/`](./docs/software/sub/models/sub/multimodal/sub/glm-5v-turbo/) — multimodal foundation model for agentic workflows.

### Notes

- [`notes/`](./docs/notes/) — concepts, benchmarks, comparisons, and practical AI notes that are not themselves software or hardware documentation.
  - [`concepts/`](./docs/notes/sub/concepts/) — practical and foundational AI concepts organized by topic and priority.
    - [`foundations-and-architecture/`](./docs/notes/sub/concepts/sub/foundations-and-architecture/) — Core concepts that explain what modern AI models are and how their main architectural families relate.
      - Essential
        - [`foundation-models/`](./docs/notes/sub/concepts/sub/foundations-and-architecture/sub/foundation-models/)
        - [`large-language-models/`](./docs/notes/sub/concepts/sub/foundations-and-architecture/sub/large-language-models/)
        - [`multimodal-models/`](./docs/notes/sub/concepts/sub/foundations-and-architecture/sub/multimodal-models/)
      - Useful
        - [`transformers/`](./docs/notes/sub/concepts/sub/foundations-and-architecture/sub/transformers/)
        - [`attention/`](./docs/notes/sub/concepts/sub/foundations-and-architecture/sub/attention/)
        - [`mixture-of-experts/`](./docs/notes/sub/concepts/sub/foundations-and-architecture/sub/mixture-of-experts/)
      - Specialized
        - [`artificial-intelligence/`](./docs/notes/sub/concepts/sub/foundations-and-architecture/sub/artificial-intelligence/)
        - [`machine-learning/`](./docs/notes/sub/concepts/sub/foundations-and-architecture/sub/machine-learning/)
        - [`deep-learning/`](./docs/notes/sub/concepts/sub/foundations-and-architecture/sub/deep-learning/)
        - [`neural-networks/`](./docs/notes/sub/concepts/sub/foundations-and-architecture/sub/neural-networks/)
        - [`self-attention/`](./docs/notes/sub/concepts/sub/foundations-and-architecture/sub/self-attention/)
        - [`encoder-decoder/`](./docs/notes/sub/concepts/sub/foundations-and-architecture/sub/encoder-decoder/)
        - [`dense-and-sparse-models/`](./docs/notes/sub/concepts/sub/foundations-and-architecture/sub/dense-and-sparse-models/)
    - [`model-usage-and-generation/`](./docs/notes/sub/concepts/sub/model-usage-and-generation/) — Concepts for using trained models effectively through chats, APIs, applications, and local runtimes.
      - Essential
        - [`tokens-and-tokenization/`](./docs/notes/sub/concepts/sub/model-usage-and-generation/sub/tokens-and-tokenization/)
        - [`context-window/`](./docs/notes/sub/concepts/sub/model-usage-and-generation/sub/context-window/)
        - [`prompting/`](./docs/notes/sub/concepts/sub/model-usage-and-generation/sub/prompting/)
        - [`system-prompts/`](./docs/notes/sub/concepts/sub/model-usage-and-generation/sub/system-prompts/)
        - [`structured-output/`](./docs/notes/sub/concepts/sub/model-usage-and-generation/sub/structured-output/)
        - [`hallucinations/`](./docs/notes/sub/concepts/sub/model-usage-and-generation/sub/hallucinations/)
      - Useful
        - [`few-shot-prompting/`](./docs/notes/sub/concepts/sub/model-usage-and-generation/sub/few-shot-prompting/)
        - [`sampling-parameters/`](./docs/notes/sub/concepts/sub/model-usage-and-generation/sub/sampling-parameters/)
        - [`reasoning-models/`](./docs/notes/sub/concepts/sub/model-usage-and-generation/sub/reasoning-models/)
        - [`model-capabilities-and-limitations/`](./docs/notes/sub/concepts/sub/model-usage-and-generation/sub/model-capabilities-and-limitations/)
      - Specialized
        - [`constrained-generation/`](./docs/notes/sub/concepts/sub/model-usage-and-generation/sub/constrained-generation/)
        - [`chain-of-thought/`](./docs/notes/sub/concepts/sub/model-usage-and-generation/sub/chain-of-thought/)
    - [`retrieval-and-knowledge/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/) — Concepts for connecting models to external information, searchable documents, and evidence-backed context.
      - Essential
        - [`rag/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/rag/)
        - [`embeddings/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/embeddings/)
        - [`chunking/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/chunking/)
        - [`semantic-search/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/semantic-search/)
        - [`hybrid-search/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/hybrid-search/)
        - [`grounding/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/grounding/)
      - Useful
        - [`vector-search/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/vector-search/)
        - [`vector-databases/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/vector-databases/)
        - [`keyword-search/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/keyword-search/)
        - [`reranking/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/reranking/)
        - [`citations/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/citations/)
        - [`metadata-filtering/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/metadata-filtering/)
      - Specialized
        - [`bm25/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/bm25/)
        - [`graph-rag/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/graph-rag/)
        - [`knowledge-graphs/`](./docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/knowledge-graphs/)
    - [`agents-and-automation/`](./docs/notes/sub/concepts/sub/agents-and-automation/) — Concepts for configuring AI systems that plan, use tools, maintain state, and perform controlled actions.
      - Essential
        - [`ai-agents/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/ai-agents/)
        - [`agentic-workflows/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/agentic-workflows/)
        - [`tool-calling/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/tool-calling/)
        - [`agent-state/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/agent-state/)
        - [`agent-memory/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/agent-memory/)
        - [`planning/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/planning/)
        - [`verification-and-reflection/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/verification-and-reflection/)
        - [`human-in-the-loop/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/human-in-the-loop/)
        - [`idempotency/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/idempotency/)
        - [`failure-recovery/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/failure-recovery/)
      - Useful
        - [`function-calling/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/function-calling/)
        - [`task-decomposition/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/task-decomposition/)
        - [`retries/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/retries/)
        - [`autonomy-levels/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/autonomy-levels/)
      - Specialized
        - [`multi-agent-systems/`](./docs/notes/sub/concepts/sub/agents-and-automation/sub/multi-agent-systems/)
    - [`inference-and-serving/`](./docs/notes/sub/concepts/sub/inference-and-serving/) — Concepts for running trained models locally or as services and understanding their resource and performance behavior.
      - Essential
        - [`inference/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/inference/)
        - [`quantization/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/quantization/)
        - [`numerical-precision/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/numerical-precision/)
        - [`model-formats/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/model-formats/)
        - [`gpu-offloading/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/gpu-offloading/)
        - [`kv-cache/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/kv-cache/)
        - [`latency/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/latency/)
        - [`throughput/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/throughput/)
        - [`performance-metrics/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/performance-metrics/)
      - Useful
        - [`model-serving/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/model-serving/)
        - [`model-loading/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/model-loading/)
        - [`cpu-inference/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/cpu-inference/)
        - [`gpu-inference/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/gpu-inference/)
        - [`context-caching/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/context-caching/)
      - Specialized
        - [`flash-attention/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/flash-attention/)
        - [`continuous-batching/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/continuous-batching/)
        - [`speculative-decoding/`](./docs/notes/sub/concepts/sub/inference-and-serving/sub/speculative-decoding/)
    - [`training-and-adaptation/`](./docs/notes/sub/concepts/sub/training-and-adaptation/) — Concepts for training models or adapting existing models to tasks, domains, preferences, and deployment constraints.
      - Essential
        - [`fine-tuning/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/fine-tuning/)
        - [`parameter-efficient-fine-tuning/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/parameter-efficient-fine-tuning/)
        - [`lora/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/lora/)
        - [`qlora/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/qlora/)
      - Useful
        - [`supervised-fine-tuning/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/supervised-fine-tuning/)
        - [`adapters/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/adapters/)
        - [`instruction-tuning/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/instruction-tuning/)
        - [`synthetic-data/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/synthetic-data/)
        - [`datasets/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/datasets/)
        - [`overfitting/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/overfitting/)
      - Specialized
        - [`pretraining/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/pretraining/)
        - [`preference-optimization/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/preference-optimization/)
        - [`rlhf/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/rlhf/)
        - [`dpo/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/dpo/)
        - [`distillation/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/distillation/)
        - [`pruning/`](./docs/notes/sub/concepts/sub/training-and-adaptation/sub/pruning/)
    - [`multimodal-and-generative-media/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/) — Concepts for models and workflows involving images, audio, video, and combinations of modalities.
      - Essential
        - [`vision-language-models/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/vision-language-models/)
        - [`image-generation/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/image-generation/)
        - [`diffusion-models/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/diffusion-models/)
        - [`image-to-image/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/image-to-image/)
        - [`inpainting/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/inpainting/)
        - [`controlnet/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/controlnet/)
        - [`multimodal-context/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/multimodal-context/)
      - Useful
        - [`text-to-image/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/text-to-image/)
        - [`outpainting/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/outpainting/)
        - [`image-embeddings/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/image-embeddings/)
        - [`speech-to-text/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/speech-to-text/)
        - [`text-to-speech/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/text-to-speech/)
        - [`video-generation/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/video-generation/)
      - Specialized
        - [`latent-space/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/latent-space/)
        - [`audio-generation/`](./docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/audio-generation/)
    - [`safety-privacy-and-reliability/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/) — Concepts for controlling model behavior, protecting data, and reducing operational risk in AI systems.
      - Essential
        - [`prompt-injection/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/prompt-injection/)
        - [`indirect-prompt-injection/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/indirect-prompt-injection/)
        - [`trust-boundaries/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/trust-boundaries/)
        - [`least-privilege/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/least-privilege/)
        - [`sandboxing/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/sandboxing/)
        - [`secret-handling/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/secret-handling/)
        - [`data-privacy/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/data-privacy/)
        - [`retrieval-poisoning/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/retrieval-poisoning/)
      - Useful
        - [`guardrails/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/guardrails/)
        - [`data-residency/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/data-residency/)
        - [`provenance/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/provenance/)
        - [`content-moderation/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/content-moderation/)
      - Specialized
        - [`jailbreaking/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/jailbreaking/)
        - [`model-alignment/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/model-alignment/)
        - [`data-poisoning/`](./docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/data-poisoning/)
    - [`evaluation-and-operations/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/) — Concepts for selecting, testing, observing, and operating AI systems under real quality, cost, and reliability constraints.
      - Essential
        - [`evals/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/evals/)
        - [`model-selection/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/model-selection/)
        - [`model-routing/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/model-routing/)
        - [`observability/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/observability/)
        - [`tracing/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/tracing/)
        - [`cost-management/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/cost-management/)
        - [`latency-and-throughput/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/latency-and-throughput/)
        - [`quality-cost-tradeoffs/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/quality-cost-tradeoffs/)
      - Useful
        - [`benchmarks/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/benchmarks/)
        - [`evaluation-datasets/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/evaluation-datasets/)
        - [`human-evaluation/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/human-evaluation/)
        - [`fallback-models/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/fallback-models/)
        - [`caching/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/caching/)
        - [`rate-limits/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/rate-limits/)
      - Specialized
        - [`llm-as-a-judge/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/llm-as-a-judge/)
        - [`retrieval-evaluation/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/retrieval-evaluation/)
        - [`reproducibility/`](./docs/notes/sub/concepts/sub/evaluation-and-operations/sub/reproducibility/)
  - [`benchmarks/`](./docs/notes/sub/benchmarks/) — benchmark and leaderboard notes for AI models, providers, and systems.
    - [`livebench/`](./docs/notes/sub/benchmarks/sub/livebench/) — AI model benchmark.
    - [`open-llm-leaderboard/`](./docs/notes/sub/benchmarks/sub/open-llm-leaderboard/) — Open LLM leaderboard view from LLM Stats.
    - [`benchlm/`](./docs/notes/sub/benchmarks/sub/benchlm/) — AI benchmark resource.
    - [`arena/`](./docs/notes/sub/benchmarks/sub/arena/) — AI leaderboard resource.
    - [`artificial-analysis/`](./docs/notes/sub/benchmarks/sub/artificial-analysis/) — provider and model analysis leaderboard.
  - [`comparisons/`](./docs/notes/sub/comparisons/) — decision-support comparisons across models, tools, workflows, platforms, and AI systems.
    - [`agentic-systems/`](./docs/notes/sub/comparisons/sub/agentic-systems/) — cross-category comparison of agents, orchestration systems, coding-agent control centers, and adjacent agentic AI tools.

## License

This repository is licensed under the MIT License.

When reusing or adapting materials from this repository, please keep the original copyright notice and reference this repository as the source.
