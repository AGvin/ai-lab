# Gateways

Gateways provide a stable control point between AI clients or applications and one or more model backends.

They do not execute models themselves and are not remote model providers. Instead, they receive requests, normalize or proxy traffic, choose a backend, and apply shared access and traffic policies before forwarding the request.

```text
Cursor / agent / Open WebUI / application
                    |
                    v
               AI gateway
                    |
       +------------+------------+
       |            |            |
       v            v            v
 local runtime   private       hosted model API
 Ollama / vLLM   deployment    OpenRouter / OpenAI
                 or cluster
```

A gateway can provide:

- one stable endpoint for several models or providers;
- model aliases and request routing;
- retries, fallback, and load balancing;
- API-key isolation and centralized authentication;
- rate limits, quotas, and budget controls;
- caching and shared telemetry.

Inference runtimes such as Ollama and vLLM execute models. Hosted model APIs provide remote access to models. Gateways coordinate access across those backends without becoming the canonical owner of the underlying runtime or service.

## Child pages

- [`model-gateways/`](./sub/model-gateways/) — gateways designed primarily for model-provider abstraction, routing, and model-specific policy.
- [`api-management-gateways/`](./sub/api-management-gateways/) — broader API ingress and control-plane products that also manage AI traffic.
