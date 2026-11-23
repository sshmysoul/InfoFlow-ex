#!/usr/bin/env node
/**
 * Place a scoped LIMIT order on InfoFlow Prediction Market via REST API.
 *
 * Required env:
 *   INFOFLOW_API_KEY   Your API key from https://infoflow.finance/en/settings/api-keys (pxk_...)
 *   MARKET_ID          Target marketId (find one via examples/node/fetch-markets.mjs)
 *
 * Optional env:
 *   LIMIT_PRICE_E6     Default: "500000" (50.0%)
 *   QUANTITY_E6        Default: "10000000" (10 shares)
 */

const API_BASE = "https://infoflow.finance/api/exchange/v1/px";
const API_KEY = process.env.INFOFLOW_API_KEY;
const MARKET_ID = process.env.MARKET_ID;

if (!API_KEY || !MARKET_ID) {
  console.error("Usage: INFOFLOW_API_KEY=pxk_... MARKET_ID=... node examples/node/place-order.mjs");
  process.exit(1);
}

const body = {
  marketId: MARKET_ID,
  outcome: "A", // "A" = Yes / primary outcome, "B" = No / opposite outcome
  side: "BUY",
  orderType: "LIMIT",
  tif: "GTC",
  limitPriceE6: process.env.LIMIT_PRICE_E6 || "500000",
  quantityE6: process.env.QUANTITY_E6 || "10000000",
  clientOrderId: `example-${Date.now()}`,
};

const res = await fetch(`${API_BASE}/orders`, {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${API_KEY}`,
    "Content-Type": "application/json",
    "User-Agent": "InfoFlow-API-Example/1.0",
  },
  body: JSON.stringify(body),
});

const json = await res.json();
console.log("HTTP", res.status, JSON.stringify(json, null, 2));
