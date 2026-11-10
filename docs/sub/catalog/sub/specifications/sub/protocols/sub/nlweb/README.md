# NLWeb

NLWeb is an open protocol for natural-language interaction with websites, applications, and agents. Its published v0.55 specification defines the `ask` interface and an asynchronous `await` helper, structured JSON responses, Schema.org/JSON-LD extensibility, and transport bindings including HTTP and MCP.

## Protocol boundary

This protocol is distinct from the Python reference implementation, the TypeSpec definition, hosted services, and individual site deployments. The upstream reference implementation is explicitly proof-of-concept code, not a production-readiness guarantee. NLWeb complements MCP, A2A, and AG-UI; exact wire fields, transports and response types must be checked against the current published specification.

## Provenance and safe use

Microsoft introduced NLWeb in May 2025; the current protocol documentation and reference code live under the `nlweb-ai` organization. Historical origin does not prove current exclusive ownership or control. The first-party specification identifies v0.55, whereas a separate TypeSpec repository still identifies v0.5; those snapshots should not be conflated.

Authentication, authorization, rate limiting, untrusted site content and sensitive-data exposure remain implementation/transport responsibilities. A documented protocol or sample server is not evidence of production security or interoperability testing.

## Official resources

- [NLWeb specification v0.55](https://nlweb.ai/docs/specification)
- [NLWeb specification source](https://github.com/nlweb-ai/website/blob/main/NLWEBSPEC.md)
- [NLWeb overview](https://nlweb.ai/docs/intro)
- [Python reference implementation](https://github.com/nlweb-ai/NLWeb)
- [Microsoft launch announcement](https://blogs.microsoft.com/blog/2025/05/19/microsoft-build-2025-the-age-of-ai-agents-and-building-the-open-agentic-web/)
