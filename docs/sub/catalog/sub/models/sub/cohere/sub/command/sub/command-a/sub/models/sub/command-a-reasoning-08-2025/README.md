# Command A Reasoning

Command A Reasoning is the 111B August 2025 text model with optional reasoning for tools, agents and multilingual tasks.

## Identity and provenance

The public card explicitly credits Cohere and Cohere Labs. Its official Hub metadata lists c4ai-command-a-03-2025 as a base model, supporting the specific derived-from relation without inferring unreported training details. [Command A Reasoning model card](https://huggingface.co/CohereLabs/command-a-reasoning-08-2025) [Command A Reasoning model card public metadata](https://huggingface.co/api/models/CohereLabs/command-a-reasoning-08-2025?blobs=true).

## Decision and operating boundaries

- The model advertises a 256K context and 23 languages; the live API identifier command-a-reasoning-08-2025 has a 32K maximum output. Reasoning and final-answer tokens must fit the applicable output budget. [Command A Reasoning documentation](https://docs.cohere.com/docs/command-a-reasoning) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Cohere reasoning controls](https://docs.cohere.com/v2/docs/reasoning).
- The Cohere Chat API enables thinking by default, can disable it, and can set a thinking-token budget. The guide recommends leaving at least 1K tokens for the final answer; local chat-template controls are implementation-specific. [Cohere reasoning controls](https://docs.cohere.com/v2/docs/reasoning) [Command A Reasoning model card](https://huggingface.co/CohereLabs/command-a-reasoning-08-2025).
- The research weights state CC-BY-NC 4.0 plus the acceptable-use policy. Reasoning can increase latency and token consumption; it does not guarantee correct plans or safe tool execution. The documented GPU examples are deployment guidance, not local measurements. [Command A Reasoning model card](https://huggingface.co/CohereLabs/command-a-reasoning-08-2025) [Command A Reasoning documentation](https://docs.cohere.com/docs/command-a-reasoning) [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license) [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).

## Catalog relations

- [Cohere Labs](../../../../../../../../../../../producers/sub/c/sub/cohere-labs/) — producer.
- [Command A](../../../../) — series or family.
- [Command A](../command-a-03-2025/) — derived from.

## Official resources

- [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- [Command A Reasoning model card](https://huggingface.co/CohereLabs/command-a-reasoning-08-2025).
- [Command A Reasoning model card public metadata](https://huggingface.co/api/models/CohereLabs/command-a-reasoning-08-2025?blobs=true).
- [Command A Reasoning documentation](https://docs.cohere.com/docs/command-a-reasoning).
- [Cohere reasoning controls](https://docs.cohere.com/v2/docs/reasoning).
- [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license).
- [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).
