import json, os
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()
REPORT_FILE = "reports/ir_summary.json"

def generate_ir_report(iocs=None):
    """Combine findings from all modules into a single IR summary."""
    paths = {
        "fim": "reports/fim_baseline.json",
        "alerts": "reports/log_alerts.json",
        "intel": "reports/intel_enrichment.json",
        "compliance": "reports/compliance_report.json"
    }

    summary = {"timestamp": datetime.now().isoformat(), "findings": {}}

    # Load whatever data exists
    for key, path in paths.items():
        if os.path.exists(path):
            with open(path) as f:
                summary["findings"][key] = json.load(f)
        else:
            summary["findings"][key] = f"{path} not found"

    # Display table summary
    table = Table(title="Incident Response Summary")
    table.add_column("Category", style="cyan")
    table.add_column("Details", style="magenta")

    modified = len(summary["findings"].get("fim", []))
    alerts = len(summary["findings"].get("alerts", []))
    intel = len(summary["findings"].get("intel", []))
    non_compliant = [
        p for p in summary["findings"].get("compliance", [])
        if isinstance(p, dict) and p.get("status") == "Non-Compliant"
    ]

    table.add_row("File Integrity", f"{modified} items scanned")
    table.add_row("Log Alerts", f"{alerts} detections")
    table.add_row("Intel Enrichment", f"{intel} IPs analyzed")
    table.add_row("Compliance", f"{len(non_compliant)} issues")

    console.print(table)

    os.makedirs("reports", exist_ok=True)
    with open(REPORT_FILE, "w") as f:
        json.dump(summary, f, indent=2)

    console.print(f"[green]Incident Response report saved to {REPORT_FILE}[/green]")
    return summary


if __name__ == "__main__":
    generate_ir_report()
