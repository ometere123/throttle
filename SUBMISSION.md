# THROTTLE submission notes

THROTTLE is a standalone reusable Intelligent Contract primitive for **semantic rate limiting**.

It solves a gap in ordinary quotas: paraphrases and independently worded operations can share the same material effect. A frozen policy defines semantic budget classes; GenLayer consensus maps each exact operation across the complete class set; deterministic code alone owns quota arithmetic.

Consensus vocabulary: `SAME_CLASS | DIFFERENT_CLASS | AMBIGUOUS`.

Deterministic outcomes: `ALLOWED | EXHAUSTED | AMBIGUOUS`.

The LLM cannot choose requested units, inspect remaining capacity, select a preferred class, or alter numeric budgets.

Network: Studionet 61999. Repository CLI: 0.39.1. Frontend: none.

Current Direct Mode: 23 passed; preflight, compile and GenVM lint/validation passed. See exact-head CI: https://github.com/ometere123/throttle/actions/runs/36356765603.
Historical deployment: FINALIZED / MAJORITY_AGREE / SUCCESS at `0xCA740cc84E421868360313E230b3f2C23F12Cf58`.
Active deployment: FINALIZED / MAJORITY_AGREE / SUCCESS at `0x88f748ae9f1A3aCcdE889aA21a86e6214DCFc2e2`, source commit `10d63983752c5170acbe73b196757af9b566a96e`.
Live lifecycle: The original semantic-budget lifecycle is recorded in `REVIEW_EVIDENCE.md`. The authorization-bound redeployment is `0x88f748ae9f1A3aCcdE889aA21a86e6214DCFc2e2`: an unrelated funded wallet was rejected with no budget change, while the authorized creator successfully charged 25 units and reduced the vendor-payment budget from 100 to 75.
