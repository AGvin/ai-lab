# mini-SWE-agent

mini-SWE-agent is the current v2 minimal software-engineering agent from the SWE-agent project. It is designed for inspectable, scriptable coding tasks such as examining a repository, editing files, running shell commands and tests, debugging failures, and producing patches.

## Execution boundary

The project deliberately keeps the agent scaffold small and shell-oriented rather than wrapping the model in a large specialized-tool system. It supports ordinary local execution as well as isolated/containerized environments for research, evaluation, and software-engineering workflows.

That simplicity does not remove execution risk. Treat repository writes, shell and test commands, sandbox boundaries, generated patches, model-provider credentials, source/log data, and secrets as explicit trust boundaries. Benchmark success is not a substitute for production workflow review or isolation.

## Project status

Current upstream guidance recommends mini-SWE-agent over the older SWE-agent for most new use, while keeping the two software identities distinct.

## Official resources

- [mini-SWE-agent documentation](https://mini-swe-agent.com/latest/)
- [mini-SWE-agent repository](https://github.com/SWE-agent/mini-swe-agent)
- [SWE-agent](../../../../../../../producers/sub/s/sub/swe-agent/)
