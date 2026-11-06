# CyberGym

**CyberGym** is a research cybersecurity benchmark designed to test AI agents on selected vulnerability analysis tasks using controlled local environments.

## Source, tasks and infrastructure

The [upstream README](https://github.com/sunblaze-ucb/cybergym/blob/c6fe2027d39471375920b92cf1025e23a99ffda5/README.md) distinguishes task data, optional smaller/binary-only distributions and large compilation/runtime resources. Some releases depend on separate hosted datasets and Docker or other prebuilt environments; installed toolchains and snapshot choices therefore determine which tasks are reproducible.

The publisher's warning is explicit: **deploy all CyberGym components locally; never expose them to the public Internet**. Challenge environments are authorized research targets only, not external systems for live testing.

## Rights and safeguards

Prevent network egress to production/public targets, isolate potentially vulnerable code and generated artifacts, restrict credentials and enforce quotas. An agent's local result on a single vulnerability scenario does not prove general offensive-security capability.

The [root LICENSE](https://github.com/sunblaze-ucb/cybergym/blob/c6fe2027d39471375920b92cf1025e23a99ffda5/LICENSE) is Apache-2.0 for covered code; third-party sources, vulnerabilities and images may be independently licensed. No task package downloaded, sandbox launched, exploit generated or model benchmark run was performed.

## Official source snapshot

- [Upstream repository](https://github.com/sunblaze-ucb/cybergym)
- [Pinned README](https://github.com/sunblaze-ucb/cybergym/blob/c6fe2027d39471375920b92cf1025e23a99ffda5/README.md)
- [Pinned root LICENSE](https://github.com/sunblaze-ucb/cybergym/blob/c6fe2027d39471375920b92cf1025e23a99ffda5/LICENSE)
