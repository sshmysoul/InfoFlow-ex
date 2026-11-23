#!/usr/bin/env node
/**
 * Fetch top active prediction markets and news-to-odds signals from InfoFlow.
 * Zero external dependencies (Node 18+).
 *
 * Usage:
 *   node examples/node/fetch-markets.mjs
 */

const API_BASE = "https://infoflow.finance/api/exchange/v1/px";
const HEADERS = { "User-Agent": "InfoFlow-API-Example/1.0" };

function fmtPct(priceE6) {
  return `${(Number(priceE6 || 0) / 1e4).toFixed(1)}%`;
}

function fmtUsd(usdE6) {
  const v = Number(usdE6 || 0) / 1e6;
  return v >= 1e6 ? `$${(v / 1e6).toFixed(2)}M` : `$${(v / 1e3).toFixed(1)}K`;
}

async function main() {
  const res = await fetch(`${API_BASE}/events?sort=volume24h&status=active&limit=5`, {
    headers: HEADERS,
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const { events = [] } = await res.json();

  console.log("\n=== InfoFlow Top 5 Prediction Markets (24h Volume) ===\n");
  for (const ev of events) {
    const top = [...(ev.topMarkets || [])].sort(
      (a, b) => Number(b.outcomeAPriceE6 || 0) - Number(a.outcomeAPriceE6 || 0),
    )[0];
    const lead = top?.groupItemTitle || top?.outcomeALabel || "Yes";
    console.log(`• ${ev.title}`);
    console.log(`  Lead: ${lead} (${fmtPct(top?.outcomeAPriceE6)}) | 24h Vol: ${fmtUsd(ev.volume24hUsdE6)}`);
    console.log(`  Market ID: ${top?.marketId || "N/A"} | URL: https://infoflow.finance/en/event/${ev.slug}\n`);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
