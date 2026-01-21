from ingestion.ssh_logs import parse_ssh_log
from detections.brute_force_detector import detect_bruteforce
from alerts.alert_manager import generate_alert
from response.block_ip import block_ip

events = parse_ssh_log("sample_logs/auth.log")
alerts = detect_bruteforce(events)

for alert in alerts:
    generate_alert(alert)
    block_ip(alert["source_ip"], simulate=True)
