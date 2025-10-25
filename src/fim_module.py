import os, hashlib, json
from rich.console import Console
from rich.table import Table

console = Console()
BASELINE_FILE = "reports/fim_baseline.json"
SCAN_PATH = "src"   # you can change to any folder you want to monitor


def hash_file(path):
    """Return SHA256 hash of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


def build_baseline():
    """Create a fresh baseline of file hashes."""
    data = {}
    for root, _, files in os.walk(SCAN_PATH):
        for file in files:
            full_path = os.path.join(root, file)
            if file.endswith(".py"):   # only hash Python files here
                data[full_path] = hash_file(full_path)
    os.makedirs("reports", exist_ok=True)
    with open(BASELINE_FILE, "w") as f:
        json.dump(data, f, indent=2)
    console.print("[green]Baseline created successfully.[/green]")


def check_integrity():
    """Compare current file hashes against baseline and detect changes."""
    if not os.path.exists(BASELINE_FILE):
        console.print("[yellow]No baseline found — creating one...[/yellow]")
        build_baseline()
        return {"status": "baseline_created", "modified": [], "missing": [], "new": []}

    with open(BASELINE_FILE) as f:
        baseline = json.load(f)

    current = {}
    for root, _, files in os.walk(SCAN_PATH):
        for file in files:
            full_path = os.path.join(root, file)
            if file.endswith(".py"):
                current[full_path] = hash_file(full_path)

    modified = [f for f in baseline if f in current and baseline[f] != current[f]]
    missing = [f for f in baseline if f not in current]
    new_files = [f for f in current if f not in baseline]

    table = Table(title="File Integrity Check")
    table.add_column("Status")
    table.add_column("File")

    for f in modified:
        table.add_row("Modified", f)
    for f in missing:
        table.add_row("Missing", f)
    for f in new_files:
        table.add_row("New", f)

    if not (modified or missing or new_files):
        table.add_row("OK", "No changes detected")

    console.print(table)

    return {"modified": modified, "missin": missing, "new": new_files}
if __name__ == "__main__":
    result = check_integrity()

