from collections import defaultdict
import time

THRESHOLD = 5
TIME_WINDOW = 120  # seconds

def detect_bruteforce(events):
    alerts = []
    attempts = defaultdict(list)

    current_time = time.time()

    for event in events:
        ip = event["source_ip"]
        attempts[ip].append(current_time)

        attempts[ip] = [
            t for t in attempts[ip]
            if current_time - t <= TIME_WINDOW
        ]

        if len(attempts[ip]) >= THRESHOLD:
            alerts.append({
                "alert_name": "SSH Brute Force",
                "source_ip": ip,
                "username": event["username"],
                "severity": "High",
                "mitre_technique": "T1110",
                "status": "Open"
            })

    return alerts
