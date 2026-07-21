# Shannon

Autonomous open-source white-box AI pentesting agent for web applications and APIs.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: Autonomous AI pentesting agent
Primary use case: Local, on-demand white-box penetration testing of source-available web applications and APIs
Access model: Open-source self-run CLI with no seat or scan caps; the user provides model credentials and pays model-provider costs
License: AGPL-3.0
Source model: Open source
Operational requirement: Docker, Node.js 18 or later, supported model-provider credentials, the target source repository, and a running authorized test application
Integration modes: CLI, local development environments, Docker worker, Linux, macOS, Windows through WSL2, and manually controlled automation workflows
Free-offering scope: White-box pentesting only
Commercial feature gap: High compared with the Keygraph platform
Black-box testing: Not available in Shannon Open Source
Adoption recommendation: Conditional; useful for its narrow local white-box lane, but not a complete pentesting or AppSec replacement when external attacker-perspective testing is required
Provider: Keygraph
Source: https://github.com/KeygraphHQ/shannon
Risk notes: Actively executes exploits and can mutate the target application; use only with explicit authorization in isolated non-production environments, protect credentials and source code, and review for prompt injection and inaccurate model-generated conclusions.
```

## Overview

Shannon is a standalone AI pentesting agent that analyzes a source repository, plans likely attack paths, interacts with the running application, executes real exploits, and reports findings that it can validate with proof-of-concept evidence.

Its workflow includes source-aware reconnaissance, live application reconnaissance, specialized vulnerability analysis, exploitation, and Markdown report generation. The current documented focus includes injection, cross-site scripting, server-side request forgery, authentication, and authorization issues.

## Fit for AI Lab

Shannon belongs under `agents/` because the canonical object is a standalone autonomous pentesting agent.

It is useful as a reference for:

- agentic penetration testing;
- source-aware dynamic application security testing;
- proof-by-exploitation reporting;
- multi-agent security workflows;
- local security-agent isolation;
- evaluating open-source security agents against commercial AppSec platforms.

## Access and feature gap

Shannon Open Source is free to self-run and does not impose seat or scan caps. The user still supplies model-provider credentials and pays the resulting inference costs.

It is not a free equivalent of the complete [Keygraph platform](../../../development/sub/application-security-tools/sub/keygraph/). Major commercial-only or platform-level capabilities include:

- black-box and grey-box pentesting;
- full parsed-code SAST and Code Property Graph analysis;
- SCA with reachability, secrets, infrastructure, and container scanning;
- business-logic security testing;
- continuous execution and native CI/CD gating;
- centralized findings, ownership, SLA tracking, dashboards, and workflow synchronization;
- automated remediation with targeted verification;
- managed, self-hosted, and air-gapped enterprise controls.

The gap should count against adoption when those capabilities are part of the actual requirement. Do not select Shannon only because it is open source and defer essential coverage until after integration.

## Major limitation: no black-box testing

Shannon Open Source requires source access and performs white-box testing. It does not provide an independent black-box assessment of the deployed application without source-code context.

This is a major limitation for comprehensive pentesting because an external attacker does not normally have repository access. Black-box testing can reveal externally reachable behavior, deployment and routing mistakes, authentication-boundary failures, exposed third-party surfaces, and runtime conditions that a source-informed process may not independently validate.

Use Shannon as a focused white-box tool, not as proof that a complete attacker-perspective security assessment has been performed. Pair it with an authorized black-box tool or service when that coverage matters.

## Relationship to Keygraph

Shannon is the pentesting engine at the center of Keygraph's commercial platform. The open-source repository provides the self-run white-box agent; Keygraph surrounds it with broader analysis, black-box testing, findings management, remediation, verification, integrations, and enterprise operation.

The relationship is important for adoption analysis because the open-source project is both useful on its own and an entry point into a substantially broader paid product.

## Operational notes

- The recommended workflow uses `npx @keygraph/shannon` and starts an ephemeral Docker worker.
- The target repository is mounted read-only in the documented worker workflow, but the running target application can still be changed by exploitation.
- Windows usage is supported through WSL2 rather than native Windows or Git Bash.
- Official model support is centered on Claude-compatible providers and documented cloud-provider routes; alternative proxy or model configurations require separate validation.
- Scan duration and model cost depend on application complexity, coverage, and the selected provider.

## Safe use

Shannon is not a passive scanner.

- Run it only against systems that you own or have explicit written authorization to test.
- Do not target production systems by default.
- Use disposable local or staging data, backups, and a recovery plan.
- Expect account creation, form submission, state changes, outbound requests, and other exploit side effects.
- Use dedicated test credentials and narrowly scoped model-provider keys.
- Keep unrelated secrets, repositories, and network access outside the worker environment.
- Do not scan untrusted or adversarial repositories without additional isolation; source content can attempt indirect prompt injection against the agent.
- Review every finding and proof of concept before treating it as confirmed security evidence.

## Evaluation notes

Evaluate before adoption:

- whether white-box-only coverage satisfies the real security objective;
- which separate tool or paid service will provide required black-box coverage;
- supported vulnerability classes and known coverage gaps;
- model-provider compatibility, inference cost, and reproducibility;
- execution isolation, network access, credential handling, and target-state recovery;
- report quality, exploit evidence, false negatives, and human-review requirements;
- AGPL-3.0 obligations for modified or service-hosted deployments;
- whether the commercial upgrade path creates unacceptable feature gating or total cost.

## References

- Shannon GitHub repository: https://github.com/KeygraphHQ/shannon
- Shannon open-source page: https://keygraph.io/open-source
- Shannon editions: https://keygraph.io/docs/explanations/editions/
- Keygraph platform overview: https://keygraph.io/docs/explanations/keygraph-platform/
- Keygraph pricing: https://keygraph.io/pricing
