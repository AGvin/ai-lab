# Documentation Requirements

## Requirements

- Identify Spring AI as the Spring ecosystem's application framework for integrating AI models and generative-AI patterns into Java and Spring applications.
- Preserve portable model APIs, chat/client abstractions, embeddings, vector-store integrations, tool calling, structured output, Advisors, MCP, ETL/data ingestion, and RAG as high-level framework capabilities.
- Preserve Spring as the canonical producer/project identity through the `produced-by` relation.
- Keep concrete model/vector-store provider inventories, Spring Boot/version compatibility, package versions, and other mutable integration facts source-backed when expanded.
- Preserve the application-framework boundary: Spring AI can implement tools and RAG without becoming primarily an agent-orchestration or retrieval-only framework.
- Include current official Spring AI reference documentation and project page.

## Validation

- The profile does not reduce Spring AI to only model API wrappers or only RAG.
- Portable APIs are not described as guaranteeing identical provider capabilities.
- The producer link resolves to the canonical Spring producer profile.
- Official resource links match canonical entity metadata.
