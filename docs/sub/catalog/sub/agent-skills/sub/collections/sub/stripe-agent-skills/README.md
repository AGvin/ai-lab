# Stripe Agent Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Stripe Agent Skills is Stripe’s first-party collection of reusable instructions for agents building Stripe integrations. Skills supply development guidance; they remain distinct from the payment API, Stripe AI SDKs, token metering, remote MCP service and provider-specific plugin packages.

## Distribution and updates

Official agent plugins can bundle skills with MCP access and update them automatically. Manual skill installation is a separate path and does not automatically update its copied content. Follow current Stripe documentation for the chosen client and inspect the selected skill revision. Individual skills and client packaging are parts or distribution surfaces of this collection, not automatically separate catalog collections.

## Execution boundary

The repository identifies its source license as MIT. Access to Stripe account data or payment operations still requires authentication and applicable account permissions and terms. Instructions do not authorize charges, refunds or production changes on their own. Keep test and live environments distinct, scope credentials to the task and review any generated financial or configuration operation before execution.

## Relations

- Produced by: [Stripe](../../../../../producers/sub/s/sub/stripe/)

## Source interpretation

Stripe's MIT repository still provides agent skills, while its legacy agent-toolkit, MCP package, AI SDK and token-meter packages are explicitly deprecated without further security updates. Skills remain separate from hosted MCP and payment APIs. Use current integration documentation and authorize test/live financial operations independently.

[Reviewed original README](https://github.com/stripe/ai/blob/7882018f33773950265a9613d12e963853cfb526/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Stripe AI repository](https://github.com/stripe/ai)
- [Agents and AI on Stripe](https://docs.stripe.com/agents)
