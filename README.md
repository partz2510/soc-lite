## 📘 SOC-Lite — Mini Security Operations Center Simulator

SOC-Lite is a Python-based, end-to-end Security Operations Center (SOC) simulator.
It automates detection, enrichment, compliance, and incident-response workflows —
showcasing how real-world SOC pipelines operate in a unified automation environment.

## 🧭 Overview

SOC-Lite ties together multiple cybersecurity functions in a single modular system:

Stage	Module	Description
🧩 1. File Integrity	fim_module.py	Detects file tampering or unauthorized modifications using SHA-256 hashes.
🧠 2. Log Analysis	log_parser.py	Parses simulated system logs to flag failed logins, odd ports, and external IPs.
🌐 3. Threat Intelligence	intel_lookup.py	Enriches detected IPs with mock data from sources like VirusTotal, OTX, and AbuseIPDB.
⚖️ 4. Compliance Scanner	compliance_checker.py	Audits key system policies (passwords, firewall, logging) and flags weak settings.
🚨 5. Incident Response	ir_automator.py	Aggregates all findings into a single JSON summary and rich-table report.
🧠 Architecture Diagram

         ┌────────────────────────────┐
         │       FIM Module           │
         │  File Integrity Checker    │
         └────────────┬───────────────┘
                      │
                      ▼
         ┌────────────────────────────┐
         │       Log Parser           │
         │  Detects Suspicious Events │
         └────────────┬───────────────┘
                      │
                      ▼
         ┌────────────────────────────┐
         │  Threat Intel Lookup       │
         │  IP Reputation & Context   │
         └────────────┬───────────────┘
                      │
                      ▼
         ┌────────────────────────────┐
         │  Compliance Checker        │
         │  GRC / Policy Validation   │
         └────────────┬───────────────┘
                      │
                      ▼
         ┌────────────────────────────┐
         │  IR Automator              │
         │  Generates SOC Summary     │
         └────────────────────────────┘

⚙️ Installation & Setup
# 1️⃣ Clone the repository
git clone https://github.com/<your-username>/soc-lite.git
cd soc-lite

# 2️⃣ Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # (on Windows)

# 3️⃣ Install dependencies
pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the project root (optional for enrichment):

VT_API_KEY=your_virustotal_api_key

🧩 Run Individual Modules

You can run any module standalone:

python src/fim_module.py
python src/log_parser.py
python src/intel_lookup.py
python src/compliance_checker.py
python src/ir_automator.py

🧠 Full SOC Pipeline

Run the orchestrator to execute the complete workflow:

python src/main.py


✅ Expected Output:

──────────────────────────── SOC-Lite — Mini Security Operations Center ────────────────────────────
1️⃣ Running File Integrity Module...
2️⃣ Running Log Analysis...
3️⃣ Running Threat Intelligence Lookup...
4️⃣ Running Compliance Check...
5️⃣ Generating Incident Response Summary...

✅ SOC-Lite Run Complete! Summary below:
• Integrity Findings: 0
• Log Alerts: 6
• Intel Results: 2
• Compliance Issues: 1
Report saved in /reports folder.

📁 Project Structure
soc-lite/
├── src/
│   ├── main.py
│   ├── fim_module.py
│   ├── log_parser.py
│   ├── intel_lookup.py
│   ├── compliance_checker.py
│   └── ir_automator.py
├── reports/
│   ├── fim_baseline.json
│   ├── log_alerts.json
│   ├── intel_enrichment.json
│   ├── compliance_report.json
│   └── ir_summary.json
├── .env
├── requirements.txt
└── README.md

🧠 Example Output Screenshot

(Insert screenshot here — run python src/main.py and screenshot the full console.)

🚀 Key Skills Demonstrated

Security Automation using modular Python scripting

Threat Intelligence Integration and IOC enrichment

File Integrity Monitoring (FIM) using hashing algorithms

Compliance & GRC Awareness through policy validation

Incident Response Reporting using rich for visual summaries

📚 Tech Stack

Python · Rich · JSON · Requests · dotenv · psutil · YAML

🧩 Future Enhancements

Integrate Splunk / ELK ingestion via API

Add email alerting and Slack notifications

Implement live threat-intel feeds using real APIs

Export reports to PDF or dashboard view

👨‍💻 Author

Parthiban Ganesan
Cybersecurity & Network Operations Specialist
GitHub
 | LinkedIn
