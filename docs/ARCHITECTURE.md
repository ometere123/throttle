# THROTTLE architecture

A policy creator defines bounded semantic budget classes while a policy is OPEN. Each class freezes a name, semantic definition and numeric capacity. The policy is then SEALED and immutable.

For every operation, THROTTLE evaluates the operation against **every class**. The caller cannot nominate a preferred class. Validators independently re-derive the complete verdict vector with `run_nondet_unsafe`.

The semantic layer sees class definitions and the operation, but **not capacity, spent or remaining values**. This prevents budget availability from biasing classification.

A valid charge requires exactly one `SAME_CLASS`, zero `AMBIGUOUS`, and explicit positive `requested_units`. Arithmetic is deterministic.

States:
- `ALLOWED`: one class matched and enough capacity existed; spent increments atomically.
- `EXHAUSTED`: one class matched but requested units exceed remaining capacity; no spend.
- `AMBIGUOUS`: zero/multiple matches or any semantic ambiguity; no spend.

THROTTLE is distinct from semantic idempotency: multiple genuinely distinct operations can all consume the same semantic budget.
