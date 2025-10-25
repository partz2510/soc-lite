from rich.console import Console
from datetime import datetime
from fim_module import check_integrity
from log_parser import analyze_logs
from intel_lookup import enrich_ioc
from compliance_checker import check_configs
from ir_automator import generate_ir_report

console = Console()

def main():
    console.rule("[bold cyan]SOC-Lite — Mini Security Operations Center[/bold cyan]")
    console.print(f"Started on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    console.print("[yellow]1️⃣ Running File Integrity Module...[/yellow]")
    fim_result = check_integrity()

    console.print("\n[yellow]2️⃣ Running Log Analysis...[/yellow]")
    log_result = analyze_logs()

    console.print("\n[yellow]3️⃣ Running Threat Intelligence Lookup...[/yellow]")
    intel_result = enrich_ioc()

    console.print("\n[yellow]4️⃣ Running Compliance Check...[/yellow]")
    comp_result = check_configs()

    console.print("\n[yellow]5️⃣ Generating Incident Response Summary...[/yellow]")
    ir_report = generate_ir_report()

    console.rule("[bold green]✅ SOC-Lite Run Complete! Summary below:[/bold green]")
    console.print(f"\n• Integrity Findings: {len(fim_result.get('modified', []))}")
    console.print(f"• Log Alerts: {len(log_result)}")
    console.print(f"• Intel Results: {len(intel_result)}")
    console.print(f"• Compliance Issues: {len([i for i in comp_result if i['status']=='Non-Compliant'])}")
    console.print("\n[green]Report saved in /reports folder.[/green]")

if __name__ == "__main__":
    main()

