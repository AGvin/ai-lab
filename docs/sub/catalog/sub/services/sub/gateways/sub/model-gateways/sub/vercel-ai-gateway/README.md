# Vercel AI Gateway

Vercel AI Gateway is Vercel's producer-operated unified model gateway and API layer.

## Service boundary

The hosted gateway provides model and provider access, routing and failover, API or protocol compatibility, usage visibility, billing or bring-your-own-key behavior, and integration with Vercel's AI tooling where currently supported. The installable Vercel AI SDK remains a separate canonical software product even when it integrates with AI Gateway.

Model counts, provider coverage, pricing, routing policy, protocol compatibility, limits, and other mutable service behavior are freshness-sensitive. Routed third-party models retain their own canonical identities rather than becoming Vercel AI Gateway entities.

## Official resources

- [Vercel AI Gateway](https://vercel.com/ai-gateway)
- [Vercel AI Gateway documentation](https://vercel.com/docs/ai-gateway)
