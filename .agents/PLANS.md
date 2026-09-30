# Execution Plans

Create an execution plan for substantial features, migrations, architecture changes,
multi-stage work, or other high-risk tasks.

Do not require plans for trivial isolated edits.

## Required sections

### Objective
What concrete outcome is required?

### Authority and scope
- authorized files/modules;
- explicitly out-of-scope areas;
- production permissions;
- migration/data permissions.

### Current-state evidence
What was actually inspected? Distinguish facts from assumptions.

### Acceptance criteria
List measurable success conditions before implementation.

### Negative criteria
What must not happen?

### Compatibility
Interfaces, versions, consumers, migration behavior, rollback.

### Implementation stages
Small coherent stages in execution order.

### Verification
Compilation, targeted tests, integration, regression, benchmarks, review.

### Resource bounds
Time, memory, disk, rows, candidates, corpus size, output size, network.

### Risks / unresolved questions
Classify anything that is not yet known.

### Completion authority
Who may declare the scoped plan complete?

Plans are living records. Update them when scope changes, but preserve superseded
decisions rather than rewriting history.
