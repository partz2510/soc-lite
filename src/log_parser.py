import os, re, json
from rich.console import Console
from rich.table import Table

console = Console()
LOG_FILE = "reports/mock_logs.txt"
ALERT_FILE = "reports/log_alerts.json"

# simple patterns for demo
PATTERNS = {
    "Failed Login": r"Failed login",
    "Suspicious Port": r"Port (22|3389)",
    "External IP": r"192\.168\.|10\."  # negate this later
}

def generate_mock_logs():
    """Create mock log data if none exists."""
    sample_logs = [
        "2025-10-25 12:05:21 - User=Admin - Failed login from 45.76.34.12 Port 22",
        "2025-10-25 12:10:10 - User=Guest - Connected from 192.168.0.5 Port 443",
        "2025-10-25 12:15:30 - User=Admin - Successful login from 8.8.8.8 Port 3389",
        "2025-10-25 12:20:45 - User=Root - File modified /etc/passwd",
    ]
    os.makedirs("reports", exist_ok=True)
    with open(LOG_FILE, "w") as f:
        f.write("\n".join(sample_logs))
    console.print("[green]Mock logs created successfully.[/green]")

def analyze_logs():
    """Scan log lines and flag risky patterns."""
    if not os.path.exists(LOG_FILE):
        generate_mock_logs()

    with open(LOG_FILE) as f:
        logs = f.readlines()

    alerts = []
    table = Table(title="Log Analysis Results")
    table.add_column("Alert Type", style="magenta")
    table.add_column("Log Entry", style="cyan")

    for line in logs:
        found = []
        if re.search(PATTERNS["Failed Login"], line):
            found.append("Failed Login")
        if re.search(PATTERNS["Suspicious Port"], line):
            found.append("Suspicious Port")
        if not re.search(PATTERNS["External IP"], line):
            found.append("External Connection")

        for alert in found:
            alerts.append({"alert": alert, "log": line.strip()})
            table.add_row(alert, line.strip())

    if not alerts:
        table.add_row("OK", "No suspicious entries found")

    console.print(table)

    with open(ALERT_FILE, "w") as f:
        json.dump(alerts, f, indent=2)

    return alerts

if __name__ == "__main__":
    analyze_logs()
