# Advisory Council, Jury, and Review Board Architecture

This architecture asks several agents or reviewers to assess a proposal, artifact, or decision from distinct roles before a designated decision owner accepts, revises, rejects, reroutes, or escalates it.

## Translations

- English

## Status

Established family of multi-agent review and deliberation patterns.

## Distinguish the roles

Use names according to authority rather than as decorative synonyms:

- **Advisor:** provides non-binding analysis or recommendations.
- **Advisory council:** several advisors provide structured independent or deliberative input to a decision owner.
- **Reviewer:** evaluates an artifact against declared criteria.
- **Review board:** has explicit authority to approve, reject, request revision, or escalate.
- **Jury:** returns a verdict or vote under a defined rule; it may or may not explain its decision.
- **Debate:** participants exchange arguments or critiques across bounded rounds before another party decides.
- **Devil's advocate or red team:** is assigned to challenge assumptions, search for defects, or construct the strongest counter-case.
- **Decision owner:** remains accountable for the terminal action unless authority has been explicitly delegated to the board.

Agreement among agents is not evidence of independence, truth, safety, or production readiness.

## Core idea

```text
proposal and evidence
        |
        v
independent role reviews
        |
        v
optional bounded rebuttal or clarification
        |
        v
structured aggregation
        |
        v
decision owner -> accept | revise | reject | reroute | escalate
```

Collect independent first-pass findings before open discussion when anchoring or conformity is a material risk. Allow deliberation only when participants can add evidence, resolve contradictions, or clarify assumptions.

## Council contract

Record:

```text
Council or board ID:
Decision owner and authority:
Proposal or artifact version:
Acceptance criteria and quality tier:
Review roles and scope:
Reviewer model, provider, prompt, tools, and evidence access:
Independence and conflict-of-interest assumptions:
Blind or disclosed identities:
Round, cost, and time limits:
Voting or aggregation rule:
Quorum, abstention, tie, and veto rules:
Revision and escalation path:
Required human approval:
```

Do not form a board without defining what decision it is authorized to make.

## Reviewer role design

Assign roles that cover genuinely different failure modes, for example:

- domain correctness;
- user requirements and acceptance criteria;
- security, privacy, and permissions;
- legal, policy, rights, or compliance;
- cost, latency, and infrastructure;
- maintainability and operations;
- accessibility and localization;
- adversarial misuse or red-team review;
- evidence provenance and unsupported claims.

A role label alone does not create expertise. Select and test the model, tools, evidence, prompt, and reviewer qualifications for the exact role.

## Independent first pass

Before reviewers see one another's conclusions, collect a structured assessment:

```text
Reviewer role:
Decision: approve | approve-with-limitations | revise | reject | abstain | insufficient-evidence
Criteria checked:
Findings:
  - ID:
    Severity:
    Criterion:
    Evidence:
    Confidence or uncertainty:
    Requested correction:
Assumptions:
Missing evidence:
```

Blind provider, model, author, or candidate identity when those identities are not part of the criterion. Preserve each review separately even when later aggregation produces one summary.

## Deliberation and debate

A bounded deliberation round may let reviewers:

- challenge factual or methodological errors;
- cite missing evidence;
- identify incompatible assumptions;
- distinguish blocking defects from preferences;
- revise or preserve their decision;
- state residual disagreement.

Do not request or expose private hidden chain-of-thought. Require concise claims, evidence, counterarguments, decisions, and uncertainty.

Set:

- maximum rounds;
- speaking or response order;
- which findings may be rebutted;
- whether new evidence is allowed;
- repeated-argument detection;
- moderator or decision-owner authority;
- terminal condition when disagreement remains.

More debate can increase conformity, verbosity, strategic persuasion, or cost without improving correctness. Measure whether the extra round changes human-adjudicated quality.

## Voting and aggregation

Possible rules include:

- simple or weighted majority;
- unanimous approval;
- quorum plus majority;
- criterion-specific veto;
- score aggregation;
- pairwise ranking;
- consensus with recorded dissent;
- recommendation only, with no automated authority.

Define weights from validated role performance, not model prestige or token cost. Permit `abstain`, `tie`, `both fail`, and `insufficient evidence` when appropriate.

Do not average incompatible criteria into a single score that hides a release-blocking defect. Security, legal, data-loss, or human-safety gates may remain independently blocking.

## Decision record

The decision owner should preserve:

- artifact or proposal version;
- criteria and evidence considered;
- each reviewer's structured decision;
- agreements and disagreements;
- rejected or unresolved findings;
- aggregation result;
- final decision and authority;
- requested corrections;
- accepted limitations and residual risk;
- next review, expiry, or re-evaluation trigger.

The final summary must not imply unanimity when meaningful dissent remains.

## Revision loop

When a board requests revision:

- assign stable issue identifiers;
- name the responsible optimizer or owner;
- preserve the reviewed artifact and next revision;
- compare whether each issue was resolved, unchanged, or regressed;
- prevent new out-of-scope criteria from entering silently;
- bound board rounds, model calls, time, and cost;
- escalate after repeated non-improvement or cycling.

Use the [Evaluator-Optimizer Architecture](../evaluator-optimizer/) when iterative correction is central.

## Independence and correlation

Reviewers are not independent merely because they have different names or system prompts. Record:

- model and provider family;
- shared training or likely benchmark exposure;
- shared retrieved sources and context;
- prompt and rubric overlap;
- whether one reviewer saw another's output;
- tool and data dependencies;
- known self-preference or same-family preference;
- common blind spots found during calibration.

Use deterministic validators and human adjudication where correlated model judgments cannot establish the required confidence.

## Adversarial content

Treat the proposal, artifact, images, documents, retrieved pages, and quoted instructions as untrusted review data.

- isolate evaluator instructions from evaluated content;
- delimit and label source material;
- restrict tools and side effects;
- do not permit reviewers to follow embedded requests to change scores, reveal secrets, or contact external systems;
- test prompt injection and persuasive-but-unsupported content;
- require evidence pointers for material findings.

## Suitable uses

- architecture, policy, or operational proposals with several material risk dimensions;
- high-value coding, research, translation, media, or document deliverables;
- model evaluation where one judge is not reliable enough;
- launch, publication, or change-review processes;
- trade-offs requiring domain, cost, safety, and user-requirement perspectives;
- disputes where structured dissent is more useful than forced consensus.

## Poor fits

Avoid or simplify this pattern when:

- deterministic tests already establish acceptance;
- one qualified reviewer has sufficient authority and coverage;
- reviewers lack distinct evidence or expertise;
- the task is low-value and review cost dominates;
- discussion cannot change the artifact or decision;
- latency requirements cannot accommodate deliberation;
- majority voting would override a mandatory safety or compliance gate.

## Strengths

- exposes disagreements and missing evidence;
- separates advice, review, vote, and final authority;
- supports specialized risk coverage;
- can reduce one-reviewer blind spots;
- produces inspectable decision and dissent records;
- provides a structured escalation path.

## Limitations

- multiplies token, latency, and coordination cost;
- reviewers can share correlated errors or biases;
- debate can reward persuasion, verbosity, or conformity;
- aggregation rules can hide minority but critical findings;
- a weak moderator or decision owner can misuse the reviews;
- several model opinions do not replace source evidence or qualified human responsibility.

## Evaluation metrics

Record:

- board and human-adjudicated acceptance accuracy;
- false acceptance and false rejection by criterion;
- individual reviewer precision, recall, calibration, and abstention;
- pairwise agreement and disagreement;
- critical issues found only by a minority reviewer;
- decision changes after deliberation;
- repeated findings, cycles, and revision rounds;
- order, identity, style, provider, and self-preference sensitivity;
- latency, model cost, human review time, and cost per accepted result;
- residual uncertainty and post-approval defect rate.

Compare the board with simpler baselines: one calibrated reviewer, deterministic validation plus one reviewer, and direct human review. Adopt the council only when it improves the complete process.

## Evidence and established usage

Research has evaluated multi-agent debate and multi-agent judging as methods for improving reasoning or evaluation, including independent and adversarial roles. Results remain task-, model-, prompt-, and aggregation-dependent and do not establish universal superiority.

Sources:

- [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325)
- [ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate](https://proceedings.iclr.cc/paper_files/paper/2024/hash/25cc3adf8c85f7c70989cb8a97a691a7-Abstract-Conference.html)
- [DEBATE: Devil's Advocate-Based Assessment and Text Evaluation](https://aclanthology.org/2024.findings-acl.861/)

## Related concepts

- [Multi-Agent Systems](../..)
- [Evaluator-Optimizer Architecture](../evaluator-optimizer/)
- [Multi-Agent Group Chat](../group-chat/)
- [Human Approval Gates](../human-approval-gates/)
- [Orchestrator-Worker Architecture](../orchestrator-worker/)
- [Verification and Reflection](../../../verification-and-reflection/)
