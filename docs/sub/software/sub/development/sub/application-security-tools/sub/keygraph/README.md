# Keygraph

Commercial agentic application security platform for continuous vulnerability discovery, exploit validation, findings management, remediation, and verification.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: Commercial agentic application security platform
Primary use case: Continuous AppSec across repositories, applications, APIs, and deployment environments
Access model: Commercial managed platform; Pro starts at $50 per active developer per month, Enterprise uses custom pricing, and model inference is billed separately through customer-managed provider credentials
License: Proprietary
Source model: Closed-source platform with the separate AGPL-3.0 Shannon Open Source pentesting agent
Operational requirement: Keygraph account or enterprise deployment, repository and application access, customer-managed model credentials, and configured source-control, CI/CD, identity, or ticketing integrations as needed
Integration modes: Source control, CI/CD, REST and webhook APIs, Jira, SSO, managed service, self-hosted deployment, air-gapped deployment, and customer-controlled LLM gateways
Free offering: Shannon Open Source
Free-offering scope: Self-run, on-demand white-box pentesting only
Commercial feature gap: High
Black-box testing: Paid Keygraph platform only; offered as a Pro add-on and included with Enterprise according to pricing verified on 2026-07-21
Adoption recommendation: Conditional; evaluate the paid platform or combine Shannon with another black-box tool when attacker-perspective testing is required
Provider: Keygraph
Source: https://keygraph.io/
Risk notes: High-trust security platform that can access source code, credentials, repositories, live applications, findings, and remediation workflows; active exploitation requires explicit authorization, isolated test targets, least-privilege access, and human review.
```

## Overview

Keygraph is a commercial AppSec platform that combines agentic static analysis with exploit-validated dynamic testing and vulnerability-lifecycle management.

The platform can correlate Code Property Graph analysis, SAST, SCA with reachability, secrets scanning, infrastructure and container checks, business-logic testing, white-box pentesting, and black-box pentesting. It then centralizes findings, ownership, status, service-level tracking, remediation, and verification.

## Relationship to Shannon

[Shannon](../../../../../agents/sub/shannon/) is the standalone open-source pentesting agent. It performs local, on-demand white-box testing and produces a local report.

Keygraph uses an enhanced Shannon build as its pentesting engine, but the commercial platform adds broader code analysis, continuous execution, black-box and grey-box modes, centralized findings, integrations, remediation, targeted verification, and enterprise deployment controls.

Treat the two resources as related but not equivalent products.

## Access and commercial feature gap

The free offering is not a free edition of the complete Keygraph platform. It is Shannon Open Source, a separate self-run tool that covers one narrower lane: source-aware white-box pentesting.

The official pricing page lists the following differences:

| Capability | Shannon Open Source | Keygraph platform |
| --- | --- | --- |
| White-box pentesting | Available | Available |
| Black-box pentesting | Not available | Paid platform capability |
| Agentic SAST and Code Property Graph analysis | Not available as the platform implementation | Available |
| SCA, secrets, infrastructure, and container coverage | Not available as a unified platform | Available depending on plan or add-on |
| Findings lifecycle and dashboards | Local Markdown report | Centralized findings, ownership, status, SLA, and reporting workflows |
| Remediation and targeted verification | Manual fix and full rerun | Paid remediation and point re-test workflows |
| Enterprise deployment | Self-run local worker | Managed, self-hosted, air-gapped, and controlled-gateway options depending on plan |

This is a substantial adoption concern. Teams may validate the open-source agent successfully and still discover that essential AppSec lifecycle capabilities require a materially more expensive commercial deployment.

## Black-box testing limitation

Black-box testing evaluates the externally reachable application without relying on source-code access. It is important when the goal includes validating the real public attack surface, deployment behavior, third-party components, routing, authentication boundaries, and issues that source-informed planning may not independently reveal.

Because Shannon Open Source is white-box only, it should not be treated as a complete free pentesting replacement when attacker-perspective testing is a requirement. In that case, adoption requires either:

- a paid Keygraph plan that includes black-box testing;
- a separate authorized black-box testing tool or service;
- or a deliberately combined testing process with clear coverage ownership.

## Fit for AI Lab

Keygraph belongs under `application-security-tools/` because its canonical role is a broad application security platform rather than a standalone agent or a general agent-orchestration framework.

It is useful as a reference for:

- agentic AppSec platforms;
- static-dynamic vulnerability correlation;
- proof-by-exploitation security workflows;
- continuous security testing in CI/CD;
- commercial feature-gap and total-cost evaluation;
- comparing integrated platforms with composable open-source security stacks.

## Evaluation notes

Evaluate before adoption:

- whether black-box testing is required and which paid plan or add-on supplies it;
- whether the per-active-developer price and separate model-provider costs are acceptable at team scale;
- whether SCA, remediation, or other required capabilities are included or sold separately;
- whether managed, self-hosted, or air-gapped deployment satisfies source-code and findings-residency requirements;
- repository, application, credential, and integration permission scopes;
- false negatives, false positives, exploit reproducibility, and required human review;
- exit cost if workflows, findings history, policies, and integrations become platform-dependent;
- whether a less restricted open-source combination provides comparable coverage with acceptable operational cost.

Pricing and packaging are time-sensitive. Recheck the official pricing page before making a purchasing decision.

## Safe use

Keygraph and Shannon perform active security testing rather than passive documentation analysis.

- Test only applications and environments that you own or have explicit written authorization to assess.
- Prefer local, sandboxed, or staging environments with disposable data and recoverable state.
- Assume exploitation can create accounts, submit forms, change application state, trigger outbound requests, and produce sensitive evidence.
- Use dedicated test credentials and least-privilege repository, cloud, model-provider, and integration access.
- Do not expose production secrets or unrelated private repositories to the platform.
- Review generated findings and remediation changes before using them for production decisions or merging code.
- Treat untrusted source repositories as a prompt-injection and supply-chain risk.

## References

- Keygraph: https://keygraph.io/
- Pricing: https://keygraph.io/pricing
- Keygraph platform overview: https://keygraph.io/docs/explanations/keygraph-platform/
- Editions comparison: https://keygraph.io/docs/explanations/editions/
- Shannon Open Source: https://github.com/KeygraphHQ/shannon
