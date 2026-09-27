# THROTTLE deployment

Use stable Studionet only: chain 61999, RPC `https://studio.genlayer.com/api`.

```bash
npm install
npx genlayer --version
npm run toolchain:check
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-test.txt
python scripts/repo-preflight.py
pytest tests/direct -v -s
npx genlayer network set studionet
npx genlayer network info
npm run deploy:studionet
```

Require CLI 0.39.1. Never use global 0.40.0rc2, Studio-dev or 61997.

After deployment call `runtime_chain_id()` and require 61999, then execute `LIVE_DEMO.md` and populate `REVIEW_EVIDENCE.md` only from actual finalized evidence.

## Observed deployment

- Source commit: `b18d6e06a09fab201838116f1fc4cab6e5c9c28e`
- Contract: `0xCA740cc84E421868360313E230b3f2C23F12Cf58`
- Deployment transaction: `0xd9f16804c713e5df4e2bc390cdc147148c9d311bfdc7eb884c4d7e76c69e8ee4`
- Result: FINALIZED / MAJORITY_AGREE / SUCCESS
- `runtime_chain_id()`: `61999`
- Source SHA-256: `159919ca97cf8eda90ac99df3408967fa821e29322f4379e0b4bbbe294a5e75d` (12,198 bytes)
- Explorer: https://explorer-studio.genlayer.com/address/0xCA740cc84E421868360313E230b3f2C23F12Cf58

The complete observed lifecycle and transaction hashes are recorded in `REVIEW_EVIDENCE.md`.
