# mini-SWE-agent

Minimal software-engineering agent for local or sandboxed shell-driven coding tasks.

## Metadata

```text
Resource type: Software engineering agent
Primary use case: Solve software-engineering tasks by editing repositories, running shell commands, executing tests, and producing patches in local or sandboxed environments
Access model: Open-source command-line tool with local usage and external model provider credentials
License: MIT
Source model: Open source
Operational requirement: mini-SWE-agent package, local or sandboxed execution environment, target repository or task workspace, shell access, selected model provider credentials, and optional benchmark harnesses
Integration modes: CLI, local repositories, shell commands, subprocess execution, local environments, Docker, Podman, Singularity, Apptainer, bubblewrap, contree, LiteLLM, OpenRouter, Portkey, SWE-bench-style evaluation workflows
Source: https://github.com/SWE-agent/mini-swe-agent
Risk notes: Autonomous shell-driven coding agent; review repository write access, command execution, test execution, sandbox boundaries, generated patches, provider credentials, secret exposure, and benchmark-versus-production assumptions before use with private repositories or sensitive data.
```

## Overview

mini-SWE-agent is a minimal software-engineering agent for coding tasks that can be performed through a shell in a local or sandboxed environment.

It is not limited to GitHub issues, but its main scope is narrower than a general-purpose assistant or IDE coding agent. It focuses on software-engineering tasks such as inspecting a repository, editing files, running commands or tests, debugging failures, and producing a patch.

The project intentionally keeps the agent scaffold small. Its default design relies on bash rather than a large set of specialized tools, uses independent subprocess calls for actions, and keeps a linear interaction history that is easier to inspect, debug, or adapt for benchmark and research workflows.

## Fit for AI Lab

mini-SWE-agent belongs under `agents/` because its primary documented role is an agent-like system for autonomous or semi-autonomous software-engineering work.

It is not an agent orchestration framework. Use `agent-orchestration/` for frameworks, runtimes, or control planes that coordinate multiple agents or agent workflows.

Use mini-SWE-agent as a reference point for:

- minimal software-engineering agent design;
- shell-driven repository editing and test execution;
- local or sandboxed coding-agent workflows;
- SWE-bench-style benchmark and research workflows;
- comparison with broader coding agents such as Aider, Cline, Goose, Claude Code, and Codex CLI;
- evaluating how much agent scaffold is needed around a capable model.

## Evaluation notes

Evaluate before adoption:

- whether the task fits shell-driven software engineering rather than IDE-style pair programming;
- local, Docker, Podman, bubblewrap, or other sandbox strategy;
- repository write boundaries and generated patch review;
- shell command and test execution risk;
- model provider support and credential handling;
- exposure of source code, logs, failures, and secrets;
- suitability for production workflows versus benchmark or research use.

## References

- mini-SWE-agent GitHub: https://github.com/SWE-agent/mini-swe-agent
- mini-SWE-agent documentation: https://mini-swe-agent.com/latest/
