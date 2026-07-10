# Sandboxing

<!--
ai_content:
  managed: true
  l10n: true
-->

Sandboxing isolates code, tools, files, or processes so failures and malicious behavior have limited impact on the host system.

## Core idea

A sandbox restricts resources such as filesystem paths, network access, process creation, devices, environment variables, and execution time. It is especially important when a model generates or selects code to execute.

## Practical controls

- Run work in disposable containers or virtual machines.
- Mount only required files.
- Disable or restrict outbound network access.
- Set CPU, memory, disk, and time limits.
- Remove host credentials and sensitive environment variables.
- Destroy the environment after the task.

## Trade-offs and limitations

Strong isolation adds startup cost and may reduce tool capability. Containers alone are not a perfect security boundary for hostile code; higher-risk workloads may need virtual-machine or microVM isolation.

## Common mistakes

- Running generated code directly on the host.
- Mounting the entire home directory into a container.
- Leaving cloud credentials available inside the sandbox.
- Allowing unrestricted network access without monitoring.

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Least Privilege](../least-privilege/)
- [Secret Handling](../secret-handling/)
- [Tool Calling](../../../agents-and-automation/sub/tool-calling/)
