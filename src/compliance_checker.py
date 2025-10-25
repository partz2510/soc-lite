import json, random
from rich.console import Console
from rich.table import Table

console = Console()
REPORT_FILE = "reports/compliance_report.json"

# pretend system policies
POLICIES = {
    "Password Length ≥ 12": True,
    "2FA Enabled": True,
    "Firewall Active": True,
    "Audit Logging Enabled": True,
    "Guest Account Disabled": True,
    "OS Patching Up-to-date": True
}

def check_configs():
    """Simulate scanning system and returning compliance status."""
    results = []
    table = Table(title="Policy Compliance Scan")
    table.add_column("Policy", style="cyan")
    table.add_column("Status", style="magenta")

    # randomly mark one or two policies as non-compliant
    failed = random.sample(list(POLICIES.keys()), k=random.randint(1, 2))

    for name, expected in POLICIES.items():
        status = "Compliant"
        if name in failed:
            status = "Non-Compliant"
        results.append({"policy": name, "status": status})
        color = "green" if status == "Compliant" else "red"
        table.add_row(name, f"[{color}]{status}[/{color}]")

    console.print(table)

    with open(REPORT_FILE, "w") as f:
        json.dump(results, f, indent=2)

    return results


if __name__ == "__main__":
    check_configs()
