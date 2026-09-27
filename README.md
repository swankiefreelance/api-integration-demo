# Live API → Running Data Log

**The problem:** Data that lives in a third-party API (rates, stock levels, weather, metrics — anything with a public or authenticated endpoint) needs to land in a spreadsheet or database on a schedule, without anyone manually checking the site and copying numbers across.

**The fix:** A Python script that calls a live API, parses the response, and appends a clean, timestamped row to a running CSV log — creating the log with headers on first run, appending on every run after. Point a scheduler (cron, Task Scheduler, or a workflow tool) at this script daily/hourly and the log builds itself.

**Result:** tested live against a real public exchange-rate API — see `rates_log.csv` for actual fetched data. The same pattern (fetch → parse → append) is what sits behind most "connect my tools together" automation requests, regardless of which API is involved.

**Files in this folder:**
- `fx_tracker.py` — the integration script
- `rates_log.csv` — real output from a live test run

---
**Upwork portfolio listing — paste-ready:**

Title: `Live API Integration → Automated Data Log`

Description: *"Built a script that pulls live data from a third-party API and appends it to a running, timestamped log automatically — the exact pattern behind most workflow/API integration requests (rates, inventory, metrics, anything with an endpoint). Point a scheduler at it and the log builds itself with zero manual checking."*

Skills to tag: Python, API Integration, Automation, REST API, Workflow Automation
