# SentinelLite-SOC 🛡️

SentinelLite-SOC is a lightweight Security Operations Center (SOC) simulation platform designed to demonstrate real-world blue team workflows: log ingestion, attack detection, alerting, and automated incident response.

This project is built for cybersecurity engineers and SOC analysts who want hands-on experience with detection engineering, incident handling, and security automation.

---

## 🎯 Project Objectives

- Simulate a **real SOC pipeline**
- Detect common attacks using log analysis
- Generate structured security alerts
- Apply automated response actions
- Map detections to **MITRE ATT&CK**
- Provide clear documentation for learning and interviews

---

## 🧠 Architecture Overview

Logs → Ingestion → Detection Rules → Alerts → Automated Response → Dashboard


### Components:
- **Ingestion**: Parses Linux authentication and SSH logs
- **Detection Engine**: Rule-based detections (YAML-style)
- **Alert Manager**: Generates structured JSON alerts
- **Response Module**: Blocks malicious IPs (simulation or real)
- **Dashboard**: Visualizes alerts and incidents (Flask)

---

## 🔍 Implemented Detections (v1)

| Detection | Description | MITRE Technique |
|---------|-------------|-----------------|
| SSH Brute Force | Multiple failed SSH logins from same IP | T1110 |
| Suspicious IP Activity | Repeated login attempts across users | T1078 |

---
⚙️ Automated Response

Current response actions:

IP blocking using iptables (simulation mode)

Incident report generation (JSON / Markdown)

Future responses:

User account lock

Email / Slack notifications

SOAR-style playbooks
## 🚨 Alert Format (Example)
---
🛠 Technology Stack

Python 3

Regex-based log parsing

YAML detection rules

Flask (dashboard)

Docker (planned)

MITRE ATT&CK Framework
---
---
📂 Project Structure
SentinelLite-SOC/
├── ingestion/        # Log parsing modules
├── detections/       # Detection rules
├── alerts/           # Alert management
├── response/         # Automated actions
├── dashboard/        # Web interface
├── sample_logs/      # Test logs
├── docs/             # Architecture & MITRE mapping
└── README.md
---
🧪 How to Run (Basic)
pip install -r requirements.txt
python ingestion/ssh_logs.py
python alerts/alert_manager.py

---
---
```json
{
  "timestamp": "2026-01-21T14:33:21Z",
  "alert_name": "SSH Brute Force",
  "source_ip": "192.168.1.50",
  "username": "root",
  "severity": "High",
  "mitre_technique": "T1110",
  "status": "Open"
}
---

