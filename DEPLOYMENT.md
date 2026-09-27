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
