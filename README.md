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

## ⚙️ Installation & Setup
``` bash
# 1️⃣ Clone the repository
git clone https://github.com/<your-username>/soc-lite.git
cd soc-lite

# 2️⃣ Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # (on Windows)

# 3️⃣ Install dependencies
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a .env file in the project root (optional for enrichment):

```bash
VT_API_KEY=your_virustotal_api_key
```

## 🧩 Run Individual Modules

You can run any module standalone:
``` bash
python src/fim_module.py
python src/log_parser.py
python src/intel_lookup.py
python src/compliance_checker.py
python src/ir_automator.py
```

## 🧠 Full SOC Pipeline

Run the orchestrator to execute the complete workflow:

```bash
python src/main.py
```


✅ Expected Output:

![SOC Summary-lite Report part 1](https://github.com/partz2510/soc-lite/blob/main/Screenshot/SOC%20Lite%201.png?raw=true)

![SOC Summary-lite Report part 2](https://github.com/partz2510/soc-lite/blob/main/Screenshot/SOC%20Lite%202.png?raw=true)





## 🚀 Key Skills Demonstrated

1. Security Automation using modular Python scripting

2. Threat Intelligence Integration and IOC enrichment

3. File Integrity Monitoring (FIM) using hashing algorithms

4. Compliance & GRC Awareness through policy validation

5. Incident Response Reporting using rich for visual summaries


## 📚 Tech Stack

Python · Rich · JSON · Requests · dotenv · psutil · YAML

## 🧩 Future Enhancements

1. Integrate Splunk / ELK ingestion via API

2. Add email alerting and Slack notifications

3. Implement live threat-intel feeds using real APIs

4. Export reports to PDF or dashboard view

## 👨‍💻 Author

Parthiban Ganesan






