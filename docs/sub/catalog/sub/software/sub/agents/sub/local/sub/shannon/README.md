# Shannon

Shannon is Keygraph's open-source autonomous white-box AI pentester for source-available web applications and APIs. It analyzes source code, plans attack paths, interacts with a running target, actively executes exploits, and reports findings supported by reproducible proof-of-concept evidence.

## Execution and safety boundary

Shannon is offensive-security tooling, not a passive scanner. Use it only against systems you own or have explicit written authorization to test, and prefer isolated non-production environments with disposable data, scoped credentials, backups, and a recovery plan.

The recommended self-run workflow uses an ephemeral Docker worker and mounts the target repository read-only, but live exploit attempts can still mutate application state or trigger external effects. Treat model-provider credentials, network access, target credentials, source content, prompt-injection risk, provider safeguard interruptions, target-state recovery, and human validation of findings as explicit trust boundaries.

Shannon's open-source identity is distinct from the broader commercial Keygraph platform. Source-aware white-box testing is useful coverage, but it should not be treated as proof that an independent external-attacker or comprehensive AppSec assessment has been completed unless the required coverage is separately verified.

## Related

- [Keygraph](../../../../../../../producers/sub/k/sub/keygraph/) — producer organization and operator of the separate commercial platform.

## Official resources

- [Shannon repository](https://github.com/KeygraphHQ/shannon)
- [Keygraph open source](https://keygraph.io/open-source)
