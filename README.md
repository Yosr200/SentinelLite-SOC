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
## 🔹 Features

- Log ingestion for Linux/SSH authentication logs
- Brute-force detection using rule-based logic
- Alerts mapped to **MITRE ATT&CK T1110 (Credential Access)**
- Automated response simulation (IP blocking)
- Flask-based SOC dashboard for monitoring alerts
- Fully containerized with Docker and Docker Compose
- Clear documentation and Mermaid diagrams for architecture

---

## 🔹 Technologies Used

- **Python 3.11** – core logic, detection, alerting  
- **Flask** – SOC dashboard  
- **Docker / Docker Compose** – containerization  
- **Mermaid** – architecture and flow diagrams  
- **JSON** – alert storage

---

## 🔹 Project Structure

```text
SentinelLite-SOC/
├── ingestion/                # Log parsing scripts
│   └── ssh_logs.py
├── detections/               # Detection logic
│   └── brute_force_detector.py
├── alerts/                   # Alert management
│   └── alert_manager.py
├── response/                 # Automated response simulation
│   └── block_ip.py
├── dashboard/                # Flask dashboard
│   ├── app.py
│   └── templates/
│       └── index.html
├── sample_logs/              # Example log files
│   └── auth.log
├── docs/                     # Diagrams & documentation
│   └── architecture.md
├── run_soc.py                # Orchestrator for SOC workflow
├── requirements.txt          # Python dependencies
└── README.md                 # This file
---
## 🔍 Implemented Detections (v1)

| Detection | Description | MITRE Technique |
|---------|-------------|-----------------|
| SSH Brute Force | Multiple failed SSH logins from same IP | T1110 |
| Suspicious IP Activity | Repeated login attempts across users | T1078 |

---

## 🚨 Alert Format (Example)

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

