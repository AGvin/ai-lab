# ClassEval

**ClassEval** is a research benchmark measuring how well language models generate code at the **Python class level**, where methods interact through class state and shared dependencies.

## Task composition

The [official first-party README](https://github.com/FudanSELab/ClassEval/blob/eaeac44d0d5dcd8a95feec50726d66fedc73a98f/README.md) describes **100 manually constructed class-level tasks**, containing **100 classes** and **410 methods**, with an average of **33.1 test cases per class**. It distinguishes dependencies on instance fields, external libraries, other methods and standalone code. Its upstream release history records an official version **v1.0.0** in January 2024.

Individual class/method questions, test suites and evaluation harnesses are parts of this benchmark, not separate source datasets. Scores depend on the exact model, generated solution sampling, test dependency versions and pass criteria.

## Execution safety and rights

Evaluating responses requires running **untrusted generated Python**. Use process isolation, limited CPU/memory/time, read-only or disposable storage, no privileged network access and no credentials. The original [MIT LICENSE](https://github.com/FudanSELab/ClassEval/blob/eaeac44d0d5dcd8a95feec50726d66fedc73a98f/LICENSE) governs covered repository code, not every third-party module or copied external code.

No generation, runtime test, sandbox execution, rights audit or whole-catalog clean pass was performed.

## Official source snapshot

- [Upstream publisher repository](https://github.com/FudanSELab/ClassEval)
- [Pinned first-party README](https://github.com/FudanSELab/ClassEval/blob/eaeac44d0d5dcd8a95feec50726d66fedc73a98f/README.md)
- [Pinned root LICENSE](https://github.com/FudanSELab/ClassEval/blob/eaeac44d0d5dcd8a95feec50726d66fedc73a98f/LICENSE)
