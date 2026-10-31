# Stripe Agent Skills

Stripe Agent Skills is Stripe’s first-party collection of reusable instructions for agents building Stripe integrations. Skills supply development guidance; they remain distinct from the payment API, Stripe AI SDKs, token metering, remote MCP service and provider-specific plugin packages.

## Distribution and updates

Official agent plugins can bundle skills with MCP access and update them automatically. Manual skill installation is a separate path and does not automatically update its copied content. Follow current Stripe documentation for the chosen client and inspect the selected skill revision. Individual skills and client packaging are parts or distribution surfaces of this collection, not automatically separate catalog collections.

## Execution boundary

The repository identifies its source license as MIT. Access to Stripe account data or payment operations still requires authentication and applicable account permissions and terms. Instructions do not authorize charges, refunds or production changes on their own. Keep test and live environments distinct, scope credentials to the task and review any generated financial or configuration operation before execution.

## Relations

- Produced by: [Stripe](../../../../../producers/sub/s/sub/stripe/)

## Official resources

- [Stripe AI repository](https://github.com/stripe/ai)
- [Agents and AI on Stripe](https://docs.stripe.com/agents)
