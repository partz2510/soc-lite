import os, json, random
from rich.console import Console
from rich.table import Table

console = Console()
ALERT_FILE = "reports/log_alerts.json"
INTEL_FILE = "reports/intel_enrichment.json"

# sample reputation scores to simulate real-world lookups
MOCK_REPUTATIONS = ["clean", "suspicious", "malicious", "unknown"]

def extract_ips():
    """Extract IP addresses from log_alerts.json."""
    if not os.path.exists(ALERT_FILE):
        console.print("[yellow]No alerts found — run log_parser.py first.[/yellow]")
        return []

    with open(ALERT_FILE) as f:
        alerts = json.load(f)

    ips = []
    for a in alerts:
        parts = a["log"].split()
        for p in parts:
            if p.count(".") == 3 and all(x.isdigit() for x in p.split(".") if x.isdigit()):
                ips.append(p)
    return list(set(ips))


def enrich_ioc(logs=None):
    """Simulate enrichment from threat-intel sources."""
    ips = extract_ips()
    if not ips:
        console.print("[yellow]No IPs found for enrichment.[/yellow]")
        return []

    enriched = []
    table = Table(title="Threat Intelligence Enrichment")
    table.add_column("IP", style="cyan")
    table.add_column("Reputation", style="magenta")
    table.add_column("Source", style="green")

    for ip in ips:
        rep = random.choice(MOCK_REPUTATIONS)
        source = random.choice(["VirusTotal", "AbuseIPDB", "OTX"])
        enriched.append({"ip": ip, "reputation": rep, "source": source})
        table.add_row(ip, rep, source)

    os.makedirs("reports", exist_ok=True)
    with open(INTEL_FILE, "w") as f:
        json.dump(enriched, f, indent=2)

    console.print(table)
    return enriched


if __name__ == "__main__":
    enrich_ioc()
