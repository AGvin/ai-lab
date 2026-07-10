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
  - [`concepts/`](./docs/notes/sub/concepts/) — explanations of AI concepts.
    - [`lora/`](./docs/notes/sub/concepts/sub/lora/) — Low-Rank Adaptation concept.
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
