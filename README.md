# THROTTLE

**Semantic rate limiting for autonomous operations.**

THROTTLE is a standalone reusable GenLayer Intelligent Contract primitive with **no frontend**.

Ordinary rate limits count API calls or wallet addresses. Autonomous agents can express the same economic or data-moving effect in endlessly different language. THROTTLE maps natural-language operations into a frozen semantic budget class under GenLayer consensus, then deterministic code performs the actual quota arithmetic.

Example:

```text
"Pay supplier Acme 30 units"
"Settle Acme invoice with 30 units"
"Remit 30 units to the vendor"
          |
          v
VENDOR_PAYMENT
capacity = 100
spent += requested_units
```

## Boundary

Consensus decides only whether the operation belongs to each frozen class:

- `SAME_CLASS`
- `DIFFERENT_CLASS`
- `AMBIGUOUS`

Deterministic code owns capacity, spent units, remaining units and the final `ALLOWED | EXHAUSTED | AMBIGUOUS` state.

Exactly one class must match. Zero matches, multiple matches, or any ambiguity fail closed without spending budget.

The model never sees remaining capacity and cannot decide how many units to charge: `requested_units` is explicit deterministic input.

## Network

- **Studionet**
- chain **61999**
- RPC `https://studio.genlayer.com/api`
- repository-local GenLayer CLI **0.39.1**
- Direct Mode GenVM **v0.2.12**
- no Studio-dev / 61997
- no frontend

See `docs/ARCHITECTURE.md`, `docs/SECURITY.md`, `LIVE_DEMO.md`, `DEPLOYMENT.md`, and `AGENT_HANDOFF.md`.
