# Human in the Loop

<!--
ai_content:
  managed: true
  l10n: true
-->

Human in the loop means that selected workflow decisions or actions require human review, input, approval, or correction.

## Core idea

Human involvement should be placed at meaningful control points rather than added as a vague final review. Approval is especially valuable before irreversible, financial, legal, public, security-sensitive, or high-impact actions.

## Common patterns

- Approve a proposed plan before execution.
- Review generated code or document changes before publication.
- Resolve low-confidence classifications.
- Confirm recipients, amounts, or permissions before an external action.
- Escalate repeated failures or policy conflicts.

## Design guidance

Show the reviewer the evidence, proposed action, expected effect, and known uncertainty. Make approve, reject, and modify paths explicit. Preserve the decision in workflow state and prevent the model from bypassing it.

## Trade-offs and limitations

Human review slows throughput and can become a rubber-stamp process when alerts are too frequent or poorly explained. Reviewers may also lack the context needed to detect subtle errors.

## Common mistakes

- Requesting approval after the action has already occurred.
- Showing only a model summary instead of source evidence.
- Treating silence or timeout as approval.
- Using humans to compensate for missing deterministic validation.

## Related concepts

- [Agents and Automation](../../)
- [Autonomy Levels](../autonomy-levels/)
- [Least Privilege](../../../safety-privacy-and-reliability/sub/least-privilege/)
- [Verification and Reflection](../verification-and-reflection/)
