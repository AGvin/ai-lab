# WebMCP

WebMCP proposes a web-platform API through which a web application exposes JavaScript functions as structured, discoverable tools to AI agents operating in the browser. It does not establish a standalone MCP server or guarantee that browsers implement the API.
## Publication and safety status
The [15 October 2026 specification](https://webmachinelearning.github.io/webmcp/) is a **Draft Community Group Report**, explicitly **not a W3C Standard or on the W3C Standards Track**. The proposed `ModelContext` API and tool registration surface remain subject to revision.
Tool descriptions and outputs may carry prompt injection; execution can alter page state or leak private context. Use browser permission policy, user authorization, input validation and bounded operations. Treat production browser support as separately verifiable.
## Official resource
- [WebMCP draft and security considerations](https://webmachinelearning.github.io/webmcp/)
