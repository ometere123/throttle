# THROTTLE submission notes

THROTTLE is a standalone reusable Intelligent Contract primitive for **semantic rate limiting**.

It solves a gap in ordinary quotas: paraphrases and independently worded operations can share the same material effect. A frozen policy defines semantic budget classes; GenLayer consensus maps each exact operation across the complete class set; deterministic code alone owns quota arithmetic.

Consensus vocabulary: `SAME_CLASS | DIFFERENT_CLASS | AMBIGUOUS`.

Deterministic outcomes: `ALLOWED | EXHAUSTED | AMBIGUOUS`.

The LLM cannot choose requested units, inspect remaining capacity, select a preferred class, or alter numeric budgets.

Network: Studionet 61999. Repository CLI: 0.39.1. Frontend: none.

Direct Mode: 21 passed; preflight, compile and GenVM lint/validation passed.
Deployment: FINALIZED / MAJORITY_AGREE / SUCCESS at `0xCA740cc84E421868360313E230b3f2C23F12Cf58`.
Live lifecycle: Policy 1 sealed with VENDOR_PAYMENT (100) and CUSTOMER_DATA_EXPORT (50). Two paraphrased vendor payments accumulated to 90 spent / 10 remaining; a 20-unit request finalized EXHAUSTED without partial spend; a customer-data export independently consumed 10 from the second class. Evidence is in `REVIEW_EVIDENCE.md`.
