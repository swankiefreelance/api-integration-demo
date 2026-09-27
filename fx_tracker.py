"""
Pulls live exchange rates from a public API and appends them to a running
CSV log — the pattern behind most "connect my tools together" automation
requests (an API feeding a spreadsheet/database on a schedule).
Usage: python3 fx_tracker.py [base] [symbols] [log_file]
       python3 fx_tracker.py GBP USD,EUR rates_log.csv
"""
import csv
import os
import sys
from datetime import datetime, timezone
from urllib.request import urlopen, Request
import json

API_URL = "https://api.frankfurter.dev/v1/latest?base={base}&symbols={symbols}"


def fetch_rates(base: str, symbols: str) -> dict:
    url = API_URL.format(base=base, symbols=symbols)
    req = Request(url, headers={"User-Agent": "freelance-ops-portfolio-demo/1.0"})
    with urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())


def append_to_log(data: dict, log_path: str) -> None:
    file_exists = os.path.exists(log_path)
    fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with open(log_path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["fetched_at", "rate_date", "base", "currency", "rate"])
        for currency, rate in data["rates"].items():
            writer.writerow([fetched_at, data["date"], data["base"], currency, rate])


if __name__ == "__main__":
    base = sys.argv[1] if len(sys.argv) > 1 else "GBP"
    symbols = sys.argv[2] if len(sys.argv) > 2 else "USD,EUR"
    log_file = sys.argv[3] if len(sys.argv) > 3 else "rates_log.csv"

    data = fetch_rates(base, symbols)
    append_to_log(data, log_file)
    print(f"Fetched {base} -> {symbols} on {data['date']}, appended to {log_file}")
    for currency, rate in data["rates"].items():
        print(f"  1 {base} = {rate} {currency}")
