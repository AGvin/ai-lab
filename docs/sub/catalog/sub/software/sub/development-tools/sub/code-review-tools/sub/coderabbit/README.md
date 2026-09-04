# CodeRabbit

CodeRabbit is an AI code-review and development-workflow product centered on automated pull-request review, with additional IDE, CLI, planning, and Slack-based surfaces. It belongs under Code Review Tools because review and code-quality feedback remain the primary product role even though the broader workflow can generate plans, suggestions, and code improvements.

## Integration and trust boundary

CodeRabbit connects to Git hosting platforms and can operate against repository and organization context. Current official integrations include GitHub, GitLab, Azure DevOps, and Bitbucket, with additional IDE, command-line, Slack, Jira, and Linear workflows.

Treat repository and organization permissions, service accounts or tokens, team knowledge, generated comments and fixes, planning outputs, Slack/IDE/CLI access, issue-tracker connections, and automation triggers as explicit trust and data-flow boundaries. AI review output should remain subject to human review before merge or execution.

## Official resources

- [CodeRabbit](https://www.coderabbit.ai/)
- [CodeRabbit documentation](https://docs.coderabbit.ai/)
- [CodeRabbit Inc.](../../../../../../../producers/sub/c/sub/coderabbit-inc/)
