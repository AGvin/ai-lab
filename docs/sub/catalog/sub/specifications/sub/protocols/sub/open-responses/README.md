# Open Responses

Open Responses is an open interoperability specification for multi-provider language-model APIs based on patterns from the OpenAI Responses API. Its common interface covers model inputs, output/context items, tool handoffs and streaming semantic events. It is a *specification*, not a deployed model or guarantee of feature parity across providers.
## Compatibility and trust boundary
The [first-party specification](https://www.openresponses.org/specification) defines supported shapes, control-flow states, HTTP requests and event streaming. Implementations may expose only subsets or vendor extensions; test actual provider coverage and conformance independently. Authentication, data privacy, safe tool execution and handling untrusted responses remain obligations of callers and providers.
## Official resources
- [Open Responses specification](https://www.openresponses.org/specification)
- [Open Responses project](https://www.openresponses.org/)
