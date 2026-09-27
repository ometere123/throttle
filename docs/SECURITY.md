# THROTTLE security model

Core invariants:

1. Every frozen class is evaluated; callers cannot select the cheapest/convenient class.
2. Validators independently reproduce the full semantic vector.
3. Capacity values are invisible to the semantic judge.
4. Requested units are explicit input; the LLM cannot invent or reduce the charge.
5. Exactly one class must match.
6. Any ambiguity, zero matches, or overlapping matches fail closed without spending.
7. Budget arithmetic is deterministic and cannot overspend.
8. Policy classes are immutable after sealing.
9. Malformed output/cardinality fails before a decision receipt is written.
10. Untrusted operation/class text is data, not prompt instructions.

Non-goals: THROTTLE does not prove an operation actually happened, infer monetary value from prose, authenticate external identities, or decide whether a budget policy is fair. A downstream executor should consume an ALLOWED receipt immediately before its protected effect and bind its own execution to the intended operation/units where necessary.
