# Documentation Requirements

## Requirements

- Catalog ChemBench as one chemistry benchmark/dataset family, not one dataset identity per topic, model or leaderboard entry. Keep the independently installable ChemBench package/evaluation runner distinct from the data content.
- The pinned source README calls ChemBench a modular Python package and benchmark suite for evaluating language and vision-language models in chemistry, loading benchmark data from the publisher's hosted distribution where configured.
- Record benchmark topic and exact data revision, prompt construction, evaluation metric, model revision and any image support. Current evaluation code is not a fixed guarantee that all benchmark components are present or unchanged.
- The upstream root LICENSE is MIT for covered project materials, but independently sourced chemistry problems, images, external datasets, model outputs and the publisher's hosted data may require different terms.
- Chemistry content may concern hazardous substances or laboratory procedures; model outputs are not validated laboratory protocols, and benchmarks should not be used to bypass chemical safety practices.
- No package installation, actual data export, benchmark execution, chemistry answer validation, comprehensive licensed-content audit or whole-catalog clean pass was performed.

## Validation

- One canonical dataset identity, pinned upstream publisher sources and a resolvable index link.
- Keep distinct code/data/right boundaries; no runtime, security, complete citation audit or clean-group gate is inferred.
