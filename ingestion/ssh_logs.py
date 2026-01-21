import re
from collections import defaultdict
from datetime import datetime

FAILED_PATTERN = re.compile(
    r"Failed password for (invalid user )?(?P<user>\w+) from (?P<ip>[\d.]+)"
)

def parse_ssh_log(file_path):
    events = []

    with open(file_path, "r") as f:
        for line in f:
            match = FAILED_PATTERN.search(line)
            if match:
                events.append({
                    "timestamp": datetime.utcnow().isoformat(),
                    "username": match.group("user"),
                    "source_ip": match.group("ip"),
                    "event_type": "failed_login"
                })

    return events
