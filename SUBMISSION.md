# THROTTLE submission notes

THROTTLE is a standalone reusable Intelligent Contract primitive for **semantic rate limiting**.

It solves a gap in ordinary quotas: paraphrases and independently worded operations can share the same material effect. A frozen policy defines semantic budget classes; GenLayer consensus maps each exact operation across the complete class set; deterministic code alone owns quota arithmetic.

Consensus vocabulary: `SAME_CLASS | DIFFERENT_CLASS | AMBIGUOUS`.

Deterministic outcomes: `ALLOWED | EXHAUSTED | AMBIGUOUS`.

The LLM cannot choose requested units, inspect remaining capacity, select a preferred class, or alter numeric budgets.

Network: Studionet 61999. Repository CLI: 0.39.1. Frontend: none.

Direct Mode: PENDING
Deployment: PENDING
Live lifecycle: PENDING
