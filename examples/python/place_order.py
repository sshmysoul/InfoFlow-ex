#!/usr/bin/env python3
"""
Place a LIMIT order on InfoFlow Prediction Market via REST API (standard library only).

Required env:
    INFOFLOW_API_KEY   Your API key from https://infoflow.finance/en/settings/api-keys (pxk_...)
    MARKET_ID          Target marketId (discover via examples/python/fetch_markets.py)
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request

API_BASE = "https://infoflow.finance/api/exchange/v1/px"
API_KEY = os.environ.get("INFOFLOW_API_KEY")
MARKET_ID = os.environ.get("MARKET_ID")

if not API_KEY or not MARKET_ID:
    print(
        "Usage: INFOFLOW_API_KEY=pxk_... MARKET_ID=... python3 examples/python/place_order.py",
        file=sys.stderr,
    )
    sys.exit(1)

payload = {
    "marketId": MARKET_ID,
    "outcome": "A",
    "side": "BUY",
    "orderType": "LIMIT",
    "tif": "GTC",
    "limitPriceE6": os.environ.get("LIMIT_PRICE_E6", "500000"),
    "quantityE6": os.environ.get("QUANTITY_E6", "10000000"),
    "clientOrderId": f"py-example-{int(time.time() * 1000)}",
}

req = urllib.request.Request(
    f"{API_BASE}/orders",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "InfoFlow-API-Example/1.0",
    },
    method="POST",
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        print("HTTP", resp.status, resp.read().decode("utf-8"))
except urllib.error.HTTPError as err:
    print("HTTP", err.code, err.read().decode("utf-8"))
