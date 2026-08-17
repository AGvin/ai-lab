# Jules

Jules is Google's hosted asynchronous coding-agent service for repository-connected software-development tasks. It can plan and perform work such as bug fixes, feature changes, documentation, tests, and review-oriented tasks while the developer continues other work.

## Service and control boundary

Jules sessions execute in Google-managed environments. The web application, Jules Tools CLI, REST API, GitHub issue workflows, and API-driven automations are control or integration surfaces for those managed sessions rather than separate local Jules runtimes.

Jules can connect to GitHub repositories and can be embedded into external workflows through its API. Treat repository permissions, Google account access, API keys, task scope, generated changes and test results, external integrations, plan approval, and merge/deploy/release decisions as explicit review boundaries.

## Official resources

- [Jules](https://jules.google/)
- [Jules documentation](https://jules.google/docs/)
- [Jules Tools CLI](https://jules.google/docs/cli/reference/)
- [Jules API](https://jules.google/docs/api/reference/)
- [Google](../../../../../../../producers/sub/g/sub/google/)
