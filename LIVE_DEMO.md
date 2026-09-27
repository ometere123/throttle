# THROTTLE live demo

Stable Studionet 61999 only.

Create and seal:
- VENDOR_PAYMENT: external vendor payment/commitment effect, capacity 100.
- CUSTOMER_DATA_EXPORT: disclosure/export of customer personal data to an external recipient, capacity 50.

Demonstrate:
1. "Send 60 units to supplier Acme" -> VENDOR_PAYMENT -> ALLOWED -> remaining 40.
2. A materially equivalent but differently worded new payment operation requesting 30 units -> same class -> ALLOWED -> remaining 10.
3. Another vendor-payment operation requesting 20 -> EXHAUSTED -> remaining stays 10.
4. Customer-data export requesting 10 -> DATA_EXPORT -> ALLOWED -> its independent remaining becomes 40.
5. A genuinely ambiguous/overlapping operation -> AMBIGUOUS and no class budget changes.

Record finalized txs, decision IDs, `get_decision`, `get_class`, remaining values and explorer links. Do not tune prompts or fabricate expected live consensus.
