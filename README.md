# InfoFlow — Leveraged Prediction Market API & AI Agent Examples

Official open-source API quickstart and autonomous AI Agent trading examples for **[InfoFlow](https://infoflow.finance)** — the global **Leveraged Prediction Market** uniting **1–10× capital efficiency**, **5-minute crypto Up/Down markets**, **real-time news-to-odds intelligence**, and **open REST / WebSocket trading APIs**.

[![Website](https://img.shields.io/badge/Website-infoflow.finance-0EA5E9?style=flat-square)](https://infoflow.finance)
[![API Docs](https://img.shields.io/badge/API_Docs-infoflow.finance/en/docs/api-6366F1?style=flat-square)](https://infoflow.finance/en/docs/api)
[![X](https://img.shields.io/badge/X-@InfoFlow__ex-111827?style=flat-square)](https://x.com/InfoFlow_ex)
[![Telegram](https://img.shields.io/badge/Telegram-t.me/InfoFlow__ex-26A5E4?style=flat-square)](https://t.me/InfoFlow_ex)
[![Discord](https://img.shields.io/badge/Discord-Join_Community-5865F2?style=flat-square)](https://discord.gg/hK6JQWXVMx)

---

## What is InfoFlow?

**[InfoFlow](https://infoflow.finance)** is a next-generation prediction market platform designed for both active traders and autonomous AI agents:

- **Leveraged Prediction Markets (1–10×)** — Trade political, macro, sports, and crypto event outcomes with up to 10× leverage, per-position liquidation pricing, and clear margin rules ([Leveraged Markets](https://infoflow.finance/en/trade/leverage)).
- **High-Frequency 5-Minute Crypto Up/Down** — Short-term BTC, ETH, SOL, and HYPE binary rounds ([5m BTC Up/Down](https://infoflow.finance/en/up-down/btc/5m)).
- **News × Odds Intelligence** — Breaking news directly linked to the prediction markets it moves ([Live News Signals](https://infoflow.finance/en/news)).
- **AI Agent & Market Maker API** — Self-serve `pxk_` API keys with scoped permissions (`read`, `place`, `cancel`), batch order placement/cancellation, and dead-man's-switch heartbeat protection ([API Documentation](https://infoflow.finance/en/docs/api)).
- **LLM-Ready Specification** — Machine-readable reference for coding & trading agents at [`https://infoflow.finance/llms-full.txt`](https://infoflow.finance/llms-full.txt).

---

## API Quick Reference

- **Base URL**: `https://infoflow.finance/api/exchange/v1/px`
- **Authentication**: `Authorization: Bearer pxk_<your_api_key>` (generate keys in [Settings → API Keys](https://infoflow.finance/en/settings/api-keys))
- **Numeric Convention**: Prices and quantities use **E6 fixed-point decimal strings** (`1.00 = "1000000"`, `52% = "520000"`).
- **Full Endpoint Reference**:
  - [API Overview & AI Agent Guide](https://infoflow.finance/en/docs/api)
  - [Market Maker Endpoints (Batch & Heartbeat)](https://infoflow.finance/en/docs/api/market-maker)
  - [Error Codes](https://infoflow.finance/en/docs/api/errors)

| Endpoint | Method | Auth | Description |
|---|---|---|---|
| `/v1/px/events` | `GET` | Public | List active prediction market events sorted by 24h volume or curation |
| `/v1/px/news` | `GET` | Public | Real-time news feed linked to affected prediction markets |
| `/v1/px/orders` | `POST` | `place` | Place a single `LIMIT` or `MARKET` order (`outcome: "A" \| "B"`) |
| `/v1/px/orders/batch` | `POST` | `place` | Submit multiple orders in a single request |
| `/v1/px/orders/batch` | `DELETE` | `cancel` | Batch-cancel open orders |

---

## Quickstart

### 1. Node.js (Zero Dependencies, Node 18+)

Fetch top active InfoFlow prediction markets and live odds:

```bash
node examples/node/fetch-markets.mjs
```

Place a limit order with your API key:

```bash
INFOFLOW_API_KEY="pxk_your_key_here" \
MARKET_ID="your_market_id" \
node examples/node/place-order.mjs
```

### 2. Python 3 (Standard Library Only)

Fetch top active InfoFlow prediction markets and news-linked signals:

```bash
python3 examples/python/fetch_markets.py
```

Place a limit order with your API key:

```bash
INFOFLOW_API_KEY="pxk_your_key_here" \
MARKET_ID="your_market_id" \
python3 examples/python/place_order.py
```

---

## Official Links

- **Platform**: https://infoflow.finance
- **Leveraged Prediction Markets**: https://infoflow.finance/en/trade/leverage
- **AI Agent & API Docs**: https://infoflow.finance/en/docs/api
- **X (Twitter)**: https://x.com/InfoFlow_ex
- **Telegram Community**: https://t.me/InfoFlow_ex
- **Discord Community**: https://discord.gg/hK6JQWXVMx

## License

MIT
