import json
from datetime import datetime

def generate_alert(alert):
    alert["timestamp"] = datetime.utcnow().isoformat()

    with open("alerts.json", "a") as f:
        f.write(json.dumps(alert) + "\n")

    print(f"[ALERT] {alert['alert_name']} from {alert['source_ip']}")
