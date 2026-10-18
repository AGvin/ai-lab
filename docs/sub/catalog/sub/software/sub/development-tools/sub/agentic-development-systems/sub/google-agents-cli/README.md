# Google Agents CLI

Google Agents CLI (`agents-cli`) is Google's released CLI and bundled-skill system for building, evaluating, deploying and operating agents on Gemini platform and Google Cloud.

## Product scope

Use it directly from a terminal or through a supported coding assistant. It supplies scaffolding, evaluation, deployment, infrastructure and agent-development skills; Google ADK, the coding assistant and the cloud services remain separate components. Local development can use an AI Studio API key, while deployment and cloud features require Google Cloud.

## Operational boundaries

Scaffolding and extensions can write project files or replace managed skills. Review those changes, model credentials, deployment identity and IAM permissions; deployed resources remain in the user's Google Cloud project.

The v1.10.0 release line enables usage telemetry by default. Command metadata is logged in the user's Cloud project, and request metadata also reaches Google; file contents and arguments are excluded. Disable telemetry with `AGENTS_CLI_TELEMETRY=0` or `DO_NOT_TRACK=1`. Check the selected release before relying on defaults.

## Relations

- Produced by: [Google](../../../../../../../producers/sub/g/sub/google/)

## Official resources

- [Repository](https://github.com/google/agents-cli)
- [Released documentation](https://github.com/google/agents-cli/blob/v1.10.0/README.md)
- [Release notes](https://github.com/google/agents-cli/blob/v1.10.0/RELEASE_NOTES.md)
