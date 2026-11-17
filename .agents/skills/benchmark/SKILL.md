---
name: benchmark
description: Runs reproducible measurements against a pinned baseline and preserves the raw data. Use when measuring performance, memory, throughput, size, or model quality.
---

# Skill: Benchmark

Load when measuring performance, memory, throughput, size, or model quality.

1. Before measuring, freeze where feasible: hypothesis, workload or dataset and split,
   baseline and candidate configuration, metric, seeds, environment, resource limits,
   and how the result will be judged.
2. Separate warmup from measured runs; repeat enough to show variance.
3. Keep the raw measurements and how the summary was derived. Keep earlier runs when
   correcting a design flaw.
4. Label each run confirmatory, exploratory, post-hoc, mechanics pilot, or
   representative evaluation. Tuning on held-out results makes the next run
   exploratory, not confirmatory.
5. Report negative and mixed results.
6. Credit a gain to the algorithm only after ruling out cache state, I/O,
   representation changes, different data or hardware, and raised resource limits.
