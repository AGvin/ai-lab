# Documentation Requirements

## Requirements

- Scope CyberGym as a cybersecurity evaluation dataset and associated local benchmark suite, not a general security testing SaaS or authorization to interact with third-party systems.
- The pinned official README prominently warns: deploy every component locally and do not expose any CyberGym component to the public Internet. Treat this as a mandatory operational boundary for research usage.
- Source describes separate Hugging Face task data, binary-only artifacts, large server/container data and selected subsets; these are independent storage/deployment configurations of one benchmark, not multiple catalog identities.
- Record exact task ID/version, pre- and post-patch source, compilation environment, allowed model tools, evaluation scoring and data snapshot for reproducibility. Artifact downloads, disk consumption and compute costs can be substantial.
- Use authorized, isolated networks; protect credentials, prevent outbound access to non-test targets and quarantine generated executable artifacts. Do not run untrusted challenge code on production hosts.
- Apache-2.0 root code licensing does not automatically include rights to every third-party source snapshot, binary, container image or original vulnerability data.
- No benchmark dataset downloaded, local infrastructure deployed, exploit code executed, model score validated, or whole-catalog clean pass performed.

## Validation

- One frozen dataset identity, pinned publisher sources, distinct benchmark task/harness/model/service artifacts and canonical index link.
- No live vulnerability code, score, legal clearance, complete CI or whole-catalog clean pass is implied.
