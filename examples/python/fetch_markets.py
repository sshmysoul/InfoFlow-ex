#!/usr/bin/env python3
"""
Fetch top active prediction markets from InfoFlow (standard library only).

Usage:
    python3 examples/python/fetch_markets.py
"""

import json
import urllib.request

API_BASE = "https://infoflow.finance/api/exchange/v1/px"
HEADERS = {"User-Agent": "InfoFlow-API-Example/1.0"}


def fmt_pct(price_e6) -> str:
    return f"{int(price_e6 or 0) / 1e4:.1f}%"


def fmt_usd(usd_e6) -> str:
    val = int(usd_e6 or 0) / 1e6
    return f"${val / 1e6:.2f}M" if val >= 1e6 else f"${val / 1e3:.1f}K"


def main() -> None:
    req = urllib.request.Request(
        f"{API_BASE}/events?sort=volume24h&status=active&limit=5",
        headers=HEADERS,
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    print("\n=== InfoFlow Top 5 Prediction Markets (24h Volume) ===\n")
    for ev in data.get("events", []):
        markets = sorted(
            ev.get("topMarkets") or [],
            key=lambda m: int(m.get("outcomeAPriceE6") or 0),
            reverse=True,
        )
        top = markets[0] if markets else {}
        lead = top.get("groupItemTitle") or top.get("outcomeALabel") or "Yes"
        print(f"• {ev['title']}")
        print(
            f"  Lead: {lead} ({fmt_pct(top.get('outcomeAPriceE6'))}) "
            f"| 24h Vol: {fmt_usd(ev.get('volume24hUsdE6'))}"
        )
        print(
            f"  Market ID: {top.get('marketId', 'N/A')} "
            f"| URL: https://infoflow.finance/en/event/{ev['slug']}\n"
        )


if __name__ == "__main__":
    main()
