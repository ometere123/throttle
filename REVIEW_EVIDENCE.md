# THROTTLE reviewer evidence

Populate only with observed evidence.

- Deployed source commit: b18d6e06a09fab201838116f1fc4cab6e5c9c28e
- Direct Mode: 21 passed
- CLI: 0.39.1
- Network: Studionet
- Chain ID: 61999
- RPC: https://studio.genlayer.com/api
- Contract address: `0xCA740cc84E421868360313E230b3f2C23F12Cf58`
- Deployment tx/finality: `0xd9f16804c713e5df4e2bc390cdc147148c9d311bfdc7eb884c4d7e76c69e8ee4` — FINALIZED / MAJORITY_AGREE / SUCCESS
- Deployed source: 12,198 bytes; SHA-256 `159919ca97cf8eda90ac99df3408967fa821e29322f4379e0b4bbbe294a5e75d`
- runtime_chain_id(): `61999`

## Live budget
- Policy ID: `1`; creation tx: `0xbee66d598a0bc4adce0ad0749e81cd2da09b294a7c88db65926746fde55263c4`
- Vendor-payment class: ID `1`, capacity `100`; tx `0xb8add693d0204aa69743d644baf611729321cd380cd32fccc20047b8903e4c47`
- Data-export class: ID `2`, capacity `50`; tx `0xed19f25a0ca0de1a36938e73caaea40718d2273b921d16bf6ae847858410bb12`
- Seal tx: `0xde5ab360ef1229b5e8e8f29424f4e03baece564ec342a2f67b51f41dc3f1d670`; readback SEALED

## Paraphrase accumulation
- operation 1: "Send 60 units to supplier Acme for invoice 7." / 60 / tx `0xf0b022dda30f1499b064a92c68bf2c57c22d3287635506cd8cee860495514b79` / decision `1` / FINALIZED / SUCCESS / ALLOWED / class `1` / remaining `40`
- operation 2: "Settle Acme invoice 8 by remitting 30 units to the vendor." / 30 / tx `0x92c686b3bec95de3e231d726d6a85bb9fdf57a4dc397d01057792a5accde93a1` / decision `2` / FINALIZED / SUCCESS / ALLOWED / class `1` / remaining `10`

## Exhaustion
- tx `0x788fbae399e37d1ac6885c3e614910a9af156377d8de1fa7dac1131c962f7c84` / decision `3` / FINALIZED / SUCCESS / EXHAUSTED / requested `20` / remaining stayed `10`, spent stayed `90`

## Ambiguity or overlap
- tx `0x5409f5004280d7644274f72cef7bc4acad4b8f6890bc74903dbf534219891965` / decision `4` / FINALIZED / SUCCESS / ALLOWED / class `2` / data-export remaining `40`; vendor-payment remained `10`

## Scope and limitations
- All five writes finalized with majority agreement and successful contract execution.
- No clean live AMBIGUOUS/overlap case was recorded; no claim is made for one.
- The CLI receipt view used here did not expose protocol fee deposit/consumed/refund fields, so no fee amounts are asserted.
- Explorer base: https://explorer-studio.genlayer.com

## Authorization-bound redeployment

- Source commit: `10d63983752c5170acbe73b196757af9b566a96e`
- Contract: `0x88f748ae9f1A3aCcdE889aA21a86e6214DCFc2e2`
- Deployment tx: `0xf2f7d3367e110c87afe61f653d28e0a6e49aca17a79029c43d97ca014abffa20`
- Result: FINALIZED / MAJORITY_AGREE / SUCCESS
- `runtime_chain_id()`: `61999`
- Policy `1` was created by the deployer, sealed with two classes, and automatically authorized its creator.
- Unauthorized wallet: `0x951e6b75530774ff82321a5ae54e14f778f0c855`; rejection tx `0xba44269e41891046929a7d5fbaad8457a25a59f643aa967521bf173da4e2b05c`; FINALIZED with `AUTH: caller is not authorized for policy`; vendor-payment remaining stayed `100`.
- Authorized deployer charge tx: `0x545f9c738bc974470c20489fecb0e38aaece819a8609d97c01c1c44777c53d62`; decision `1`; FINALIZED / SUCCESS / ALLOWED; requested `25`; vendor-payment remaining became `75`.
- The caller allowlist is bounded at 8 entries, creator-controlled only while OPEN, and exposed by `get_policy()`.

Never fabricate addresses, hashes, finality or consensus results.
